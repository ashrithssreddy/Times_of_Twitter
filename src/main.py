"""
main.py

This is the main script for Times of Twitter. It coordinates the entire workflow:
1. Authenticates with the Twitter API.
2. Extracts tweets from the user's timeline.
3. Summarizes the tweets using AI.
4. Generates a PDF with the summarized tweets.
5. Sends the PDF via email.
"""

from src.twitter_extraction import authenticate_twitter, extract_tweets
from src.summarizer import load_summarizer, summarize_tweets
from src.pdf_formatter import generate_pdf
from src.email_service import send_email_with_attachment
import yaml

# Load email receiver from config.yaml
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

def main():
    """
    Main function to coordinate the process of extracting, summarizing, and emailing tweets.

    Returns:
        None
    """
    print("Starting Times of Twitter...")

    # Step 1: Authenticate and extract tweets
    print("Authenticating with Twitter API...")
    api = authenticate_twitter()

    print("Extracting tweets from timeline...")
    tweets = extract_tweets(api, count=10)
    
    if not tweets:
        print("No tweets extracted. Exiting...")
        return
    
    # Step 2: Summarize tweets
    print("Loading summarizer model...")
    summarizer = load_summarizer()

    print("Summarizing tweets...")
    summarized_tweets = summarize_tweets(tweets, summarizer)
    
    if not summarized_tweets:
        print("No tweets to summarize. Exiting...")
        return
    
    # Step 3: Generate PDF
    print("Generating PDF for the summarized tweets...")
    pdf_filename = "twitter_digest.pdf"
    generate_pdf(summarized_tweets, output_filename=pdf_filename)
    
    # Step 4: Email the PDF
    print("Sending the PDF via email...")
    recipient_email = config['gmail']['email_receiver']
    subject = "Your Daily Twitter Digest"
    body = "Here's your daily Twitter digest in PDF format."
    
    send_email_with_attachment(recipient_email, subject, body, pdf_filename)
    
    print("Process complete! The PDF has been emailed.")

if __name__ == "__main__":
    main()
