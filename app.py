import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Calculadora Geométrica", layout="centered")

st.title("Calculadora Geométrica y Visualización 🔺📐📊")
st.header("Parte 1: Área y Perímetro")

figura = st.selectbox("Selecciona una figura:", ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"])

area = 0.0
perimetro = 0.0

# Definir variables según la figura
if figura == "Círculo":
    radio = st.number_input("Radio", min_value=0.0, value=1.0)
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio

elif figura == "Triángulo":
    a = st.number_input("Lado a", min_value=0.0, value=1.0)
    b = st.number_input("Lado b", min_value=0.0, value=1.0)
    c = st.number_input("Lado c", min_value=0.0, value=1.0)
    altura = st.number_input("Altura (para el área)", min_value=0.0, value=1.0)
    area = 0.5 * b * altura
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

st.header("Parte 2: Visualización de la Figura")

# Selector de color
color = st.color_picker("Selecciona un color para la figura", "#00f900")

# Crear figura para matplotlib
fig, ax = plt.subplots()

if figura == "Círculo":
    circle = plt.Circle((0, 0), radio, color=color, fill=False, linewidth=2)
    ax.add_patch(circle)
    ax.set_xlim(-radio * 1.2, radio * 1.2)
    ax.set_ylim(-radio * 1.2, radio * 1.2)

elif figura == "Triángulo":
    puntos = [[0, 0], [b, 0], [b / 2, altura]]
    triangulo = plt.Polygon(puntos, edgecolor=color, fill=False, linewidth=2)
    ax.add_patch(triangulo)
    ax.set_xlim(-1, b + 1)
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

ax.set_aspect('equal')
ax.axis('off')  # Ocultar ejes

st.pyplot(fig)

st.header("Parte 3: Funciones Trigonométricas")

funcion = st.selectbox("Selecciona una función:", ["Seno", "Coseno", "Tangente"])
rango = st.slider("Rango en x (0 a ...)", min_value=1, max_value=20, value=6)
amp = st.slider("Amplitud", 0.1, 2.0, 1.0)

x = np.linspace(0, rango, 300)

if funcion == "Seno":
    y = amp * np.sin(x)
elif funcion == "Coseno":
    y = amp * np.cos(x)
elif funcion == "Tangente":
    y = amp * np.tan(x)

    fig2, ax2 = plt.subplots()
    ax2.plot(x, y, color=color)
    ax2.set_title(f"Función {funcion}")
    st.pyplot(fig2)
