# -*- coding: utf-8 -*-
"""João Pedro Artero - 232_LP_Funcao_cc_m.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V83MVzq5F3grmEGTO6oMcBU4ELrmYa9k

### 1. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba por parâmetro um número e o multiplique por 2, retorne e apresente o resultado da função.
"""

def multiplicar(numero):
    return numero * 2

def multiplicar1(numero):
    resultado = numero * 2
    return numero, resultado

def main():
    n = int(input('Informe o valor: '))
    print("Resultado = ",multiplicar(n))
    ############################################
    #chamada de uma função que retorna 2 valores
    a, b = multiplicar1(n)
    print('O número',a,'multiplicado a 2 é igual a',b)

main()

"""### 2. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba dois números via parâmetro, some os dois valores, retorne e apresente o resultado."""

def soma(valor1,valor2):
    resultado = valor1 + valor2
    return resultado

def main():
    valor1 = int(input("Insira o primeiro valor para soma: "))
    valor2 = int(input("Insira o segundo valor para soma: "))
    print(soma(valor1,valor2))
main()

"""### 3. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento via parâmetro, aplique este aumento a um salário de um funcionário, retorne e apresente o novo salário."""

def aumento(salario,porcentagem):
    aumento = (salario / 100) * porcentagem
    novosalario = salario + aumento
    return novosalario

def main():
    salario = float(input("Insira o valor do salário do funcionário: "))
    porcentagem = float(input("Insira a porcentagem do aumento: "))
    print("O novo salário do funcionário é de: R$",aumento(salario,porcentagem))
main()

"""### 4. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba duas notas (P1, P2) calcule a média, chame outra função na main que avalie se este aluno esta aprovado ou reprovado retornando a str/string 'Aprovado' ou 'Reprovado'."""

def operacao(p1,p2):
    media = (p1 + p2) / 2
    if media >= 6:
        return media,'Aprovado'
    else:
        return media,'Reprovado'

def main():
    p1 = float(input("Insira a nota da p1: "))
    p2 = float(input("Insira a nota da p2: "))
    print(operacao(p1,p2))
main()

"""### 5. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento e um salário via parâmetro, aplique este aumento ao salário do funcionário. Na parte principal (main) do programa, na chamada da função, utilize um laço de repetição para ler 10 salários, chame a função para aplicar o aumento e gerar o novo salário, ainda dentro da estrutura de repetição acumule os novos salários e ao final apresente quanto será gasto no novo salário. Também apresente qual será a diferença entre o que se pagava para todos os funcionário e o que será pago após o aumento."""

def aumento(salario,porcentagem):
    aumento_salario = (salario / 100) * porcentagem
    novo_salario = salario + aumento_salario
    return novo_salario


def main():
    porcentagem = float(input("Insira quanto será o aumento em %: "))
    vetor = []
    vetor2 = []
    total_salario_antigo = 0
    total_salario_novo = 0
    for i in range(10):
        salario = float(input("Insira o valor do funcionário: R$"))
        vetor.append(salario)
        total_salario_antigo = total_salario_antigo + vetor[i]
        vetor2.append(aumento(salario,porcentagem))
        total_salario_novo = total_salario_novo + vetor2[i]
        diferenca = total_salario_novo - total_salario_antigo
    print("O gasto antigo com salários era de: R$: ",total_salario_antigo," e o total dos novos gastos é de: R$",total_salario_novo, ". Uma diferença de R$ ",diferenca,".")
main()

"""### 6. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
a) Crie uma função para apresentar o menu e retornar a opção/número/cálculo escolhido.

    Menu de cálculos
    1.   Número ao quadrado
    2.   Número ao cubo
    3.   Raiz do número
    4.   Raiz cúbica do número
    Qual é a opção desejada?

b) Desenvolva uma função para cada opção de cálculo.

c) A função main() chamará todas as outras.


Observação: Na chamada das funções deve-se utilizar uma estrutura de repetição, que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos **números** do menu.

"""

def quadrado(valor):
    resultado = valor ** 2
    return resultado

def cubo(valor):
    resultado = valor ** 3
    return resultado

def raiz(valor):
    resultado = valor ** (1/2)
    return resultado

