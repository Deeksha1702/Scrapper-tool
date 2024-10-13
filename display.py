def display_article(article_data, sentiment):
    print("Title:", article_data["headline"])
    print("Date & Time:", article_data["date_and_time"])  # Display the date and time
    print("Content:\n", article_data["content"])
    print("Sentiment:", sentiment)
    print("\n" + "=" * 50 + "\n")
