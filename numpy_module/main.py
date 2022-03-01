from tracemalloc import stop
import numpy as np
 
n1 = np.array([1, 2, 3, 4, 5, 6])

print("array criada com o método array\n{}".format(n1))

n2 = np.array([[1, 2, 3, 4, 5], [20, 30, 40, 50, 60]])

print('array(matriz) multidimensional criada pelo metodo array\n{}'.format(n2))

# inicializando uma array com zeros

n3 = np.zeros(shape=(1, 2), dtype="int")

print("array criada pelo metodo zeros\n{}".format(n3))

#  criando uma matriz 3x3 prenchida de zeros - zeros method

n4 = np.zeros(shape=(3,3), dtype="int")

# print(n4)

# criando uma matriz 6x6 prenchida de um número escolhido - full method

n5 = np.zeros(shape=(6,6), dtype="int")
print(n5)

n6 = np.full(shape=(6,7), dtype="float", fill_value=10.78)

print("n6\n{}".format(n6))

# inicializando um array com um inervalo de numeros - arange method

n7 = np.arange(10, 21)

print("array criada com o metodo arange\n{}".format(n7))

n8 = np.arange(start=10, stop=100, step = 4)
print(f"array criada pelo metodo arange\n{n8}")

# criando e preenchendo um array com valores aleatórios