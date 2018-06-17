import requests
import json

response = requests.get("http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1")

data = response.json()

print(data[0]['title'])
print(data[0]['content'])
