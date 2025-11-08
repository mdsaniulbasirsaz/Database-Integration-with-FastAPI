## Database Integration with FastAPI
This repository contains the exercises and projects completed during the FastAPI hands-on lab. The goal of this lab was to learn and practice building APIs using FastAPI, integrating with databases, and understanding core concepts of Python web development.

![alt text](image.png)

## Output
![alt text](api-docs.png)
![alt text](Ui1.png)
![alt text](ui2.png)

## Project Overview
This lab demonstrates:

- Creating REST APIs using **FastAPI**
- Connecting to databases using **SQLModel** and **SQLAlchemy**
- CRUD operations for a sample `Book` model
- Exploring FastAPI documentation with **Swagger UI**
- Using environment variables and `.env` for configuration

## Features

- Create, read, update, and delete books
- Async and sync API endpoints
- Auto-generated API documentation at `/docs` and `/redoc`
- MySQL database integration
- Easy-to-follow hands-on exercises

## Installation

1. Clone the repository:

```bash
git clone https://github.com/mdsaniulbasirsaz/Database-Integration-with-FastAPI
cd Database-Integration-with-FastAPI
```
2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Configure database in `.env`:
```
DATABASE_URL="mysql+pymysql://{username}:<password>@{host}:{port}/{database_name}"
API_TITLE="FastAPI Hands-On Lab API"
API_VERSION="1.0.0"
```
## Start the FastAPI server:
```
uvicorn app.main:app --reload
```
Open browser and visit:

API documentation: http://127.0.0.1:8000/docs

## API Endpoints
| Method | Endpoint           | Description         |
| ------ | ------------------ | ------------------- |
| GET    | /api/v1/books/     | List all books      |
| GET    | /api/v1/books/{id} | Get book by ID      |
| POST   | /api/v1/books/     | Create a new book   |
| PUT    | /api/v1/books/{id} | Update a book by ID |
| DELETE | /api/v1/books/{id} | Delete a book by ID |


## Database

1. MySQL is used as the database backend
2. SQLModel/SQLAlchemy for ORM
3. Database tables are created automatically at startup
4. Sample Book model fields:
```
title: str
author: str
year: int
price: float
in_stock: bool = True
description: Optional[str] = None
```

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request