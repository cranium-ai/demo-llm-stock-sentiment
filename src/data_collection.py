import yfinance as yf
import tweepy
import pandas as pd

def collect_stock_data(tickers):
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data[ticker] = stock.history(period='1y')
    return data

def collect_twitter_data(api_key, api_secret_key, access_token, access_token_secret, query, max_tweets=100):
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en").items(max_tweets)
    tweet_data = [[tweet.created_at, tweet.text] for tweet in tweets]
    return pd.DataFrame(tweet_data, columns=['Datetime', 'Text'])

if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'GOOGL']
    stock_data = collect_stock_data(tickers)
    for ticker, data in stock_data.items():
        data.to_csv(f'data/{ticker}_stock_data.csv')
    
    api_key = 'YOUR_API_KEY'
    api_secret_key = 'YOUR_API_SECRET_KEY'
    access_token = 'YOUR_ACCESS_TOKEN'
    access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
    twitter_data = collect_twitter_data(api_key, api_secret_key, access_token, access_token_secret, query='AAPL')
    twitter_data.to_csv('data/twitter_data.csv', index=False)
