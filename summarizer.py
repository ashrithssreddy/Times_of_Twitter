from transformers import pipeline

# Step 1: Load Summarization Pipeline
def load_summarizer():
    # Using a pre-trained model from Hugging Face for summarization
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarizer