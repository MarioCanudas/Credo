import asyncio
from typing import Optional

from core import DATABASE_URL
from pydantic import BaseModel
from sqlalchemy import Engine, Inspector, inspect
from sqlmodel import SQLModel, Table, create_engine


class _SchemaValidationResult(BaseModel):
    success: bool
    is_empty: bool = False
    missing_tables: set[str] = set()
    extra_tables: set[str] = set()
    message: str = ""


class DBConnectionService:
    engine: Engine | None = None

    _instance: Optional["DBConnectionService"] = None
    _initialized: bool = False

    def __new__(cls) -> "DBConnectionService":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not self._initialized:
            self._create_engine()
            DBConnectionService._initialized = True

            engine_validation = asyncio.run(self._validate_schema())
            if not engine_validation.success:
                raise Exception(
                    f"Database schema validation failed: {engine_validation.message}"
                )

    def _create_engine(self) -> None:
        if self.engine is None:
            self.engine = create_engine(DATABASE_URL, echo=True)

    async def _validate_schema(self) -> _SchemaValidationResult:
        if self.engine is None:
            return _SchemaValidationResult(
                success=False,
                is_empty=True,
                message="Database engine is not initialized.",
            )

        inspector = inspect(self.engine)
        tables_schema = SQLModel.metadata.tables

        db_tables = set(inspector.get_table_names())
        expected_tables = set(SQLModel.metadata.tables.keys())

        missing_tables = expected_tables - db_tables
        extra_tables = db_tables - expected_tables
        is_empty = len(db_tables) == 0

        message_parts: list[str] = []
        if missing_tables:
            message_parts.append(
                f"Missing tables: {', '.join(sorted(missing_tables))}."
            )
        if extra_tables:
            message_parts.append(f"Extra tables: {', '.join(sorted(extra_tables))}.")
        if is_empty:
            message_parts.append("Database is empty.")

        table_errors: dict[str, list[str]] = {}
        if not bool(missing_tables):
            tasks: dict[str, asyncio.Task[list[str]]] = {}

            async with asyncio.TaskGroup() as tg:
                for table in tables_schema.values():
                    tasks[table.name] = tg.create_task(
                        self._verify_table_columns(inspector, table)
                    )

                for table, task in tasks.items():
                    column_errors = task.result()
                    if column_errors:
                        table_errors[table] = column_errors

        if table_errors:
            table_details: list[str] = []
            for table, errors in table_errors.items():
                formatted_errors = ", ".join(errors)
                table_details.append(f"{table}: {formatted_errors}")

            error_details = "; ".join(table_details)
            message_parts.append(f"Column errors found in tables: {error_details}.")

        success = (
            not is_empty
            and not missing_tables
            and not extra_tables
            and not table_errors
        )

        result = _SchemaValidationResult(
            success=success,
            is_empty=is_empty,
            missing_tables=missing_tables,
            extra_tables=extra_tables,
            message=" ".join(message_parts),
        )

        return result

    async def _verify_table_columns(
        self, inspector: Inspector, table: Table
    ) -> list[str]:
        expected_schema: dict[str, str] = {}
        for col in table.columns:
            expected_schema[col.name] = str(col.type)

        engine_schema: dict[str, str] = {}
        for col in inspector.get_columns(table.name):
            engine_schema[col["name"]] = str(col["type"])

        errors: list[str] = []

        missing_columns = set(expected_schema.keys()) - set(engine_schema.keys())
        for col_name in sorted(missing_columns):
            errors.append(
                f"missing column '{col_name}' "
                f"(expected type: {expected_schema[col_name]})"
            )

        extra_columns = set(engine_schema.keys()) - set(expected_schema.keys())
        for col_name in sorted(extra_columns):
            errors.append(
                f"extra column '{col_name}' (engine type: {engine_schema[col_name]})"
            )

        common_columns = set(expected_schema.keys()) & set(engine_schema.keys())
        for col_name in sorted(common_columns):
            expected_type = expected_schema[col_name]
            engine_type = engine_schema[col_name]
            if expected_type != engine_type:
                errors.append(
                    f"type mismatch in column '{col_name}' "
                    f"(expected: {expected_type}, engine: {engine_type})"
                )

        return errors
