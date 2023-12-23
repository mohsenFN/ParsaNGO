# Parsa NGO Sms Processing and ‌Booking System

[![LICENSE](https://img.shields.io/badge/LICENSE-GPL--3.0-green)](https://github.com/mohsenFN/ParsaNGO/blob/main/LICENSE) 
[![Requirements](https://img.shields.io/badge/Requirements-See%20Here-orange)](https://github.com/mohsenFN/ParsaNGO/blob/main/requirements.txt)

This Project is done by Mohsen FN for a charity company named Parsa NGO 

<div dir="rtl"> 
این یک پروژه برای دریافت و پردازش و ارسال اسمس به کاربران و همچنین انتقال آن ها به صفحه رزرو اصلی برای همایش این خیریه میباشد.
این پروژه برای خیراندیشان پارسا یک خیریه در سطح کشوری انجام شده است.

- پایتون
- جنگو
- ای پی آی های دریافت و ارسال اسمس از درگاه ملی پیامک
- مای اسکوئل/ماریا دیبی

</div>

## How to run
1. Install python3, pip3, virtualenv, MySQL in your system.
2. Clone the project `git clone https://github.com/mohsenFN/ParsaNGO.git`
3. edit `app/SETTINGS_CONFIG.py` and `v1/API_CONFIG.py` based on your usage.
4. db configs are in SETTINGS_CONFIG.py. 
5. Create a virtualenv.
6. Connect to virtualenv.
7. From the project folder, install packages using `pip install -r requirements.txt`
8. Now environment is ready. Run it !

## Example of creating db and granting access:

> Note: this is just a sample. You have to find your own systems commands.



#### Create a database for saving phone-numbers and bookings
```
CREATE DATABASE DB_NAME;
```

#### Install venv and run following command for installing requirements
```
source venv_name/bin/activate --> (to activate virtual env)
pip install -r requirements.txt --> (installing necessary libraries)
```

#### Migrate database models in your database
```
python manage.py makemigrations
python manage.py migrate
```
#### Running App (default settings are for local host !)
```
python manage.py runserver
```