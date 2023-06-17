import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Cargar los datos
url = "https://raw.githubusercontent.com/rociochavezmx/Rocio-Chavez-youtube-Files/master/Contaminacion%20Atmosferica.csv"
df = pd.read_csv(url)

# Seleccionar las variables de interés
variable1 = df['Fabricas']
variable2 = df['Habitantes']
variable3 = df["Temperatura"]

# Calcular la matriz de correlación
correlation_matrix = np.corrcoef(variable1, [variable2, variable3])
print("Matriz de correlación:\n", correlation_matrix)

# Visualizar la matriz de correlación con un mapa de calor
print("\nColumnas del DataFrame:", df.columns)
plt.matshow(df.corr())
plt.colorbar()
plt.title("Mapa de calor de la matriz de correlación")
plt.show()

# Ajustar un modelo de regresión lineal y visualizarlo
slope, intercept = np.polyfit(df['Contaminacion_SO2'], df['Fabricas'], 1)
plt.scatter(df['Contaminacion_SO2'], df['Fabricas'], label='Datos')
plt.plot(df['Contaminacion_SO2'], slope * df['Contaminacion_SO2'] + intercept, color='red', label='Ajuste lineal')
plt.xlabel('Contaminacion_SO2')
plt.ylabel('Fabricas')
plt.title('Regresión Lineal entre Contaminacion_SO2 y Fabricas')
plt.legend()
plt.show()

# Calcular el coeficiente de correlación de Pearson y el p-valor
corr, p_value = pearsonr(df['Contaminacion_SO2'], df['Fabricas'])
print("Coeficiente de correlación de Pearson:", corr)
print("P-valor:", p_value)
