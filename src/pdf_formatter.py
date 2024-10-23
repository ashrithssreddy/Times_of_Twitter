"""
pdf_formatter.py

This module handles generating a newspaper-style PDF from summarized tweets.
It uses the ReportLab library to format the tweets and output a PDF file.
"""

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def generate_pdf(summarized_tweets_df, output_filename="twitter_digest.pdf"):
    """
    Generates a PDF from summarized tweets.

    Args:
        summarized_tweets_df (DataFrame): DataFrame containing summarized tweets.
        output_filename (str): Name of the output PDF file.

    Returns:
        None
    """
    pdf = SimpleDocTemplate(output_filename, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    # Title
    title = Paragraph("Times of Twitter - Daily Digest", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 0.25 * inch))

    # Loop through the DataFrame rows instead of a list
    for index, row in summarized_tweets_df.iterrows():
        tweet = row['text']  # Assuming 'text' is the column name for the tweet content
        tweet_paragraph = Paragraph(tweet, styles['BodyText'])
        story.append(tweet_paragraph)
        story.append(Spacer(1, 0.15 * inch))

    pdf.build(story)
