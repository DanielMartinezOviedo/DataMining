import requests
import io
import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import re
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import numbers
import statsmodels.api as sm
from statsmodels.regression.linear_model import OLS, WLS
df = pd.read_csv("Top100Streamed.csv")

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

def transform_variable(df: pd.DataFrame, x:str)->pd.Series:
    if isinstance(df[x][0], numbers.Number):
        return df[x] # type: pd.Series
    else:
        return pd.Series([i for i in range(0, len(df[x]))])

def linearRegression(df: pd.DataFrame, x:str, y: str)->None:
    fixed_x = transform_variable(df, x)
    model = sm.OLS(df[y],sm.add_constant(fixed_x)).fit()
    #print(model.summary())

    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    df.plot(x=x,y=y, kind='scatter', figsize=(22,14))
    plt.plot(df[x],[pd.DataFrame.mean(df[y]) for _ in fixed_x.items()], color='green')
    plt.plot(df_anio_pop[x],[ coef.values[1] * x + coef.values[0] for _, x in fixed_x.items()], color='red')
    plt.xticks(rotation=90)
    plt.savefig(f'graficas/linealRegression_{y}_{x}.png')
    plt.close()

df_anio_pop = df.groupby(["Anio"], as_index=False)["Popularidad"].aggregate(pd.DataFrame.max)
df_anio_bai = df.groupby(["Anio"], as_index=False)["Bailabilidad"].aggregate(pd.DataFrame.mean)
df_anio_ener = df.groupby(["Anio"], as_index=False)["Energia"].aggregate(pd.DataFrame.max)

linearRegression(df_anio_pop, "Anio", "Popularidad")
linearRegression(df_anio_bai, "Anio", "Bailabilidad")
linearRegression(df_anio_ener, "Anio", "Energia")