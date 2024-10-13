from fetcher import fetch_article
from parser import parse_article
from display import display_article
from sentiment_analyzer import analyze_sentiment  # Import the sentiment analyzer

urls = [
    "https://timesofindia.indiatimes.com/city/bengaluru/discover-karnatakas-hidden-gems-8-must-visit-places-from-hampi-to-badami/photostory/111403217.cms",
    "https://timesofindia.indiatimes.com/city/bengaluru/renukaswamy-neha-hiremath-anjali-ambigera-5-most-gruesome-murders-in-karnataka-that-shook-entire-nation-in-recent-past/photostory/111110939.cms",
]

for url in urls:
    content = fetch_article(url)
    article_data = parse_article(content)
    article_sentiment = analyze_sentiment(article_data['content'])

    display_article(article_data, article_sentiment)
