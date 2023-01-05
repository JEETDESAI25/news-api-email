import requests
from send_email import send_email

api_key = "3f5ea31f064b425fbee90949cd7a3ef4"

url = "https://newsapi.org/v2/everything?q=tesla&from=2022-12-05&sortBy=publishedAt&apiKey=3f5ea31f064b425fbee90949cd7a3ef4"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
body = ""

for article in content["articles"]:

    body = body + article["title"] + "\n" + article["description"] + 2 * "\n"


body = body.encode("utf-8")
send_email(message=body)
