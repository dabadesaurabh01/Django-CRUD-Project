# Django-CRUD-Project
# Author - Saurabh Dabade
# Book Management System 

A simple Django-based CRUD application for managing books using PostgreSQL.

## 🚀 Features
- Add a new book 📖
- View a list of books 📜
- Update book details ✏️
- Delete a book ❌

## 🛠️ Technologies Used
- **Django** - Backend framework
- **PostgreSQL** - Database
- **HTML, CSS** - Frontend templates

## 🔧 Installation & Setup



###  Create & Activate a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

###  Configure PostgreSQL Database
Ensure PostgreSQL is installed and running. Update the `settings.py` file:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'book_db',  # Change if necessary
        'USER': 'your_postgres_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser 
```bash
python manage.py createsuperuser
```

###  Run the Development Server
```bash
python manage.py runserver
```

### Access the Application
Open your browser and visit:
```
http://127.0.0.1:8000/
```

## 📂 Project Structure
```
book_management/
│── books/                # Django app for books management
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML Templates
│   ├── models.py         # Database models
│   ├── views.py          # Application logic
│   ├── urls.py           # URL Routing
│   ├── forms.py          # Forms for book management
│
│── book_management/      # Main Django project settings
│   ├── settings.py       # Project settings
│   ├── urls.py           # Root URL configurations
│   ├── wsgi.py           # WSGI entry point
│
│── manage.py             # Django command-line utility
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
```


