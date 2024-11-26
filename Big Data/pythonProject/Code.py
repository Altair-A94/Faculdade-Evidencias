import pandas as pd

# Definindo manualmente os nomes das colunas
colunas = ['Municipio', 'CEP']

df = pd.read_csv('Municipio', sep='/', names=colunas, header=None, on_bad_lines='skip')

# Exibir a tabela
print(df)

df.to_excel('CEP.xlsx', index=False)