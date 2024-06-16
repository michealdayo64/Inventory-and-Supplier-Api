# Inventory and Supplier Api Documentation

## Guideline on how to setup this project on your local machine

## Step 1: 
Clone project into your local machine. Open your terminal and paste the command: "git clone https://github.com/michealdayo64/Inventory-and-Supplier-Api"

## Step 1: 
Create virtual enviroment in your system. That's where you will install dependencies needed for this project
- Command for windows system: "virtualenv venv"
- Command for Mac and Linux system: "python3 -m venv venv"

## Step 2: 
Then you activate the virtual enviroment. cd into the venv folder
- Command for windows system: ".\scripts\activate"
- Command for Mac and Linux system: "source bin/activate"

## Step 3:
Install Dependencies for the project
- Command: "pip install -r requirements.txt"

## Step 4:
Run the project
- Command: "python manage.py runserver"


## All API Endpoint to test the project

You will need a postman application to test the endpoints. You can download postman from this Link: https://www.postman.com/downloads/

- User API Endpoint to view Inventory and Supplier data
  http://127.0.0.1:8000/inventory-api/user-create/
  
  request method: POST

 - API Endpoint for Supplier List Items
   http://127.0.0.1:8000/inventory-api/supplier-list-items/<param>/

   request method: PUT
   header authorization: token ""

- API Endpoint to view all items in the store
  http://127.0.0.1:8000/inventory-api/view-all-items/

   request method: GET
   header authorization: token ""

- API Endpoint to add Items
  http://127.0.0.1:8000/inventory-api/add_item/

   request method: POST
   header authorization: token ""

- API Endpoint to update an Item
  http://127.0.0.1:8000/inventory-api/update_item/1/

   request method: PUT
   header authorization: token ""

- API Endpoint to delete an item
  http://127.0.0.1:8000/inventory-api/remove_item/1/

   request method: DELETE
   header authorization: token ""

- API Endpoint to view suppliers of a particular item
  http://127.0.0.1:8000/supplier-api/view-suppliers-item/

   request method: POST
   header authorization: token ""

- API Endpoint to add Supplier
  http://127.0.0.1:8000/supplier-api/add-supplier/

   request method: POST
   header authorization: token ""

- API Endpoint to update supplier
  http://127.0.0.1:8000/supplier-api/update-supplier/4/

   request method: PUT
   header authorization: token ""

- API Endpoint to get all list of supplier
  http://127.0.0.1:8000/supplier-api/all-supplier-list/

   request method: GET
   header authorization: token ""

- API Endpoint to get a supplier detail information
  http://127.0.0.1:8000/supplier-api/all-supplier-list/

   request method: GET
   header authorization: token ""






