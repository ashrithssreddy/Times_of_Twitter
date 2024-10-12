
# Known Issues and FAQs

## Known Issues
1. **Email Delivery Delays**:
   Some users may experience delays in email delivery depending on their email service provider.

2. **Rate Limiting**:
   Hitting Twitter API rate limits may cause delays in retrieving tweets if multiple requests are made too frequently.

## FAQs

### Why do I need a Twitter Developer account?
The Twitter API requires authentication via developer credentials. By creating a developer account, you can get the API keys needed to access your feed programmatically.

### Why is my email not sending?
Check that your SMTP settings are correct and that you've provided the correct email address and password in the `config.yaml` file. For Gmail users, make sure you've enabled App Passwords.

### Can I customize the newspaper's format?
The current version generates a standard newspaper-style PDF. Future versions will include customization options.
