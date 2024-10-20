# main.py

# Step 1: Import necessary modules
from src.twitter_extraction import authenticate_twitter, extract_tweets
from src.summarizer import load_summarizer, summarize_tweets
from src.pdf_formatter import generate_pdf
from src.email_service import send_email_with_attachment

# Main function to coordinate all steps
def main():
    print("Starting Times of Twitter...")

    # Step 2: Authenticate and extract tweets
    print("Authenticating with Twitter API...")
    api = authenticate_twitter()

    print("Extracting tweets from timeline...")
    tweets = extract_tweets(api, count=10)  # Fetch 10 tweets from the user's timeline
    
    if not tweets:
        print("No tweets extracted. Exiting...")
        return
    
    # Step 3: Summarize tweets
    print("Loading summarizer model...")
    summarizer = load_summarizer()

    print("Summarizing tweets...")
    summarized_tweets = summarize_tweets(tweets, summarizer)
    
    if not summarized_tweets:
        print("No tweets to summarize. Exiting...")
        return
    
    # Step 4: Generate PDF
    print("Generating PDF for the summarized tweets...")
    pdf_filename = "twitter_digest.pdf"
    generate_pdf(summarized_tweets, output_filename=pdf_filename)
    
    # Step 5: Email the PDF
    print("Sending the PDF via email...")
    recipient_email = "recipient@example.com"  # Replace with actual recipient email
    subject = "Your Daily Twitter Digest"
    body = "Here's your daily Twitter digest in PDF format."
    
    send_email_with_attachment(recipient_email, subject, body, pdf_filename)
    
    print("Process complete! The PDF has been emailed.")

if __name__ == "__main__":
    main()
