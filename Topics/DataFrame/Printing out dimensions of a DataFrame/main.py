import pandas as pd


def print_dim(df):
    data = pd.DataFrame(df)
    dim = data.shape
    print(f'This DataFrame contains {dim[0]} rows and {dim[1]} columns')
