import os
import sys

def main():
    print("=" * 70)
    print("Railway Database Migration Script")
    print("=" * 70)

    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        print("ERROR: DATABASE_URL environment variable is not set!")
        print("\nPlease ensure you have:")
        print("  1. Added a PostgreSQL database to your Railway project")
        print("  2. Linked DATABASE_URL to your web service")
        print("=" * 70)
        sys.exit(1)

    print(f"Database URL: {database_url[:40]}...")

    print("\nImporting Flask app and models...")
    try:
        from app import app
        from models import db, User, Transaction, Category
        print("✓ Imports successful")
    except Exception as e:
        print(f"✗ Import failed: {e}")
        sys.exit(1)

    tables = list(db.metadata.tables.keys())
    print(f"\nFound {len(tables)} models: {', '.join(tables)}")

    print("\nCreating database tables...")
    try:
        with app.app_context():
            db.create_all()
            print("✓ Database tables created successfully!")

            print("\nVerifying tables...")
            try:
                User.query.count()
                print("  ✓ users table accessible")
                Category.query.count()
                print("  ✓ categories table accessible")
                Transaction.query.count()
                print("  ✓ transactions table accessible")
            except Exception as e:
                print(f"  ⚠ Warning: Could not verify tables: {e}")

    except Exception as e:
        print(f"✗ Failed to create tables: {e}")
        print(f"\nError type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    print("=" * 70)
    print("Database migration completed successfully!")
    print("=" * 70)

if __name__ == "__main__":
    main()