def raizCubica(valor):
    resultado = valor ** (1/3)
    return resultado


def menu(opcao):
    if opcao == 1:
        print("Você escolheu: Número ao quadrado.")
        valor = float(input("Insira um valor para a sua operação: "))
        return quadrado(valor)
    elif opcao == 2:
        print("Você escolheu: Número ao cubo.")
        valor = float(input("Insira um valor para a sua operação: "))
        return cubo(valor)
    elif opcao == 3:
        print("Você escolheu: Raíz do número.")
        valor = float(input("Insira um valor para a sua operação: "))
        return raiz(valor)
    elif opcao == 4:
        print("Você escolheu: Raíz cúbica.")
        valor = float(input("Insira um valor para a sua operação: "))
        return raizCubica(valor)
    else:
        return 'Você não selecionou uma opção válida e a operação foi encerrada.'

def main():
    print("Escolha uma opção: \n1. Número ao quadrado \n2. Número ao cubo \n3. Raíz do número \n4. Raíz cúbica do número")
    opcao = int(input("Qual é a opção desejada?: "))
    print(menu(opcao))
main()

"""### 7. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
a) Crie uma função para apresentar o menu e retornar **caracter** do cálculo escolhido.

    *** Minha Calculadora ***

    Digite um número.....:
    Digite outro número..:
        + Soma dois números
        - Subtrai dois números
        * Multiplica dois números
        / Divide dois números
    Qual opção deseja?

b) Desenvolva uma função para cada opção de cálculo, **mas estas não terão retorno**.

c) A função main() chamará todas as outras, passando a elas os valores digitados dos dois números.

Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos **caracteres** do menu.


"""

def menu():
    opcao = input("*** Minha Calculadora *** \n \nDigite um número.....: \nDigite outro número..: \n    + Soma dois números \n    - Subtrai dois números \n    * Multiplica dois números \n    / Divide dois números \nQual opção deseja?")
    return opcao

def soma(num1, num2):
    resultado = num1 + num2
    print(f"Resultado da soma: {resultado}")

def subtracao(num1, num2):
    resultado = num1 - num2
    print(f"Resultado da subtração: {resultado}")

def multiplicacao(num1, num2):
    resultado = num1 * num2
    print(f"Resultado da multiplicação: {resultado}")

def divisao(num1, num2):
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado da divisão: {resultado}")
    else:
        print("Erro: Divisão por zero!")

def main():
    while True:
        opcao = menu()
        if opcao == '+':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            soma(num1, num2)
        elif opcao == '-':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            subtracao(num1, num2)
        elif opcao == '*':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            multiplicacao(num1, num2)
        elif opcao == '/':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            divisao(num1, num2)
        else:
            print("Opção inválida. Tente novamente.")
            break
main()

"""### 8. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
a) Crie uma função para apresentar o menu e retornar **caracter** do cálculo escolhido.

    *** Minha Calculadora ***
    Digite um número.....:
    Digite outro número..:
        + Soma dois números
        - Subtrai dois números
        * Multiplica dois números
        / Divide dois números
    Qual opção deseja?

b) Desenvolva uma função para cada opção de cálculo, **que deverá ter retorno**.

c) A função main() chamará todas as outras, passando a elas os valores digitados dos dois números.

Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos **caracteres** do menu.
"""

def soma(valor1,valor2):
    resultado = valor1 + valor2
    return resultado

def subtracao(valor1,valor2):
    resultado = valor1 - valor2
    return resultado

def multiplicacao(valor1,valor2):
    resultado = valor1 * valor2
    return resultado

def divisao(valor1,valor2):
    resultado = valor1 / valor2
    return resultado

def menu(opcao):
    if opcao == '+':
        print('Você escolheu a opção: Soma.')
        valor1 = int(input("Insira o primeiro valor: "))
        valor2 = int(input("Insira o segundo valor: "))
        return soma(valor1,valor2)
        main()
    elif opcao == '-':
        print("Você escolheu a opção: Subtração.")
        valor1 = int(input("Insira o primeiro valor: "))
        valor2 = int(input("Insira o segundo valor: "))
        return subtracao(valor1,valor2)
        main()
    elif opcao == '*':
        print("Você escolheu a opção: Multiplicação.")
        valor1 = int(input("Insira o primeiro valor: "))
        valor2 = int(input("Insira o segundo valor: "))
        return multiplicacao(valor1,valor2)
        main()
    elif opcao == '/':
        print("Você escolheu a opção: Divisão.")
        valor1 = int(input("Insira o primeiro valor: "))
        valor2 = int(input("Insira o segundo valor: "))
        return divisao(valor1,valor2)
        main()
    else:
        return 'Você não selecionou uma opção válida e a operação foi encerrada.'

