# On Boarding Project

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


