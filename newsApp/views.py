from django.shortcuts import render
import requests
from django.conf import settings
import json

def index(request):
    # Your NewsData.io API key from settings
    api_key = settings.NEWS_API_KEY

    # Get the selected category from the request (default to 'sports')
    selected_category = request.GET.get('category', 'sports')

    # API parameters (you could make country and language dynamic later)
    country = 'us'
    language = 'en'

    # Fetch headlines for the selected category using NewsData.io
    url = f'https://newsdata.io/api/1/news?apikey={api_key}&country={country}&category={selected_category}&language={language}'

    articles = []
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        # Check for API success
        articles = data.get('results', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        # Handle the error appropriately, maybe set articles to an empty list
    except json.JSONDecodeError:
        print("Error decoding JSON response")
        # Handle the error appropriately

    # Prepare data for the template
    desc = [article.get('description', 'No Description') for article in articles]
    news = [article.get('title', 'No Title') for article in articles]
    img = [article.get('image_url') for article in articles]
    content = [article.get('content', 'No Content Available') for article in articles]
    urls = [article.get('link', '#') for article in articles]

    mylist = zip(desc, news, img, content, urls)

    # List of categories
    news_categories = {
        "Top Headlines": "top",
        "World": "world",
        "Politics": "politics",
        "Business": "business",
        "Sports": "sports",
        "Technology": "technology",
        "Science": "science",
        "Health": "health",
        "Entertainment": "entertainment",
        "Environment": "environment",
        "Education": "education",
        "Food": "food",
        "Tourism": "tourism",
        "Crime": "crime"
    }

    # Pass the selected category and news categories to the template
    return render(request, 'main/index.html', {
        "mylist": mylist,
        "news_categories": news_categories,
        "selected_category": selected_category
    })