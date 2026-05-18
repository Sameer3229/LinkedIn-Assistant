# LinkedIn Message Tracker - Admin Portal Setup Guide

## 🎯 Overview

The admin portal has been successfully implemented! This provides a centralized web interface for managing prompts and viewing chat history, replacing the extension popup with a full-featured dashboard.

### Key Features
- ✅ User authentication with JWT tokens
- ✅ Multi-prompt management per user
- ✅ Set default prompts (used automatically by extension)
- ✅ Chat history tracking with timestamps
- ✅ Responsive design (works on mobile)

---

## 📋 Quick Start

### Step 1: Install Dependencies

```bash
cd /mnt/E08EC7468EC71446/linkedin-msg-tracker

# Install required packages
./linkedln/bin/pip install PyJWT bcrypt python-multipart
```

### Step 2: Create Admin Account

Run the setup script to create your first admin user:

```bash
./linkedln/bin/python setup_admin.py
```

Follow the prompts to enter:
- Admin username (min 3 characters)
- Admin password (min 6 characters)

**Example:**
```
==============================================================
CREATE ADMIN ACCOUNT
==============================================================
Enter admin username: john_doe
Enter admin password: MySecurePass123
✅ Admin account created successfully!
```

### Step 3: Start the Backend Server

```bash
./linkedln/bin/python app_new.py
```

You should see output like:
```
INFO:     Uvicorn running on http://0.0.0.0:9011
```

The server is now running on `http://localhost:9011`

### Step 4: Access Admin Portal

1. **Option A - Via Extension Popup:**
   - Open the LinkedIn Message Tracker extension popup
   - Click "Open Admin Panel" button
   - Browser will redirect to `http://localhost:9011/admin`

2. **Option B - Direct Access:**
   - Open browser and navigate to `http://localhost:9011/admin`
   
3. **Log In:**
   - Use the credentials you created in Step 2
   - Click "Login"

---

## 🎨 Using the Admin Portal

### Prompt Manager Tab

**Create a New Prompt:**
1. Click the "Add New Prompt" section
2. Fill in:
   - **Prompt Name**: e.g., "Cricket Coach"
   - **Description**: e.g., "For coaching inquiries"
   - **Prompt Content**: Your system instructions (e.g., "You are replying on behalf of...")
3. Click "Save Prompt"

**Edit a Prompt:**
1. Find the prompt in the table
2. Click "Edit" button
3. Modify the fields
4. Click "Update Prompt"

**Delete a Prompt:**
1. Find the prompt in the table
2. Click "Delete" button
3. Confirm deletion

**Set Default Prompt:**
1. Find the prompt in the table
2. Click "Set Default" button
3. The extension will use this prompt automatically for all messages

### Chat History Tab

**View History:**
- All messages sent via the extension will appear here
- Shows: Date, Contact Name, Inbound Message Preview, Reply Preview

**Clear History:**
- Click "Clear All History" button at the top
- Confirms before clearing

---

## 🔌 Extension Integration

### How It Works

1. **Prompt Selection:**
   - When you set a prompt as default in the admin portal
   - The prompt ID is automatically stored in browser localStorage
   - The extension reads this ID on the next message

2. **Message Sending:**
   - User sends a LinkedIn message
   - Extension fetches the message text from the thread
   - Extension sends to backend: `{message, prompt_id: X}`
   - Backend looks up the prompt from database
   - AI generates a reply using that prompt
   - Reply is sent back to extension

3. **History Tracking:**
   - After sending a reply
   - Extension sends chat details to backend
   - Authenticated with JWT token
   - Message appears in admin portal Chat History tab

---

## 🗄️ Database Schema

**Users Table:**
```
id (PRIMARY KEY)
username (UNIQUE)
password_hash
created_at
```

**Prompts Table:**
```
id (PRIMARY KEY)
user_id (FOREIGN KEY → users)
name
description
content
is_default (1 = default prompt for user)
created_at
updated_at
```

