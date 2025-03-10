import numpy as np
import pandas as pd

houses = pd.read_csv('houses_to_rent.csv') 

houses.head()

houses.describe()

# O tratamento de outliers se refere a dados que se destoam dos demais. 
#ex: a média de banheiros de um conjunto de casas é 3, mas uma só casa tem 25 banheiros. 
#esse dado pode atrapalhar o calculo de uma média, por exemplo. 

# Critérios de detecção de outliers: 
#(Distância entre o registro do describe 0,75 e 0,25 : 
# > 3° quartil + 1,5 essa distância - outliers para mais
# ou < 1° quartil - 1,5 essa distância - outliers para menos)
#IQR: distância inter quartil 
q1 = houses['bathroom'].quantile(0.25) # Primeiro quartil
q3 = houses['bathroom'].quantile(0.75) 

IQR = q3 - q1
print(f'IQR: {IQR}')

houses_outliers = houses[houses['bathroom'] < q1 - (IQR * 1.5) 
                         | houses['bathroom'] > q3 + (IQR * 1.5)]

houses_outliers #retorna só os resultados "fora da curva"


houses_inliers = houses[houses['bathroom'] >= q1 - (IQR * 1.5) 
                         & houses['bathroom'] <= q3 + (IQR * 1.5)]

houses_inliers #retorna só os resultados dentro do padrão

# Tirar esses dados da análise diminui a base mas faz com que os resultados
#sejam mais acertivos. 