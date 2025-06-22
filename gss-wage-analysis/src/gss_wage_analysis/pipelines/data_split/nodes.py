"""
This is a boilerplate pipeline 'data_split'
generated using Kedro 0.19.13
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
import joblib

def split_data(df: pd.DataFrame):
    y = df["gender"]
    X = df.drop(columns=["gender", "Unnamed: 0"], errors="ignore")

    cat_cols = ["educcat", "occrecode", "wrkstat", "maritalcat"]
    X = pd.get_dummies(X, columns=cat_cols, drop_first=True)

    num_cols = X.select_dtypes(include=["float64", "int64"]).columns
    scaler = StandardScaler()
    X[num_cols] = scaler.fit_transform(X[num_cols])

    joblib.dump(scaler, "data/06_models/scaler.pkl")

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    return X_train, X_test, y_train.to_frame(name="gender"), y_test.to_frame(name="gender")
