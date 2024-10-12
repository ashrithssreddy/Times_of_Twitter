
# Email Service Documentation

## Email Configuration
Times of Twitter uses the Python `smtplib` library to send emails with your newspaper PDF attached. You will need to provide your email credentials in the `config.yaml` file.

## Supported Email Providers
- Gmail
- Outlook
- Custom SMTP servers

## Example Configuration (Gmail)
```yaml
email:
  smtp_server: "smtp.gmail.com"
  smtp_port: 587
  email_address: "your_email@gmail.com"
  email_password: "your_app_specific_password"
```

**Note**: If you're using Gmail, you may need to generate an **App Password** to use in place of your usual Gmail password.

## Troubleshooting
- **Authentication Errors**: Check that you’ve enabled "Less Secure Apps" (or generated an App Password) for Gmail.
