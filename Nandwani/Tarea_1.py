import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ruta_2023 = "temperatura_aire_ceaza/2023/2023_temperatura_aire_ceaza.csv"
ruta_2020 = "temperatura_aire_ceaza/2020/2020_temperatura_aire_ceaza.csv"

df_2023 = pd.read_csv(ruta_2023)
df_2020 = pd.read_csv(ruta_2020)

df = pd.concat([df_2023, df_2020])

df['Fecha'] = pd.to_datetime(df['Fecha'])
df_abril = df[df['Fecha'].dt.month == 4]

df_abril['Promedio'] = df_abril.mean(axis=1)

sns.kdeplot(data=df_abril['Promedio'])
plt.xlabel('Temperatura')
plt.ylabel('Probabilidad')
plt.title('Distribución de temperatura promedio en la Región Metropolitana (Abril)')
plt.show()

