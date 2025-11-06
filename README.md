# MyShop — Flask Online Shop Management (starter)

This is a small Flask starter project for an online shop management system using a light blue & white theme and SQLAlchemy.

Quick start (Windows Powershell):

1. Create and activate venv (if not already done):

   python -m venv .venv; .\.venv\Scripts\Activate.ps1

2. Install dependencies:

   pip install -r requirements.txt

3. Initialize the database and run the app:

   # run the server — it will create the SQLite DB automatically
   python main.py

The app listens on http://127.0.0.1:5000 by default.

Notes:
- The database file is created in the `instance/` folder as `myshop.sqlite`.
- This is a minimal starter: you can extend it with authentication, file uploads, admin UI, and tests.
