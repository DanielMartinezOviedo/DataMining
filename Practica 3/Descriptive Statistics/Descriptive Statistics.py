
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

def graficaBoxPlotCantidadPelisPorClasificacion(file_name:str):
    df = pd.read_csv(file_name)
    df_aux = df.groupby(["Clasificacion","Cantidad"])[["Cantidad"]].aggregate(pd.DataFrame.sum)
    df_aux.boxplot(by = "Clasificacion", figsize=(30,15))
    plt.xticks(rotation=45)
    plt.savefig("graficas/BoxPlotCantidadPelisPorClasificacion.png")
    plt.close()

def graficaByCategoryDocumentariesByReleaseYear(file_name:str):
    df = pd.read_csv(file_name)
    df_aux = df.groupby(["listed_in", "date_added"])[["release_year"]].aggregate(pd.DataFrame.mean)
    df_aux.reset_index(inplace=True)
    df_aux.set_index("listed_in", inplace=True)
    df[df["listed_in"] == "Documentaries"].plot(y =["release_year"],figsize=(15,9))
    plt.xticks(rotation=90)
    plt.savefig("graficas/ItCategoryDocumentariesByReleaseYear.png")
    plt.close()

def graficaDateAddedCategoryMovieByReleaseYear(file_name:str):
    df = pd.read_csv(file_name)
    df_aux = df.groupby(["date_added", "listed_in"])[["release_year"]].mean().unstack()
    df_aux.plot(y = 'release_year', legend=False,figsize=(25,15))
    plt.xticks(rotation=90)
    plt.savefig("graficas/FooDateAddedCategoryMovieByReleaseYear.png")
    plt.close()


graficaBoxPlotCantidadPelisPorClasificacion("CantidadPelisPorClasificacion.csv")
graficaByCategoryDocumentariesByReleaseYear("ContentUSAinNetflix.csv")
graficaDateAddedCategoryMovieByReleaseYear("ContentUSAinNetflix.csv")