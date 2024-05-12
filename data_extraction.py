# data_extraction.py
import requests
from bs4 import BeautifulSoup

def extract_links(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a')]
    return links

def extract_article_data(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    titles = [title.text for title in soup.find_all('h2')]
    descriptions = [desc.text for desc in soup.find_all('p')]
    return titles, descriptions
