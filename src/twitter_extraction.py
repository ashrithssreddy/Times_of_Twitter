"""
twitter_extraction.py

This module handles authentication with the Twitter API and extraction of tweets
from the user's timeline using the Tweepy library.
"""

import tweepy
import yaml

# Load credentials from config.yaml
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

def authenticate_twitter():
    """
    Authenticates with the Twitter API using credentials from config.yaml.

    Returns:
        api (tweepy.API): Authenticated Tweepy API object.
    """
    api_key = config['twitter']['api_key']
    api_secret = config['twitter']['api_key_secret']
    access_token = config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Twitter Authentication Successful")
    except Exception as e:
        print(f"Error during authentication: {e}")
    
    return api

def extract_tweets(api, count=10):
    """
    Extracts tweets from the user's home timeline.

    Args:
        api (tweepy.API): Authenticated Tweepy API object.
        count (int): Number of tweets to extract.

    Returns:
        tweet_data (list): List of dictionaries containing tweet details.
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
        
        return tweet_data

    except Exception as e:
        print(f"Error during tweet extraction: {e}")
        return []

if __name__ == "__main__":
    api = authenticate_twitter()
    tweets = extract_tweets(api, count=10)

    for tweet in tweets:
        print(f"{tweet['created_at']} - {tweet['user']}: {tweet['text']}")
