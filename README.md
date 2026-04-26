<div align="center">
<h1>Credo - Credit Score API</h1>

**A FastAPI-based Credit Score Prediction API powered by TensorFlow Machine Learning Models**

[Features](#features) • [Quick Start](#quick-start) • [Roadmap](#roadmap) 
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
- **Database**: Sqlite (can be easily switched to PostgreSQL or MySQL)
- **Deployment**: (To be specified)

---

## Installation

### Prerequisites
- Python 3.9 or higher
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

---

## Quick Start

> 📝 This section will be added in future releases with example requests and API usage documentation.

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
├── test/                    # Unit and integration tests
├── data.db                    # Sqlite database file
├── init_db.py                    # Database initialization script
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
| **Determine ScoreCard Schema** | 🔀 Changed | 🟡 Medium Priority | Changed to more granular schema definition (see Determine Basic Schemas) |
| **Determine Basic Schemas** | ✅ Completed | 🟡 Medium Priority | Define basic Pydantic schemas for applications and user info |
| **Implement DataBase** | ✅ Completed | 🔴 High Priority | Implement the database schema and initialization |
| **Implement API Endpoints** | 🔄 In progress | 🔴 High Priority | Create the API endpoints to manage petitions and responses |
| **Integrate ML Model with API** | 🔄 In progress | 🔴 High Priority | Connect the trained model to the FastAPI endpoints for inference |
| **Testing & Validation** | ⏳ Planned | 🟢 Low Priority | Implement unit and integration tests for API and ML model |
| **Documentation & Examples** | ⏳ Planned | 🟡 Medium Priority | Create comprehensive documentation and usage examples |
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
- 

---

## Usage Examples

> 📝 This section will be added in future releases with example requests and API usage documentation.
