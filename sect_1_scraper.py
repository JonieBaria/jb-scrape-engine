import requests
from lxml import html

# Sample URL of a "New Releases" section (you can change this to your target)
url = 'https://www.example.com/new-releases'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
tree = html.fromstring(response.content)

# Sample XPath for titles and links — update based on the site's HTML
titles = tree.xpath('//div[@class="product-title"]/a/text()')
links = tree.xpath('//div[@class="product-title"]/a/@href')

# Combine and print results
for title, link in zip(titles, links):
    print(f"Title: {title.strip()}")
    print(f"Link: https://www.example.com{link}")
    print("---")
