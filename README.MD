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

payload = 
{
	"username": "<your_username>",
	"password": "<your_password>"
}

- method type: POST

You will obtain 2 tokens:
- access
- refresh

> Use the access token

## API Endpoints

### For Creation
- /plan/merchants/
- - Method type: POST

Payload - 
    {
	"merchant_name": "New merch"
}

- /plan/stores/
- - method type: POST

payload - 
    {
    "store_name": "New store",
    "store_address": "created by api",
    "s_latitude": null,
    "s_longitude": null,
    "merchant": 5
}

- /plan/items/
- - Method type: POST

payload - {
	"item_name": "new item - 1",
	"merchant": 6
}

### For Updation
- /plan/merchants/
- - Method type: PUT/PATCH

payload - {
	"merchant_name": "changed/new"
}

- /plan/stores/
- - Method type: PUT/PATCH

payload - {
	"store_name": "postman-updated-new",
	"store_address": "postman-add",
	"merchant": 5 
}

- /plan/items/
- - Method type: PUT/PATCH

payload - {
	"item_name":"updated",
	"merchant": 5
}

### For Deleting
- /plan/merchants/pk/
- - Method type: DELETE

- /plan/stores/pk/
- - Method type: DELETE

- /plan/items/pk/
- - Method type: DELETE

## For Retrieving
- /plan/merchants/
- - Method type: GET

- /plan/stores/
- - Method type: GET

-/plan/items/
- - Method type: GET

