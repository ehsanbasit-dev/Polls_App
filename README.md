# Django Polls App

## About the Project

This is a simple **Polls Web Application built using Django**.
Users can view poll questions, select a choice, and see the voting results.

This project was created while learning Django using the **official Django documentation tutorial**.

## Features

* View poll questions
* Vote for a choice
* See voting results
* Admin panel to manage polls

## Technologies Used

* Python
* Django
* HTML
* SQLite
* Git & GitHub

## Project Structure

Polls_App
│
├── Polls_App/        # Project settings
├── polls/            # Polls application
├── manage.py         # Django management file
├── requirements.txt  # Project dependencies
└── README.md

## Installation

### 1 Clone the repository

git clone https://github.com/ehsanbasit-dev/Polls_App.git

### 2 Go to project folder

cd Polls_App

### 3 Create virtual environment

python -m venv venv

### 4 Activate virtual environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 5 Install dependencies

pip install -r requirements.txt

### 6 Run migrations

python manage.py migrate

### 7 Run the development server

python manage.py runserver

Open in your browser:
http://127.0.0.1:8000/polls/

## Admin Panel

Create admin user:

python manage.py createsuperuser

Admin URL:
http://127.0.0.1:8000/admin/

## Author

**Ehsan Basit**
BS Software Engineering
Backend Developer (Python / Django)
