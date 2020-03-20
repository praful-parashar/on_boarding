# On Boarding Project

## Introduction

This project covers basic flow of a transactional system. 

### For setting up the project

- Prerequisites:
  - python 3.x
  - virtualenv

- clone the repository

- Set up virtualenv

	- ```$ python -m venv venv```
	- ```$ source venv/bin/activate```

- cd into project directory

	- ``` $ pip install -r requirements.txt```

> You might face issues while setting it up, I have addressed the ones I think you will at the end of this README. Go and have a look.

So after successfully setting up the project. It's time for the django drill
```

$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver

```

Your application is now running at:
http://127.0.0.1:800/plan/

Now for the API endpoints to work 
you need to authorize your user.

Token Endpoint
> http://127.0.0.1:8000/plan/api/token/
```
{
	"username": "<your_username>",
	"password": "<your_password>"
}
```

- method type: POST

You will obtain 2 tokens:
- access
- refresh

> Use the access token with `Bearer` prefix
for eg.: In request header:
```
'Authorization': 'Bearer <JWT_ACCESS_TOKEN>'
```

## API Endpoints

### For Creation - Method Type: POST

- /plan/merchants/
 
```
{	
 "merchant_name": "New merch"
}
```


- /plan/stores/

```
{
	"store_name": "New store",
    "store_address": "created by api",
    "s_latitude": null,
    "s_longitude": null,
    "merchant": 5
}
```

- /plan/items/

```
{
	"item_name": "new item - 1",
	"merchant": 6
}
```

### For Updation - Method Type: PUT/PATCH
- /plan/merchants/pk/

```
{
	"merchant_name": "changed/new"
}
```

- /plan/stores/pk/

```
{
	"store_name": "postman-updated-new",
	"store_address": "postman-add",
	"merchant": 5 
}
```

- /plan/items/pk/

```
{
	"item_name":"updated",
	"merchant": 5
}
```

### For Deleting - Method Type: DELETE
- /plan/merchants/pk/

- /plan/stores/pk/

- /plan/items/pk/

### For Retrieving - Method Type: GET
- /plan/merchants/

- /plan/stores/

- /plan/items/

## Issues You can face while setting up the project

### 1. Error while installing `mysqlclient`
- It is possible that your python3 version is not compatible with the mysqlclient, probably python3.7.5
- you will need to install python3.6 which is compatible with mysqlclient.
- Link for github repo through which multiple verisons of python can exist on your system - https://github.com/pyenv/pyenv
- The readme of this repo very well explains the installation part of different versions of python.
- Still I would jot down the steps you'll need 
	- clone the repo - Pyenv
	- set env variables in your ~/.bashrc and restart terminal
	- cd into the project directory - Onboarding_project
	- Run this command ``` $pyenv local 3.6.5```
- After these steps a file will be created as .python-version - which specifies the python version in that directory
- create virtualenv and source into it

### 2. Setting up root user in mysql with all the permissions.
```
Access denied to user 'root'@'localhost'
```
- If you have an existing user with all the permissions granted. Make the credential changes in the `settings` file against DB configurations.
- But, If you have installed mysql-server for the first time. Chances are that you have to grant permissions to root user yourself.
-  There are several links to follow on google, I found this one best: [link](https://stackoverflow.com/questions/41542045/mysql-django-db-utils-operationalerror-1698-access-denied-for-user-root)

