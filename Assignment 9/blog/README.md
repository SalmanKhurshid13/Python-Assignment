# Django REST Framework Blog Post API

## Project Overview

This project is a RESTful Blog Post Management API developed using Django and Django REST Framework (DRF). It allows authenticated users to create, read, update, and delete their own blog posts. The API also supports filtering, searching, ordering, and pagination.

---

## Features

- User Authentication
- CRUD Operations for Blog Posts
- Custom Permissions (Users can edit/delete only their own posts)
- Search Blog Posts
- Filter Blog Posts by Creation Date
- Order Blog Posts by ID
- Pagination (5 posts per page)
- JSON API Responses
- Django Admin Panel

---

## Technologies Used

- Python 3
- Django
- Django REST Framework
- SQLite3
- django-filter

---

## Project Structure

```
blog/
│
├── blog/
│   ├── settings.py
│   ├── urls.py
│
├── helloworld/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── filters.py
│   ├── urls.py
│   ├── admin.py
│
├── manage.py
├── db.sqlite3
└── README.md
```

---

## Installation

Clone the repository or extract the ZIP file.

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

macOS/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install django djangorestframework django-filter
```

Apply migrations:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

---

## API Endpoints

### Login

```
/api-auth/login/
```

### Blog Posts

```
GET    /api/posts/
POST   /api/posts/
GET    /api/posts/<id>/
PUT    /api/posts/<id>/
PATCH  /api/posts/<id>/
DELETE /api/posts/<id>/
```

---

## Search

```
/api/posts/?search=blog
```

---

## Filter

```
/api/posts/?created_at=YYYY-MM-DD
```

Example:

```
/api/posts/?created_at=2026-07-29
```

---

## Ordering

```
/api/posts/?ordering=id
```

---

## Pagination

The API returns **5 blog posts per page**.

---

## Authentication

The API uses Django Session Authentication.

Only authenticated users can access the API.

Users can only update or delete their own blog posts.

---

## Testing

Run:

```bash
python manage.py check
python manage.py test
```

---

## Author

**Salman Khurshid**


---

## License

This project is created for educational purposes as part of a Django REST Framework assignment.