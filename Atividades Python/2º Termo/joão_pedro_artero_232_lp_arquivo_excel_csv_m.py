# -*- coding: utf-8 -*-
"""João Pedro Artero - 232_LP_Arquivo_Excel_Csv_m.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cpz5n3V78_PNToFlwu74CuX-DlCeOq1M
"""

import matplotlib.pyplot as plt
rotulos = ['Gerente de TI', 'Desenvolvedor', 'Gerente BD']
tamanho = [12, 54, 19]
cores = ['red', 'pink', 'orange']
fig, ax = plt.subplots()
ax.pie(tamanho, labels=rotulos, colors=cores, autopct="%1.1f%%")
ax.set_title('Cargos')
plt.show()

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
df = pd.read_excel('/content/drive/MyDrive/Vendas.xlsx')
print(df)
print('-'*100)
print(df.info())
print('-'*100)
print(df.columns.ravel())
print('-'*100)
df2 = pd.read_csv('/content/drive/MyDrive/Propaganda.csv')
print(df2)
print('-'*100)
print(df2.columns.ravel())

import pandas as pd
df = pd.read_excel('/content/drive/MyDrive/Vendas.xlsx')
print(df['ID Loja'].value_counts())

import pandas as pd
df = pd.read_excel('/content/drive/MyDrive/Vendas.xlsx')
faturamento = df['Valor Final'].sum()
print(f'Faturamento obtido R$ {faturamento:,.2f}')
df.sample()
df.sample(10)
print('Quantidade de lojas=', sum(df['ID Loja'] == 'Shopping Lua') )
#seleção apenas dos Shopping Lua
tem_shopping_lua = df['ID Loja'] == 'Shopping Lua'
#a variável shopping_lua recebe todas as colunas dos dados apenas deste shopping
shopping_lua = df[tem_shopping_lua]
print(f'Média de preços do Shopping Lua=',shopping_lua['Valor Final'].mean())
print(f'Faturamente total do Shopping Lua=',shopping_lua['Valor Final'].sum())
print(f'Quantidade de Shopping Lua=',shopping_lua['Valor Final'].count())

import pandas as pd
df = pd.read_excel('/content/drive/MyDrive/Vendas.xlsx')
faturamento = df['Valor Final'].sum()
f_sem_formatar = f'{faturamento:.2f}'
print('Faturamento obtido R$',f_sem_formatar)
f_formatado = f_sem_formatar.replace('.',',')
print('Faturamento obtido R$',f_formatado)

import pandas as pd
df = pd.read_excel('/content/drive/MyDrive/Vendas.xlsx')
#print(df)
#print(df.columns.ravel())
#print(df['ID Loja'].value_counts())
#faturamento = df['Valor Final'].sum()
#print(f'Faturamento obtido R$ {faturamento:,.2f}')
#print(df.sample())
#print(df.sample(10))
#print('Quantidade de lojas=', sum(df['ID Loja'] == 'Shopping Lua') )
#seleção apenas dos Shopping Lua
#tem_shopping_lua = df['ID Loja'] == 'Shopping Lua'
#a variável shopping_lua recebe todas as colunas dos dados apenas deste shooping
#shopping_lua = df[tem_shopping_lua]
#print(f'Média de preços do Shopping Lua=',shopping_lua['Valor Final'].mean())
#print(f'Faturamente total do Shopping Lua=',shopping_lua['Valor Final'].sum())
#print(f'Quantidade de Shopping Lua=',shopping_lua['Valor Final'].count())
#import matplotlib.pyplot as plt
#plt.hist(shopping_lua['Valor Final'], 5, rwidth=0.8, color = 'red')
#plt.title('Vendas realizadas pelo Shopping Lua')
#plt.xlabel('Preço dos produtos')
#plt.ylabel('Quantidade de produtos')
#plt.show()

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/Propaganda.csv')
#print(df)

import plotly.express as px
fig = px.histogram(df, x="TV")
fig.show()

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/Propaganda.csv')

import plotly.express as px
fig = px.bar(df, title="Vendas por Mês")
#ou
#fig = px.bar(df, x='TV',title="Vendas por Mês")
#fig = px.scatter(df, x = 'TV')
fig.show()

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/Propaganda.csv')

import plotly.express as px
fig = px.histogram(df, x= 'TV')
fig.show()

"""### 1. Crie um programa que carregue o arquivo Vendas.xlsx, por meio da biblioteca Pandas. Calcule e apresente a média da coluna do arquivo 'Valor Unitário'.

"""

# Digite seu código aqui
# .mean()
import pandas as pd
df = pd.read_excel('/content/drive/MyDrive/Vendas.xlsx')
media_valor_unitario = df['Valor Unitário'].mean()
print(f'A média da coluna "Valor Unitário" é: {media_valor_unitario:.2f}')

"""### 2. Crie um programa que carregue o arquivo Vendas.xlsx, por meio da biblioteca Pandas. Calcule e apresente a quantidade mínima da coluna do arquivo 'Quantidade'.

"""

# Digite seu código aqui
# .min()

import pandas as pd
df = pd.read_excel('/content/drive/MyDrive/Vendas.xlsx')
qtde_min = df['Quantidade'].min()
print(f'A quantidade mínima é de: {qtde_min}')

"""### 3. Crie um programa que carregue o arquivo Vendas.xlsx, por meio da biblioteca Pandas. Calcule e apresente o valor máximo da coluna do arquivo 'Valor Final'.

"""

# Digite seu código aqui
# .max()

import pandas as pd
df = pd.read_excel('/content/drive/MyDrive/Vendas.xlsx')
valor_max = df['Valor Final'].max()
print(f'O valor máximo do valor final é de: {valor_max}')

"""### 4. Crie um programa que carregue o arquivo Propaganda.csv, por meio da biblioteca Pandas. Calcule e apresente o valor máximo da coluna do arquivo 'Jornal'.

"""

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/Propaganda.csv')
valor_max = df['Jornal'].max()
print(f'O valor máximo da coluna jornal é: {valor_max}')

"""### 5. Crie um programa que carregue o arquivo Propaganda.csv, por meio da biblioteca Pandas. Gere um histograma, referente a coluna Rádio, utilizando a biblioteca plotly.

"""

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/Propaganda.csv')

import plotly.express as px
fig = px.histogram(df, x='Radio', title='Histograma da Coluna Rádio')
fig.show()

"""### 6. Crie um programa que carregue o arquivo Propaganda.csv, por meio da biblioteca Pandas. Gere um histograma, referente a coluna TV, utilizando a biblioteca Matplotlib, apresente na cor blueviolet.

"""

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/Propaganda.csv')

import matplotlib.pyplot as plt
plt.hist(df['TV'], color = 'blueviolet')
plt.title('Histograma da coluna TV')
plt.xlabel('Valores da TV')
plt.ylabel('Frequência')
plt.show()