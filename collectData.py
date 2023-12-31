import yfinance as yf
import pandas as pd
from tqdm import tqdm
from datetime import datetime, timedelta

# Set date range for data
start_date = '2023-01-01'

yesterday = datetime.now() - timedelta(days=1)
end_date = yesterday.strftime('%Y-%m-%d')

# Replace 'AAPL' with the desired stock symbol
symbols = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'ORCL', 'ADBE', 'CRM', 'AMD', 'NFLX']

for ticker_symbol in tqdm(symbols):
    # Imports data from Yahoo Finance API
    data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Save data to a CSV file
    data.to_csv(f'{ticker_symbol}_historical_data.csv')

# print("End of file")
