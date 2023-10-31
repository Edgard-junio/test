import pandas as pd
import numpy as np

# Carregamento do arquivo original
data = pd.read_csv("wines/winequality-white.csv", sep=';')

columns = [
"fixed acidity",
"volatile acidity",
"citric acid",
"residual sugar",
"chlorides",
"free sulfur dioxide",
"total sulfur dioxide",
"density",
"pH",
"sulphates",
"alcohol"]

def extremes_to_remove(data, column, pertil_1, pertil_2):

    # Calcula os percentils personalizados
    tmp = data[column].describe(percentiles=[pertil_1, pertil_2])

    # Extrai os valores extremos
    min_rmv = tmp[f'{pertil_1*100}%']
    max_rmv = tmp[f'{pertil_2*100}%']

    return [min_rmv, max_rmv]

def removing_extremes(data, columns, pertil_1, pertil_2):

    # Inicialização da variável final
    data_out = data
    
    # Inicialização de ista com extremos
    remove = []

    # Preenchimento da lista
    for column in columns:
        extremes = extremes_to_remove(data, column, pertil_1, pertil_2)
        remove.append(extremes[0])
        remove.append(extremes[1])

    # Remoção dos valores extremos (outliers)
    count = 0
    for column in columns:
        data_out = data[data[column] <= remove[count + 1]]
        data_out = data[data[column] >= remove[count]]
        count += 2

    return data_out

# Inicialização dos percentils desejados
pertil_1 = 0.005
pertil_2 = 0.995

# Remoção dos outliers
data = removing_extremes(data, columns, pertil_1, pertil_2)

# Salvamento do arquivo modificado
data.to_csv("wines_out/winewhite_out.csv", sep=';')