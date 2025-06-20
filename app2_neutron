import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
import io

st.set_page_config(page_title="Predicción COSMOS", layout="wide")
st.title("🌱 Predicción de COSMOS Volumetric Water Content (%)")

# 🔽 URL del modelo en GitHub (RAW)
MODEL_URL = "https://raw.githubusercontent.com/usuario/repositorio/main/random_forest_regressor_model.pkl"

# 🧠 Cargar modelo desde GitHub
@st.cache_resource
def cargar_modelo():
    try:
        response = requests.get(MODEL_URL)
        response.raise_for_status()
        modelo = joblib.load(io.BytesIO(response.content))
        return modelo
    except Exception as e:
        st.error(f"❌ No se pudo cargar el modelo: {e}")
        st.stop()

modelo = cargar_modelo()

# 🧾 Lista de columnas de entrada
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

# 📊 Crear datos de ejemplo
ejemplo = pd.DataFrame([{
    'Month': 6, 'Day': 20, 'Albedo - 1': 0.2, 'COSMOS Neutron Counts (corrected) - count': 1400,
    'D86 75M - cm': 22.5, 'Soil Heat Flux 1 - W m-2': 5.3, 'Soil Heat Flux 2 - W m-2': 4.8,
    'Longwave Radiation - Incoming - MJ m-2 day-1': 20.0,
    'Longwave Radiation - Outgoing - MJ m-2 day-1': 15.0,
    'Atmospheric Pressure - hPa': 1012.5, 'Potential Evaporation - mm': 3.1,
    'Precipitation (Pluvio) - mm': 0.0, 'Absolute Humidity - g m-3': 10.0,
    'Relative Humidity - %': 60.0, 'Net Radiation - MJ m-2 day-1': 8.5,
    'STP 01 Soil Temperature at 2cm - degC': 25.0,
    'STP 02 Soil Temperature at 5cm - degC': 24.5,
    'STP 03 Soil Temperature at 10cm - degC': 23.0,
    'STP 04 Soil Temperature at 20cm - degC': 22.0,
    'STP 05 Soil Temperature at 50cm - degC': 20.0,
    'Shortwave Radiation - Incoming - MJ m-2 day-1': 18.0,
    'Shortwave Radiation - Outgoing - MJ m-2 day-1': 2.0,
    'Air Temperature - degC': 26.0, 'Air Temperature - Maximum - degC': 30.0,
    'Air Temperature - Minimum - degC': 20.0,
    'TDT 01 - Soil Temperature at 10cm - degC': 23.5,
    'TDT 02 - Soil Temperature at 10cm - degC': 23.7,
    'TDT 01 - Volumetric Water Content at 10cm - %': 12.5,
    'TDT 02 - Volumetric Water Content at 10cm - %': 12.8,
    'Wind Direction - deg': 180.0, 'Wind Speed - m s-1': 2.5
}])

# 📌 Selección del modo de ingreso
modo = st.radio("¿Cómo quieres ingresar los datos?", ["📋 Usar datos de ejemplo", "✍️ Ingresar manualmente"])

if modo == "📋 Usar datos de ejemplo":
    st.dataframe(ejemplo)
    df_input = ejemplo.copy()

elif modo == "✍️ Ingresar manualmente":
    valores = []
    st.subheader("✍️ Ingrese los valores:")
    for col in columnas:
        val = st.number_input(f"{col}", key=col, format="%.4f")
        valores.append(val)
    df_input = pd.DataFrame([valores], columns=columnas)

# 🔮 Botón para predecir
if st.button("🔍 Predecir COSMOS Volumetric Water Content"):
    try:
        prediccion = modelo.predict(df_input)
        st.success(f"✅ Predicción: {prediccion[0]:.2f} %")
    except Exception as e:
        st.error(f"❌ Error en la predicción: {e}")
