import pandas as pd
from datetime import datetime


def generate_html_from_dataframe(df):
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Times of Twitter - Daily Digest</title>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap">
        <style>
            body {{
                font-family: 'Roboto', sans-serif;
                background-color: #f8f9fa;
                margin: 0;
                padding: 0;
                color: #333;
            }}
            .container {{
                width: 80%;
                margin: 0 auto;
                padding: 20px;
                max-width: 800px;
                background-color: #ffffff;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                text-align: center;
                padding: 20px;
            }}
            .header h1 {{
                font-weight: 700;
                font-size: 2.5rem;
            }}
            .article {{
                border-bottom: 1px solid #ddd;
                padding: 20px 0;
            }}
            .article:last-child {{
                border-bottom: none;
            }}
            .article-title {{
                font-weight: 500;
                font-size: 1.5rem;
                margin-bottom: 10px;
            }}
            .article-meta {{
                font-size: 0.9rem;
                color: #777;
                margin-bottom: 10px;
            }}
            .article-content {{
                font-size: 1rem;
                line-height: 1.6;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Times of Twitter - Daily Digest</h1>
                <p>Stay informed with the top tweets of the day</p>
            </div>
            
            {articles}
        </div>
    </body>
    </html>
    """

    article_template = """
    <div class="article">
        <h2 class="article-title">{title}</h2>
        <p class="article-meta">Posted on {created_at} | #{id}</p>
        <p class="article-content">{summary}</p>
    </div>
    """

    articles_html = ""
    for _, row in df.iterrows():
        articles_html += article_template.format(
            title=row['text'],
            created_at=datetime.strptime(row['created_at'], "%Y-%m-%d %H:%M:%S").strftime("%B %d, %Y"),
            id=row['id'],
            summary=row['summary']
        )

    return html_template.format(articles=articles_html)


# Example usage
if __name__ == "__main__":
    data = {
        'id': [1, 2],
        'created_at': ['2024-10-22 12:00:00', '2024-10-23 14:30:00'],
        'text': ["Bitcoin rises to $52,000 amid increased institutional interest.",
                 "Elon Musk's tweet sends Bitcoin price to $54,000!"],
        'summary': ["Bitcoin has seen a significant uptick, hitting $52,000 as institutional interest surges.",
                    "Elon Musk's latest tweet has once again moved the crypto markets, pushing Bitcoin up to $54,000."]
    }
    df = pd.DataFrame(data)
    html_output = generate_html_from_dataframe(df)
    with open("twitter_daily_digest.html", "w", encoding="utf-8") as file:
        file.write(html_output)
