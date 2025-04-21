

```markdown
# 🛠️ Complaint Manager Web App

A simple Flask-based web application that allows users to register, log in, and submit complaints with optional images. Complaints are stored in JSON files, making it lightweight and easy to run without needing a database server.

---

## 🌐 Features

- User registration and login
- Complaint submission with:
  - Title
  - Description
  - Category
  - Location
  - Date & Urgency
  - Optional image upload
- Admin/User role support (future scope)
- JSON file storage (no external database needed)

---

## 🧰 Tech Stack

- Python 3.x
- Flask
- HTML, CSS (Jinja2 templating)
- JSON for data storage
- Gmail SMTP for email notifications

---

## 📁 Folder Structure

```
Complaint-Manager/
├── app.py                 # Main Flask app
├── db.py                  # JSON file interaction logic
├── static/
│   └── uploads/           # Uploaded complaint images
├── templates/             # HTML pages (login, register, complaint)
├── users.json             # Stores registered user data
├── complaints.json        # Stores submitted complaints
├── .env                   # Environment variables (email credentials)
└── README.md              # Project documentation
```

---

## ⚙️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/complaint-manager.git
cd complaint-manager
```

2. **Create a virtual environment and activate it**

```bash
python -m venv .venv
source .venv/bin/activate     # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install flask python-dotenv
```

4. **Create `.env` file**

```

> 💡 Make sure "2-Step Verification" is enabled in your Google account to generate an App Password.  
> Guide: https://support.google.com/accounts/answer/185833?hl=en

5. **Create `users.json` and `complaints.json`**

```json
// users.json
[]

---

// complaints.json
[]
```

6. **Run the App**

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## ✉️ Email Setup Tips

- SMTP Server: `smtp.gmail.com`
- Port: `587`
- Requires Gmail **App Password**, not your normal password.

---

## 🚀 Future Improvements

- Admin dashboard for complaint management
- Search and filter complaints
- Image preview support
- Email verification on registration
- Database migration (SQLite or PostgreSQL)

---

## 📝 License

This project is open-source and free to use for educational or non-commercial purposes.

---

## 🙌 Acknowledgements

Thanks to Flask and Python's simplicity for enabling quick prototyping and development!
```
