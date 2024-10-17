# Example-Pagination-FastAPI
- The example shows how to create the pagination API with FastAPI and using MySQL as a database.
- The article of this repository https://blog.stackpuz.com/create-a-pagination-api-with-fastapi
- To find more resources, please visit https://stackpuz.com

## Prerequisites
- Python 3.10
- MySQL

## Installation
- Clone this repository `git clone https://github.com/stackpuz/Example-Pagination-FastAPI`
- Activate virtual environment and install packages. `pip install -r requirements.txt`
- Create a new database and run [/database.sql](/database.sql) script to create tables and import data.
- Edit the database configuration in [/.env](/.env) file.

## Run project

- Run project `uvicorn app.main:app`
- Navigate to http://localhost:8000