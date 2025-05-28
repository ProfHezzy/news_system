from django.shortcuts import render
from newsapi import NewsApiClient
import requests

def index(request):
    newsApi = NewsApiClient(api_key='de3cf4782b81464e8845bde3d8fca06a')
    selected_source = request.GET.get('source', 'fox-sports')

    try:
        headlines = newsApi.get_top_headlines(sources=selected_source)
        articles = headlines.get('articles', [])
    except requests.exceptions.RequestException as e:
        # Network or HTTP error
        print(f"Request error: {e}")
        articles = []
    except Exception as e:
        # Other errors, including JSON decode errors
        print(f"Error fetching news: {e}")
        articles = []

    desc, news, img, content, urls = [], [], [], [], []

    for article in articles:
        desc.append(article.get('description'))
        news.append(article.get('title'))
        img.append(article.get('urlToImage'))
        content.append(article.get('content', 'No Content Available'))
        urls.append(article.get('url', '#'))

    mylist = zip(desc, news, img, content, urls)

    news_sources = {
        "Fortune": "fortune",
        "ABC News": "abc-news",
        "Al Jazeera English": "al-jazeera-english",
        "BBC News": "bbc-news",
        "BBC Sport": "bbc-sport",
        "Business Insider": "business-insider",
        "Crypto Coins News": "crypto-coins-news",
        "Entertainment Weekly": "entertainment-weekly",
        "Financial Post": "financial-post",
        "Fox News": "fox-news",
        "Fox Sports": "fox-sports",
        "Google News": "google-news",
        "Medical News Today": "medical-news-today"
    }

    return render(request, 'main/index.html', {
        "mylist": mylist,
        "news_sources": news_sources,
        "selected_source": selected_source
    })
