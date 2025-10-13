import streamlit as st
st.title("Mi aplicacion para calcular el area de un circulo 🔢 ")
import math
#Widget para ingresar el radio
radio = st.slider("Selecciona el radio",0.0, 10.0, 5.0)
#calculo del area
area = math.pi * radio **2
#Mostrar resultado
st.write(f"El area del circulo {radio} es {area: .2f}")
