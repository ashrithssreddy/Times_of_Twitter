"""
pdf_formatter.py

This module handles generating a newspaper-style PDF from summarized tweets.
It uses the ReportLab library to format the tweets and output a PDF file.
"""

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def generate_pdf(summarized_tweets, output_filename="twitter_digest.pdf"):
    """
    Generates a PDF from summarized tweets.

    Args:
        summarized_tweets (list): List of dictionaries containing summarized tweets.
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

    # Loop through the summarized tweets and add them to the PDF
    for tweet in summarized_tweets:
        heading = f"{tweet['user']} - {tweet['created_at']}"
        heading_paragraph = Paragraph(heading, styles['Heading2'])
        story.append(heading_paragraph)

        summary_paragraph = Paragraph(tweet['summary'], styles['BodyText'])
        story.append(summary_paragraph)

        story.append(Spacer(1, 0.5 * inch))

    # Build the PDF document
    pdf.build(story)
    print(f"PDF generated: {output_filename}")
