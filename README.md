# Real-Time-Chat-Application-Backend-Django# 🗨️ Real-Time Chat Application Backend (Django)

Welcome to the **Real-Time Chat Application Backend**! 🚀 This Django-powered backend is the magic behind seamless, real-time communication. With WebSockets, Django Channels, and a solid database setup, you're on your way to building the next big thing in chat applications. Buckle up, and let’s dive in! 🎉

---

## 📌 Features

✅ **Blazing-fast real-time messaging** with Django Channels & WebSockets ⚡  
✅ **Secure user authentication** (Signup, Login, JWT-based auth) 🔐  
✅ **Private & group chat support** 🎭  
✅ **Persistent message storage** using PostgreSQL 📦  
✅ **Scalable architecture** with Redis and ASGI 🏗️  
✅ **Well-structured RESTful API** for frontend integration 🌐  
✅ **Robust testing** with Pytest & Django’s Test Framework 🧪  

---

## 🛠️ Tech Stack

| Technology    | Purpose |
|--------------|---------|
| **Django**   | Backend framework |
| **Django Channels** | Handles real-time WebSocket communication |
| **PostgreSQL** | Stores chat messages and user data |
| **Redis** | Enables fast, in-memory messaging and caching |
| **DRF (Django Rest Framework)** | API development |
| **JWT (JSON Web Tokens)** | Ensures secure authentication |
| **Pytest** | Runs automated tests |
| **Docker** | Containerizes the application |

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/real-time-chat-backend.git
cd real-time-chat-backend
```

### 2️⃣ Create & Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file and configure:
```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://username:password@localhost:5432/chatdb
REDIS_URL=redis://localhost:6379
```

### 5️⃣ Run Database Migrations
```bash
python manage.py migrate
```

### 6️⃣ Start Redis Server (if not running)
```bash
redis-server
```

### 7️⃣ Run the Development Server
```bash
python manage.py runserver
```

### 8️⃣ Run WebSocket Server
```bash
python manage.py runworker
```

🎉 Your chat backend is now live!

---

## 🧪 Running Tests

To ensure everything is running smoothly:
```bash
pytest
```

---

## 📖 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/api/auth/register/` | Register a new user |
| `POST` | `/api/auth/login/` | Login and receive JWT token |
| `GET` | `/api/chat/rooms/` | Fetch available chat rooms |
| `POST` | `/api/chat/rooms/create/` | Create a new chat room |
| `GET` | `/api/chat/messages/{room_id}/` | Retrieve messages from a chat room |
| `POST` | `/api/chat/messages/send/` | Send a message |

---

## 🚢 Deploying to Production

To make your app production-ready:
- Use **Gunicorn** or **Daphne** as an ASGI server
- Set `DEBUG=False` in `.env`
- Ensure **PostgreSQL** is used instead of SQLite
- Deploy **Redis** for WebSockets

---

## 👨‍💻 Contributing

Want to improve this project? Fantastic! 🎉
1. **Fork** the repository
2. **Create a feature branch** (`git checkout -b feature/your-feature`)
3. **Make your changes** and commit (`git commit -m 'Added cool feature'`)
4. **Push to GitHub** (`git push origin feature/your-feature`)
5. **Submit a Pull Request** and let’s make it better together!

---

## 📞 Contact
Got questions? Let's connect! 🚀
- 📧 Email: harish.s@kalvium.community
- 🐙 GitHub: [Harish Karthick S](https://github.com/HarishKarthickS)

---

### 🎉 Happy Coding & Chatting! 🚀💬

