# -*- coding: utf-8 -*-
"""Práctica 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ae-PY4izZMeLzNRx7m47ZsI3GepLsbUr

# **Práctica 1: Sentencias simples**

Alumno: Christian Geovany Muñoz Rodríguez \
Código: 221350605

# **Ejercicio 1**
"""

nombre = input("¿Cuál es tu nombre?: ")
domicilio = input("¿Cuál es tu domicilio?: ")
telefono = int (input("Proporcione su teléfono: "))
edad = int (input("Proporcione su edad: "))

print("\nUsted es:", nombre, "\nSu edad es:", edad, "años","\nVive en:", domicilio, "\nSu teléfono es:", telefono)

"""# **Ejercicio 2**"""

pesos = float (input("¿Cuántos pesos tienes?: "))
euros = pesos/26.31
euros = round(euros, 2)
dolares = pesos/22.41
dolares = round(dolares, 2)

print("Usted tiene", euros," euros o", dolares, "dólares")

"""# **Ejercicio 3**"""

arista = float (input("¿Cuánto mide la arista de su cubo?: "))
radio = float (input("¿Cuánto mide el radio de su esfera?: "))
v_cubo = arista ** 3
v_esfera = (4 * 3.1416 * radio ** 3) / 3

print("El volumen de su cubo es: ", v_cubo, "Unidades cúbicas")
print("El volumen de su esfera es: ", v_esfera, "Unidades cúbicas")

"""# **Ejercicio 4**"""

nombre_producto = input("¿Qué desea comprar?: ")
cantidad_producto = int (input("¿Cuáantas unidades desea adquirir?: "))
precio_unitario = float (input("¿Cuál es el precio unitario del producto?: "))
descuento = int (input("¿Qué porcentaje de descuento tiene el producto?: "))

precio_total = precio_unitario * cantidad_producto
precio_final = precio_total - (precio_total * (descuento * 0.01))

print("\nUsted adquirió este producto:", nombre_producto)
print("\nAdquirió estas unidades:", cantidad_producto)
print("\nSin el descuento usted pagaría", precio_total, "pesos")
print("\nCon el descuento aplicado del", descuento, "por ciento usted paga", precio_final, "pesos")

"""# **Ejercicio 5**"""

segundos0 = int (input("ingrese una cantidad en segundos: "))

horas = segundos0 // 3600
segundos = segundos0 % 3600
minutos = segundos // 60
segundos = segundos % 60


print("\n", segundos0, "segundo(s) equivale(n) a:", horas, "hora(s)", minutos, "minuto(s) y", segundos, "Segundo(s)")