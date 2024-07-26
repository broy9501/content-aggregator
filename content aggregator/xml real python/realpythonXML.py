from bs4 import BeautifulSoup
import requests
import sys

# Ensure the script uses UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

req = requests.get("https://realpython.com/atom.xml")
soup = BeautifulSoup(req.content, 'xml')
entries = soup.find_all('entry')

#list = {}

for entry in entries:
    title = entry.title.text
    link = entry.link['href']
    summary = entry.summary.text

    # list = {
    #     "Title": title,
    #     "Link": link,
    #     "Summary": summary
    # }

    # print(list)

    print(f"Title: {title}\n\nLink: {link}\n\nSummary: {summary}\n\n------------------------------------------")