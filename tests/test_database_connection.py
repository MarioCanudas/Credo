import os
import sys

# Add the project root to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "app"))

from app.services import DBConnectionService


def test_connection():
    print("Testing database connection and schema validation...")
    try:
        # DBConnectionService now uses connect() to initialize and validate
        db_service = DBConnectionService()
        db_service.connect()
        print(
            "Success: DBConnectionService connected and schema validated successfully."
        )
    except Exception as e:
        print(f"Error: Database connection service failed: {e}")
        sys.exit(1)
    finally:
        # Always disconnect after testing
        DBConnectionService().disconnect()


if __name__ == "__main__":
    test_connection()
