# Neonumy Photo Album

A simple Django-based photo album web application that allows you to upload, view, and manage images.

## Features

*   Image upload and storage
*   Thumbnail generation
*   Image detail view
*   Image deletion
*   RESTful API for CRUD operations
*   PostgreSQL database integration

## Requirements

*   Python 3.8 or higher
*   PostgreSQL
*   Django 4.0 or higher
*   Pillow
*   Django REST Framework

## Development Setup

1.  Clone the repository

    ```bash
    git clone https://github.com/yourusername/neonumy-photo-album.git
    cd neonumy-photo-album
    ```

2.  Create and activate a virtual environment

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Linux/macOS
    # venv\Scripts\activate  # On Windows
    ```

3.  Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

4.  Set up PostgreSQL database

    Make sure PostgreSQL is installed and running. Then create a database:

    ```bash
    # Connect to PostgreSQL
    psql -U postgres

    # Inside PostgreSQL shell, create a database
    CREATE DATABASE Your-DB-Name;
    \q
    ```

5.  Configure database settings

    Create .env file that contains the needed configurations:

    ```python
    
    SECRET_KEY=*****
    ENGINE_DB=*****
    NAME_DB=*****
    USER_DB=*****
    PASSWORD_DB=*****
    HOST_DB_DEV=***** # Here you can use the container ip addr or the service name 'db'
    PORT_DB=*****
    ```

6.  Apply migrations

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7.  Run the development server

    ```bash
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000/`

## API Endpoints

*   `GET /api/images/` - List all images
*   `POST /api/images/` - Create a new image
*   `GET /api/images/<id>/` - Retrieve a specific image
*   `PUT /api/images/<id>/` - Update an image
*   `DELETE /api/images/<id>/` - Delete an image

## Project Structure

*   `photos/` - Main app directory
    *   `models.py` - Contains the `Image` model
    *   `views.py` - Contains both web and API views
    *   `serializers.py` - API serializers
    *   `forms.py` - Forms for image upload
    *   `urls.py` - URL routing
    *   `templates/photos/` - HTML templates

## Bonus Tasks Implementation

### Docker Setup

If you want to run the application using Docker, a `Dockerfile` and `docker-compose.yml` file are provided.

Build and run the application with:

```bash
    cd To-Project-Path/ops/compose/dev && docker compose up --build -d 
```