def main():
    print("*** Minha Calculadora *** \n \nDigite um número.....: \nDigite outro número..: \n    + Soma dois números \n    - Subtrai dois números \n    * Multiplica dois números \n    / Divide dois números \nQual opção deseja?")
    opcao = input("Insira o carácter da operação escolhida: ")
    print(menu(opcao))
main()

"""

```
# Isto está formatado como código
```

###9. (Função com retorno com parâmetro) Crie uma função para calcular/apresentar a distância entre dois pontos dados pelas coordenadas (x1, y1) e(x2, y2).![distancia.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXQAAAAkCAIAAAAW+FZHAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAACXLSURBVHhe7dx79OdT9T/wr6hktawSrUIuIUJKSn6YkJCQiJQoyjVEKiKXxqVc0zDjOkqikNuQSqSEaIxbRSZdRS6JKLri93i/nu/PnjPvz8yYjMuw5vnHa+2zzz777LPPPvvs857L/z0+C7MwC7PwNGDKyeWxDv1Gg//+97/Ff/TRRzV90VOTnzbaIfQ8CQ3/K0wRg1sUEwFhPusYcIgmb/cbHap3QKxPPV/Qrm5gpa0HQocZujDARMRLvkH4iH//+9+hyQx4W3OAM4ASoCdzlebnBKbmnzALelvJ0MUZwKzkMomJgDCfdQw4RDOxW6jeAbE+9XxBu7qBlbYeCB1m6MIAExEv+QbhI2YllxCx3Hf4EvS2kqGLM4DJkkvUlWg39rH//Oc/LaeIAp+2o6YNkpFPMxqCcJ5umCjWQqIhzHaZMxU6S/tgOTD7gQce2H///UeNGrXnnnv+vwarrrpqn3peYOWVV853lVVWCT0cuvrUVCRXWmmlPtUgjop8OC0NLQ16od8YhupCZDrEc24v2lX48sDwJWRdI0aM6LcbrLXWWmPHjr3zzjuFaEJ3MLn0o7g7ZiGEcogaU80BIr3TQISDtjk9Y58qZFLfIsLMMiPzrKO1BF3NzluP3nPPPVdfffVmm2127LHHjhkzZrshbL/99jvuuKNvv/08gkXtsMMO/cZ222277bY4WWnLD+cJQSyjipgibRYIR3NAeXXB8F7N59BesBNqRTHboiwhnBYR7jca7LbbbhdccMG9994rRBOuU3gWCWXdbUwDTorG4muWlulEqxCdEuZ/VTKDiA29NQwRHbuHYj67YEPrk+EmXXfddUcdddSmm256/fXXp3dmMPsph0VlXeIEisk5A2VmJ9hv6qrXTaEVAHSrMAS0NJCZWnC2GgqYkUcE4T8nwNp//etf7EfkG/S7h2DV3Euy354cGdhvVHKJIiPbvnDoapnGDzi9N7JDvz1NZCzhVgNMv4anBAPToQeW+exiwDZf7orH2Dl69OgVVljh2muvffDBB/U6Tp3gTLeKGYSFVJDUMhEQZpCghRIONAckNflnQAxayQhoUqtZas0eDuCEGWSsbyH85y5qCYiBPN6it9QOaA6Jf1rnTKpcCOFGuvwYOswB6G0VPSFIDqjqdzSLeWaQ2YM+qzOvT82UYGoslFMOOOCA9dZb77777ksqKfzzn//8wx/+cOuttypNM+q5Douy6qwO/va3v91yyy033XSTrpZfuPnmm8eNG3fyySd/4xvfuOOOOx555JFWSY3qqW5o30Ir2Un1evMtfkuD43f77bdPnDjxzjvv7A0YQsSg357pwdSsLs1//OMfd91115VXXsmN4XfL7Qtw9fnnnx9X//GPf3z44YfxC9EwWeUCBksBUHwRzHE33HDDhAkTuM+U4ZPkVojkEyLyZVxvsiEjingGYC42BJ0JPYQfgZkNZV6IMWPG7LHHHnvuuWea1aVS/dOf/nT22WePHz8eka7nAbJNoVVql1xyyZlnnimaq4YPNP/617+eccYZxx577CGHHPL5z39e0N94440Srt5WSSfewwCzmr2+IVRvEa2YY2Le+++//6yzzvrJT34is4ffyfZTTzVnfmR1kKacctttt51wwgmOP9+mC7j0gQceOP3004XioYceOnLkyNNOO03Gj6szNugnlwxDcJZsgogc9z300EOf/exnN9544/XXX59GF0KMMDfQmOHT40Qy5DMRJNeEfmYQyy1QirRSHAuM8flCJGcGxJ7WRZp2Yffdd7/66quLk/yukLn00kvf8Y53/OpXv8oOPm8QJ/R88dhj55xzjsRx0kknSTTptYP4lv/Tn/50p512kn1+/etfjx07dokllhC3d999d8QKVBmSoq/PauI/NAFEYiOcbvK+GTi+0cAMKYzbr7nmmrg99kTG97mC1lp0mr/5zW/cZMcff/z111+fLrjnnnuUM9tuu614E2wnnngiV++7777DXT1Z5dIS5VBQiu+8887zzjvvd7/7XSp0wWabbbbjjjsed9xxkezUPAEko1GjRimCJMI+q4Ph069kBiHpelOIQjeb5jOf4KYHcYVvECbLL7roog022GD06NFydAUxoN3Yu+yyiyCQNzPq+QEntt0gLyORvdpqq/lKKDgR+8UvfqFgwb/gggtcG3y15JJLbrLJJl5JtjgySRmBZhHxJEw7Eggkj0cY2CaKttxyy/z+ZXhNoTfztvIzM9jZRlRggZy86aabfulLX/r973+PQ0aRcsQRR4wYMUI0EuDqRRddVDb4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)"""

