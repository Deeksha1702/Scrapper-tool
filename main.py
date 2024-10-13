from fetcher import fetch_article
from parser import parse_article
from display import display_article

urls = [
    "https://timesofindia.indiatimes.com/city/bengaluru/discover-karnatakas-hidden-gems-8-must-visit-places-from-hampi-to-badami/photostory/111403217.cms",
    "https://timesofindia.indiatimes.com/city/bengaluru/renukaswamy-neha-hiremath-anjali-ambigera-5-most-gruesome-murders-in-karnataka-that-shook-entire-nation-in-recent-past/photostory/111110939.cms",
    # Add more URLs here if needed
]
for url in urls:
    content = fetch_article(url)
    article_data = parse_article(content)
    display_article(article_data)
