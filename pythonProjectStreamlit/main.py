from azure.storage.blob import BlobServiceClient
import joblib
import os

def download_model_from_azure(connection_string, container_name, blob_name, download_path):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    with open(download_path, "wb") as f:
        blob_data = container_client.download_blob(blob_name)
        f.write(blob_data.readall())

    print("Model downloaded.")
    return joblib.load(download_path)
