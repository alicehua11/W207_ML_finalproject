import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import codecs
import regex as re
import requests

df = pd.read_csv('Data/OnlineNewsPopularity.csv')
data.columns = [x[1:] if x[0] == ' ' else x for x in data.columns]
urls = list(df['url'])


for page in urls:
    r = request.get(page)
    soup = BeautifulSoup(r.content, 'html.parser')

# get total share
shareNode = bs.find('div', {'class': 'total-shares'})
if(shareNode):
  article.shares = shareNode.get_text().replace('\n', '').replace('Shares', '')
else:
  shareNode = bs.find(lambda tag: tag.has_attr('data-shares'))
article.shares = shareNode.get('data-shares')


class Article(object):
    def __init__(self):
        self.id = None
        self.link = None
        self.post_date = None
        self.title = None
        self.author = None
        self.shares = 0
        self.channel = None
        self.type = None
        self.content = None
        self.timedelta = None
        self.n_tokens_title = 0
        self.n_tokens_content = 0
        self.num_hrefs = 0
        self.num_self_hrefs = 0
        self.num_imgs = 0
        self.num_videos = 0
        self.num_keywords = 0
        self.topics = None
        self.content_sentiment_polarity = None
        self.content_subjectivity = None
        self.title_sentiment_polarity = None
        self.title_subjectivity = None

