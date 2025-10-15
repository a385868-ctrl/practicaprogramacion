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


st.header("Parte 2: Visualización de Figuras (Simple)")

if figura == "Círculo":
    st.latex(r"Área = \pi r^2,\quad Perímetro = 2\pi r")
elif figura == "Triángulo":
    st.latex(r"Área = \tfrac{1}{2} b h,\quad Perímetro = a+b+c")
elif figura == "Rectángulo":
    st.latex(r"Área = b \times h,\quad Perímetro = 2(b+h)")
elif figura == "Cuadrado":
    st.latex(r"Área = l^2,\quad Perímetro = 4l")

st.info("Nota: Como no usamos librerías gráficas, solo mostramos las fórmulas.")

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
