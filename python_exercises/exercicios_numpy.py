#Exercicio 01
#Crie um array NumPy unidimensional com 10 elementos inteiros aleatórios.
import numpy as np
a01 = np.random.randint(2, 150, 6)
a01

#Exercicio 02
#Crie um array NumPy bidimensional de tamanho 3x3 preenchido com zeros.
a02 = np.zeros((3,3))
a02

#Exercicio 03
#Crie um array NumPy bidimensional de tamanho 2x4 preenchido com uns.
a03 = np.ones((2,4))
a03

#Exercicio 04
#Crie um array NumPy unidimensional contendo os números pares de 0 a 10.
a04a = np.arange(0,11,2)
print(a04a)
a04b = np.arange(0, 11)[::2] # faz  % 2 == 0 direto
print(a04b)

#Exercicio 05
#Crie um array NumPy unidimensional contendo os números ímpares de 1 a 11.
a05a = np.arange(1,12,2)
print(a05a)
a05b = np.arange(11)[1::2] # faz  % 2 == 1 direto
print(a05b)
a05c = np.arange(11)[np.arange(11) % 2 == 1]
print(a05c)

#Exercicio 06
#Crie um array NumPy unidimensional de números espaçados uniformemente entre 0 e 10 com 50 elementos.
a06 = np.linspace(0, 10, 50)
a06

#Exercicio 07
#Crie um array NumPy unidimensional de números espaçados logaritmicamente entre 1 e 1000 com 10 elementos.
a07 = np.logspace(0, 3, 10)
a07

#Exercicio 08
#Dado um array NumPy unidimensional, calcule a soma de todos os elementos.
a08 = np.random.randint(0,50, 5)
print(a08)
print(np.cumsum(a08)) # Vai mostrando a soma cumulativa dos itens do array
print(np.sum(a08)) # Mostra a soma total

#Exercicio 09
#Dado um array NumPy bidimensional, calcule a média de cada linha (axis = 1).
e09a = np.arange(9).reshape(3, 3)
print(e09a)
print(np.median(e09a, axis=1))

#Exercicio 10
#Dado um array NumPy bidimensional, calcule o desvio padrão de cada coluna (axis = 0).
e09a = np.arange(12).reshape(3, 4)
print(e09a)
print(np.pa(e09a, axis=0))

#Dado um array NumPy unidimensional, encontre o valor máximo e sua posição.
#Dado um array NumPy bidimensional, encontre o valor mínimo e sua posição em cada linha.
#Dado um array NumPy unidimensional, crie uma cópia do array e inverta a ordem dos elementos.
#Dado um array NumPy bidimensional, aplique a função exponencial a todos os elementos.
#Dado um array NumPy unidimensional, remova todos os elementos repetidos.
#Dado um array NumPy bidimensional, faça a transposição da matriz.
#Dado um array NumPy unidimensional, substitua todos os valores negativos por zero.
#Dado um array NumPy bidimensional, ordene cada linha em ordem crescente.
#Dado um array NumPy unidimensional, calcule a diferença entre elementos consecutivos.
#Dado um array NumPy bidimensional, conte quantos elementos são maiores que um determinado valor.