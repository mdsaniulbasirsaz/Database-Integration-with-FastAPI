import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from app.database import create_db_and_tables
from app.api import router
from dotenv import load_dotenv

load_dotenv()

API_TITLE = os.getenv("API_TITLE", "BookStore API")  
API_VERSION = os.getenv("API_VERSION", "1.0.0")  
ROOT_PATH = os.getenv("ROOT_PATH", "") 

if ROOT_PATH:
    app = FastAPI(root_path=ROOT_PATH, title=API_TITLE, version=API_VERSION)
else:
    app = FastAPI(title=API_TITLE, version=API_VERSION)

    # Add CORS middleware
origins = [
    "http://localhost",         # Allow localhost
    "http://127.0.0.1:5500", 
    "http://127.0.0.1:5500/index.html"   # Allow frontend port
    # Add other domains as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Origins allowed to make requests
    allow_credentials=True,
    allow_methods=["*"],         # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],         # Allow all headers
)


# Define a route for "/"
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.on_event("startup")
def on_startup():
    # Ensure the database and tables are created
    create_db_and_tables()

# Include the router for API versioning
app.include_router(router, prefix="/api/v1")
