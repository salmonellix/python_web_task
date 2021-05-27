PYTHON WEB DEVELOPMENT TASK 
=====

## Description ##


It is a website design displaying data sorted by state and city. 

**FEATURES:** 

### Left Panel: ###

:ballot_box_with_check: Smaller width showing for each state number of row, city name, number of people living there.

:ballot_box_with_check: Each count links to right panel with details for each city

:ballot_box_with_check: Shows only cities with number of people >= 2

:ballot_box_with_check: States are sorted alphabetically

:ballot_box_with_check: Cities in each table are sorted by counts

###  Right Panel: ###

:ballot_box_with_check: Shows people from each city

:ballot_box_with_check: Shows details for each person (Name, Surname, Email), sorted alphabetically by first name


## Getting Started ##


**1. Install requirements** 
```   
pip install -r requirements.txt
```

**2. Edit project settings**

+ Open settings file ./web_task/web_task/settings.py
+ Edit Database configurations with your MySQL configurations - Search for DATABASES section.
```   
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'addressbook',
        'USER': '<mysql-user>',
        'PASSWORD': '<mysql-password>',
        'HOST': '<mysql-host>',
        'PORT': '<mysql-port>',
    }
}
```
+ Save the file

**3. Run server** 
+ Make migrations

```
python manage.py makemigrations
python manage.py migrate
```
+ Run server
```
python manage.py runserver
```

**4. Open [http://localhost:8000](http://localhost:8000) in browser**