
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, tablefmt='github', showindex=False, numalign='center', stralign='left',headers="keys"))

df = pd.read_csv("Top100Streamed.csv")

#Data Cleaning

#Renombrando las columnas
df.rename(columns={'artist':'Nombre_artista',
                    'title':'Nombre_cancion',
                    'length':'Duracion(ms)',
                    'year':'Anio',
                    'popularity':'Popularidad',
                    'danceability':'Bailabilidad',
                    'energy':'Energia',
                    'loudness.dB':'Sonoridad',
                    'speechiness':'Speechiness',
                    'acousticness':'Acousticness',
                    'liveness':'Liveness',
                    'valance':'Valence',
                    'beats.per.minute':'Pulsos por minuto',
                    'top genre':'Genero',
                    },inplace=True)

df.to_csv("Top100Streamed.csv")

#Data Statistics

print("\nMuestra de Registros\n")

print("Primeros 5 registros: \n",df.head())

print("Ultimos 5 registros: \n",df.tail())

print("Información general del dataframe :\n",df.info())

print("Informe de los datos estadisticos: \n",df.describe())

print('Promedio general de los duracion de las canciones: \n',df['Duracion(ms)'].mean())
print('Mediana general de los los años con mas presencia:\n',df['Anio'].median())
print('Desviación estándar general de la bailabilidad:\n',df['Bailabilidad'].std())

print("Correlacion es:\n", df.corr())

print("\nCantidad de valores en finlas: \n",df.count())

print("\nMaximos de cada columna: \n",df.max())

print("\nMinimos de cada columna: \n",df.min())

fig, ax = plt.subplots()
df.hist('Bailabilidad', ax=ax)
fig.savefig('graficas/histogramaBailabilidad.png')
df.hist('Duracion(ms)', ax=ax)
fig.savefig('graficas/histogramaDuration.png')
df.hist('Energia', ax=ax)
fig.savefig('graficas/histogramaEnergia.png')
df.hist('Popularidad', ax=ax)
fig.savefig('graficas/histogramaPopularidad.png')