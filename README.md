# 💰 Finance Tracker

A full-featured Flask web application for tracking personal finances with user authentication, modal-based operations, category management, and real-time transaction filtering. Built with PostgreSQL for secure, cloud-based data storage accessible from any device.

![Finance Tracker Dashboard](./assets/dashboard-page.png)
*Modern dashboard with real-time financial overview and interactive charts*

## Project Overview

Finance Tracker is a comprehensive personal finance management application that enables users to track income and expenses, manage custom categories, and visualize their financial health through interactive charts. The application features a secure authentication system, modal-based interfaces for quick data entry, and a responsive design that works seamlessly across all devices.

## The Why

Managing personal finances effectively is crucial for financial wellness, yet many solutions are either too complex or lack essential features. This Finance Tracker bridges that gap by providing an intuitive, feature-rich platform that makes financial tracking simple and accessible. With cloud-based storage and multi-device access, users can manage their finances anytime, anywhere.

## User & Business Goals

- **Secure Access**: Provide user authentication with CSRF protection for data security
- **Quick Operations**: Enable fast transaction and category management through modal popups
- **Visual Insights**: Offer clear financial summaries with interactive charts
- **Smart Organization**: Allow custom categories with transaction count tracking
- **Data Protection**: Prevent accidental deletion of categories with linked transactions
- **Universal Access**: Ensure responsive design works on desktop, tablet, and mobile
- **Cloud Persistence**: Store data securely in PostgreSQL accessible from any device

## (UX) User Experience

Users can register for an account, create custom categories, and manage transactions through intuitive modal interfaces. The dashboard provides real-time financial overview with total balance, income, expenses, and visual pie chart comparison. Advanced filtering allows users to analyze transactions by type and category.

### User Stories with Screenshots

#### First-Time Users Goals:

**User Story 1**: *"As a first-time user, I want to understand what this application does so that I can decide if it meets my needs."*

![Homepage Screenshot](./assets/home-screen.png)
*The hero page clearly explains the application's purpose and features with a beautiful gradient design, allowing new users to understand the value proposition immediately.*

---

**User Story 2**: *"As a first-time user, I want to create an account easily so that I can start tracking my finances."*

![Registration Page](./assets/register-page.png)
*Clean registration form with validation ensures users can create accounts quickly and securely with automatic login after registration.*

---

**User Story 3**: *"As a first-time user, I want to add categories for my transactions so that I can organize my finances."*

![Categories Page](./assets/categories-page.png)
*The categories management page allows users to create, edit, and view transaction categories with quick modal-based operations.*

---

**User Story 4**: *"As a first-time user, I want to see a clean dashboard overview so that I can quickly understand my financial status."*

![Dashboard Overview](./assets/dashboard-page.png)
*The main dashboard provides an immediate overview with total balance, income, and expenses prominently displayed, along with a visual pie chart comparison and recent transactions table.*

---

**User Story 5**: *"As a first-time user, I want to easily add my first transaction so that I can start tracking my finances."*

![Add Transaction Modal](./assets/add-transaction.png)
*Clicking the "Add Transaction" button opens a modal form with all necessary fields, making it simple to add transactions without page navigation.*

---

#### Returning Users Goals:

**User Story 6**: *"As a returning user, I want to quickly view my recent transactions so that I can review my spending patterns."*

![Transactions Table](./assets/dashboard-page.png)
*The transactions table displays all recent transactions with clear categorization, type indicators (green for income, red for expenses), and quick edit/delete actions.*

---

**User Story 7**: *"As a returning user, I want to filter my transactions by type and category so that I can analyze my finances."*

![Filter Transactions](./assets/filter-screenshot.png)
*Dropdown filters allow users to quickly switch between viewing all transactions, specific types (income/expense), or specific categories for focused financial analysis.*

---

**User Story 8**: *"As a returning user, I want to edit transactions when I make mistakes so that my records stay accurate."*

![Edit Transaction Modal](./assets/edit-transaction.png)
*The edit modal pre-fills all transaction data, allowing users to quickly make corrections with the same intuitive interface used for adding transactions.*

---

**User Story 9**: *"As a returning user, I want to see visual representations of my financial data so that I can understand my spending habits at a glance."*

![Financial Charts](./assets/chart-screenshot.png)
*The interactive pie chart provides an immediate visual comparison between total income and expenses, making it easy to understand financial balance.*

