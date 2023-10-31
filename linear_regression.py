import pandas as pd
import statsmodels.api as sm

# Carregando os dados do arquivo CSV
data = pd.read_csv("wines_out/winewhite_out.csv", sep=';')

# Definindo as variáveis independentes (X) e a variável dependente (y)
X = data[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
          'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']]
X = sm.add_constant(X)  # Adicionando a coluna de 1s para representar a constante
y = data['quality']

# Criando o modelo de regressão
modelo = sm.OLS(y, X).fit()

# Obtendo os resultados do modelo
resultados = modelo.summary()

# Convertendo as tabelas de resultados para DataFrames
coeficientes = pd.DataFrame(resultados.tables[1])
erros_padrao = pd.DataFrame(resultados.tables[1])

# Salvando os coeficientes e erros padrão em um arquivo CSV
with open('wines_out/resultados_regressao_.csv', 'w') as file:
    file.write("# Coeficientes:\n")
    coeficientes.to_csv(file, sep=';', index=False)

    file.write("\n\n# Erros Padrão:\n")
    erros_padrao.to_csv(file, sep=';', index=False)

