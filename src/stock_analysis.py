import pandas as pd
import matplotlib.pyplot as plt

def analyze_stock_data(file_path):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    plt.figure(figsize=(10, 5))
    plt.plot(df['Close'], label='Close Price')
    plt.title('Stock Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    analyze_stock_data('data/AAPL_stock_data.csv')
