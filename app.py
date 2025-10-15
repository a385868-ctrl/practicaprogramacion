import streamlit as st
import math


st.title("Mi aplicacion para calcular el area de un circulo 🔢 ")

#Widget para ingresar el radio
radio = st.slider("Selecciona el radio",0.0, 10.0, 5.0)
#calculo del area
area = math.pi * radio **2
#Mostrar resultado
st.write(f"El area del circulo {radio} es {area: .2f}")

import streamlit as st
import math

st.title("Calculadora Geométrica y Gráficos Simples")

st.header("Parte 1: Calculadora de Área y Perímetro")

figura = st.selectbox("Selecciona una figura:", ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"])

area = 0.0
perimetro = 0.0

if figura == "Círculo":
    r = st.number_input("Radio", min_value=0.0, value=1.0)
    area = math.pi * r**2
    perimetro = 2 * math.pi * r

elif figura == "Triángulo":
    a = st.number_input("Lado a", min_value=0.0, value=1.0)
    b = st.number_input("Lado b", min_value=0.0, value=1.0)
    c = st.number_input("Lado c", min_value=0.0, value=1.0)
    h = st.number_input("Altura (para el área)", min_value=0.0, value=1.0)
    area = 0.5 * b * h
    perimetro = a + b + c

elif figura == "Rectángulo":
    base = st.number_input("Base", min_value=0.0, value=1.0)
    altura = st.number_input("Altura", min_value=0.0, value=1.0)
    area = base * altura
    perimetro = 2 * (base + altura)

elif figura == "Cuadrado":
    lado = st.number_input("Lado", min_value=0.0, value=1.0)
    area = lado ** 2
    perimetro = 4 * lado

# Mostrar resultados
st.success(f"Área: {area:.2f}")
st.success(f"Perímetro: {perimetro:.2f}")

import streamlit as st
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

st.subheader("Visualización de la figura")

# Selector de color
color = st.color_picker("Selecciona un color para la figura", "#00f900")

# Crear figura y ejes
fig, ax = plt.subplots()

if figura == "Círculo":
    circle = plt.Circle((0, 0), radio, color=color, fill=False, linewidth=2)
    ax.add_patch(circle)
    ax.set_xlim(-radio * 1.2, radio * 1.2)
    ax.set_ylim(-radio * 1.2, radio * 1.2)

elif figura == "Triángulo":
    puntos = [[0, 0], [base, 0], [base / 2, altura]]
    triangulo = plt.Polygon(puntos, edgecolor=color, fill=False, linewidth=2)
    ax.add_patch(triangulo)
    ax.set_xlim(-1, base + 1)
    ax.set_ylim(-1, altura + 2)

elif figura == "Rectángulo":
    rect = plt.Rectangle((0, 0), base, altura, edgecolor=color, fill=False, linewidth=2)
    ax.add_patch(rect)
    ax.set_xlim(-1, base + 1)
    ax.set_ylim(-1, altura + 1)

elif figura == "Cuadrado":
    rect = plt.Rectangle((0, 0), lado, lado, edgecolor=color, fill=False, linewidth=2)
    ax.add_patch(rect)
    ax.set_xlim(-1, lado + 1)
    ax.set_ylim(-1, lado + 1)

# Ajustes visuales
ax.set_aspect('equal')
ax.axis('off')  # Ocultar ejes

# Mostrar figura
st.pyplot(fig)
import numpy as np

st.header("Parte 3 — Relaciones trigonométricas")

# Slider para seleccionar el rango máximo en radianes (desde 0 hasta max_x)
max_x = st.slider("Selecciona el rango máximo de x (en radianes)", min_value=1.0, max_value=10.0, value=2*np.pi, step=0.1)

# Slider para modificar la amplitud
amp = st.slider("Amplitud", 0.1, 5.0, 1.0)

# Generar datos x en el rango 0 a max_x
x = np.linspace(0, max_x, 500)

# Graficar funciones trigonométricas usando st.pyplot
fig, ax = plt.subplots(figsize=(8, 4))

ax.plot(x, amp * np.sin(x), label='sin(x)')
ax.plot(x, amp * np.cos(x), label='cos(x)')
# Para tan(x), limitar el rango para evitar valores muy grandes (usar np.clip para visualización)
tan_values = amp * np.tan(x)
tan_values = np.clip(tan_values, -10, 10)  # limitar valores para que gráfico sea legible
ax.plot(x, tan_values, label='tan(x) (limitado)')

ax.set_title("Funciones trigonométricas")
ax.set_xlabel("x (radianes)")
ax.set_ylabel("Amplitud ajustada")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# Parte 4 — Extensión creativa: pestañas y calculadora de Pitágoras

st.header("Parte 4: opcional")

# Crear pestañas para separar Geometría y Trigonometría
tab_geom, tab_pitagoras = st.tabs(["Geometría", "Teorema de Pitágoras"])

with tab_geom:
    st.subheader("Calculadora de Áreas y Perímetros y Visualización")
   
    # (Aquí repetirías el código que tienes para geometría y visualización,
    # o si quieres puedes definir funciones para modularizarlo y solo llamar)
   
    # Como ya mostraste la geometría arriba, puedes solo mostrar un mensaje aquí
    st.info("La calculadora de áreas, perímetros y visualización se muestra en la Parte 1 y 2.")

with tab_pitagoras:
    st.subheader("Calculadora del Teorema de Pitágoras")

    st.write("Calcula la hipotenusa o un cateto de un triángulo rectángulo.")

    opcion = st.radio("¿Qué deseas calcular?", ["Hipotenusa", "Cateto"])

if opcion == "Hipotenusa":
        cateto1 = st.number_input("Introduce el cateto 1", min_value=0.0, value=3.0)
        cateto2 = st.number_input("Introduce el cateto 2", min_value=0.0, value=4.0)
        hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
        st.success(f"La hipotenusa es: {hipotenusa:.2f}")

else:  # Calcular cateto
         hipotenusa = st.number_input("Introduce la hipotenusa", min_value=0.0, value=5.0)
        cateto_conocido = st.number_input("Introduce el cateto conocido", min_value=0.0, value=3.0)

if hipotenusa <= cateto_conocido:
            st.error("La hipotenusa debe ser mayor que el cateto conocido.")
else:
            cateto_desconocido = math.sqrt(hipotenusa**2 - cateto_conocido**2)
            st.success(f"El cateto desconocido es: {cateto_desconocido:.2f}")