**Chat History Table:**
```
id (PRIMARY KEY)
user_id (FOREIGN KEY → users)
name (contact name)
inbound (the incoming message)
reply (the bot's response)
time (when message was sent)
created_at
```

---

## 🔐 Security

- **Password Hashing**: Bcrypt with salt
- **Authentication**: JWT tokens
- **Data Isolation**: Each user only sees their own data
- **Token Storage**: Stored in browser localStorage
- **HTTPS**: Recommended for production

---

## 🐛 Troubleshooting

### Backend won't start
- Ensure all dependencies are installed: `./linkedln/bin/pip install -r requirements.txt`
- Check port 9011 is not in use: `lsof -i :9011`
- Check .env file exists with JWT_SECRET

### Can't log in
- Verify admin was created: `./linkedln/bin/python setup_admin.py`
- Ensure database file exists at path specified in .env (default: `data/admin.db`)

### Extension not using prompt
- Reload extension in Chrome
- Clear browser cache
- Verify prompt is set as "Default" in portal
- Check browser console for errors

### Chat history not saving
- Verify auth token is stored in localStorage
- Check JWT token is valid
- Ensure background.js is running
- Check browser console for errors

---

## 📁 File Structure

```
linkedin-msg-tracker/
├── app_new.py                 # FastAPI backend (port 9011)
├── setup_admin.py             # Admin setup script
├── requirements.txt           # Python dependencies
├── .env                       # Configuration
└── linkedin_extension/
    ├── popup.html             # Extension popup (opens admin portal)
    ├── popup.js               # Popup button handler
    ├── content.js             # Sends messages to backend
    ├── background.js          # Saves chat history
    └── admin/
        ├── auth.html          # Login/register page
        ├── auth.js            # Auth logic
        ├── index.html         # Admin dashboard
        ├── app.js             # Dashboard logic
        └── styles.css         # Styling
```

---

## 📊 API Reference

### Authentication

**Login:**
```http
POST /admin/auth/login
Content-Type: application/json

{
  "username": "john_doe",
  "password": "MySecurePass123"
}

Response:
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "user_id": 1,
  "username": "john_doe"
}
```

### Prompts

**List Prompts:**
```http
GET /admin/prompts
Authorization: Bearer {access_token}

Response:
{
  "prompts": [
    {
      "id": 1,
      "name": "Cricket Coach",
      "description": "For cricket inquiries",
      "content": "You are replying on behalf of...",
      "is_default": true,
      "created_at": "2024-01-15T10:30:00"
    }
  ]
}
```

**Create Prompt:**
```http
POST /admin/prompts
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "name": "Sales Manager",
  "description": "For sales inquiries",
  "content": "You are replying on behalf of..."
}
```

### Chat Endpoint

**Send Message (with prompt_id):**
```http
POST /chat
Content-Type: application/json

{
  "message": "...",
  "prompt_id": 1
}

Response:
{
  "reply": "Thanks for reaching out..."
}
```

---

## ✅ Verification Checklist

- [ ] Admin account created successfully
- [ ] Backend server running on port 9011
- [ ] Can log in to admin portal
- [ ] Can create a new prompt
- [ ] Can set a prompt as default
- [ ] Extension shows "Open Admin Panel" button
- [ ] Can open admin portal from extension popup
- [ ] Extension sends messages with prompt_id
- [ ] Chat history displays in portal
- [ ] Can clear chat history

---

## 🚀 Next Steps

1. **Configure Production:**
   - Change JWT_SECRET in .env to a strong random value
   - Set DATABASE_URL for remote database
   - Enable HTTPS

2. **Add Features:**
   - Password reset functionality
   - Logout from all devices
   - Prompt templates library
   - Analytics dashboard

3. **Monitor & Maintain:**
   - Monitor server logs for errors
   - Back up database regularly
   - Review chat history for sensitive data

---

## 📞 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Review browser console for JavaScript errors
3. Check server logs for backend errors
4. Verify all files are in correct locations

---

**Admin Portal Implementation Complete! 🎉**

The system is now ready to use. Start with Step 1 of the Quick Start guide.
