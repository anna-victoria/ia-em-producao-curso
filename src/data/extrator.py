import yfinance as yf
import pandas as pd

def download_data(symbols, start_date, end_date):
    path  = '/home/iaemproducao/iaemproducao/data/raw'
    for symbol in symbols:
        path_full = path+symbol+'parquet.gzip'
        
        df = yf.download(symbol, start_date, end_date)
        if df.shape[0]==0:
            print (f"a base {symbol} não retornou dados")
        else:
            df.to_parquet(path_full, compression='gzip')