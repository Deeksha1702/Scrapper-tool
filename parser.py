from bs4 import BeautifulSoup

def parse_article(content):
    soup = BeautifulSoup(content, 'html.parser')
    headline = soup.find('h1').text.strip() if soup.find('h1') else 'No headline found.'

    # (publication date)
    byline_div = soup.find('div', class_='byline')
    if byline_div:
        author = byline_div.find('a').text.strip() if byline_div.find('a') else 'No author found.'
        date = byline_div.find('span').text.strip() if byline_div.find('span') else 'No date found.'
        byline = f"{author} / {date}"
    else:
        byline = 'No byline found.'

    #main content from the specific class
    content_sections = []
    for section in soup.find_all('h2'):
        title = section.text.strip()
        description = section.find_next('div', class_='rWkSP')
        description_text = description.text.strip() if description else 'No description found.'

        # Filter out unwanted sections
        if title not in ["Visual Stories", "Photostories", "TOI", "Featured In City"]:
            content_sections.append(f"{title}: {description_text}")

    content = "\n".join(content_sections) if content_sections else 'No content found.'

    return {
        "headline": headline,
        "date_and_time": byline,
        "content": content
    }

