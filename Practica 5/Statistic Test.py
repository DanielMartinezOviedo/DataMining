import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.read_csv("Top100Streamed.csv")

df_por_genero = df.groupby(["Genero"]).agg({'Popularidad':['mean']})
df_por_genero.reset_index(inplace=True)
df_por_genero.columns = ['Genero', 'PromedioPopularidad']
df_por_genero.set_index("Genero", inplace=True)


#ANOVA POR GENERO-POPULARIDAD
moore_lm = ols('Genero ~PromedioPopularidad', data=df_por_genero).fit()
table = sm.stats.anova_lm(moore_lm, typ=2) # Type 2 Anova DataFrame
print(table)

