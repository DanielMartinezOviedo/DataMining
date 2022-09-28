import pandas as pd
from tabulate import tabulate
from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile

api = KaggleApi()
api.authenticate()
api.dataset_download_file('ariyoomotade/netflix-data-cleaning-analysis-and-visualization', file_name='netflix1.csv')
test_file_name = "netflix1.csv.zip"

with ZipFile(test_file_name, 'r') as zip:
    zip.printdir()
    zip.extractall()

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, tablefmt='orgtbl', stralign='center', numalign='center'))
df = pd.read_csv("netflix1.csv")
print_tabulate(df)
