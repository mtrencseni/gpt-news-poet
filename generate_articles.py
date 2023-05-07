import json
import openai
import urllib.request
import urllib.parse
from datetime import datetime
import secrets

def gnews_top_news(category='general', q=None):
    apikey = secrets.gnews_apikey
    url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang=en&country=us&max=10&apikey={apikey}"
    if q is not None:
        url += "&" + urllib.parse.urlencode({"q": q})
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))
        return data["articles"]

def query_gpt_35(prompt, model="text-davinci-003", max_tokens=4000):
    openai.api_key = secrets.openai_apikey
    response = openai.Completion.create(
        engine=model,
        prompt=prompt, 
        max_tokens=max_tokens-len(prompt),
        n=1,
        stop=None,
        temperature=0.8,
    )
    generated_text = response.choices[0].text.strip()
    return generated_text
    
articles = gnews_top_news()
for i, a in enumerate(articles):
    articles_text = f"{a['title']}. {a['description']}"
    poet_prompt = f"Write a witty 4 line poem about the following news: {articles_text}"
    for _ in range(5):
        response = query_gpt_35(poet_prompt)
        if len(response.split("\n")) == 4:
            break
    a['poem'] = response.strip()

directory = "articles/"
filename = f"articles-{datetime.now().strftime('%Y-%m-%d')}.json"
with open(directory + filename, "w") as f:
    json.dump(articles, f)
