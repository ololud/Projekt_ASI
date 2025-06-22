"""
This is a boilerplate pipeline 'model_upload'
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

def upload_model_to_azure(model_input=None) -> None:
    from azure.storage.blob import BlobServiceClient


    #Connection String pusty dla bezpieczeństwa
    connection_string = ""
    container_name = "asikontener"

    model_path = "data/06_models/best_model.pkl"
    features_path = "data/06_models/feature_names.pkl"
    scaler_path = "data/06_models/scaler.pkl"

    model_blob = "best_model.pkl"
    features_blob = "feature_names.pkl"
    scaler_blob = "scaler.pkl"

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    def upload(local_path, blob_name):
        with open(local_path, "rb") as f:
            container_client.upload_blob(name=blob_name, data=f, overwrite=True)
            print(f"Uploaded: {blob_name}")

    upload(model_path, model_blob)
    upload(features_path, features_blob)
    upload(scaler_path, scaler_blob)