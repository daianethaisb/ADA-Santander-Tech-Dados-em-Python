import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Importando dataset da biblioteca seaborn
iris = sns.load_dataset('iris')

# histplot: Gera um grafico de frequencia dos valores contínuos distribuidos,
#chamado histograma, onde x é a coluna horizontal
# Kde = true: mostra a curva da evolução
col = 'sepal_length' 
sns.histplot(data=iris, x=col, kde=True).set_title(f'Distribuição da variável {col}')

# o For mostra mais de um grafico de uma vez só.
#removemos a coluna espécies pois esse tipo de gráfico não performa muito bem
#com variáveis categóricas, estamos trabalhando com vars contínuas.
for col in iris.drop(columns='species'):
    sns.histplot(data=iris, x=col, kde=True).set_title(f'Distribuição da variável {col}')
    plt.show() #hue:mostra o gráfico colorido por espécies

# hue: diferencia com base em uma coluna (espécies) através de cores
for col in iris.drop(columns='species'):
    sns.histplot(data=iris, x=col, kde=True, hue=iris['species']).set_title(f'Distribuição da variável {col}')
    plt.show() 

# barplot: gera um gráfico que mostra a relação entre uma variável numérica 
#e uma categórica, valor médio.
# y: define a coluna vertical que estamos analisando dentro do gráfico. 
# ci: intervalo de confiança.
for col in iris.drop(columns='species'):
    sns.barplot(data=iris, x=col, kde=True, hue=iris['species'], y=col, ci=90)
    plt.show() 

# Em um caso onde desejamos visualizar o desempenho mensal das vendas de 
#uma loja online ao longo de 2022, por exemplo, podemos usar o seguinte
#comando, considerando um DataFrame df com uma coluna 'data' e uma coluna 'vendas'

#df.plot(x='data', y='vendas')
#seasonal_decompose(): desagrega uma série temporal em componentes de tendência, sazonalidade e resíduo
