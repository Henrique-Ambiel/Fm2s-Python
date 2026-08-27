import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv("material_case.xlsx - Medicamentos.csv", sep=";")

print(dados)
print(dados.info()) # Exibe informações sobre o DataFrame
print(dados.describe()) # Exibe estatísticas descritivas do DataFrame
print(dados.head()) # Exibe as primeiras linhas do DataFrame
print(dados.tail()) # Exibe as últimas linhas do DataFrame
