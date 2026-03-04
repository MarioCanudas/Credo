from typing import Optional

import joblib
import xgboost as xgb
from core import ML_MODEL_PATH, PREPROCESSOR_PATH
from sklearn.compose import ColumnTransformer


class MLService:
    "Singleton class for ML model and scaler"

    preprocessor: ColumnTransformer
    model: xgb.XGBClassifier

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
        # Load sklearn preprocessor
        self.preprocessor = joblib.load(PREPROCESSOR_PATH)

        self.model = xgb.XGBClassifier()
        self.model.load_model(ML_MODEL_PATH)
