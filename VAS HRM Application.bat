@echo off
REM Change directory to where your Django project is located
cd E:\Software Developments\SBT HRM
REM Activate virtual environment if you have one
call env\Scripts\activate


REM Start Django development server
cd E:\Software Developments\SBT HRM\master
python manage.py runserver 192.168.1.11:8000
