# -*- coding: utf-8 -*-
"""Práctica 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BYOF0VihPOO9J3CjWBv1YLGrjYadymE-

# **Práctica 3: Sentencia iterativa while**

**Nombre:** Christian Geovany Muñoz Rodríguez \
**Código:** 221350605

# **Ejercicio 1**
"""

fact = int (input("Ingrese un número entero: "))
x=fact
count = fact

while count > 1:
  prod = count - 1
  fact = fact * prod
  count = count - 1

print("\nEl factorial de",x,"es:",fact)

"""# **Ejercicio 2.**"""

print("---------------ESTA ES UNA CUENTA REGRESIVA DEL 100 AL 1---------------")
var = 100
while var > 0:
  print(var)
  var -= 1
  
print("---------------FIN---------------")

"""# **Ejercicio 3.**"""

num = int (input("Dame un número: "))

print("\nTu número es",num)
print("\nEsta es la secuencia que genera",num, "al decrementarlo dos unidades:\n")

while num > -1:
  print(num)
  num -= 2

print("\nFIN")

"""# **Ejercicio 4**"""

num = int (input("Deme un número entero positivo:"))
if num < 0:
  print("Ingrese un valor permitido")
else:
  print("\nLa conjetura ULAM de",num, "es:\n")
  print(num)
  while num > 1:
    if num % 2 == 0:
      num = num / 2
      print(int (num))
    else:
      num = (num * 3) + 1
      print(int (num))

"""# **Ejercicio 5.**"""

print("Los múltiplos de 9 que se encuentran entre 45 y 194 son:\n")
i = 45
x = 0
p = 0


while i < 194:
  p += 1
  x += i
  print(i)
  i += 9
  
  
print("\nLa suma de los números es",x)
print("\nEl promedio de los números es",int (x/p))