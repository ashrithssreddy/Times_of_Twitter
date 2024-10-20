from transformers import pipeline

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