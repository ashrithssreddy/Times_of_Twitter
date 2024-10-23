"""
twitter_extraction.py

This module handles authentication with the Twitter API and extraction of tweets
from the user's timeline using the Tweepy library.
"""

import tweepy
import yaml
import pytz
from datetime import datetime
import pandas as pd

# Load credentials from config.yaml
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

import tweepy

def authenticate_twitter():
    """
    Authenticates to Twitter API v2 using Tweepy's Client class and the Bearer Token.

    Returns:
        tweepy.Client: Authenticated Tweepy Client object.
    """
    try:
        # Read your bearer token from the YAML or your credentials
        bearer_token = "YOUR_BEARER_TOKEN"

        # Authenticate using Tweepy's Client class for Twitter API v2
        client = tweepy.Client(bearer_token=bearer_token)
        
        print("Twitter Authentication Successful")
        return client

    except Exception as e:
        print(f"Error during Twitter authentication: {e}")
        return None


def extract_tweets_from_timeline(api, count=10):
    """
    Extracts tweets from the user's home timeline.

    Args:
        api (tweepy.API): Authenticated Tweepy API object.
        count (int): Number of tweets to extract.

    Returns:
        tweet_data (DataFrame): DataFrame containing tweet details.
    """
    try:
        tweets = api.home_timeline(count=count, tweet_mode='extended')
        tweet_data = []

        for tweet in tweets:
            tweet_data.append({
                'id': tweet.id,
                'created_at': tweet.created_at,
                'text': tweet.full_text,
                'user': tweet.user.screen_name
            })
        
        return pd.DataFrame(tweet_data)

    except Exception as e:
        print(f"Error during tweet extraction: {e}")
        return pd.DataFrame()


def extract_top_tweets(api, keyword=None, start_time=None, end_time=None, timezone='UTC', count=10):
    """
    Extracts top tweets containing a specific keyword or phrase within a date and time range,
    including timezone support. If no keyword is provided, retrieves top tweets regardless of keyword.

    Args:
        api (tweepy.Client): Authenticated Tweepy API Client object.
        keyword (str or None): Keyword or phrase to search for in tweets. Defaults to None.
        start_time (str or None): Start date and time in 'YYYY-MM-DD HH:MM' format. Defaults to None.
        end_time (str or None): End date and time in 'YYYY-MM-DD HH:MM' format. Defaults to None.
        timezone (str): Timezone for start and end times. Defaults to 'UTC'.
        count (int): Number of tweets to return.

    Returns:
        tweet_data (DataFrame): DataFrame containing tweet details.
    """
    try:
        # Convert start_time and end_time to the specified timezone
        if start_time:
            naive_start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M')
            start_time = pytz.timezone(timezone).localize(naive_start_time).astimezone(pytz.utc)
            start_time = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')  # ISO 8601 format for Twitter API v2

        if end_time:
            naive_end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M')
            end_time = pytz.timezone(timezone).localize(naive_end_time).astimezone(pytz.utc)
            end_time = end_time.strftime('%Y-%m-%dT%H:%M:%SZ')  # ISO 8601 format for Twitter API v2

        query = keyword if keyword else ''  # If keyword is None, set to empty string

        # Adjust for Twitter API v2 (Tweepy Client usage)
        tweets = api.search_recent_tweets(query=query, start_time=start_time, end_time=end_time, max_results=count, tweet_fields=['created_at', 'text', 'author_id'])

        tweet_data = []
        for tweet in tweets.data:
            tweet_data.append({
                'id': tweet.id,
                'created_at': tweet.created_at,
                'text': tweet.text,
                'user': tweet.author_id  # In Twitter API v2, 'author_id' is used instead of screen_name
            })
        
        return pd.DataFrame(tweet_data)

    except Exception as e:
        print(f"Error during tweet extraction: {e}")
        return pd.DataFrame()


if __name__ == "__main__":
    api = authenticate_twitter()
    
    if api:
        # Extract top tweets without a keyword
        top_tweets = extract_top_tweets(api, count=5)
        for tweet in top_tweets:
            print(f"{tweet['created_at']} - {tweet['user']}: {tweet['text']}")

        # Extract top tweets with a keyword phrase and specific times with timezone
        keyword = "BTC price"  # Example of a keyword phrase
        start_time = "2023-01-01 00:00"  # Start time
        end_time = "2023-01-31 23:59"  # End time
        timezone = "America/New_York"  # Example timezone
        top_tweets_with_keyword = extract_top_tweets(api, keyword, start_time, end_time, timezone, count=5)
        for tweet in top_tweets_with_keyword:
            print(f"{tweet['created_at']} - {tweet['user']}: {tweet['text']}")

