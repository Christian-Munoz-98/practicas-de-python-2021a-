# -*- coding: utf-8 -*-
"""Práctica 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ME2ZDom8-hjaIgcgOsQJAQTqRTJa66pa

## **Práctica 4: Sentencias iterativa for**

**Alumno:** Christian Geovany Muñoz Rodríguez  **Código:** 221350605

# **Ejercicio 1**
"""

""""
Solicitar al usuario una secuencia de n números y posteriormente determinar y mostrar en pantalla:
a) Los múltiplos de 5 y los múltiplos de 3.
b) La suma de los pares y el producto de los que son múltiplo de 7.
"""

#Declaración de variables
n = int (input("¿Hasta dónde llega su secuencia de números?: "))
p = 0 #Contador para sumar los números pares
q = 1 #Contador para multiplicar los múltiplos de 7

#Impresión de los múltiplos de 5 entre 1 y n
print("\nLos múltiplos de 5 entre 1 y",n,"Son:\n")
for i in range(5,n+1,5):
  print(i)

#Impresión de los múltiplos de 3 entre 1 y n
print("\nLos múltiplos de 3 entre 1 y",n,"Son:\n")
for i in range(3,n+1,3):
  print(i)

#Suma de todos los pares entre 1 y n
for i in range(2,n+1,2):
  p +=i
print("\nLa suma de los pares es",p,"\n")

#Producto de los múltiplos de 7 entre 1 y n
for i in range(7,n+1,7):
  q *= i
print("El producto de los multiplos de 7 es",q,"\n")

"""# **Ejercicio 2**"""

"""
Realizar un programa que imprima de forma inversa los números que se encuentran desde el 100 al 1.
"""

print("_____________________CUENTA REGRESIVA DEL 100 AL 1_____________________")
for i in range(100,0,-1):
  print(i)
print("_____________________FIN_____________________")

"""# **Ejercicio 3**"""

"""
Calcular e imprimir el promedio de los cuadrados de los números comprendidos entre 1 y un número n
dado. 
"""

#Declaración de variables
n = int (input("Ingrese un número límite: "))
p = 0 #Sumatoria de los cuadrados entre 1 y n

#Impresión de los cuadrados y caálculo de la sumatoria
print("\nLos cuadrados de 1 a",n,"son:\n")
for i in range(1,n+1):
  print (i**2)
  p += i**2

#Impresión de la suma de los cuadrados y el promedio
print("\nLa suma de los cuadrados entre 1 y n es",p)
print("\nEl promedio de dicha suma es",p/n)

"""# **Ejercicio 4**"""

"""
Solicitar un número entero y decrementarlo en 2 hasta que el número sea menor que 0, imprimir en
pantalla el número actual. Ejemplo: Si el usuario ingresa el número 13, se imprimirá en pantalla la
siguiente secuencia: 13, 11, 9, 7, 5, 3, 1.
"""
#Declaración de variables
n = int (input("Dame un número entero: "))
print("\nEsta es su secuencia: \n")

#Impresión de la secuencia numérica
for i in range(n,-1,-2):
  print(i)

"""# **Ejercicio 5**"""

"""
Realizar un programa que solicite al usuario diez números e imprima en pantalla el número mayor, el
número menor, la suma y el promedio de los 10 números ingresados.
"""
#El usuario ingresa 10 números
a = int (input("Dame el primer número: "))
b = int (input("Dame el Segundo número: "))
c = int (input("Dame el tercer número: "))
d = int (input("Dame el cuarto número: "))
e = int (input("Dame el quitno número: "))
f = int (input("Dame el sexto número: "))
g = int (input("Dame el séptimo número: "))
h = int (input("Dame el octavo número: "))
i = int (input("Dame el noveno número: "))
j = int (input("Dame el decimo número: "))

#Declaración de variables
numeros = [a,b,c,d,e,f,g,h,i,j]#Lista de los números ingresados
suma = 0 #Variable para sumar los valores de la lista
x = a #Variable para obtener el número mayor mediante comparación
y = a #Variable para obtener el número menor

#Se obtiene el número mayor
for numero in numeros:
    if x > numero:
      x = x
    else:
      x = numero

#Se obtiene el número menor
for numero in numeros:
    if y < numero:
      y = y
    else:
      y = numero
#Se suman los números
for numero in numeros:
  suma += numero

#Se imprimen los valores solicitados
print("\nEl número menor es", y)
print("\nEl número mayor es",x)
print("\nLa suma de los 10 números es",suma)
print("\nEl promedio de los 10 números es",suma/10)

"""# **Ejercicio 6**"""

"""
Realice un programa que muestre al usuario los términos de la serie armónica y su respectiva suma, a
partir de un número total de elementos que el usuario deseé conocer.
"""
#Declaración de variables
n = int (input("¿Cuántos elementos de la serie armónica desea conocer?: "))
suma = 0 #Variable para calcula la suma de los términos de la serie armónica

#Impresión de los términos y cálculo de la suma
print("\nLos términos de la serie armónica hata",n,"son:\n")

for i in range(1,n+1):
  suma += 1/i
  c = "1/"+str (i)
  print(c)

#Impresión de la suma
print("\nLa suma de",n,"Elementos de la suma armónica es",suma)