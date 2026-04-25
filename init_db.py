from sqlmodel import SQLModel, create_engine

from app.core import DATABASE_URL


def init_db():
    print(f"Initializing database at: {DATABASE_URL}")
    engine = create_engine(DATABASE_URL, echo=True)
    SQLModel.metadata.create_all(engine)
    print("Database initialization complete.")


if __name__ == "__main__":
    init_db()
