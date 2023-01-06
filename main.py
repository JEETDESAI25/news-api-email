import requests
from send_email import send_email

topic = "tesla"

api_key = "3f5ea31f064b425fbee90949cd7a3ef4"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2022-12-05&sortBy=publishedAt&apiKey=3f5ea31f064b425fbee90949cd7a3ef4&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
body = ""

for article in content["articles"][:20]:

    body = (
        "Subject: Today's news"
        + "\n"
        + body
        + article["title"]
        + "\n"
        + article["description"]
        + "\n"
        + article["url"]
        + 2 * "\n"
    )


body = body.encode("utf-8")
send_email(message=body)
