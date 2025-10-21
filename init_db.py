from app import app
from models import db

with app.app_context():
    # Drop all tables and recreate (WARNING: This will delete all data!)
    # Comment out db.drop_all() if you want to keep existing data
    db.drop_all()
    print("Dropped all existing tables...")

    # Create all tables
    db.create_all()
    print("Database tables created successfully!")
    print("\nTables created:")
    print("- users")
    print("- categories")
    print("- transactions")
    print("\nYou can now register a user and add categories!")
