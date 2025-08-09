#Importación de librerias
import pandas as pd
import streamlit as st
import plotly.express as px

#Carga de datos
vehicles = pd.read_csv('vehicles_us.csv')

#Diccionario de variables a graficar
variable = {
    "Año del modelo":"model_year",
    "Tacometro":"odometer",
    "Color":"paint_color",
    "Condición":"condition",
    "Tipo":"type",
    "Precio":"price",
    "Cilindros":"cylinders",
    "Días publicado":"days_listed"
}

st.title("Visualización gráfica de los datos del sitio de venta de vehiculos")

#Graficación de un histograma
st.subheader("Histograma")
option = st.selectbox(
    "¿Cuál variable quieres graficar en histograma?",
    ("Año del modelo", "Tacometro", "Condición", "Color", "Tipo", "Precio", "Cilindros", "Días publicado"),
)


st.write("Seleccionaste:", option)

hist_button = st.button('Construir histograma')


if hist_button:
    st.write('Creacion de histograma exitoso')

    hist = px.histogram(vehicles, x=variable[option])

    st.plotly_chart(hist, use_container_width=True)


#Creación de un gráfico de dispersión
st.subheader("Gráfico de dispersión")

col1, col2 = st.columns(2)

with col1:
    y_axis = st.selectbox(
    "¿Qué variable quieres incluir en la gráfica de dispersión en el eje Y?",
    ("Año del modelo", "Tacometro", "Precio", "Cilindros", "Días publicado"),
)
    
with col2:
    x_axis = st.selectbox(
    "¿Qué variable quieres incluir en la gráfica de dispersión en el eje X?",
    ("Año del modelo", "Tacometro", "Precio", "Cilindros", "Días publicado"),
)
    
disp_button = st.button('Construir gráfico de dispersión')


if disp_button:
    st.write('Creacion de gráfico de dispersión exitoso')

    disp = px.scatter(vehicles, x=variable[x_axis], y=variable[y_axis])

    st.plotly_chart(disp, use_container_width=True)
