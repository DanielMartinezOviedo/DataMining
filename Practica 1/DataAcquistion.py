import pandas as pd
from tabulate import tabulate
from kaggle.api.kaggle_api_extended import KaggleApi
import os

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, tablefmt='github', showindex=False, numalign='center', stralign='left',headers="keys"))

api = KaggleApi()
api.authenticate()
api.dataset_download_file('pavan9065/top-100-most-streamed-songs-on-spotify', file_name='Top 100 most Streamed - Sheet1.csv')
os.rename('Top%20100%20most%20Streamed%20-%20Sheet1.csv', 'Top100Streamed.csv')

