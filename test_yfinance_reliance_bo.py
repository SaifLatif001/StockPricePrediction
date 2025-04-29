import yfinance as yf
data = yf.download('RELIANCE.BO', start='2024-01-01', end='2024-12-31')
print(data.head())