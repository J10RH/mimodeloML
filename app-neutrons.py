import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(page_title="🌱 Predicción COSMOS", layout="wide")
st.title("🌱 Predicción de COSMOS Volumetric Water Content (%)")

# Cargar el modelo desde archivo local
@st.cache_resource
def cargar_modelo():
    ruta_modelo = "xgb_mejor_modelo_cv.pkl"
    if not os.path.exists(ruta_modelo):
        st.error(f"❌ El archivo del modelo no se encontró en: {ruta_modelo}")
        st.stop()
    try:
        modelo = joblib.load(ruta_modelo)
    except Exception as e:
        st.error(f"❌ Error al cargar el modelo: {e}")
        st.stop()
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

# Crear formulario para ingresar valores
with st.form("formulario_prediccion"):
    st.subheader("🔢 Ingrese los valores requeridos")

    valores = []
    for col in columnas:
        val = st.number_input(f"{col}", key=col, format="%.4f")
        valores.append(val)

    enviar = st.form_submit_button("🔍 Predecir")

# Predicción al enviar
if enviar:
    df = pd.DataFrame([valores], columns=columnas)
    try:
        prediccion = modelo.predict(df)
        st.success(f"✅ Predicción de COSMOS Volumetric Water Content: {prediccion[0]:.2f} %")
    except Exception as e:
        st.error(f"❌ Error al realizar la predicción: {e}")
