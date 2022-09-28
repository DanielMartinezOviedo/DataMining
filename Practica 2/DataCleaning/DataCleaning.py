
import pandas as pd
from tabulate import tabulate

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='github'),'\n\n')


def FiltroSoloPeliculasDeUSA(file_name:str):
    df = pd.read_csv(file_name)
    df_USA=df[(df["country"]=="United States") & (df["type"]=="Movie")]
    df_USA.to_csv('ContentUSAinNetflix.csv')

def CantidadDePeliculasPorCategoria(file_name:str):
    df = pd.read_csv(file_name)
    df_listed_in = df.groupby(["listed_in"]).agg({'listed_in': ['count']})
    df_listed_in.reset_index(inplace=True)
    df_listed_in.columns = ['Categoria', 'Cantidad']
    print_tabulate(df_listed_in)

def CantidadDePeliculasPorClasificacion(file_name:str):
    df = pd.read_csv(file_name)
    df_category = df.groupby(["rating"]).agg({'rating': ['count']})
    df_category.reset_index(inplace=True)
    df_category.columns = ['Clasificacion', 'Cantidad']
    df_category.to_csv("CantidadPelisPorClasificacion.csv")
    print_tabulate(df_category)

FiltroSoloPeliculasDeUSA("netflix1.csv")
CantidadDePeliculasPorCategoria("ContentUSAinNetflix.csv")
CantidadDePeliculasPorClasificacion("ContentUSAinNetflix.csv")
