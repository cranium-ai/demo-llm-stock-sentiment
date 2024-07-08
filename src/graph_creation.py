import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

def create_stock_network(tickers):
    G = nx.Graph()
    for ticker in tickers:
        G.add_node(ticker)
    for i in range(len(tickers)):
        for j in range(i + 1, len(tickers)):
            correlation = get_stock_correlation(tickers[i], tickers[j])
            G.add_edge(tickers[i], tickers[j], weight=correlation)
    return G

def get_stock_correlation(ticker1, ticker2):
    df1 = pd.read_csv(f'data/{ticker1}_stock_data.csv')
    df2 = pd.read_csv(f'data/{ticker2}_stock_data.csv')
    df1['Date'] = pd.to_datetime(df1['Date'])
    df2['Date'] = pd.to_datetime(df2['Date'])
    merged_df = pd.merge(df1, df2, on='Date', suffixes=(f'_{ticker1}', f'_{ticker2}'))
    correlation = merged_df[f'Close_{ticker1}'].corr(merged_df[f'Close_{ticker2}'])
    return correlation

if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'GOOGL']
    G = create_stock_network(tickers)
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 10))
    nx.draw(G, pos, with_labels=True, node_size=7000, node_color='skyblue', font_size=20, font_color='black')
    plt.title('Stock Price Network Graph')
    plt.show()
