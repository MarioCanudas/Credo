import sys

from ..app.services import DBConnectionService


def test_connection():
    print("Testing database connection and schema validation...")
    try:
        # DBConnectionService validates the schema in its __init__
        DBConnectionService()
        print(
            "Success: DBConnectionService initialized and schema validated successfully."
        )
    except Exception as e:
        print(f"Error: Database connection service failed validation: {e}")
        sys.exit(1)


if __name__ == "__main__":
    test_connection()
