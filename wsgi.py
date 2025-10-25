import os
import sys

from app import app

from models import db, User, Transaction, Category

def init_db():
    """Initialize database tables if DATABASE_URL is set"""
    database_url = os.environ.get('DATABASE_URL')

    if not database_url:
        print("=" * 60)
        print("WARNING: DATABASE_URL environment variable is not set!")
        print("Database tables will NOT be created.")
        print("Please add a PostgreSQL database in Railway.")
        print("=" * 60)
        return False

    print("=" * 60)
    print("Initializing database...")
    print(f"Database URL: {database_url[:30]}...")

    try:
        with app.app_context():
            
            tables = list(db.metadata.tables.keys())
            print(f"Tables to create: {', '.join(tables)}")


            db.create_all()


            print(f"✓ Successfully created {len(tables)} tables!")
            print("=" * 60)
            return True

    except Exception as e:
        print("=" * 60)
        print(f"ERROR: Failed to initialize database!")
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        print("\nThe application will start, but database operations will fail.")
        print("Please check:")
        print("  1. DATABASE_URL is correctly set in Railway")
        print("  2. PostgreSQL service is running")
        print("  3. Database connection credentials are valid")
        print("=" * 60)
        return False


init_db()


if __name__ == "__main__":
    app.run()
