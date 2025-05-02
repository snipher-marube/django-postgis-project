Collecting workspace informationHere is a professional README file for your project:

```markdown
# GeoDjango Project

This project is a Django-based application that leverages PostGIS for geospatial data management. Below are the steps to set up the project and configure the database.

## Prerequisites

1. **Python**: Ensure Python 3.13 is installed.
2. **PostgreSQL**: Install PostgreSQL with PostGIS extension.
3. **Django**: Install Django 5.2.
4. **Check PostgreSQL Version**:
   ```bash
   psql --version
   ```
   Ensure the version supports PostGIS.

## Setting Up the Database

1. **Create  PostgreaSQL Database**:
   ```bash
   sudo -u postgres createdb geodjango_db -O postgres
   ```

2. **Enable PostGIS Extension**:
   ```bash
   sudo -u postgres psql -d geodjango_db -c "CREATE EXTENSION postgis;"
   ```

## Configuring Django Settings

Update the `DATABASES` configuration in settings.py as follows:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'geodjango_db',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',  # Replace with your PostgreSQL password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Ensure `django.contrib.gis` is added to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'django.contrib.gis',  # Required for PostGIS
]
```

## Running the Project

1. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

3. Access the application at `http://127.0.0.1:8000`.

## Additional Notes

- For more information on PostGIS, visit the [PostGIS Documentation](https://postgis.net/documentation/).
- For Django GIS support, refer to the [Django GIS Documentation](https://docs.djangoproject.com/en/5.2/ref/contrib/gis/).

