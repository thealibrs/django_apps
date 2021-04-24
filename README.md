# Some Django Helpers

### Start App

```django-admin startproject "project-name" ```

### Run Server
``` python manage.py runserver ```

### Creating Default DB Tables
```python manage.py migrate``` 

### Creating Super User
```python manage.py createsuperuser```

### Creating App
```python manage.py startapp "app-name"``` than dont forget to save into **INSTALLED_APPS**

### Run this command whenever created Models
```python manage.py makemigrations``` and then 
run ```python manage.py migrate``` and then add your model into admin.py like
``` admin.site.register(model-name)```
