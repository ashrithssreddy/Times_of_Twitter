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

# Step 2: Extract Tweets from Timeline
def extract_tweets(api, count=10):
    try:
        # Get the user's home timeline tweets
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

# Main function to run the extraction
if __name__ == "__main__":
    api = authenticate_twitter()
    tweets = extract_tweets(api, count=10)
    
    # Display extracted tweets
    for tweet in tweets:
        print(f"{tweet['created_at']} - {tweet['user']}: {tweet['text']}")
