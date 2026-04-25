"""Train and evaluate classification models for credit application status.

This script performs the full training workflow:
1. Load raw application data.
2. Rename columns to internal canonical names.
3. Clean categorical values.
4. Build preprocessing transformations.
5. Split data into train/test sets.
6. Apply SMOTE to rebalance classes.
7. Train Logistic Regression, Random Forest, and XGBoost models.
8. Evaluate each model using cross-validation and test-set metrics.

Artifacts:
- `preprocessor.joblib`: fitted preprocessing pipeline used for inference.

Recommended usage:
- Run this script with uv:
    uv run ml_engine/training/training_models.py
"""

import pathlib
import re

import joblib
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from xgboost import XGBClassifier

ML_ENGINE_PATH = pathlib.Path(__file__).parent.parent
ARTIFACTS_PATH = ML_ENGINE_PATH / "artifacts"
TRAINING_PATH = ML_ENGINE_PATH / "training"
DATA_PATH = TRAINING_PATH / "data"


data = pd.read_csv(DATA_PATH / "applications.csv")

# Map dataset column names to the internal schema used by the project.
renamed_columns = {
    "Applicant_ID": "id",
    "Applicant_Gender": "gender",
    "Owned_Car": "car",
    "Owned_Realty": "realty",
    "Total_Children": "cnt_children",
    "Total_Income": "income",
    "Income_Type": "income_type",
    "Education_Type": "education_type",
    "Family_Status": "fam_status",
    "Housing_Type": "housing_type",
    "Owned_Mobile_Phone": "mobile_phone",
    "Owned_Work_Phone": "work_phone",
    "Owned_Phone": "phone",
    "Owned_Email": "email",
    "Job_Title": "job_title",
    "Total_Family_Members": "cnt_fam_members",
    "Applicant_Age": "age",
    "Years_of_Working": "work_experience",
    "Total_Bad_Debt": "bad_debt",
    "Total_Good_Debt": "good_debt",
    "Status": "status",
}

data.rename(columns=renamed_columns, inplace=True)

# Target and identifier columns used in the training pipeline.
id_col = "id"
outcome_col = "status"

# Binary input features that are passed through without one-hot encoding.
binary_columns = [
    "car",
    "realty",
    "mobile_phone",
    "work_phone",
    "phone",
    "email",
]

# Nominal/categorical input features to be one-hot encoded.
categorical_columns = [
    "gender",
    "income_type",
    "education_type",
    "fam_status",
    "housing_type",
    "job_title",
]

# Remaining features are treated as numeric and standardized.
numerical_columns = list(
    set(data.columns)
    - set(categorical_columns)
    - set(binary_columns)
    - {id_col, outcome_col}
)


def delete_slash(text: str) -> str:
    """Normalize category labels that may contain slash-separated values.

    Example:
        "commercial associate / manager" -> "commercial_associate"
    """
    return re.split(r"\s*/\s*", text, maxsplit=1)[0].strip().replace(" ", "_").lower()


# Clean categorical text values to keep category vocabularies consistent.
for col in categorical_columns:
    data[col] = data[col].apply(lambda x: delete_slash(x) if isinstance(x, str) else x)

train_data = data.sample(frac=0.8, random_state=3)
test_data = data.drop(train_data.index)

train_data.to_csv(DATA_PATH / "train.csv")
test_data.to_csv(DATA_PATH / "test.csv")

# Preprocessing pipeline:
# - scale numeric columns,
# - one-hot encode categorical columns,
# - pass binary columns through as-is.
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_columns),
        ("num", StandardScaler(), numerical_columns),
        ("bin", "passthrough", binary_columns),
    ]
)

# Split into features and target.
X_train = train_data.drop(columns=[id_col, outcome_col])
y_train = train_data[outcome_col].values

X_test = test_data.drop(columns=[id_col, outcome_col])
y_test = test_data[outcome_col].values

# Fit and persist preprocessor so the same transformations can be reused.
X__train = preprocessor.fit_transform(X_train)
X_test = preprocessor.transform(X_test)
joblib.dump(preprocessor, ARTIFACTS_PATH / "preprocessor.joblib")

# Rebalance classes in training data.
smote = SMOTE(random_state=3)
X_train_resampled, y_train_resampled = smote.fit_resample(X__train, y_train)  # type: ignore

# Train XGBoost classifier.
xgb_classifier = XGBClassifier(random_state=3)
xgb_classifier.fit(X_train_resampled, y_train_resampled)
xgb_y_pred = xgb_classifier.predict(X_test)

# Evaluate XGBoost with CV and holdout metrics.
accuracy_xgb = cross_val_score(
    estimator=xgb_classifier, X=X_train_resampled, y=y_train_resampled, cv=10
)
print(
    "XGBoost CV Accuracy: %.2f%% +/- %.2f%%"
    % (accuracy_xgb.mean() * 100, accuracy_xgb.std() * 100)
)
print("XGBoost Accuracy:", accuracy_score(y_test, xgb_y_pred))
print(confusion_matrix(y_test, xgb_y_pred))

xgb_classifier.save_model(ARTIFACTS_PATH / "model_a01.json")
