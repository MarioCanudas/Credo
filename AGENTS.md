# Project Description
Credo is a Fintech API designed to determine the approval of loans or credit cards for new users. The decision engine relies on a machine learning model that analyzes a user's credit history and personal data (such as income, education, employment, and debt history, as defined in `app/models/user_model.py`). While structurally straightforward, it performs a highly critical banking function.

# Technology Stack
- **API Framework:** FastAPI
- **Machine Learning:** Scikit-learn, XGBoost
- **Database & ORM:** SQLModel, SQLite
- **Package Management & Execution:** uv
- **Linting & Typing (LSP):** BasedPyright, Ruff

# Agent Persona & Coding Guidelines
- **Pythonic Code:** Always write idiomatic Python code.
- **Type Hinting:** Make extensive and rigorous use of type hints across all code.
- **API Standards:** Act as an expert in REST APIs. Ensure endpoints, status codes, and responses follow standard RESTful conventions.
- **LSP Compliance:** Ensure all code conforms strictly to Ruff and BasedPyright standards.

# Project Architecture

## `/app` (Main API Directory)
- `/app/api/`: Contains all FastAPI route definitions, routers, and endpoint logic.
- `/app/core/`: Core application configuration, constants, settings, and lifecycle events.
- `/app/db/`: SQLModel classes representing the database tables (database schema).
- `/app/enums/`: Enumeration classes (Enums) used for data validation and strict typing across the application.
- `/app/models/`: SQLModel/Pydantic models used for request/response validation and Data Transfer Objects (DTOs).
- `/app/services/`: Microservices containing the core business logic. This separation ensures code readability, modularity, and easier testing.
- `/app/main.py`: The main FastAPI application entry point.

## `/ml_engine` (Machine Learning Engine)
Contains all components related to the machine learning pipelines, including training scripts, datasets, preprocessors, and artifacts (like the serialized models).
## `/tests` (Test Suite)
Contains unit and integration tests to ensure the application's reliability and correct business logic execution.