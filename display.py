def display_article(article_data):
    print("Title:", article_data["headline"])
    print("Date & Time:", article_data["date_and_time"])
    print("Content:\n", article_data["content"])
    print("\n" + "="*50 + "\n")
