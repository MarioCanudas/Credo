import os
import sys

# Add the project root to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "app"))

from app.services import DBConnectionService


def test_connection():
    print("Testing database connection and schema validation...")
    try:
        # DBConnectionService validates the schema in its __init__
        db_service = DBConnectionService()
        db_service.validate_or_raise()
        print(
            "Success: DBConnectionService initialized and schema validated successfully."
        )
    except Exception as e:
        print(f"Error: Database connection service failed validation: {e}")
        sys.exit(1)


if __name__ == "__main__":
    test_connection()
