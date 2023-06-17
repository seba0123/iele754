import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

# Cargar los datos de casos de COVID-19
url = 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto1/Covid-19.csv'
df = pd.read_csv(url)

# Seleccionar las columnas de interés (fechas y casos confirmados)
df = df.loc[:, '30-03-2020':'28-06-2020']

# Calcular el total de casos por fecha
df['Total casos'] = df.sum(axis=1)

# Ajustar una distribución a los datos
mu, std = norm.fit(df['Total casos'])

# Generar valores para la distribución ajustada
x = np.linspace(df['Total casos'].min(), df['Total casos'].max(), 100)
y = norm.pdf(x, mu, std)

# Visualizar el histograma y la distribución ajustada
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Total casos', kde=True, color='blue', alpha=0.5)
plt.plot(x, y, 'r-', linewidth=2, label='Distribución normal')
plt.xlabel('Número de casos')
plt.ylabel('Frecuencia')
plt.title('Distribución de casos de COVID-19 y ajuste de distribución normal')
plt.legend()
plt.grid(True)
plt.show()


