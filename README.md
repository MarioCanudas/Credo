<div align="center">
<h1>Credo - Credit Score API v1.0.0</h1>

**A FastAPI-based Credit Score Prediction API powered by TensorFlow Machine Learning Models**

[Features](#features) • [Quick Start](#quick-start) • [Usage Examples](#usage-examples) • [API Documentation](#api-documentation) • [Roadmap](#roadmap) 
</div>

---

## Overview

Credo is a modern, scalable Credit Score API designed specifically for Fintech applications. It leverages machine learning models built with TensorFlow to predict credit scores based on financial history and application data. The API is built with FastAPI, providing high performance, automatic documentation, and easy integration.

### Key Highlights
- **High Performance** - Built on FastAPI for lightning-fast inference
- **ML-Powered** - ML models for accurate credit predictions
- **Easy Integration** - RESTful API with automatic Swagger/OpenAPI documentation
- **Production-Ready** - Designed with Fintech requirements in mind
- **Scalable** - Ready for deployment in cloud environments

---

## Tech Stack

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Python Version**: 3.9+
- **Database**: Sqlite (SQLModel)
- **ML Framework**: TensorFlow / Keras
- **Package Manager**: [UV](https://docs.astral.sh/uv/)

---

## Installation

### Prerequisites
- Python 3.10 or higher
- [UV](https://docs.astral.sh/uv/) package manager

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/MarioCanudas/credo.git
cd credo
```

2. **Install dependencies with UV**
```bash
uv sync
```

3. **Activate virtual environment**
```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Start the API

```bash
uv run fastapi dev app/main.py
```

The API will be available at `http://127.0.0.1:8000`.

---

## Quick Start

Once the API is running, you can start making requests. The typical workflow is:
1. **Create a User** with their financial profile.
2. **Submit a Credit Application** for that user to get a prediction.

### 1. Create a User
```bash
curl -X POST "http://127.0.0.1:8000/users/" \
     -H "Content-Type: application/json" \
     -d '{
           "gender": "m",
           "car": true,
           "realty": true,
           "cnt_children": 0,
           "income": 200000,
           "income_type": "working",
           "education_type": "higher_education",
           "fam_status": "married",
           "housing_type": "house",
           "mobile_phone": true,
           "work_phone": true,
           "phone": true,
           "email": true,
           "job_title": "managers",
           "cnt_fam_members": 2,
           "age": 35,
           "work_experience": 10,
           "bad_debt": 0,
           "good_debt": 5
         }'
```

### 2. Request Credit Prediction
```bash
curl -X POST "http://127.0.0.1:8000/applications/" \
     -H "Content-Type: application/json" \
     -d '{"user_id": 1}'
```

---

## API Documentation

Credo provides automatic documentation via Swagger UI. Once the server is running, navigate to:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Core Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/users/` | Create a new user profile |
| `GET` | `/users/{user_id}` | Retrieve user profile details |
| `PUT` | `/users/{user_id}` | Update an existing user profile |
| `DELETE` | `/users/{user_id}` | Delete a user and their data |
| `POST` | `/applications/` | Submit a credit application (Predicts status) |
| `GET` | `/applications/{user_id}` | Retrieve the latest application status |

---

## Usage Examples

### Updating User Information
If a user's income or job status changes, you can update their profile:
```bash
curl -X PUT "http://127.0.0.1:8000/users/1" \
     -H "Content-Type: application/json" \
     -d '{
           "gender": "m",
           "car": true,
           "realty": true,
           "cnt_children": 1,
           "income": 250000,
           "income_type": "working",
           "education_type": "higher_education",
           "fam_status": "married",
           "housing_type": "house",
           "mobile_phone": true,
           "work_phone": true,
           "phone": true,
           "email": true,
           "job_title": "managers",
           "cnt_fam_members": 3,
           "age": 36,
           "work_experience": 11,
           "bad_debt": 0,
           "good_debt": 6
         }'
```

### Checking Application Status
```bash
curl -X GET "http://127.0.0.1:8000/applications/1"
```

---

## Project Structure
```
credo/
├── app/                          # FastAPI application
│   ├── main.py                  # Application entry point
│   ├── api/                     # API routes/endpoints
│   ├── core/                    # Core configuration
│   ├── db/                      # Database setup
│   ├── models/                 # Pydantic models
│   ├── services/                 # Business logic and ML integration
│   └── enums/                 # Enums datatypes to be used in the database
├── ml_engine/                    # Machine Learning module
│   ├── artifacts/               # Saved ML models
│   └── training/
│       └── data/               # Training datasets
├── tests/                    # Unit and integration tests
├── data.db                    # Sqlite database file
├── pyproject.toml
└── README.md
```

---

## Roadmap

| Feature | Status | Priority | Notes |
|---------|--------|----------|-------|
| **Initial Project Setup** | ✅ Completed | 🟢 Low Priority | Basic FastAPI structure with UV setup |
| **Design Initial ML Model** | ✅ Completed | 🔴 High Priority | Define features and architecture for the credit score model |
| **Train Initial ML Model** | ✅ Completed | 🔴 High Priority | Develop and train the first TensorFlow model (using Keras) |
| **Determine Basic Schemas** | ✅ Completed | 🟡 Medium Priority | Define basic Pydantic schemas for applications and user info |
| **Implement DataBase** | ✅ Completed | 🔴 High Priority | Implement the database schema and initialization |
| **Implement API Endpoints** | ✅ Completed | 🔴 High Priority | Create the API endpoints to manage petitions and responses |
| **Integrate ML Model with API** | ✅ Completed | 🔴 High Priority | Connect the trained model to the FastAPI endpoints for inference |
| **Testing & Validation** | ✅ Completed | 🟢 Low Priority | Implement unit and integration tests for API and ML model |
| **Documentation & Examples** | ✅ Completed | 🟡 Medium Priority | Create comprehensive documentation and usage examples |
| **Other fancy features** | ⏳ Planned | 🟢 Low Priority | Additional features |

**Status Legend:**
- ✅ Completed
- ⏳ Planned
- 🔄 In Progress
- 🔀 Changed

**Priority Legend:**
- 🔴 High Priority
- 🟡 Medium Priority
- 🟢 Low Priority
