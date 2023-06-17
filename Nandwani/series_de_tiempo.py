import pandas as pd

data_url = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto14/FallecidosCumulativo.csv"
df = pd.read_csv(data_url)

# Muestra las primeras filas del dataframe
print(df.head())

# Verifica si hay valores faltantes
valores_faltantes = df.isnull().sum()

# Maneja los valores faltantes rellenándolos con el valor anterior en la columna
df_limpio = df.fillna(method='ffill')

# Convierte una columna a datetime
df_limpio['Fecha'] = pd.to_datetime(df_limpio['Fecha'])

# Calcula la media de la columna '2020-05-30'
valor_medio = df_limpio['2020-05-30'].mean()
print(f'Media de la columna "2020-05-30": {valor_medio}')

import matplotlib.pyplot as plt

# Dibuja un histograma de la columna '2020-05-30'
plt.hist(df_limpio['2020-05-30'])
plt.title('Histograma de la columna "2020-05-30"')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()

# Calcula la correlación entre las columnas '2020-05-30' y '2021-05-30'
correlacion = df_limpio['2020-05-30'].corr(df_limpio['2021-05-30'])
print(f'Correlación entre "2020-05-30" y "2021-05-30": {correlacion}')


# Dibuja las columnas '2020-05-30' y '2021-05-30' como series temporales
plt.plot(df_limpio['2020-05-30'], label='2020-05-30')
plt.plot(df_limpio['2021-05-30'], label='2021-05-30')
plt.legend()
plt.title('Comparación de las columnas "2020-05-30" y "2021-05-30"')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.show()


