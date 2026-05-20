# CTRL-ALT-ELITE
Welcome to the CTRL-ALT-ELITE-CAFE Mini-Project!
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Project background
The purpose of this project is to build a command line interface (CLI) cafe app (CTRL-ALT-ELITE-CAFE) in a busy business district. 
The cafe offers homemade lunches and drinks, and the client needs a simple but functional system to help manage products, couriers and customer orders. 

The project was developed during the Data Engineering Bootcamp with Generation. 

The app was built with:
* Python(weeks 1 - 6)
* CSV files for data persistence (weeks 1 - 4)
* PostgreSql database for products, couriers and orders (weeks 5 - 6)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Client Requirements

A week by week break down off what the client requried for this project: 

Week-1
* Create a product list 
* View all prodcuts
* Stretch goal; Update or delete a product

Week-2
* Create a product or order, and add it to the relevant list
* View all products or orders
* Stretch goal, update or delete a product or order

Week-3
* Create a product, courier, or order and add it to a list
* View all products, couriers, or orders
* Update the status of an order
* Persist my data (products and couriers)
* Stretch goal, update or delete a product, order, or courier

Week-4
* Create a product, courier, or order dictionary and add it to a list
* View all products, couriers, or orders
* Update the status of an order
* Persist my data
* Stretch goal, update or delete a product, order, or courier
* Bonus list orders by status or courier

Week-5
* Create a product or courier and add it to a database table
* Create an order and add the order dictionary to a list
* View all products, couriers, or orders
* Update the status of an order
* Persist my data
* Stretch goal, update or delete a product, order, or courier
* Bonus list orders by status or courier
* Bonus track my product inventory
* Bonus import/export my entities in CSV format
  
Week-6
* Create a product, courier, or order and add it to a table
* View all products, couriers, or orders
* Update the status of an order
* Persist my data in a database
* Stretch goal, delete or update a product, order, or courier
* Bonus display orders by status or courier
* Bonus import/export my entities in CSV format

Breakdown - 
* Maintain a collection of products and couriers 
  The app allows users to view, add, update, and delete products in both food/drink categories as well as the couriers.
  All data is sorted in dictionaries in lists and saved to .csv files. 

* When a customer makes a new order, to create this on the system 
  New customer orders can be created, viewed, updated, and deleted.
  Each order contains customers name, address, phone, chosen courier, status, and items ordered. 

* Update the status of an order i.e.: preparing, out-for-delivery, delivered. 
  All orders can be updated to reflect different status such as preparing, out-for-delivery, and delivered. 

* Upon exist off the app, all data to be persisted and not lost 
  All data for products, orders and couriers is saved to .csv files each time the app exists, so nothing is lost between app usage. This was from weeks 1 -4
  From weeks 5 - 6 - all data for products, couriers and orders have been updated to an postgreSQL Database and csv is no longer needed. 

* Upon starting the app, to load all persisted data 
  When the app loads it automatically loads all the latest saved data from sql database. 

* Need to be sure the app has been tested and proven to work well 
  The code is split across modules with functions making it easier to write unit tests for each individual part later.
  The code is split for better readability.

* Need to receive regular software updates. 
  The app is modular and uses functions for every menu action, which makes it easier to extend / improve without having to re-write everything.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Modules
  
  Main.py - Main application file which handles mnues and user navigation

  db.py - Create the database tables in PostgresSQL 
  
  Products.py - CRUD operations for products
  
  Couriers.py - CRUD operations for couriers
  
  Orders.py - CRUD operations for orders  
 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## How to run the app

1. To run the app you will first need to clone the repository - This will allow you to download all the codes and files to run the app
   https://github.com/DE-NAT4/CTRL-ALT-ELITE.git

2. You will then need to create and activate a virtual enviornment
   To do this you will need to run the following codes in your terminal -
   * python -m venv venv
   * for those with a windows device you will need to run - venv\scripts\activate
   * for those with a mac device you will need to run - source venv/bin/activate
     
3. Once you virtual enviorment is running you wll then need to install the dependecies and to do this you will need to run the following code in your terminal -
   pip install -r requirements.txt
   
4. You also need to ensure PostgreSQL is running and you have created the required database and tables.
   
5. Finally you are now ready to run the app - in your terminal you can run the app with the following code -
   python main.py 
----------------------------------------------------------------------------------------------------