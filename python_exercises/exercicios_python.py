# ------------------------- Curso em vídeo -------------------------
# === Desafio 001 ===
# Crie um programa que escreva "Olá, Mundo!" na tela.
print("Olá, mundo!") #aspas duplas
print('Olá, mundo!') #aspas simples
msg = 'Olá, mundo!'
print(msg)


# === Desafio 002 ===
# Digite seu nome
nome = input('Digite seu nome:')
print('É um prazer te conhecer, {}!'.format(nome))


# === Desafio 003 ===
# Soma entre dois números
var1 = input("Digite um número")
var2 = input("Digite outro número") # podemos converter em int logo no input int(input("Digite outro número"))
print("{} + {} = {}".format(var1, var2, int(var1)+int(var2)))


# === Desafio 004 ===
# Dissecando uma variável
algo = input("Digite algo: ") #função input retorna só string
print("O tipo primitivo desse valor é ", type(algo))
print("Só tem espaços? ", algo.isspace())
print("É um número? ", algo.isnumeric())
print("É alfabético?", algo.isalpha())
print("É alfanumérico?", algo.isalnum())
print("Está em maiúsculas?", algo.isupper())
print("Está em minúsculas?", algo.islower())
print("Está capitalizada?", algo.istitle())

# === Desafio 005 ===
# Antecessor e Sucessor
# Faça um programa que leia um número inteiro e mostre na tela o sucessor e o antecessor.
numero = int(input('Digite um número'))
print('O sucessor é {} e o antecessor é {}'.format(numero-1, numero+1))

# === Desafio 006 ===
# Dobro, Triplo, Raiz Quadrada
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from itertools import count
import math
numero = int(input('Digite um número'))
print('O dobro é ',numero*2)
print('O triplo é ',numero*3)
print('A raiz quadrada é ',math.sqrt(numero))
print('A raiz quadrada é {:.2f}. '.format(numero**(1/2)))

# === Desafio 007 ===
# Média aritmética
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
nota1 = float(input('Digite a 1ª nota'))
nota2 = float(input('Digite a 2ª nota'))
print('a média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(nota1, nota2, (nota1+nota2)/2))

# === Desafio 008 ===
# Conversor de medidas
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
valor = float(input('Digite um valor em metros: '))
print('O valor {}m em centímetros é {:.1f}cm e em milímetros é {:.1f}mm'.format(valor, valor*100, valor*1000))

# === Desafio 009 ===
# Tabuada
# Escreva um programa que leia um número e exiba a tabuada para este número
valor = int(input('Digite um número: '))
print('-------------------------------')
for tabuada in range(1,11):
    print('{:2} x {:2} = {}'.format(tabuada, valor, valor*tabuada))
print('-------------------------------')

# === Desafio 010 ===
# Conversor de Moedas
# Crie um programaque leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$1.00 = R$5,03
valor = float(input('Digite quantos reais você possui na carteira: R$'))
real = 5.03
print('com R${:.2f} você consegue comprar US${:.2f}'.format(valor, valor/real))

# === Desafio 011 ===
# Pintando parede
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
area = altura * largura
capacidade_tinta = area/2
print('Sua parede tem a dimensão de {:.2f}x{:.2f}. Sua área é de {:.2f}m²'.format(altura, largura, area))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(capacidade_tinta))

# === Desafio 012 ===
# Calculando descontos
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco_produto = float(input('Digite o preço do produto em reais: R$'))
desconto_aplicado = preco_produto-(preco_produto*0.05)
print('O produto de valor R${:.2f} com 5%` de desconto ficará no valor de R${:.2f}.'.format(preco_produto, desconto_aplicado))