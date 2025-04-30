# Django To-Do List

A simple task management web application built with Python and Django.  
Users can register, log in, add tasks, edit them, mark as completed, delete, and view their progress.

## Features

- User authentication (registration, login, logout)
- Create, edit, delete, and complete tasks
- Task status tracking
- Task completion progress bar
- Responsive design with Bootstrap 5

## Technologies Used

- Python 3
- Django
- HTML & CSS
- Bootstrap 5
- SQLite (default Django database)
- Git & GitHub for version control

## Setup Instructions

1. Clone the repository:
 
   git clone https://github.com/DoNeR997/django-todo-list.git
   cd django-todo-list
2. Create and activate a virtual environment:
 
 python -m venv venv
venv\Scripts\activate  # on Windows
3. Install dependencies:

  pip install -r requirements.txt
4. Apply migrations and start the development server:

python manage.py migrate
python manage.py runserver
5.Open your browser and go to:

http://127.0.0.1:8000/


