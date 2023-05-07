import os
import re
import json
from datetime import date, datetime
from jinja2 import Environment, FileSystemLoader

def format_date(date_str: str) -> str:
    date_object = datetime.strptime(date_str, "%Y-%m-%d")
    formatted_date = date_object.strftime("%A, %B %d, %Y")
    return formatted_date

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index.jinja.html')
directory="/home/mtrencseni/gpt-news-poet/articles/"
pattern = re.compile(r'articles-\d{4}-\d{2}-\d{2}\.json')    
files = [f for f in os.listdir(directory) if pattern.match(f)]
for file in files:
    dt = file[len("articles-"):len("articles-YYYY-MM-DD")]
    filepath = os.path.join(directory, file)
    with open(filepath, 'r') as f:
        html = template.render(
            articles=json.load(f),
            dt=format_date(dt),
            )
        with open("www/archive/" + dt + ".html", "w") as f:
            f.write(html)
