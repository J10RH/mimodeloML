import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Predicción COSMOS", layout="wide")
st.title("🌱 Predicción de COSMOS Volumetric Water Content (%)")

# Cargar el modelo desde archivo local
@st.cache_resource
def cargar_modelo():
    ruta_modelo = "random_forest_regressor_model.pkl"
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








# 🧾 Columnas de entrada
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

# 📊 Datos de ejemplo
ejemplo = pd.DataFrame([{
    'Month': 6, 'Day': 20, 'Albedo - 1': 0.2, 'COSMOS Neutron Counts (corrected) - count': 1450,
    'D86 75M - cm': 23.0, 'Soil Heat Flux 1 - W m-2': 6.1, 'Soil Heat Flux 2 - W m-2': 5.7,
    'Longwave Radiation - Incoming - MJ m-2 day-1': 19.8,
    'Longwave Radiation - Outgoing - MJ m-2 day-1': 14.6,
    'Atmospheric Pressure - hPa': 1011.0, 'Potential Evaporation - mm': 3.2,
    'Precipitation (Pluvio) - mm': 0.2, 'Absolute Humidity - g m-3': 9.8,
    'Relative Humidity - %': 65.0, 'Net Radiation - MJ m-2 day-1': 7.9,
    'STP 01 Soil Temperature at 2cm - degC': 24.0,
    'STP 02 Soil Temperature at 5cm - degC': 23.0,
    'STP 03 Soil Temperature at 10cm - degC': 22.5,
    'STP 04 Soil Temperature at 20cm - degC': 21.0,
    'STP 05 Soil Temperature at 50cm - degC': 19.0,
    'Shortwave Radiation - Incoming - MJ m-2 day-1': 17.0,
    'Shortwave Radiation - Outgoing - MJ m-2 day-1': 2.1,
    'Air Temperature - degC': 25.0, 'Air Temperature - Maximum - degC': 29.0,
    'Air Temperature - Minimum - degC': 19.0,
    'TDT 01 - Soil Temperature at 10cm - degC': 22.5,
    'TDT 02 - Soil Temperature at 10cm - degC': 22.7,
    'TDT 01 - Volumetric Water Content at 10cm - %': 11.5,
    'TDT 02 - Volumetric Water Content at 10cm - %': 11.7,
    'Wind Direction - deg': 170.0, 'Wind Speed - m s-1': 2.3
}])

# 🔄 Modo de entrada
modo = st.radio("¿Cómo quieres ingresar los datos?", ["📋 Usar datos de ejemplo", "✍️ Ingresar manualmente"])

if modo == "📋 Usar datos de ejemplo":
    st.dataframe(ejemplo)
    df_input = ejemplo.copy()

elif modo == "✍️ Ingresar manualmente":
    st.subheader("✍️ Ingrese los valores:")
    valores = []
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
