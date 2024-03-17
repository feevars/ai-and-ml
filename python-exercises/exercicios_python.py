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