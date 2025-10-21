# Setup Guide

## Local Development Setup

### 1. Create Virtual Environment
```bash
python -m venv venv
```

### 2. Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL Database
1. Open pgAdmin
2. Create a new database called `finance_tracker`
3. Note your PostgreSQL username and password

### 5. Create Environment File
Create a file called `.env` in the project root with:
```
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://username:password@localhost/finance_tracker
DEBUG=True
```

Replace `username` and `password` with your PostgreSQL credentials.

### 6. Initialize Database
```bash
python init_db.py
```

### 7. Run the Application
```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`

## Troubleshooting

- If you get database connection errors, check your DATABASE_URL in .env
- Make sure PostgreSQL is running
- Check that your database name, username, and password are correct
