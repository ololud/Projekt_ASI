import streamlit as st
import pandas as pd
import joblib
from main import download_model_from_azure

#Connection string pusty dla bezpieczenstwa
connection_string = ""
container_name = "asikontener"

model = download_model_from_azure(connection_string, container_name, "best_model.pkl", "downloaded_model.pkl")
download_model_from_azure(connection_string, container_name, "feature_names.pkl", "downloaded_feature_names.pkl")
download_model_from_azure(connection_string, container_name, "scaler.pkl", "downloaded_scaler.pkl")

feature_names = joblib.load("downloaded_feature_names.pkl")
scaler = joblib.load("downloaded_scaler.pkl")

st.title("Predykcja płci na podstawie danych demograficznych")

age = st.number_input("Wiek", min_value=18, max_value=100, value=30)
realrinc = st.number_input("Dochód roczny (realrinc)", min_value=0, value=25000)
childs = st.number_input("Liczba dzieci", min_value=0, max_value=10, value=1)

educcat = st.selectbox("Poziom wykształcenia", [
    "Less Than High School", "High School", "Junior College", "Bachelor", "Graduate"
])

maritalcat = st.selectbox("Stan cywilny", [
    "Married", "Never Married", "Separated", "Widowed"
])

wrkstat = st.selectbox("Status zawodowy", [
    "Housekeeper", "Other", "Part-Time", "Retired", "School",
    "Temporarily Not Working", "Unemployed, Laid Off"
])

if st.button("Przewiduj płeć"):

    input_data = {
        "year": 2024,
        "realrinc": realrinc,
        "age": age,
        "occ10": 0,
        "prestg10": 0,
        "childs": childs,
    }

    educcat_options = [
        "educcat_Graduate",
        "educcat_High School",
        "educcat_Junior College",
        "educcat_Less Than High School"
    ]
    for option in educcat_options:
        input_data[option] = 1 if option == f"educcat_{educcat}" else 0

    maritalcat_options = [
        "maritalcat_Married",
        "maritalcat_Never Married",
        "maritalcat_Separated",
        "maritalcat_Widowed"
    ]
    for option in maritalcat_options:
        input_data[option] = 1 if option == f"maritalcat_{maritalcat}" else 0

    wrkstat_options = [
        "wrkstat_Housekeeper",
        "wrkstat_Other",
        "wrkstat_Part-Time",
        "wrkstat_Retired",
        "wrkstat_School",
        "wrkstat_Temporarily Not Working",
        "wrkstat_Unemployed, Laid Off"
    ]
    for option in wrkstat_options:
        input_data[option] = 1 if option == f"wrkstat_{wrkstat}" else 0

    occrecode_options = [
        "occrecode_Business/Finance",
        "occrecode_Construction/Extraction",
        "occrecode_Farming, Fishing, and Forestry",
        "occrecode_Installation, Maintenance, and Repair",
        "occrecode_Office and Administrative Support",
        "occrecode_Production",
        "occrecode_Professional",
        "occrecode_Sales",
        "occrecode_Service",
        "occrecode_Transportation"
    ]
    for option in occrecode_options:
        input_data[option] = 0

    for col in feature_names:
        if col not in input_data:
            input_data[col] = 0

    df = pd.DataFrame([input_data])[feature_names]

    scaler_features = scaler.feature_names_in_
    df[scaler_features] = scaler.transform(df[scaler_features])

    prediction = model.predict(df)[0]
    predicted_gender = "Male" if prediction == 1 else "Female"
    st.success(f"Przewidywana płeć: **{predicted_gender}**")
