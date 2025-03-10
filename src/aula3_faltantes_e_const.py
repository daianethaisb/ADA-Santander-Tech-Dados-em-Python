import numpy as np
import pandas as pd

houses_sp = pd.read_csv('houses_sp.csv') 

houses_sp.head(10)

houses_sp['city'].value_counts() #city:coluna

# Dados constantes:
#A coluna cidade se repete para todos os resultados e isso acaba não sendo
#interessante para esta análise. Sendo assim, ela pode ser removida 
#para que não sejam consumidos recursos de processamento desnecessários. 
houses_sp = houses_sp.drop(columns=['city'])

# Dados errôneos: dados nulos ou dados com erro de digitação, por ex.
houses_sp['rooms']
houses_sp.info()

#remover dados por ter uma coluna nula não é o mais indicado pois perderemos os
#demais dados da coluna. Nesse caso, podemos usar a mediana para fazer o preenchimento. O comando a seguir preenche os dados nulos.
houses_sp['rooms'].median()

# Preenche os dados nulos com um valor definido
houses_sp['rooms'] = houses_sp['rooms'].fillna(houses_sp['rooms'].median())

# Substitui valores em uma coluna (neste caso. - por 0)
houses_sp.loc[houses_sp['floor'] == '-', 'floor'] = '0'



