import pathlib

ROOT_DIR = pathlib.Path(__file__).parent.parent.parent
APP_DIR = ROOT_DIR / "app"
ML_ENGINE_DIR = ROOT_DIR / "ml_engine"

ML_ARTIFACTS_DIR = ML_ENGINE_DIR / "artifacts"

ML_MODEL_PATH = ML_ARTIFACTS_DIR / "model_a01.json"
PREPROCESSOR_PATH = ML_ARTIFACTS_DIR / "preprocessor.joblib"

DATABASE_PATH = ROOT_DIR / "data.db"
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
