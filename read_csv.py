import pandas as pd

def get_usage(date):
    df = pd.read_csv(f'./csvs/{date}.csv')
    df = df[['Time', 'Usage tier 1 (kWh)']]
    df.columns = ['time', 'usage']
    df_t = df.T
    df_t.columns = df_t.iloc[0]
    df_t = df_t[1:]
    df_t.insert(0, 'date', date)
    df_t = df_t.rename_axis('index', axis=1)
    return df_t.reset_index(drop=True)