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
- **ML-Powered** - TensorFlow models for accurate credit predictions
- **Easy Integration** - RESTful API with automatic Swagger/OpenAPI documentation
- **Production-Ready** - Designed with Fintech requirements in mind
- **Scalable** - Ready for deployment in cloud environments

---

## Tech Stack

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **ML Framework**: [TensorFlow](https://www.tensorflow.org/)
- **Python Version**: 3.9+
- **Database**: (To be specified)
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

### Code Quality Tools

This project uses the following tools to maintain code quality:

- **[Ruff](https://docs.astral.sh/ruff/)** - Fast Python linter and formatter
- **[basedpyright](https://docs.basedpyright.com/latest/)** - Static type checker for Python

Run the following commands to check and format your code:

```bash
# Lint code
uv run ruff check .

# Format code
uv run ruff format .

# Type checking
uv run basedpyright
```

### Start the API

```bash
fastapi dev app/main.py
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
│   ├── crud/                    # Database operations
│   ├── db/                      # Database setup
│   └── schemas/                 # Pydantic models
├── ml_engine/                    # Machine Learning module
│   └── training/
│       └── data/               # Training datasets
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## Roadmap

| Feature | Status | Priority | Notes |
|---------|--------|----------|-------|
| **Initial Project Setup** | ✅ Completed | 🟢 Low Priority | Basic FastAPI structure with UV setup |
| **Design Initial ML Model** | 🔄 In progress | 🔴 High Priority | Define features and architecture for the credit score model |
| **Train Initial ML Model** | 🔄 In Progress | 🔴 High Priority | Develop and train the first TensorFlow model (using Keras) |
| **Determine ScoreCard Schema** | ⏳ Planned | 🟡 Medium Priority | Define the data schema for credit score inputs/outputs |
| **Implement API Endpoints** | ⏳ Planned | 🔴 High Priority | Create the API endpoints to manage petitions and responses |
| **Integrate ML Model with API** | ⏳ Planned | 🔴 High Priority | Connect the trained model to the FastAPI endpoints for inference |
| **Testing & Validation** | ⏳ Planned | 🟢 Low Priority | Implement unit and integration tests for API and ML model |
| **Documentation & Examples** | ⏳ Planned | 🟡 Medium Priority | Create comprehensive documentation and usage examples |
| **Other fancy features** | ⏳ Planned | 🟢 Low Priority | Additional features |

**Status Legend:**
- ✅ Completed
- ⏳ Planned
- 🔄 In Progress
- 🔴 High Priority
- 🟡 Medium Priority
- 🟢 Low Priority

---

## Usage Examples

> 📝 This section will be added in future releases with example requests and API usage documentation.