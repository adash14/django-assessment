# Django Polls Project

This is a Django web application created as part of a Django learning assignment. The project allows users to view poll questions, select answer choices, submit votes, and view voting results. It also includes a customized Django admin interface for managing poll questions and choices.

## Project Overview

The purpose of this project is to practice the core features of Django, including:

* Creating a Django project and app
* Defining database models
* Running migrations
* Using Django’s object-relational mapper, or ORM
* Creating views and URL routes
* Rendering HTML templates
* Handling form submissions
* Using generic class-based views
* Adding static files such as CSS and images
* Customizing the Django admin page

## Technologies Used

* Python
* Django
* SQLite
* HTML
* CSS

## Main Features

### Poll Questions

The application displays a list of recent poll questions. Users can click on a question to view the available answer choices.

### Voting

Users can select one answer choice and submit their vote. After voting, the app redirects users to a results page that shows the current vote totals.

### Results Page

The results page displays each answer choice for a question along with the number of votes it has received.

### Admin Interface

The project uses Django’s built-in admin site to manage poll data. The admin interface allows an authenticated admin user to add, edit, and delete questions and choices.

The admin page was customized to improve usability by adding:

* Organized field sections
* Inline answer choices
* A question list display
* Date filters
* Search functionality

## How to Run the Project

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Go Into the Project Folder

```bash
cd YOUR_PROJECT_FOLDER_NAME
```

### 3. Install Django

```bash
python -m pip install Django
```

### 4. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

### 6. Open the Website

Open this URL in your browser:

```text
http://127.0.0.1:8000/polls/
```

If localhost does not work on your computer, use:

```text
http://127.0.0.1:8000/
```

or run the server with:

```bash
python manage.py runserver 0.0.0.0:8000
```

## Admin Page

The Django admin page can be opened at:

```text
http://127.0.0.1:8000/admin/
```

To create an admin user, run:

```bash
python manage.py createsuperuser
```

Then follow the prompts to create a username, email, and password.

## Project Structure

```text
djangotutorial/
    manage.py
    db.sqlite3
    README.md

    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py

    polls/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        urls.py
        views.py

        migrations/
            __init__.py
            0001_initial.py

        templates/
            polls/
                index.html
                detail.html
                results.html

        static/
            polls/
                style.css
                images/
                    background.png
```

## Important Files

### `manage.py`

This is the command-line utility used to interact with the Django project. It is used to run commands such as:

```bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### `mysite/settings.py`

This file contains the main settings for the Django project. It includes configuration for installed apps, the database, templates, static files, and development settings.

The `polls` app is added to `INSTALLED_APPS` so Django can detect its models, templates, static files, and admin settings.

### `mysite/urls.py`

This file contains the main project URL routes. It connects the project-level URLs to the polls app using `include()`.

### `polls/models.py`

This file defines the database structure for the app.

The project uses two main models:

* `Question`: Stores the poll question text and publication date.
* `Choice`: Stores answer choices connected to a specific question and tracks the number of votes.

The `Choice` model uses a foreign key relationship so that each choice belongs to one question.

### `polls/views.py`

This file controls the logic for each page.

The project includes views for:

* Displaying the latest poll questions
* Showing details for one question
* Showing results for one question
* Handling vote submissions

The project also uses Django generic views, including `ListView` and `DetailView`, to reduce repeated code.

### `polls/urls.py`

This file maps URL patterns to the correct views in the polls app.

The app includes routes for:

* The polls index page
* The question detail page
* The results page
* The vote submission page

The app uses the namespace `polls` so templates can refer to routes using names such as:

```django
{% url 'polls:detail' question.id %}
```

This avoids hardcoding URLs directly in HTML files.

### `polls/templates/polls/`

This folder contains the HTML templates for the polls app.

Important templates include:

* `index.html`: Displays the latest questions
* `detail.html`: Displays a question and its answer choices
* `results.html`: Displays vote totals

### `polls/static/polls/style.css`

This file contains the CSS styling for the polls app. Static files are loaded into templates using Django’s `{% static %}` template tag.

### `polls/admin.py`

This file customizes how the polls app appears in the Django admin interface.

The admin page includes:

* Inline choices for each question
* Organized fieldsets
* A list display for questions
* Filters by publication date
* A search box for question text

## Database and Migrations

This project uses SQLite as the database.

After creating or changing models, migrations are created with:

```bash
python manage.py makemigrations
```

The migrations are applied to the database with:

```bash
python manage.py migrate
```

Migrations allow Django to translate Python model changes into database table changes.

## How the Voting System Works

The detail page displays a form with radio buttons for each answer choice.

When a user submits the form:

1. The selected choice ID is sent using a POST request.
2. Django checks which choice was selected.
3. The vote count for that choice increases by 1.
4. The user is redirected to the results page.

The form uses Django’s `{% csrf_token %}` tag to protect against cross-site request forgery attacks.

## Static Files

The project includes static files for styling and images.

The CSS file is stored in:

```text
polls/static/polls/style.css
```

Images can be stored in:

```text
polls/static/polls/images/
```

The static file is loaded in the template with:

```django
{% load static %}
<link rel="stylesheet" href="{% static 'polls/style.css' %}">
```

## What I Learned

Through this project, I learned how Django connects the backend, database, and frontend of a web application.

I practiced using Django models to define data, migrations to create database tables, views to control page behavior, templates to display dynamic content, and URL routing to connect browser paths to Python code.

I also learned how Django’s admin interface can quickly create a usable backend for managing data. By customizing the admin page with inline choices, filters, search fields, and organized fieldsets, I was able to make the admin interface easier to use.

This project helped me understand how a static design or prototype can become a working web application with real data, user interaction, and database updates.

## Running Tests

To run tests for the polls app, use:

```bash
python manage.py test polls
```

## Notes

This project was created for a Django learning assignment. The code, settings, and project structure are documented so that another person can understand, run, and review the project more easily.
