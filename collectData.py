import yfinance as yf
import pandas as pd
from tqdm import tqdm
from datetime import datetime, timedelta
import sqlite3

symbols = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'ORCL', 'ADBE', 'CRM', 'AMD', 'NFLX']

# Set date range for historical data
lweek = datetime.now() - timedelta(days=9)
start_date = lweek.strftime('%Y-%m-%d')

yesterday = datetime.now() - timedelta(days=3)
end_date = yesterday.strftime('%Y-%m-%d')

# Set date range for test data
lweek = datetime.now() - timedelta(days=2)
start_date2 = lweek.strftime('%Y-%m-%d')

yesterday = datetime.now() - timedelta(days=1)
end_date2 = yesterday.strftime('%Y-%m-%d')

for ticker_symbol in tqdm(symbols):
    # Imports data from Yahoo Finance API
    hist_data = yf.download(ticker_symbol, start=start_date, end=end_date, interval="15m")
    test_data = yf.download(ticker_symbol, start=start_date2, end=end_date2, interval="15m")

    # Save data to SQLite database
    conn = sqlite3.connect('stock_data.db')
    hist_data.to_sql(f'{ticker_symbol}_historical', conn, if_exists='replace')

    # Save data to a CSV file
    test_data.to_csv('data/' + f'{ticker_symbol}_test_data.csv')
