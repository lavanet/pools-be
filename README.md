# Versions

Ubuntu 24.04

Python 3.12

Python dependencies listed in requirements.txt

https://www.djangoproject.com/

# Install dependencies

pip install requirements.txt

# Initiate database

python manage.py migrate

# Reset database

python manage.py startup

# Run tests

python manage.py test

# Run dev server

python manage.py runserver

# Recompile proto files

python compile_protos.py

# Apps Descriptions

    - apps.core.blockchains:
        Blockchain models and periodic tasks.

    - apps.core.lava_queries:
        Utils to fetch data from Lava nodes.

    - apps.api:
        REST public API for Lava. Read-only for all unauthenticated users.
        Swagger docs available at /api/swagger/
        Redoc docs available at /api/redoc/
