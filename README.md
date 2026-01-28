# FastAPI Backend with PostgreSQL

This project is a backend application built using FastAPI and PostgreSQL, with a focus on clean API design, database integration, and environment-based configuration.

The main purpose of this project is to demonstrate backend development skills such as secure database connectivity, proper project structure, and professional Git practices.

---

## Tech Stack

- Backend Framework: FastAPI
- Database: PostgreSQL
- ORM: SQLAlchemy
- ASGI Server: Uvicorn
- Language: Python 3

---

## Project Structure

fastapi-backend-postgres/
│
├── main.py                # FastAPI application entry point
├── database.py            # Database connection and session management
├── models.py              # SQLAlchemy models
├── database_models.py     # Database-related schemas / models
├── requirements.txt       # Project dependencies
├── .gitignore             # Ignored files and folders
└── frontend/              # Frontend scaffold (not the main focus)

Note:  
The frontend directory exists as a scaffold. The primary focus of this project is backend development.

---

## Database Configuration

The application uses environment variables for database configuration to ensure security and production readiness.

Required environment variable:

DATABASE_URL=postgresql://username:password@host:port/database_name

Example (Local Development – PowerShell):

$env:DATABASE_URL="postgresql://postgres:password@localhost:5432/fastapi_db"

Database credentials are never hardcoded and are intentionally excluded from the repository.

---

## Running the Project Locally

1. Clone the repository:
git clone https://github.com/dishambha/fastapi-backend-postgres.git  
cd fastapi-backend-postgres

2. Create and activate a virtual environment:
python -m venv myenv  
myenv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Set the database environment variable (see above).

5. Start the FastAPI server:
uvicorn main:app --reload

6. Open API documentation in your browser:
http://127.0.0.1:8000/docs

---

## Key Highlights

- Clean FastAPI project structure
- PostgreSQL integration using SQLAlchemy
- Environment-based configuration for production readiness
- Secure handling of database credentials
- Clean Git history and repository hygiene

---

## Future Improvements

- Authentication using JWT
- Role-based access control
- Cloud deployment
- Full frontend integration

---

## Author

Dishambha Awasthi  
B.Tech Computer Science Engineering  
Aspiring Backend / Software Engineer


