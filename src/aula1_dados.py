import numpy as np
import pandas as pd

# Import do dataset (Base: kaggle)
cuisine_rating = pd.read_csv('Cuisine_rating.csv')

# Mostra os 5 primeiros registros por padrão ou exibe a quantidade de linhas
#definida entre parenteses.
cuisine_rating.head()

# Mostra os 10 ultimos registros
cuisine_rating.tail(10)

# Para informações em geral, ex: qnt entradas, se há dados nulos, etc. 
cuisine_rating.info()

cuisine_rating['Cuisines'] #informações da coluna
# Conta a frequência que aparece cada culinaria na base, 
#como os dados estão distribuidos na coluna
cuisine_rating['Cuisines'].value_counts()

# Filtra coluna por resultado
cuisine_rating[cuisine_rating['Cuisines'] == 'Japanese']

# Faz uma média das avaliações (Overall Rating) onde a culinária é japonesa
cuisine_rating[cuisine_rating['Cuisines'] == 'Japanese']['Overall Rating'].mean()