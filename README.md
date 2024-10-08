# **Twitter Newspaper**

**Twitter Newspaper** is a tool that extracts tweets from your Twitter feed, summarizes them using AI, formats the summarized content into a newspaper-style PDF, and emails it to you every morning. This allows you to receive a daily digest of relevant information from your feed in a clean, readable format.

## **Current Capabilities**

1. **Twitter Feed Extraction**:
   - Extracts tweets from your home timeline using the Twitter API. 
   - Fetches tweets from the accounts you follow to ensure relevance.

2. **AI-Powered Summarization**:
   - Summarizes the tweets using AI, providing concise and easy-to-read versions of the raw tweets.
   - Condenses long tweet threads or groups of tweets into key takeaways.

3. **PDF Newspaper Formatting**:
   - Converts the summarized tweets into a newspaper-style format.
   - Organizes the information in a clean, structured layout for easy reading.

4. **Automated Email Delivery**:
   - Emails the generated PDF to the user every morning.
   - Ensures you receive the latest information without manual effort.

## **Project Structure**

```bash
Twitter_Newspaper/
│
├── README.md                # Project description and setup instructions
├── main.py                  # Main script to run the project
├── twitter_extraction.py     # Script for extracting tweets from your feed
├── summarizer.py             # Script for summarizing tweets using AI
├── pdf_formatter.py          # Script for generating the newspaper-style PDF
├── email_service.py          # Script for sending the PDF via email
├── requirements.txt          # List of dependencies required for the project
├── config/                   # Configuration files (API keys, credentials, etc.)
├── assets/                   # Folder for storing generated images or PDFs
└── .gitignore                # Ignoring unnecessary files and sensitive data
```

## **Installation and Setup**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ashrithssreddy/Twitter_Newspaper.git
   cd Twitter_Newspaper
   ```

2. **Install dependencies**:
   Make sure you have Python installed. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up configuration**:
   - Create a `config/config.yaml` file to store your API keys and other credentials (Twitter API keys, email SMTP settings, etc.).
   - Example `config.yaml` format:
     ```yaml
     twitter:
       consumer_key: "your_consumer_key"
       consumer_secret: "your_consumer_secret"
       access_token: "your_access_token"
       access_token_secret: "your_access_token_secret"

     email:
       smtp_server: "your_smtp_server"
       smtp_port: your_smtp_port
       email_address: "your_email"
       email_password: "your_password"
     ```

## **How to Use**

1. **Run the main script**:
   The main script orchestrates the extraction, summarization, and formatting process. To generate your daily newspaper, run:
   ```bash
   python main.py
   ```

2. **Receive the Newspaper via Email**:
   After running the script, the summarized PDF will be emailed to you automatically.

## **Future Enhancements**

- **Real-time streaming of tweets**.
- **AI-generated images** for tweets.
- **Sentiment analysis** for added insights into tweet tone.
- **Advanced customization of feed filters and newspaper sections**.
- **Trend prediction** and topic clustering.

## **Contributing**

If you'd like to contribute to the project, feel free to submit pull requests or open issues to discuss potential improvements.
