# Backend

Petition Management System Backend

## Installation

    pip install -r requirements.txt

## Usage

    python manage.py makemigrations api
    python manage.py migrate
    python add_permission.py
    python populate.py
    python manage.py runserver

## Note

Before running migration comment these lines in urls.py

    from api.tasks import fetch_users, fetch_organizations
    from background_task.models import Task
    if not Task.objects.filter(verbose_name="fetch_users").exists():
        fetch_users(repeat=5, repeat_until=None, verbose_name="fetch_users")
    if not Task.objects.filter(verbose_name="fetch_organizations").exists():
        fetch_organizations(repeat=5, repeat_until=None, verbose_name="fetch_organizations")

