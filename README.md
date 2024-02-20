# Band App

## Introduction
This Django Capstone Project aims to create a Band App with user authentication features. This README provides documentation, Docker support, and instructions for building and running the application.

## Project Structure
The project structure includes the following directories:

- bandsite: The main Django project folder.
- user_auth: Django app for user authentication.
- myapp: Django app containing the project's running settings and URLs.
- docs: User-friendly documentation generated using Sphinx.

### Getting Started

## Prerequisites
Ensure you have the following prerequisites installed on your system:

- Python 3.12.1
- Django (install via requirements.txt)
- Docker (optional, for containerization)

## Installation
Clone the repository:

```bash
git clone https://github.com/Zaidbismillah/Band.git
cd bandsite

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

### Running the Application Locally

Run the development server:

python manage.py runserver

Access the application at http://127.0.0.1:8000/

Access the admin interface at http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

Using Docker (Optional)
Build the Docker image:

bash
Copy code
docker build -t band-app .
Run the Docker container:

bash
Copy code
docker run -p 8000:8000 band-app
Access the application at http://127.0.0.1:8000/

Access the admin interface at http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

Documentation
Explore the user-friendly documentation in the docs directory for more details on project structure, endpoints, and usage.

Credits
This project is developed by [Zaid Bismillah]. If you have any questions or suggestions, feel free to contact me. Contributions are welcome!


