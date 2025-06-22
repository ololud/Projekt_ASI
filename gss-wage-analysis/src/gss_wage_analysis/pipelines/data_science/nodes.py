"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.14
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
import joblib

def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    df = df.dropna().copy()

    df["gender"] = df["gender"].map({"Female": 0, "Male": 1})

    return df




