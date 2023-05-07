import os
import re
import json
from datetime import date, datetime
from jinja2 import Environment, FileSystemLoader

def get_latest_articles(directory="/home/mtrencseni/gpt-news-poet/articles/"):
    pattern = re.compile(r'articles-\d{4}-\d{2}-\d{2}\.json')    
    files = [f for f in os.listdir(directory) if pattern.match(f)]
    files.sort(reverse=True)
    latest_file_path = os.path.join(directory, files[0])
    with open(latest_file_path, 'r') as f:
        return json.load(f)

env = Environment(loader=FileSystemLoader('templates'))
html = env.get_template('index.jinja.html').render(
    articles=get_latest_articles(),
    dt=date.today().strftime("%A, %B %d, %Y")
    )
directory = "www/archive/"
filename = datetime.now().strftime('%Y-%m-%d') + ".html"
with open(directory + filename, "w") as f:
    f.write(html)
directory = "www/"
filename = "index.html"
with open(directory + filename, "w") as f:
    f.write(html)