---

**User Story 10**: *"As a returning user, I want to manage my categories efficiently without accidentally deleting ones that contain transactions."*

![Category Protection](./assets/categories-page.png)
*Categories with linked transactions display a lock icon (🔒) and show transaction counts, preventing accidental deletion and providing clear visual feedback.*

---

## Design

The design focuses on usability, clarity, and modern aesthetics with smooth animations and responsive interactions.

### Design Brief

- **Color Scheme**:
  - **Purple Gradient (#667eea to #764ba2)**: Primary theme for landing page and accents
  - **Green (#4caf50)**: Represents income, success actions, and positive indicators
  - **Red (#f44336)**: Represents expenses, delete actions, and warnings
  - **Blue (#007bff)**: Edit actions and informational elements
  - **Yellow (#ffc107)**: Warning badges and alerts
  - **Neutral Tones**: Clean backgrounds and readable text

- **Typography**:
  - **Clean Sans-serif**: Arial for maximum readability
  - **Hierarchical Sizing**: Clear distinction between headers, body text, and labels
  - **Optimized for Data**: Monospace-style presentation for financial figures

- **Layout**:
  - **Card-based Design**: Glassmorphic cards with subtle shadows
  - **Responsive Grid**: Adapts seamlessly from desktop to mobile
  - **Modal Popups**: Smooth animated overlays for quick operations
  - **Sticky Navigation**: Fixed navbar with user greeting and hamburger menu
  - **Color-coded Tables**: Visual distinction between income and expense entries

- **Animations**:
  - **Fade In/Out**: Flash messages auto-dismiss after 5 seconds
  - **Slide Animations**: Modal popups and mobile navigation
  - **Hover Effects**: Interactive feedback on buttons and links
  - **Smooth Transitions**: All state changes animated for polish

## Features

### Existing Features

- **🔐 User Authentication**: Secure registration and login system with password hashing
- **🛡️ CSRF Protection**: Flask-WTF CSRF tokens on all forms for security
- **🎯 Modal-Based Operations**: Quick add/edit for transactions and categories without page reloads
- **📊 Dashboard Stats**: Real-time display of total balance, income, and expenses
- **📈 Interactive Charts**: Pie chart visualization using Chart.js
- **🏷️ Category Management**: Create, edit, and delete custom transaction categories
- **📝 Transaction Tracking**: Add, edit, and delete income/expense transactions
- **🔍 Advanced Filtering**: Filter transactions by type (income/expense) and category
- **📱 Responsive Design**: Hamburger menu for mobile/tablet, full navbar for desktop
- **🔒 Smart Deletion Protection**: Lock icon and warnings for categories with transactions
- **📊 Transaction Count Tracking**: Visual badges showing transaction count per category
- **⚡ Auto-dismiss Alerts**: Flash messages with smooth fade animations
- **⌨️ Keyboard Shortcuts**: ESC key closes modals, click outside to dismiss
- **☁️ Cloud Database**: PostgreSQL storage accessible from any device
- **🎨 Modern UI/UX**: Glassmorphic cards, gradient backgrounds, smooth transitions
- **⚠️ Custom Error Pages**: User-friendly 404 and 500 error pages with navigation options

### Future Features

- **📅 Recurring Transactions**: Automatically add regular income/expenses (e.g., monthly salary, rent)
- **💰 Budget Tracking**: Set monthly budgets per category with progress indicators
- **📊 Advanced Analytics**: Monthly/yearly reports with trend charts and spending patterns
- **📥 Export Data**: Download transactions as CSV or PDF reports
- **🌍 Multi-currency Support**: Handle transactions in different currencies
- **📎 Receipt Upload**: Attach receipt images to transactions
- **🎨 Category Icons**: Visual icons for each category
- **🌙 Dark Mode**: Toggle between light and dark themes
- **📧 Email Notifications**: Budget alerts and spending summaries
- **📱 Mobile App**: Native iOS/Android applications
- **👥 Shared Accounts**: Family/team finance tracking with permissions

## Technologies

### Languages Used

- [Python 3.10+](https://www.python.org/) - Backend logic and application framework
- [HTML5](https://en.wikipedia.org/wiki/HTML5) - Page structure and content
- [CSS3](https://en.wikipedia.org/wiki/CSS) - Styling, animations, and responsive design
- [JavaScript (ES6)](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - Modal interactions, menu toggle, form handling

### Frameworks & Libraries

- [Flask 3.0.0](https://flask.palletsprojects.com/) - Python web framework
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) - Database ORM
- [Flask-Login](https://flask-login.readthedocs.io/) - User session management
- [Flask-WTF](https://flask-wtf.readthedocs.io/) - Form handling and CSRF protection
- [WTForms](https://wtforms.readthedocs.io/) - Form validation
- [Chart.js](https://www.chartjs.org/) - Interactive pie chart visualizations
- [PostgreSQL](https://www.postgresql.org/) - Production database
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Environment variable management

### Development Tools

- [Git](https://git-scm.com/) - Version control
- [GitHub](https://github.com/) - Code repository and collaboration
- [VS Code](https://code.visualstudio.com/) - Development environment
- [pgAdmin](https://www.pgadmin.org/) - PostgreSQL database management

## Database Schema

### Users Table
```sql
- id (Primary Key)
- username (Unique, String)
- email (Unique, String)
- password_hash (String)
- created_at (DateTime)
```

### Categories Table
```sql
- id (Primary Key)
- user_id (Foreign Key → Users)
- name (String)
- created_at (DateTime)
```

### Transactions Table
```sql
- id (Primary Key)
- user_id (Foreign Key → Users)
- category_id (Foreign Key → Categories)
- description (String)
- amount (Decimal)
- transaction_type (Enum: 'income' or 'expense')
- date (Date)
- created_at (DateTime)
```

## Installation & Setup

### Prerequisites

- Python 3.10 or higher
- PostgreSQL 14 or higher
- pip (Python package manager)
- Git

### Local Development Setup

1. **Clone the Repository**

```bash
git clone https://github.com/Tahir-khan007/MSP3.git
cd MSP3
```

2. **Create Virtual Environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Set Up PostgreSQL Database**

- Open pgAdmin or use PostgreSQL command line
- Create a new database named `finance_tracker`
- Note your PostgreSQL username and password

5. **Configure Environment Variables**

Create a `.env` file in the project root:

```bash
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=postgresql://username:password@localhost/finance_tracker
DEBUG=True
```

Replace `username` and `password` with your PostgreSQL credentials.

6. **Initialize Database**

```bash
python init_db.py
```

7. **Run the Application**

```bash
python app.py
```

Visit `http://127.0.0.1:5001` in your browser.

## Deployment

### Live Demo

The application is deployed and accessible at: [Finanace Tracker](https://msp3.up.railway.app/)

The application's Github repository is available at: [Github repo](https://github.com/Tahir-khan007/MSP3)

### Railway.app Deployment (Recommended)

This project is configured for easy deployment on Railway.app with automatic PostgreSQL provisioning.

**Why Railway?**
- ✅ $5/month free credit (covers most hobby projects)
- ✅ Automatic HTTPS
- ✅ Auto-deploy on git push
- ✅ Built-in PostgreSQL
- ✅ Easy environment variable management
- ✅ One-click rollback

**Deployment Steps:**

1. **Push to GitHub**

```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

2. **Deploy on Railway**

- Visit [railway.app](https://railway.app)
- Sign up/Login with GitHub
- Click "New Project" → "Deploy from GitHub repo"
- Select your repository
- Railway will auto-detect Flask and deploy

3. **Add PostgreSQL Database**

- In Railway dashboard, click "New" → "Database" → "Add PostgreSQL"
- Database URL is automatically added as `DATABASE_URL` environment variable

4. **Set Environment Variables**

Go to your project → Variables tab and add:

```bash
SECRET_KEY=your-strong-secret-key-here
DEBUG=False
```

Note: `DATABASE_URL` is already set by Railway automatically.

5. **Initialize Database**

Use Railway CLI or deploy the `init_db.py` script through the web interface.

6. **Access Your App**

Railway provides a public URL automatically. Click "Settings" → "Generate Domain" if not auto-generated.

### Alternative Deployment Options

**Render.com** - Free tier with limitations (sleeps after inactivity)
**Fly.io** - Free tier available, great performance
**PythonAnywhere** - Free tier with restrictions

### Environment Variables for Production

```bash
SECRET_KEY=<strong-random-secret-key>
DATABASE_URL=<automatically-set-by-hosting-platform>
DEBUG=False
```

## Testing

### Manual Testing

#### Authentication Testing
- ✅ User registration with validation
- ✅ Password hashing and secure storage
- ✅ Login with correct credentials
- ✅ Login rejection with incorrect credentials
- ✅ Auto-login after registration
- ✅ Session persistence across page reloads
- ✅ Logout functionality
- ✅ Protected routes redirect to login

#### Transaction Management Testing
- ✅ Add transaction via modal
- ✅ Transaction appears in table immediately
- ✅ Edit transaction via modal with pre-filled data
- ✅ Delete transaction with confirmation
- ✅ Transaction validation (all fields required)
- ✅ CSRF token validation on form submission
- ✅ Amount accepts decimal values
- ✅ Date defaults to current date

#### Category Management Testing
- ✅ Add category via modal
- ✅ Edit category via modal
- ✅ Delete empty category
- ✅ Prevent deletion of category with transactions
- ✅ Lock icon display for protected categories
- ✅ Transaction count tracking
- ✅ Duplicate category name prevention
- ✅ Category-specific transaction filtering

#### Filtering & Display Testing
- ✅ Filter by transaction type (All/Income/Expense)
- ✅ Filter by category
- ✅ Combined filters work correctly
- ✅ Statistics update with filters
- ✅ Chart reflects current filter state
- ✅ Empty state handled gracefully

#### UI/UX Testing
- ✅ Modal opens/closes smoothly
- ✅ ESC key closes modals
- ✅ Click outside closes modals
- ✅ Flash messages auto-dismiss after 5 seconds
- ✅ Manual dismiss with × button
- ✅ Hamburger menu works on mobile/tablet
- ✅ Navigation links work correctly
- ✅ Color coding (green for income, red for expense)
- ✅ Hover effects on interactive elements

#### Responsive Design Testing
- ✅ Desktop (1920x1080, 1366x768)
- ✅ Tablet (768x1024, 834x1112)
- ✅ Mobile (375x667, 414x896)
- ✅ Hamburger menu appears on screens ≤1024px
- ✅ Tables scroll horizontally on small screens
- ✅ Modals are responsive and centered
- ✅ Forms adapt to screen size

#### Database & Security Testing
- ✅ Data persists after server restart
- ✅ User data isolation (users see only their data)
- ✅ CSRF protection active on all forms
- ✅ SQL injection prevention via ORM
- ✅ Password hashing (not stored as plain text)
- ✅ Unauthorized access prevention

#### Error Handling Testing
- ✅ 404 error page displays for non-existent routes
- ✅ 404 page shows appropriate navigation options (Dashboard/Home)
- ✅ 404 page maintains navbar and site styling
- ✅ 500 error page displays for server errors
- ✅ 500 page includes helpful troubleshooting suggestions
- ✅ Error pages are responsive on all devices
- ✅ Error pages provide "Go Back" functionality

### User Stories Testing

This section demonstrates thorough testing of all user stories documented in the UX section.

#### User Story 1: Understanding the Application
**Test Case**: First-time user visits homepage to understand the application purpose
- **Steps**: Navigate to homepage (/)
- **Expected Result**: Clear hero section with application description and call-to-action buttons
- **Actual Result**: Homepage displays purple gradient hero with "Track Your Finances with Ease" heading, feature description, and "Get Started" button
- **Status**: ✅ PASS

#### User Story 2: Account Creation
**Test Case**: New user creates an account
- **Steps**: Click "Get Started" → Fill registration form → Submit
- **Expected Result**: Account created, auto-login, redirect to dashboard with success message
- **Actual Result**: User successfully registered, automatically logged in, redirected to dashboard with "Registration successful! Welcome to Finance Tracker." message
- **Status**: ✅ PASS

#### User Story 3: Adding Categories
**Test Case**: User creates custom categories for transaction organization
- **Steps**: Navigate to Categories page → Click "Add Category" → Enter name → Submit
- **Expected Result**: Category created and appears in list immediately
- **Actual Result**: Modal opens, category added successfully, appears in categories table with transaction count of 0
- **Status**: ✅ PASS

#### User Story 4: Dashboard Overview
**Test Case**: User views financial summary on dashboard
- **Steps**: Login → Navigate to dashboard
- **Expected Result**: Display total balance, income, expenses, pie chart, and transactions table
- **Actual Result**: Dashboard shows all financial metrics at top, interactive Chart.js pie chart, and complete transactions table with color-coded entries
- **Status**: ✅ PASS

#### User Story 5: Adding First Transaction
**Test Case**: User adds their first income or expense transaction
- **Steps**: Click "Add Transaction" → Fill form (category, description, amount, type, date) → Submit
- **Expected Result**: Transaction saved, appears in table, statistics update
- **Actual Result**: Modal opens with form, transaction added successfully, table updates immediately, balance recalculated automatically
- **Status**: ✅ PASS

#### User Story 6: Viewing Recent Transactions
**Test Case**: Returning user reviews transaction history
- **Steps**: Login → View dashboard transactions table
- **Expected Result**: All transactions displayed with category, description, amount, type, and date
- **Actual Result**: Table displays all transactions sorted by date (newest first), color-coded by type (green for income, red for expense)
- **Status**: ✅ PASS

#### User Story 7: Filtering Transactions
**Test Case**: User filters transactions by type and category
- **Steps**: Use filter dropdowns → Select type (All/Income/Expense) → Select category
- **Expected Result**: Table updates to show only matching transactions, statistics recalculate
- **Actual Result**: Filters work correctly, can combine type and category filters, URL updates with query params, statistics reflect filtered data
- **Status**: ✅ PASS

#### User Story 8: Editing Transactions
**Test Case**: User corrects a transaction mistake
- **Steps**: Click edit icon on transaction → Modify fields in modal → Submit
- **Expected Result**: Transaction updated, changes reflected immediately
- **Actual Result**: Edit modal opens with pre-filled data, changes saved successfully, table and statistics update without page reload
- **Status**: ✅ PASS

#### User Story 9: Visual Financial Data
**Test Case**: User views pie chart for spending analysis
- **Steps**: View dashboard with transactions
- **Expected Result**: Interactive pie chart showing income vs expenses ratio
- **Actual Result**: Chart.js pie chart displays with green (income) and red (expenses) sections, shows percentages and amounts on hover
- **Status**: ✅ PASS

#### User Story 10: Managing Categories Safely
**Test Case**: User attempts to delete category with linked transactions
- **Steps**: Try to delete category that has transactions
- **Expected Result**: Deletion prevented with warning message, lock icon displayed
- **Actual Result**: Lock icon (🔒) shown next to category name, delete attempt shows error: "Cannot delete category - it has X transaction(s) linked to it"
- **Status**: ✅ PASS

### CRUD Operations Testing

This section verifies all Create, Read, Update, Delete operations function correctly.

#### Transactions CRUD
| Operation | Endpoint | Test | Result |
|-----------|----------|------|--------|
| **Create** | `POST /transaction/add` | Add new transaction with valid data | ✅ Transaction created, appears in dashboard |
| **Create** | `POST /transaction/add` | Add transaction without category | ✅ Redirects to category management with warning |
| **Create** | `POST /transaction/add` | Add transaction with missing fields | ✅ Validation error, flash message displayed |
| **Read** | `GET /dashboard` | View all user transactions | ✅ All transactions displayed correctly |
| **Read** | `GET /dashboard?filter=income` | Filter by income type | ✅ Only income transactions shown |
| **Read** | `GET /dashboard?category=1` | Filter by category | ✅ Only transactions from selected category shown |
| **Update** | `POST /transaction/edit/<id>` | Edit transaction with valid data | ✅ Transaction updated successfully |
| **Delete** | `POST /transaction/delete/<id>` | Delete own transaction | ✅ Transaction removed from database |

#### Categories CRUD
| Operation | Endpoint | Test | Result |
|-----------|----------|------|--------|
| **Create** | `POST /category/add` | Add new category | ✅ Category created and listed |
| **Create** | `POST /category/add` | Add duplicate category name | ✅ Prevented with warning message |
| **Read** | `GET /categories` | View all user categories | ✅ Categories displayed with transaction counts |
| **Update** | `POST /category/edit/<id>` | Edit category name | ✅ Category updated successfully |
| **Delete** | `POST /category/delete/<id>` | Delete empty category | ✅ Category removed successfully |
| **Delete** | `POST /category/delete/<id>` | Delete category with transactions | ✅ Prevented with error message and transaction count |

#### Users CRUD
| Operation | Endpoint | Test | Result |
|-----------|----------|------|--------|
| **Create** | `POST /register` | Register with valid data | ✅ User created, password hashed, auto-login |
| **Create** | `POST /register` | Register with existing email | ✅ Validation error shown |
| **Read** | `@login_required` routes | Access user data | ✅ Only own data accessible |
| **Update** | N/A | Update profile | ⚠️ Not implemented (future feature) |
| **Delete** | N/A | Delete account | ⚠️ Not implemented (future feature) |

### Code Validation

#### HTML Validation
- ✅ W3C HTML Validator - No errors
- ✅ Semantic HTML structure
- ✅ Proper accessibility attributes (aria-label, alt tags)
- ✅ Valid form structures

#### CSS Validation
- ✅ W3C CSS Validator - No errors
- ✅ Responsive design principles
- ✅ Cross-browser compatible styles
- ✅ Proper CSS animations

## Challenges & Learning

### Key Learnings

- **Full-Stack Integration**: Gained deep understanding of Flask backend with dynamic frontend
- **Database Design**: Learned proper foreign key relationships and data integrity
- **Security Best Practices**: Implemented CSRF protection, password hashing, and user isolation
- **Responsive Design**: Developed mobile-first approach with progressive enhancement

## Project Structure

```
MSP3/
├── app.py                      # Main Flask application with routes
├── models.py                   # SQLAlchemy database models
├── forms.py                    # WTForms form definitions
├── config.py                   # Application configuration
├── init_db.py                  # Database initialization script
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python version for deployment
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore rules
├── README.md                   # Project documentation
├── SETUP.md                    # Detailed setup instructions
│
├── static/
│   └── css/
│       ├── style.css           # Global styles, navbar, modals, forms
│       └── finance.css         # Dashboard and category page styles
│
├── templates/
│   ├── base.html              # Base template with navbar, alerts, scripts
│   ├── index.html             # Landing page
│   ├── register.html          # User registration
│   ├── login.html             # User login
│   ├── dashboard.html         # Dashboard with transaction modals
│   └── categories.html        # Category management with modals
│
└── assets/                    # Screenshots for documentation
    ├── homepage-screenshot.png
    ├── dashboard-page.png
    ├── categories-page.png
    └── ...
```

## Credits

### Code & Resources

- **Flask Documentation** - [flask.palletsprojects.com](https://flask.palletsprojects.com/)
- **Chart.js Documentation** - [chartjs.org](https://www.chartjs.org/)
- **PostgreSQL Documentation** - [postgresql.org](https://www.postgresql.org/docs/)
- **MDN Web Docs** - [developer.mozilla.org](https://developer.mozilla.org/)
- **Flask-Login Docs** - [flask-login.readthedocs.io](https://flask-login.readthedocs.io/)
- **Railway Deployment Guide** - [docs.railway.app](https://docs.railway.app/)

### Design Inspiration

- Minimalist dashboard designs
- Material Design principles for modals and interactions

### Acknowledgements

- **Code Institute** - For comprehensive learning materials and project guidance
- **Mentors** - For valuable feedback
- **Flask Community** - For extensive documentation and tutorials

## Support

For issues, questions, or feature requests:
- **GitHub Issues**: [github.com/Tahir-khan007/MSP3/issues](https://github.com/Tahir-khan007/MSP3/issues)
- **Email**: Contact through GitHub profile

## Troubleshooting

### Common Issues

**Port Already in Use**
```python
# Change port in app.py
app.run(debug=True, port=5002)  # Change 5001 to any available port
```

**Database Connection Error**
- Verify PostgreSQL is running
- Check `DATABASE_URL` in `.env` file
- Ensure database `finance_tracker` exists
- Verify username and password are correct

**Import Errors**
```bash
# Activate virtual environment
venv\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt
```

**Modal Not Opening**
- Ensure JavaScript is enabled in browser
- Check browser console for errors
- Clear browser cache
- Verify CSRF token is present

**Category Won't Delete**
- Check if category has linked transactions
- Look for lock icon (🔒) indicating protection
- Delete all transactions from that category first
- Transaction count is shown in the table

**Flash Messages Not Disappearing**
- Messages auto-dismiss after 5 seconds
- Click × to dismiss manually
- Ensure JavaScript is enabled
- Clear browser cache if issue persists

**Hamburger Menu Not Working**
- Test on screens ≤1024px width
- Check browser console for JavaScript errors
- Ensure navigation IDs match JavaScript selectors
- Clear cache and reload

---

**Built using Flask, PostgreSQL, and modern web technologies**
