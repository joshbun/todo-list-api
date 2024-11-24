# To-Do List API

A simple RESTful API built using **FastAPI** for managing a To-Do list. This project demonstrates how to create and manage a backend API with Python, PostgreSQL, and Docker.

---

## Features
- Create, read, update, and delete To-Do items.
- Uses PostgreSQL as the database.
- Dockerized for easy deployment.
- Interactive API documentation with Swagger UI.

---

## Installation and Setup

### Prerequisites
- Python 3.10+
- Docker and Docker Compose
- PostgreSQL (optional if using Docker)

### Clone the Repository
```bash
git clone <repository-url>
cd todo_api


Project Structure

todo_api/
├── app/
│   ├── __init__.py          # Empty initializer
│   ├── main.py              # Main application file
│   ├── models.py            # Database models
│   ├── schemas.py           # Pydantic schemas
│   └── database.py          # Database connection and setup
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker configuration for API
└── docker-compose.yml       # Docker Compose for API and PostgreSQL
