from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template
app = Flask(__name__)

rssFeed = [
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "http://rss.cnn.com/rss/edition.rss"
]

def parse_and_fetch(url):
    url = requests.get(url)
    soup = BeautifulSoup(url.content, 'xml')
    return soup

def fetch_news():
    articles = []
    for url in rssFeed:
        soup = parse_and_fetch(url)
        items = soup.findAll("item")
        for item in items:
            article = {
                "title": item.title.text if item.title else 'N/A',
                "link": item.link.text if item.link else 'N/A',
                "description": item.description.text if item.description else 'N/A',
                "published": item.pubDate.text if item.pubDate else 'N/A'
            }
            articles.append(article)
    return articles

@app.route('/')
def home():
    articles = fetch_news()
    return render_template("home.html", articles=articles)

if __name__ == '__main__':
    app.run(debug=True)