# -*- coding: utf-8 -*-
"""Práctica 5: Listas(Parte 1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VzUFJ2_yDmmmLIClR8s3d32BPIIumvha

# **Prácica 5: Listas(Parte 1)**

**Alumno:** Christian Geovany Muñoz Rodríguez **Código:**221350605

# **Ejercicio 1**
"""

''' Definir una lista que contenga el nombre de su película, serie, videojuego, género musical, canción y
cantante favorito (Lista con 6 elementos):'''

my_list= ['El Arbol de la Vida','Dark','Limbo','Música electrónica','The mother we share','Sufjan Stevens']

#Imprimir todos los elementos de la lista
print(f'\nLista completa: {my_list}')

#Imprimir solo a los primeros 3 elementos de la lista
print(f'\nPrimeros 3 elementos de la lista: {my_list[0:3]}')

#Imprimir al último elemento de la lista
print(f'\nUtimo elemento de la lista: {my_list[-1]}')

#Cambiar al cuarto y quinto elemento de la lista e imprimir la nueva lista
my_list[3:5]= 'Indie pop','Just like fireflies'
print(f'\nNueva lista con cuarto y quinto elemento sustituidos: {my_list}')

#Agregar su deporte favorito al final de la lista e imprimir la nueva lista
my_list.append('Basketball')
print(f"\nSe agregó mi deporte favorito a la lista: {my_list}")

#Agregar su comida, fruta y libro favorito al final de la lista e imprimir la nueva lista
my_list.extend(['Chilaquiles','Sandía','1984'])
print(f'\nSe extendió la lista: {my_list}')

#Agregar su color favorito en la posición 5 de la lista e imprimir la nueva lista
my_list.insert(4, 'Rojo')
print(f'\nSe agregó mi color favorito en el indice 5: {my_list}')

#Eliminar a los elementos que se encuentran de la posición 0 a 2 e imprimir la nueva lista
del my_list[0:3]
print(f'\nSe eliminaron los elementos del indice 0 al 2: {my_list}')

#Eliminar a su fruta favorita de la lista por medio de la función remove e imprimir la nueva lista
my_list.remove('Sandía')
print(f'\nSe retiró la fruta favorita de la lista: {my_list}')

#Eliminar a su canción favorita de la lista por medio de la función pop e imprimir la nueva lista
my_list.pop(2)
print(f'\nSe elimino el elemento del indice 2 de la lista: {my_list}')

#Eliminar a todos los elementos de la lista e imprimir la nueva lista.
my_list = []
print(f'\nSe vació la lista: {my_list}')

"""# **Ejercicio 2**"""

''' Solicitarle al usuario los elementos de la lista, una vez que lleno la lista desplegarla en pantalla y
preguntarle al usuario si desea cambiar algún elemento, si la respuesta es afirmativa preguntarle qué
elemento desea cambiar y cuál va a ser su nuevo valor. Desplegar en pantalla la lista actualizada. Ejemplo:'''

lista = []
n = int(input("Cuántos elementos quiere en su lista: "))
for i in range(1,n+1):
  elemento = input(f"\nAgregue el elemento {i} a la lista:")
  lista.append(elemento)

print(f'\nSu lista es: {lista}')

respuesta = input("\n¿Desea reemplazar algún elemento de la lista?\n\nEscriba 'Y' para sí y 'N' para no")
respuesta = respuesta.upper()

if respuesta == 'Y':
  viejo = input("\n¿Cuál es el elemento que desea reemplazar?: ")
  try:
    lista.index(viejo)
    nuevo = input("\n¿Por cuál elemento lo va a sustituir?:")
    indice = lista.index(viejo)
    lista[indice] = nuevo
    print(f'\nSu nueva lista es: {lista}')
  except:
    print("\nElemento no disponible")
  
else:
  print("\nGracias por usar este programa")