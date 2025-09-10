# My Django Project

This is a Django-based web application that allows users to input multiple paragraphs, search for words, and get the top 10 paragraphs where the word occurs most frequently.

---

## Features

- User Authentication (Signup, Login, Logout)
- Paragraph Submission (Multiple paragraphs per submission)
- Word Frequency Search (Top 10 paragraphs where a word occurs most frequently)
- Password Reset via Email

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

### 5 Run the Development Server

python manage.py runserver




