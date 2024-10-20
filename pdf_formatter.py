from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Frame, PageTemplate

# Step 1: Function to create PDF from summarized tweets
def generate_pdf(summarized_tweets, output_filename="twitter_digest.pdf"):
    # Create a PDF document
    pdf = SimpleDocTemplate(output_filename, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    # Title
    title = Paragraph("Times of Twitter - Daily Digest", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 0.25 * inch))

    # Loop through the summarized tweets and add them to the PDF
    for tweet in summarized_tweets:
        # Heading for each tweet with username and timestamp
        heading = f"{tweet['user']} - {tweet['created_at']}"
        heading_paragraph = Paragraph(heading, styles['Heading2'])
        story.append(heading_paragraph)
        
        # Summary of the tweet
        summary_paragraph = Paragraph(tweet['summary'], styles['BodyText'])
        story.append(summary_paragraph)

        # Spacer between tweets
        story.append(Spacer(1, 0.5 * inch))

    # Build the PDF document
    pdf.build(story)
    print(f"PDF generated: {output_filename}")
