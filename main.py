import requests

api_key = "3f5ea31f064b425fbee90949cd7a3ef4"

url = "https://newsapi.org/v2/everything?q=tesla&from=2022-12-05&sortBy=publishedAt&apiKey=3f5ea31f064b425fbee90949cd7a3ef4"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
    
