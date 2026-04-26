# 🛒 Mystore - Django E‑Commerce Project

## 📌 Overview
Mystore is a full‑stack e‑commerce web application built with **Django**.  
It allows users to browse and purchase products such as **laptops, PCs, and tablets**, with features like product listings, shopping cart, and checkout.

---

## 🚀 Features
- User authentication (sign up, login, logout)
- Product catalog (laptops, PCs, tablets)
- Add to cart and manage cart items
- Order placement and checkout flow
- Admin dashboard for product management
- Responsive design with Django templates

---

## 🛠️ Tech Stack
- **Backend:** Django (Python)
- **Database:** SQLite (default) or PostgreSQL/MySQL
- **Frontend:** HTML, CSS, Bootstrap
- **Version Control:** Git + GitHub

---

## 📂 Project Structure
mystore/
├── mystore/          # Main Django project settings
├── products/         # App for product management
├── templates/        # HTML templates
├── static/           # CSS, JS, images
├── db.sqlite3        # Database (local dev)
└── manage.py

---

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/sattiprasanna0916-prog/mystore.git
   cd mystore
Create and activate a virtual environment:

bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
Install dependencies:

bash
pip install -r requirements.txt
Run migrations:

bash
python manage.py migrate
Start the development server:

bash
python manage.py runserver
Open in browser:

Code
http://127.0.0.1:8000/