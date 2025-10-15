import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

st.title("Mi aplicación para calcular el area de un circulo 🧮" 
import math
#Widget para ingresar el radio
radio = st.slider("Selecciona el radio", 0.0, 10.0, 5.0)
#calculo del area
area = math.pi * radio **2
#Mostrar resultado
st.write(f"El área del círculo con radio (radio) es: {area:.2f}")

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

st.header("Parte 3: Relaciones Trigonométricas")

max_x = st.slider("Selecciona el rango máximo de x (en radianes)", min_value=1.0, max_value=10.0, value=2*math.pi, step=0.1)
amplitud = st.slider("Amplitud", 0.1, 5.0, 1.0)

x = np.linspace(0, max_x, 500)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, amplitud * np.sin(x), label='sin(x)', color='blue')
ax.plot(x, amplitud * np.cos(x), label='cos(x)', color='orange')

# Tangente con limitación
tan_values = amplitud * np.tan(x)
tan_values = np.clip(tan_values, -10, 10)
ax.plot(x, tan_values, label='tan(x) (limitado)', color='green')

ax.set_title("Funciones Trigonométricas")
ax.set_xlabel("x (radianes)")
ax.set_ylabel("Amplitud ajustada")
ax.legend()
ax.grid(True)

st.pyplot(fig)
