# My Django Project

This is a Django-based web application that allows users to input multiple paragraphs, search for words, and get the top 10 paragraphs where the word occurs most frequently.

---

## Features

- User Authentication (Login / Signup / Logout)
- Password Reset via Email
- Add Multiple Paragraphs in One Submission
- Search Word Across Paragraphs
- Show Top 10 Paragraphs Based on Word Frequency
- Containerized with Docker

---

## Prerequisites

- Python 3.11+
- pip (Python package manager)
- Virtualenv (Recommended)
- Git

---

## Setup Instructions

### 1 Clone the Repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

### 2 Create Virtual Environment
python -m venv venv
source venv/bin/activate      # For Linux/Mac
venv\Scripts\activate         # For Windows

### 3 Install Dependencies

pip install -r requirements.txt

### 4 Apply Database Migrations

python manage.py migrate
python manage.py migrate

### 5 Run the Development Server

python manage.py runserver

Using Docker (Optional)

Build Docker Image
docker compose build

Start the Containers
docker compose up

