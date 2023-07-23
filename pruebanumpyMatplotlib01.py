import numpy as np
import matplotlib.pyplot as plt

print("PRUEBAS CON LA LIBREBRÍA NUMPY")
#Cada dimensión se denomina axis#
a = np.zeros((2, 4))

print("MATRIZ DE CEROS DE 2 FILAS Y 4 COLUMNAS ")
print(a)
#longitud #

print("El número total de elementos (multiplicación de la longitud de las dimensiones) se denomina siz")
print(a.size)
print("La lista de dimensiones con su correspondiente longitud se denomina shape")
print(a.shape)

print("Numero de dimensiones")
print(a.ndim)

print("MATRIZ DE CEROS DE 3 FILAS Y 4 COLUMNAS ")
b = np.ones((3, 4))
print(b)
#longitud #

print("El número total de elementos (multiplicación de la longitud de las dimensiones) se denomina siz")
print(b.size)
print("La lista de dimensiones con su correspondiente longitud se denomina shape")
print(b.shape)

print("Numero de dimensiones")
print(b.ndim)
print("  ")

print("Matriz de valores aleatorios 1  ")

# Inicialización del array con valores aleatorios
d=np.random.rand(2, 3, 4)
print(d)

print("El número total de elementos (multiplicación de la longitud de las dimensiones) se denomina siz")
print(b.size)
print("La lista de dimensiones con su correspondiente longitud se denomina shape")
print(b.shape)
print("Numero de dimensiones")
print(b.ndim)

# Inicialización del array con valores aleatorios#
""""" 
print("  ")
print("MATRIZ RANDOM  de 10x10x4 ")
f=np.random.rand(10,10,4)
print(f)
"""""
print("  ")
print("MATRIZ RANDOM  de 3x5x4 ")
f=np.random.rand(3,5,4)
print(f)


print("  ")
print("MATRIZ de 8's  de 2x3x4 ")
# Array cuyos valores son todos el valor indicado como segundo parámetro de la función
g=np.full((2, 3, 4), 8)
print(g)


# Inicialización del array con valores aleatorios conforme a una distribución normal
print("Inicialización del array con valores aleatorios conforme a una distribución normal")
h=np.random.randn(2, 4)
print(h)

print(" ")

print("GENERACIÓN DE VALORES ALEATORIOS y VISUALIZACIÓN CON MATPLOTLIB ")
num=int(input("Inserta un número muy grande de valores y tendrás \n el gráfico de dispersión normal: "))


c = np.random.randn(num)

plt.hist(c, bins=200)
plt.show()