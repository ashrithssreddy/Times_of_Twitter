"""
summarizer.py

This module summarizes tweets using a pre-trained transformer model from Hugging Face.
It processes the extracted tweets and provides concise summaries.
"""

from transformers import pipeline
import pandas as pd

def load_summarizer():
    """
    Loads the pre-trained summarization model from Hugging Face.

    Returns:
        summarizer (transformers.Pipeline): Summarization model pipeline.
    """
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarizer

def summarize_tweets(tweets_df, summarizer):
    """
    Summarizes tweets using the provided summarizer model.

    Args:
        tweets_df (DataFrame): DataFrame containing tweets to be summarized.
        summarizer (Pipeline): Hugging Face model pipeline for summarization.

    Returns:
        summarized_tweets_df (DataFrame): DataFrame with summarized tweets.
    """
    summarized_tweets = []

    for index, row in tweets_df.iterrows():
        text = row['text']  # Assuming 'text' is the column name for the tweet content

        # Skip short tweets
        if len(text.split()) < 30:
            summarized_text = text
        else:
            summarized_text = summarizer(text, max_length=50, min_length=25, do_sample=False)[0]['summary_text']

        summarized_tweets.append({
            'id': row['id'],
            'created_at': row['created_at'],
            'text': text,
            'summary': summarized_text
        })

    # Return a DataFrame with the summarized tweets
    return pd.DataFrame(summarized_tweets)