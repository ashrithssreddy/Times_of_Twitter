"""
summarizer.py

This module summarizes tweets using a pre-trained transformer model from Hugging Face.
It processes the extracted tweets and provides concise summaries.
"""

from transformers import pipeline

def load_summarizer():
    """
    Loads the pre-trained summarization model from Hugging Face.

    Returns:
        summarizer (transformers.Pipeline): Summarization model pipeline.
    """
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarizer

def summarize_tweets(tweets, summarizer, max_length=100):
    """
    Summarizes a list of tweets using the provided summarizer model.

    Args:
        tweets (list): List of tweets to be summarized.
        summarizer (Pipeline): Hugging Face model pipeline for summarization.
        max_length (int): Maximum length of the summary.

    Returns:
        summarized_tweets (list): List of dictionaries with summarized tweets.
    """
    summarized_tweets = []

    for tweet in tweets:
        text = tweet['text']
        
        if len(text.split()) < 30:
            summarized_text = text
        else:
            summary = summarizer(text, max_length=max_length, min_length=30, do_sample=False)
            summarized_text = summary[0]['summary_text']
        
        summarized_tweets.append({
            'id': tweet['id'],
            'created_at': tweet['created_at'],
            'user': tweet['user'],
            'original_text': text,
            'summary': summarized_text
        })
    
    return summarized_tweets
