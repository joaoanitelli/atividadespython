# -*- coding: utf-8 -*-
"""João Pedro Artero - 221_Est_Rep_SemContador_m.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yu9HxR49eXdrjnEtrVsFez8Vp9aKvIPN

### **EXERCÍCIOS DE ESTRUTURA DE REPETIÇÃO SEM CONTADOR**

###1. Construir um algoritmo para calcular e apresentar o total de salários pagos de funcionários, mas não é informado a quantidade de pessoas, então use como critério de parada (condição da estrutura de repetição, digitar zero no salário para sair.
"""

salario = float(input("Informe seu salário..."))
acu_salario = 0
while salario > 0:
    acu_salario = acu_salario + salario
    salario = float(input("Informe seu salário..."))
print(acu_salario)

"""###2. Faça um programa que receba a altura de 5 pessoas. Encontre e apresente a altura da pessoa mais alta e da mais baixa e seus respectivos nomes."""

for pessoas in range(1,6):
   nome = input('Qual o seu nome? ')
   altura = float(input('Qual a sua altura? '))

   if pessoas == 1:
    cont_alto = altura
    cont_baixo = altura
    nome_alto = nome
    nome_baixo = nome

   if altura >= cont_alto:
    cont_alto = altura
    nome_alto = nome

   if altura <= cont_baixo:
    cont_baixo = altura
    nome_baixo = nome
print(f'A pessoa mais alta tem {cont_alto} e seu nome é {nome_alto}')
print(f'A pessoa mais baixa tem {cont_baixo} e seu nome é {nome_baixo}')

"""###3. Faça um programa que receba a altura de várias pessoas. Encontre e apresente a altura da pessoa mais alta e da mais baixa e seus respectivos nomes. Para encerrar a entrada de dados, zero na altura, mas esta não poderá ser considerada como resposta da altura da pessoa mais baixa.

"""

altura = float(input("Insira sua altura..."))
if altura > 0:
    alto = altura
    baixo = altura
    nome_baixo = nome
    nome_alto = nome

while altura > 0:
    nome = str(input('Qual o seu nome...'))

    if altura >= alto:
        alto = altura
        nome_alto = nome

    if altura <= cont_baixo:
        baixo = altura
        nome_baixo = nome

    altura = float(input("Insira sua altura..."))

print(f'A pessoa mais alta é {nome_alto} e tem {alto}')
print(f'A pessoa mais baixa é {nome_baixo} e tem {baixo}')

"""###4. Faça um programa que receba a idade e a altura de várias pessoas. Calcule e exiba a média das alturas das pessoas com mais de 20 anos. Para encerrar a entrada de dados, digite uma idade negativa ou igual a zero.



"""

idade = int(input('Informe a idade... '))
total_de_altura = 0
cont = 0
while idade > 0:
  altura = float(input('Informe a altura... '))
  if idade > 20:
    total_de_altura = total_de_altura + altura
    cont = cont + 1
  idade = int(input('Informe a idade... '))
media = total_de_altura / cont
print(f'A média das alturas de pessoas acima dos 20 anos é de: {media:.2f}')

"""###5. Construir um algoritmo para calcular e apresentar a idade atual de algumas pessoas em relação ao ano atual, mas não é informado a quantidade de pessoas, então use como critério de parada (condição da estrutura de repetição, digitar zero no ano de nascimento para sair."""

print('Seja bem vindo ao programa! Para encerrar, digite 0!')
print('\n\n')

ano_de_nascimento = int(input('Digite o ano de nascimento '))

while ano_de_nascimento > 0:
  idade = 2022 - ano_de_nascimento
  ano_de_nascimento = int(input('Digite o ano de nascimento '))
print(f'A sua idade atual é de {idade}')

"""###6. Faça um programa que receba um conjunto de valores inteiros, calcule e exiba o maior e o menor valor do conjunto.


*   Para encerrar a entrada de dados, deve ser digitado o valor zero;
*   Para valores negativos, deve ser enviada uma mensagem;
*   Esses valores (zero e negativos) não entrarão na lógica de encontrar o maior e o menor valor.


"""

numero = int(input('Digite um numero inteiro (Positivo e Maior que 0) '))

if numero > 0:
  num_maior = numero
  num_menor = numero

while numero > 0:
  if numero > num_maior:
    num_maior = numero

  if numero < num_menor:
    num_menor = numero

  numero = int(input('Digite um numero inteiro (Positivo e Maior que 0) '))
print(f'O maior numero é {num_maior} e o menor numero é {num_menor}')

"""###7. No final do ano muitas pessoas compram presentes. Faça um programa que registre alguns dados das pessoas, usando como critério de parada a letra ‘n’, para a pergunta “Deseja cadastrar outro (‘s’/’n’)?”, para identificar o perfil dos compradores numa loja de roupas e apresente como resultado a:
a)   Quantidade de mulheres e de homens;

b)   Quantidade de mulheres e de homens abaixo e acima de 18 anos.
"""

qntd_homem = 0
qntd_mulher = 0
mulher_18 = 0
homem_18 = 0
mulher_menor = 0
homem_menor = 0

print(f'Seja bem vindo a nossa loja!')
cadastro = str(input('Deseja realizar o cadastro? (Digite Sim/Nao)'))

while cadastro == 'sim':
  genero = str(input('Qual o seu genero? M/F '))
  idade = int(input('Qual a sua idade? '))
  if genero == 'M':
    qntd_homem = qntd_homem + 1
    if idade >= 18:
      homem_18 = homem_18 + 1
    else:
      homem_menor = homem_menor + 1
  elif genero == 'F':
    qntd_mulher = qntd_mulher + 1
    if idade >= 18:
      mulher_18 = mulher_18 + 1
    else:
      mulher_menor = mulher_menor + 1
  cadastro = str(input('Gostaria de realizar outro cadastro? (Digite Sim/Nao)'))
print(f'A quantidade de Homens cadastrados é: {qntd_homem}')
print(f'A quantidade de Mulheres cadastradas é: {qntd_mulher}')
print(f'A quantidade de Homens acima de 18 anos é: {homem_18}')
print(f'A quantidade de Mulheres acima de 18 anos é: {mulher_18}')
print(f'A quantidade de Homens abaixo de 18 anos é: {homem_menor}' )
print(f'A quantidade de Mulheres abaixo de 18 anos é: {mulher_menor}')