import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from scipy import stats
import squarify as sq
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
df = pd.read_csv("Top100Streamed.csv")

plt.figure(figsize = (40,12))
df.groupby('Nombre_artista')['Nombre_cancion'].agg(len).sort_values(ascending = False).plot(kind = 'bar')
plt.ylabel('Numero de canciones', fontsize = 15)
plt.title('Artista vs Canciones en la lista', fontsize = 15)
plt.savefig("graficas/Canciones en la lista por artista.png")
plt.close()

plt.figure(figsize = (40,12))
df.groupby('Genero')['Nombre_cancion'].agg(len).sort_values(ascending = False).plot(kind = 'bar')
plt.ylabel('Numero de canciones', fontsize = 15)
plt.title('Genero vs Canciones en la lista', fontsize = 15)
plt.savefig("graficas/Genero en la lista por artista.png")
plt.close()

plt.figure(figsize=(40,12))
sq.plot(sizes=df.Genero.value_counts(), label=df["Genero"].unique(), alpha=.8 )
plt.axis('off')
plt.savefig("graficas/Generos populares en la lista.png")
plt.close()

labels = df.Nombre_artista.value_counts().index
sizes = df.Nombre_artista.value_counts().values
colors = ['red', 'yellowgreen', 'lightcoral', 'lightskyblue','cyan', 'green', 'black','yellow']
plt.figure(figsize = (10,10))
plt.pie(sizes, labels=labels, colors=colors)
autopct=('%1.1f%%')
plt.axis('equal')
plt.savefig("graficas/Artistas populares.png")
plt.close()

plt.subplots(figsize=(10,10))
plt.title('Dependencia entre la energia y la popularidad')
sns.regplot(x='Energia', y='Popularidad',
            ci=None, data=df)
plt.savefig("graficas/Dependencia entre la energia y la popularidad.png")
plt.close()

