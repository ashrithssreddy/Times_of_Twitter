from src.twitter_extraction import extract_tweets

# Step 1: Load Summarization Pipeline
def load_summarizer():
    # Using a pre-trained model from Hugging Face for summarization
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarizer

# Step 2: Summarize a List of Tweets
def summarize_tweets(tweets, summarizer, max_length=100):
    summarized_tweets = []

    for tweet in tweets:
        text = tweet['text']
        
        # If the tweet is already short, no need to summarize
        if len(text.split()) < 30:  # Adjust word limit as needed
            summarized_text = text
        else:
            # Summarize the tweet (truncate long text, optional max_length)
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

# Main function to run summarization
if __name__ == "__main__":
    # Import the extracted tweets from twitter_extraction.py
    from twitter_extraction import extract_tweets, authenticate_twitter
    
    # Step 1: Authenticate and extract tweets
    api = authenticate_twitter()
    tweets = extract_tweets(api, count=10)  # Fetch real tweets from the timeline
    
    # Step 2: Load the summarizer model
    summarizer = load_summarizer()
    
    # Step 3: Summarize the extracted tweets
    summarized_tweets = summarize_tweets(tweets, summarizer)
    
    # Display summarized tweets
    for tweet in summarized_tweets:
        print(f"Original Tweet: {tweet['original_text']}\nSummary: {tweet['summary']}\n")