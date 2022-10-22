
import pandas as pd
from tabulate import tabulate

def analysis_danceability(df: pd.DataFrame)->pd.DataFrame:
    df_by_d = df.groupby(["Genero"]).agg({'Bailabilidad': ['sum', 'count', 'mean', 'min', 'max']})
    df_by_d = df_by_d.reset_index()
    return df_by_d

df = pd.read_csv("Top100Streamed.csv")

#Análisis de la bailabilidad de las canciones por genero con el DF normalizado
df_analysis = analysis_danceability(df)

df_analysis.to_csv("Analisis Bailabilidad De Las Canciones por Genero.csv")


