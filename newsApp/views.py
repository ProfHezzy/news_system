from django.shortcuts import render
from newsapi import NewsApiClient

def index(request):
    # Initialize NewsApiClient
    newsApi = NewsApiClient(api_key='de3cf4782b81464e8845bde3d8fca06a')

    # Get the selected source from the request (default to 'fox-sports')
    selected_source = request.GET.get('source', 'fox-sports')

    # Fetch headlines for the selected source
    headlines = newsApi.get_top_headlines(sources=selected_source)
    articles = headlines['articles']

    # Prepare data for the template
    desc = []
    news = []
    img = []
    content = []
    urls = []

    for article in articles:
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        content.append(article.get('content', 'No Content Available'))
        urls.append(article.get('url', '#'))

    mylist = zip(desc, news, img, content, urls)

    # List of news sources
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

    # Pass the selected source and news sources to the template
    return render(request, 'main/index.html', {
        "mylist": mylist,
        "news_sources": news_sources,
        "selected_source": selected_source
    })