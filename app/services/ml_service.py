from typing import Optional


class MLService:
    "Singleton class for ML model and scaler"

    _instance: Optional["MLService"] = None
    _initialized: bool = False

    def __new__(cls) -> "MLService":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not self._initialized:
            self._load_artifacts()
            MLService._initialized = True

    def _load_artifacts(self) -> None:
        "Load the preprocessor and model artifacts to process data"