def calculo(x1,x2,y1,y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) / (1/2)

def main():
    x1 = float(input("Insira um valor para x1: "))
    x2 = float(input("Insira um valor para x2: "))
    y1 = float(input("Insira um valor para y1: "))
    y2 = float(input("Insira um valor para y2: "))
    print(calculo(x1,x2,y1,y2))
main()

"""### 10. (Função com retorno com parâmetro) Crie uma função que verifique se um número é divisível por outro. Use o caracter %."""

def calculo(valor1,valor2):
    if valor1 % valor2 == 0:
        return "O valor 1 é divisível pelo valor 2"
    else:
        return "O valor 1 não é divisível pelo valor 2"

def main():
    valor1 = int(input("Insira um valor: "))
    valor2 = int(input("Insira outro valor: "))
    print(calculo(valor1,valor2))
main()

"""11. (Função com retorno com parâmetro) Na função main() o usuário deverá informar a quantidade de linhas e colunas, crie/chame uma função para criar e digitar os elementos de uma matriz, retorne-a. Crie/chame outra função que a calculará a soma de todas as linhas e armazenará num vetor do tamanho da quantidade de linhas, retorne-o e apresente na main()."""

def criar_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            elemento = float(input(f'Digite o elemento da posição ({i+1}, {j+1}): '))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def calcular_soma_linhas(matriz):
    soma_linhas = []
    for linha in matriz:
        soma = sum(linha)
        soma_linhas.append(soma)
    return soma_linhas

def main():
    num_linhas = int(input("Digite a quantidade de linhas da matriz: "))
    num_colunas = int(input("Digite a quantidade de colunas da matriz: "))
    matriz = criar_matriz(num_linhas, num_colunas)
    print("\nMatriz inserida:")
    for linha in matriz:
        print(linha)

    soma_linhas = calcular_soma_linhas(matriz)

    print("\nSoma das linhas:")
    for i, soma in enumerate(soma_linhas):
        print(f"Soma da linha {i+1}: {soma}")

main()