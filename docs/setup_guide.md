
# Setup Guide

## Prerequisites
- Python 3.8+
- Twitter Developer Account for API keys
- Email SMTP server (e.g., Gmail)

## Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/ashrithssreddy/Times_of_Twitter.git
   cd Times_of_Twitter
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the project**:
   - Create a `config/config.yaml` file with your Twitter API credentials and email server details:
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

4. **Run the project**:
   Run the main script to generate the newspaper:
   ```bash
   python main.py
   ```
