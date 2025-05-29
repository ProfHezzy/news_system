from django.shortcuts import render
import requests

def index(request):
    # Your NewsData.io API key
    api_key = 'pub_b9245d5f1b614c0dbbe7983b3d4aa8b0'

    # Get the selected category from the request (default to 'sports')
    selected_category = request.GET.get('category', 'sports')

    # Fetch headlines for the selected category using NewsData.io
    url = f'https://newsdata.io/api/1/news?apikey={api_key}&country=us&category={selected_category}&language=en'

    response = requests.get(url)
    data = response.json()

    # Check for API success
    articles = data.get('results', [])

    # Prepare data for the template
    desc = []
    news = []
    img = []
    content = []
    urls = []

    for article in articles:
        desc.append(article.get('description', 'No Description'))
        news.append(article.get('title', 'No Title'))
        img.append(article.get('image_url', 'https://via.placeholder.com/150'))
        content.append(article.get('content', 'No Content Available'))
        urls.append(article.get('link', '#'))

    mylist = zip(desc, news, img, content, urls)

    # List of categories instead of sources
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
