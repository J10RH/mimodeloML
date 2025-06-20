import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
import io

st.set_page_config(page_title="Predicción de Humedad Volumétrica", layout="wide")

st.title("🌱 Predicción de COSMOS Volumetric Water Content (%)")

# Cargar el modelo desde GitHub
@st.cache_data
def cargar_modelo():
    url_modelo = "https://github.com/usuario/repositorio/raw/main/xgb_mejor_modelo_cv.pkl"
    response = requests.get(url_modelo)
    modelo = joblib.load(io.BytesIO(response.content))
    return modelo

modelo = cargar_modelo()

# Lista de columnas de entrada
columnas = [
    'Month', 'Day', 'Albedo - 1', 'COSMOS Neutron Counts (corrected) - count',
    'D86 75M - cm', 'Soil Heat Flux 1 - W m-2', 'Soil Heat Flux 2 - W m-2',
    'Longwave Radiation - Incoming - MJ m-2 day-1',
    'Longwave Radiation - Outgoing - MJ m-2 day-1',
    'Atmospheric Pressure - hPa', 'Potential Evaporation - mm',
    'Precipitation (Pluvio) - mm', 'Absolute Humidity - g m-3',
    'Relative Humidity - %', 'Net Radiation - MJ m-2 day-1',
    'STP 01 Soil Temperature at 2cm - degC',
    'STP 02 Soil Temperature at 5cm - degC',
    'STP 03 Soil Temperature at 10cm - degC',
    'STP 04 Soil Temperature at 20cm - degC',
    'STP 05 Soil Temperature at 50cm - degC',
    'Shortwave Radiation - Incoming - MJ m-2 day-1',
    'Shortwave Radiation - Outgoing - MJ m-2 day-1',
    'Air Temperature - degC', 'Air Temperature - Maximum - degC',
    'Air Temperature - Minimum - degC', 'TDT 01 - Soil Temperature at 10cm - degC',
    'TDT 02 - Soil Temperature at 10cm - degC',
    'TDT 01 - Volumetric Water Content at 10cm - %',
    'TDT 02 - Volumetric Water Content at 10cm - %',
    'Wind Direction - deg', 'Wind Speed - m s-1'
]

# Crear un formulario
with st.form("formulario_prediccion"):
    st.subheader("🔢 Ingrese los valores de entrada")

    valores = []
    for i, columna in enumerate(columnas):
        valor = st.number_input(f"{columna}", key=f"{columna}", format="%.4f")
        valores.append(valor)

    boton_predecir = st.form_submit_button("🔍 Predecir")

# Cuando el usuario presiona el botón
if boton_predecir:
    df_input = pd.DataFrame([valores], columns=columnas)
    prediccion = modelo.predict(df_input)
    st.success(f"✅ Predicción de 'COSMOS Volumetric Water Content - %': {prediccion[0]:.2f} %")
