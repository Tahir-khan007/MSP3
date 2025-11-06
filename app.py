from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_wtf.csrf import CSRFProtect
from config import Config
from models import db, User, Transaction, Category
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
csrf = CSRFProtect(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        # Auto-login the user after registration
        login_user(user)
        flash('Registration successful! Welcome to Finance Tracker.', 'success')
        return redirect(url_for('dashboard'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Login failed. Please check your email and password.', 'danger')

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


@app.route('/dashboard')
@login_required
def dashboard():
    filter_type = request.args.get('filter', 'all')
    category_filter = request.args.get('category', 'all')

    # Base query
    query = Transaction.query.filter_by(user_id=current_user.id)

    # Apply transaction type filter
    if filter_type == 'income':
        query = query.filter_by(transaction_type='income')
    elif filter_type == 'expense':
        query = query.filter_by(transaction_type='expense')

    # Apply category filter
    if category_filter != 'all':
        query = query.filter_by(category_id=int(category_filter))

    transactions = query.order_by(Transaction.date.desc()).all()

    total_income = sum(t.amount for t in Transaction.query.filter_by(user_id=current_user.id, transaction_type='income').all())
    total_expenses = sum(t.amount for t in Transaction.query.filter_by(user_id=current_user.id, transaction_type='expense').all())
    balance = total_income - total_expenses

    # Get user's categories for the filter dropdown
    categories = Category.query.filter_by(user_id=current_user.id).order_by(Category.name).all()

    return render_template('dashboard.html',
                         transactions=transactions,
                         total_income=total_income,
                         total_expenses=total_expenses,
                         balance=balance,
                         filter_type=filter_type,
                         category_filter=category_filter,
                         categories=categories)


@app.route('/transaction/add', methods=['POST'])
@login_required
def add_transaction():
    # Check if user has any categories
    categories = Category.query.filter_by(user_id=current_user.id).all()
    if not categories:
        flash('Please add at least one category before creating a transaction.', 'warning')
        return redirect(url_for('manage_categories'))

    # Manual validation for modal form submission
    category_id = request.form.get('category_id')
    description = request.form.get('description')
    transaction_type = request.form.get('transaction_type')
    amount = request.form.get('amount')
    date_str = request.form.get('date')

    # Basic validation
    if not all([category_id, description, transaction_type, amount, date_str]):
        flash('All fields are required.', 'danger')
        return redirect(url_for('dashboard'))

    try:
        transaction = Transaction(
            user_id=current_user.id,
            category_id=int(category_id),
            description=description,
            amount=float(amount),
            transaction_type=transaction_type,
            date=datetime.strptime(date_str, '%Y-%m-%d')
        )
        db.session.add(transaction)
        db.session.commit()
        flash('Transaction added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error adding transaction. Please try again.', 'danger')

    return redirect(url_for('dashboard'))


@app.route('/transaction/edit/<int:id>', methods=['POST'])
@login_required
def edit_transaction(id):
    transaction = Transaction.query.get_or_404(id)

    if transaction.user_id != current_user.id:
        flash('You do not have permission to edit this transaction.', 'danger')
        return redirect(url_for('dashboard'))

    # Manual validation for modal form submission
    category_id = request.form.get('category_id')
    description = request.form.get('description')
    transaction_type = request.form.get('transaction_type')
    amount = request.form.get('amount')
    date_str = request.form.get('date')

    # Basic validation
    if not all([category_id, description, transaction_type, amount, date_str]):
        flash('All fields are required.', 'danger')
        return redirect(url_for('dashboard'))

    try:
        transaction.category_id = int(category_id)
        transaction.description = description
        transaction.amount = float(amount)
        transaction.transaction_type = transaction_type
        transaction.date = datetime.strptime(date_str, '%Y-%m-%d')
        db.session.commit()
        flash('Transaction updated successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error updating transaction. Please try again.', 'danger')

    return redirect(url_for('dashboard'))


@app.route('/transaction/delete/<int:id>', methods=['POST'])
@login_required
def delete_transaction(id):
    transaction = Transaction.query.get_or_404(id)

    if transaction.user_id != current_user.id:
        flash('You do not have permission to delete this transaction.', 'danger')
        return redirect(url_for('dashboard'))

    db.session.delete(transaction)
    db.session.commit()
    flash('Transaction deleted successfully!', 'success')
    return redirect(url_for('dashboard'))


# Category Management Routes
@app.route('/categories')
@login_required
def manage_categories():
    categories = Category.query.filter_by(user_id=current_user.id).order_by(Category.name).all()

    # Get transaction count for each category
    category_data = []
    for category in categories:
        transaction_count = Transaction.query.filter_by(category_id=category.id).count()
        category_data.append({
            'category': category,
            'transaction_count': transaction_count
        })

    return render_template('categories.html', category_data=category_data)


@app.route('/category/add', methods=['POST'])
@login_required
def add_category():
    # Manual validation for modal form submission
    name = request.form.get('name')

    if not name:
        flash('Category name is required.', 'danger')
        return redirect(url_for('manage_categories'))

    # Check if category name already exists for this user
    existing_category = Category.query.filter_by(
        user_id=current_user.id,
        name=name
    ).first()

    if existing_category:
        flash(f'Category "{name}" already exists.', 'warning')
        return redirect(url_for('manage_categories'))

    try:
        category = Category(
            user_id=current_user.id,
            name=name
        )
        db.session.add(category)
        db.session.commit()
        flash('Category added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error adding category. Please try again.', 'danger')

    return redirect(url_for('manage_categories'))


@app.route('/category/edit/<int:id>', methods=['POST'])
@login_required
def edit_category(id):
    category = Category.query.get_or_404(id)

    if category.user_id != current_user.id:
        flash('You do not have permission to edit this category.', 'danger')
        return redirect(url_for('manage_categories'))

    # Manual validation for modal form submission
    name = request.form.get('name')

    if not name:
        flash('Category name is required.', 'danger')
        return redirect(url_for('manage_categories'))

    # Check if new name conflicts with existing category
    existing_category = Category.query.filter_by(
        user_id=current_user.id,
        name=name
    ).filter(Category.id != id).first()

    if existing_category:
        flash(f'Category "{name}" already exists.', 'warning')
        return redirect(url_for('manage_categories'))

    try:
        category.name = name
        db.session.commit()
        flash('Category updated successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error updating category. Please try again.', 'danger')

    return redirect(url_for('manage_categories'))


@app.route('/category/delete/<int:id>', methods=['POST'])
@login_required
def delete_category(id):
    category = Category.query.get_or_404(id)

    if category.user_id != current_user.id:
        flash('You do not have permission to delete this category.', 'danger')
        return redirect(url_for('manage_categories'))

    # Check if category has transactions
    transaction_count = Transaction.query.filter_by(category_id=id).count()
    if transaction_count > 0:
        flash(f'Cannot delete category "{category.name}" - it has {transaction_count} transaction(s) linked to it. Please delete or reassign all transactions from this category first, then try again.', 'danger')
        return redirect(url_for('manage_categories'))

    db.session.delete(category)
    db.session.commit()
    flash('Category deleted successfully!', 'success')
    return redirect(url_for('manage_categories'))


# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors by rendering a custom error page"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors by rendering a custom error page"""
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True, port=5001)
