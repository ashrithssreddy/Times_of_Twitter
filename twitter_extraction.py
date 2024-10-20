import tweepy
import os

# Step 1: Authenticate with Twitter API
def authenticate_twitter():
    # Use environment variables to store your credentials securely
    api_key = os.getenv('TWITTER_API_KEY')
    api_secret = os.getenv('TWITTER_API_SECRET')
    access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    # Authenticate using Tweepy
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    try:
        api.verify_credentials()
        print("Twitter Authentication Successful")
    except Exception as e:
        print(f"Error during authentication: {e}")
    
    return api

