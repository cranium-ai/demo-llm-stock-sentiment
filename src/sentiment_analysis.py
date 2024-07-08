from transformers import pipeline
import pandas as pd
import openai

# Initialize the OpenAI API client
openai.api_key = 'YOUR_OPENAI_API_KEY'

def perform_sentiment_analysis(file_path):
    df = pd.read_csv(file_path)
    sentiment_pipeline = pipeline("sentiment-analysis")
    df['Sentiment'] = df['Text'].apply(lambda text: sentiment_pipeline(text)[0]['label'])
    return df

def generate_summary(sentiment_df):
    texts = sentiment_df['Text'].tolist()
    combined_text = " ".join(texts)
    
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=f"Summarize the overall sentiment of the following tweets: {combined_text}",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    summary = response.choices[0].text.strip()
    return summary

if __name__ == "__main__":
    sentiment_df = perform_sentiment_analysis('data/twitter_data.csv')
    sentiment_summary = generate_summary(sentiment_df)
    sentiment_df['Sentiment_Summary'] = sentiment_summary
    sentiment_df.to_csv('data/twitter_sentiment_data.csv', index=False)
    print("Sentiment summary added to the dataframe.")
