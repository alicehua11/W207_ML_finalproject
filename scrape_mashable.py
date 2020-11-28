from bs4 import BeautifulSoup
import requests
import pandas as pd

# Initialize dataframe
df = pd.DataFrame(columns=['link', 'title', 'article', 'topic'])

# Here the page starts at 1 and ends at 540 for 2019, ends at 394 for 2020.
# Change the number in "range" for pages, and change the year in "url" variable to
# change the year
lst = []
for page in range(1, 540):
    url = "https://mashable.com/2019/?page=" + str(page)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    # Get all the links to articles at that page
    for art in soup.find_all("div", class_ = "article-container"):
        art = art.h2.a['href']
        lst.append(art)

    # Here parse each article and set link, title, article to a DataFrame
    # You can change the number in "range" to specify the number of articles to be parsed on
    # that page
    for i in range(len(lst)):
        link = lst[i]
        source = requests.get(link).text
        soup = BeautifulSoup(source, "html.parser")
        titles = soup.find("h1", class_ = "title")
        if titles:
            title = titles.get_text().replace('\n', '')
        else:
            pass
        
        sect = soup.find("section", class_ = "article-content")
        if sect: 
            article = sect.get_text().replace('\n', '')
        else: 
            pass

        topics = soup.find('h2')
        if topics:
            topic = topics.get_text()
        else: 
            pass
        

        
        df.loc[i] = [link, title, article, topic]

# Make a csv from the dataframe
df.to_csv("scrape_mashable.csv")
