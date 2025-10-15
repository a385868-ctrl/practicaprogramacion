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

import matplotlib.pyplot as plt
st.header("Parte 2: Visualización de Figuras")

color = st.color_picker("Elige un color", "#0000FF")

fig, ax = plt.subplots()

if figura == "Círculo":
    circle = plt.Circle((0, 0), r, color=color, fill=False)
    ax.set_xlim(-radio * 1.2, radio * 1.2)
    ax. set ylin(-radio * 1.2, radio * 1.2)

elif figura = "Triángulo":
    puntos = ([0, 0], [base, 0], [base / 2, altura])
    triangulo = plt. Polygon (puntos, edgecolor=color, fill-False, linewidth=2)
    ax. add patch(triangulo)
    ax.set_xlim(-1, base + 1)
    ax. set ylin(-1, altura + 2)
    
elif figura = "Rectángulo" :
    rect = plt.Rectangle((0, 0), base, altura, edgecolor=color, fill-False, linewidth=2)
    ax. add patch(rect)
    ax.set_xlim(-1, base + 1)
    ax. set_ylin(-1, altura + 1)
    
elif figura = "Cuadrado":
    rect - plt.Rectangle((0, 0), lado, lado, edgecolor=color, fill-false, Linewidth=2)
    ax. add patch(rect)
    ax. set xlin(-1, lado + 1)
    ax.setyLim(-1, lado + 1)
    
ax.set _aspect ('equal')
ax.axis ('off') #ocultar ejes

st. pyplot(fig)

st.header("Parte 3: Funciones Trigonométricas")

funcion = st.selectbox("Selecciona una función:", ["Seno", "Coseno", "Tangente"])
rango = st.slider("Rango en x (0 a ...)", min_value=1, max_value=20, value=6)
amp = st.slider("Amplitud", 0.1, 2.0, 1.0)

# Generamos puntos para graficar (sin numpy)
x_vals = [i * 0.1 for i in range(rango * 10)]
y_vals = []

for x in x_vals:
    if funcion == "Seno":
        y_vals.append(amp * math.sin(x))
    elif funcion == "Coseno":
        y_vals.append(amp * math.cos(x))
    elif funcion == "Tangente":
        try:
            y_vals.append(amp * math.tan(x))
        except:
            y_vals.append(None)

# Graficamos con st.line_chart
chart_data = {"x": x_vals, "y": y_vals}
st.line_chart(chart_data)
