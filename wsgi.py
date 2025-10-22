from app import app
from models import db
import os

if os.environ.get('DATABASE_URL'):
    try:
        with app.app_context():
            db.create_all()
            print("Database tables initialized successfully!")
    except Exception as e:
        print(f"Warning: Could not initialize database tables: {e}")
        print("The app will start anyway. Tables may need to be created manually.")
else:
    print("Warning: DATABASE_URL not set. Database tables not initialized.")

if __name__ == "__main__":
    app.run()
