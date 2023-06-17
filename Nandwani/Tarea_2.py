import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# a) Cargar los datos del número de casos de COVID-19 en Chile entre marzo y junio de 2020.
url = 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto1/Covid-19.csv'
df = pd.read_csv(url)

# Columnas de interés
columnas_interes = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna', 'Poblacion',
                    '30-03-2020', '01-04-2020', '03-04-2020', '06-04-2020', '08-04-2020',
                    '10-04-2020', '13-04-2020', '15-04-2020', '17-04-2020', '20-04-2020',
                    '24-04-2020', '27-04-2020', '01-05-2020', '04-05-2020', '08-05-2020',
                    '11-05-2020', '15-05-2020', '18-05-2020', '22-05-2020', '25-05-2020',
                    '29-05-2020', '01-06-2020', '05-06-2020', '08-06-2020', '12-06-2020',
                    '15-06-2020', '19-06-2020', '23-06-2020', '28-06-2020']

# Filtrar las columnas de interés
df_filtered = df[columnas_interes]

# b) Visualizar la evolución temporal del número de casos utilizando gráficos de línea.
plt.figure(figsize=(10, 6))
fechas = columnas_interes[5:]  # Ignorar las primeras 5 columnas que contienen información de ubicación
num_casos = df_filtered.iloc[:, 5:].sum(axis=0)  # Sumar el número de casos por fecha
plt.plot(fechas, num_casos, marker='o', linestyle='-', color='b')
plt.xlabel('Fecha')
plt.ylabel('Número de casos')
plt.title('Evolución temporal del número de casos de COVID-19 en Chile (Marzo-Junio 2020)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# c) Análisis exploratorio de datos univariado y bivariado

# Análisis univariado
# Histograma del número total de casos por comuna
total_casos = df_filtered.iloc[:, 5:].sum(axis=1)  # Calcular el número total de casos por comuna
plt.figure(figsize=(8, 6))
plt.hist(total_casos, bins=20, color='b', alpha=0.7)
plt.xlabel('Número total de casos por comuna')
plt.ylabel('Frecuencia')
plt.title('Distribución del número total de casos de COVID-19 por comuna (Marzo-Junio 2020)')
plt.grid(True)
plt.show()

# Análisis bivariado
# Relación entre población y número total de casos
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df_filtered['Poblacion'], y=total_casos, color='b')
plt.xlabel('Población')
plt.ylabel('Número total de casos por comuna')
plt.title('Relación entre población y número total de casos de COVID-19 por comuna (Marzo-Junio 2020)')
plt.grid(True)
plt.show()

# Estadísticas descriptivas
print(total_casos.describe())

# Ccorrelación entre población y número total de casos
correlation = df_filtered['Poblacion'].corr(total_casos)
print('Correlación entre población y número total de casos:', correlation)
