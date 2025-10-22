from app import app
from models import db

# Initialize database tables on startup
with app.app_context():
    db.create_all()
    print("Database tables initialized!")

if __name__ == "__main__":
    app.run()
