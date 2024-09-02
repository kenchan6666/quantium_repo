import pandas as pd

def process_csv(file_path):
    df = pd.read_csv(file_path)

    df = df[df['product'].str.lower() == 'pink morsel']

    df['sales'] = df['quantity'] * df['price']

    df = df[['sales', 'date', 'region']]

    return df