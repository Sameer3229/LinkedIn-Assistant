#!/usr/bin/env python3
"""
Setup script to create the first admin user for the LinkedIn Message Tracker admin portal
"""

import os
import sqlite3
import bcrypt
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
db_path = os.getenv("ADMIN_DB_PATH", "data/admin.db")

def hash_password(password: str) -> str:
    """Hash password using bcrypt"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def create_admin():
    """Create first admin user"""
    # Create data directory if needed
    os.makedirs(os.path.dirname(db_path) or ".", exist_ok=True)
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Initialize database schema if needed
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS prompts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                description TEXT,
                content TEXT NOT NULL,
                is_default BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id),
                UNIQUE(user_id, name)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                name TEXT,
                inbound TEXT,
                reply TEXT,
                time TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        conn.commit()
    except Exception as e:
        print(f"Database initialization warning: {e}")
    
    # Check if any admin exists
    cursor.execute("SELECT COUNT(*) as count FROM users")
    user_count = cursor.fetchone()[0]
    
    if user_count > 0:
        print("❌ Admin already exists!")
        print("Only one admin account is allowed.")
        conn.close()
        return False
    
    print("\n" + "="*60)
    print("CREATE ADMIN ACCOUNT")
    print("="*60)
    
    username = input("Enter admin username: ").strip()
    
    if not username or len(username) < 3:
        print("❌ Username must be at least 3 characters")
        conn.close()
        return False
    
    password = input("Enter admin password: ").strip()
    
    if not password or len(password) < 6:
        print("❌ Password must be at least 6 characters")
        conn.close()
        return False
    
    password_confirm = input("Confirm password: ").strip()
    
    if password != password_confirm:
        print("❌ Passwords do not match")
        conn.close()
        return False
    
    # Hash password and create user
    password_hash = hash_password(password)
    
    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, password_hash)
        )
        conn.commit()
        conn.close()
        
        print("\n" + "="*60)
        print("✅ ADMIN ACCOUNT CREATED SUCCESSFULLY!")
        print("="*60)
        print(f"Username: {username}")
        print("\nYou can now log in to the admin portal at:")
        print("http://localhost:9011/admin")
        print("="*60 + "\n")
        
        return True
    except Exception as e:
        print(f"❌ Error creating admin: {e}")
        conn.close()
        return False

if __name__ == "__main__":
    create_admin()
