from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Frame, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Register the custom fonts
pdfmetrics.registerFont(TTFont('Georgia', 'Georgia.ttf'))

def generate_pdf(summarized_tweets_df, output_filename="twitter_digest.pdf"):
    """
    Generates a PDF from summarized tweets styled like the New York Times.

    Args:
        summarized_tweets_df (DataFrame): DataFrame containing summarized tweets.
        output_filename (str): Name of the output PDF file.

    Returns:
        None
    """
    pdf = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()

    # Add custom title and body text styles
    styles.add(ParagraphStyle(name='NYT_Title', fontName='Georgia', fontSize=28, spaceAfter=20, alignment=1, textColor=colors.black, leading=32))
    styles.add(ParagraphStyle(name='NYT_SectionHeader', fontName='Georgia', fontSize=18, spaceAfter=12, textColor=colors.black))
    styles.add(ParagraphStyle(name='NYT_Body', fontName='Georgia', fontSize=11, leading=14, spaceAfter=12))

    story = []

    # Add an image (use the provided image file here)
    img = Image('image.png', 6*inch, 3*inch)
    story.append(img)
    story.append(Spacer(1, 0.3 * inch))

    # Title
    title = Paragraph("Times of Twitter - Daily Digest", styles['NYT_Title'])
    story.append(title)
    story.append(Spacer(1, 0.5 * inch))

    # Section Header
    section_header = Paragraph("Today's Top Tweets", styles['NYT_SectionHeader'])
    story.append(section_header)
    story.append(Spacer(1, 0.2 * inch))

    # Create two-column layout using Frames
    frame1 = Frame(inch, inch, 3.5*inch, 9*inch, showBoundary=0)
    frame2 = Frame(4.25*inch, inch, 3.5*inch, 9*inch, showBoundary=0)

    # Add summarized tweets to columns
    for index, row in summarized_tweets_df.iterrows():
        tweet = row['summary']  # Assuming 'summary' column contains the summarized tweet content
        tweet_paragraph = Paragraph(tweet, styles['NYT_Body'])
        story.append(tweet_paragraph)
        story.append(Spacer(1, 0.15 * inch))

    # Build the PDF with the two frames
    pdf.addPageTemplates([PageTemplate(frames=[frame1, frame2])])
    pdf.build(story)
