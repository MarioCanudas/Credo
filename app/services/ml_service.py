from typing import Optional

import joblib
import pandas as pd
import xgboost as xgb
from core import ML_MODEL_PATH, PREPROCESSOR_PATH
from enums import ApplicationStatus
from models import UserBase
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

    def predict_application(self, user: UserBase) -> ApplicationStatus:
        """Predicts the application status based on user information."""
        # Convert user model to DataFrame for preprocessor
        user_data = user.model_dump()
        df = pd.DataFrame([user_data])

        # Preprocess data
        processed_data = self.preprocessor.transform(df)

        # Predict
        prediction = self.model.predict(processed_data)[0]

        # Map prediction to ApplicationStatus
        # Assuming 1 is APPROVED and 0 is REJECTED based on common conventions
        return (
            ApplicationStatus.APPROVED
            if prediction == 1
            else ApplicationStatus.REJECTED
        )
