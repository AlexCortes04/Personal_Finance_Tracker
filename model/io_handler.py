import pandas as pd
from pathlib import WindowsPath


def read_csv(path_str):
    path = WindowsPath(path_str.replace('"', ''))
    return pd.read_csv(path)


def write_csv(df, filename):
    df.to_csv(filename, index=False)
