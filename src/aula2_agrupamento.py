import numpy as np
import pandas as pd

cuisine_rating = pd.read_csv('Cuisine_rating.csv') 

# Calcula um conjunto de estatísticas descritivas
# ex: media, mediana, qnt elementos, valor min e max de uma coluna, etc.
cuisine_rating.describe()

# Agrupando pela região e exibindo a culinária mais bem avaliada de uma região
cuisine_rating['Location'].value_counts()
cuisine_rating.select_dtypes(include=np.number) #seleciona somente as colunas numéricas
numeric_cols = cuisine_rating.select_dtypes(include=np.number).columns.to_list()
numeric_cols
cuisine_rating[numeric_cols] #mostra a lista de colunas

# Calcula a média para cada coluna
cuisine_rating.groupby(['Location'])[numeric_cols].mean()

# Agrupando pelo lugar e pela culinária
cuisine_rating.groupby(['Location', 'Cuisines'])[numeric_cols].mean()