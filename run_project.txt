@echo off
cd c:\project\CROP
start "" http://127.0.0.1:8000/
python manage.py runserver
