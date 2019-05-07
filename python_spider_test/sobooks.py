import requests
from bs4 import BeautifulSoup

def getHtml(url):
	html = requests.get(url).content
	soup = BeautifulSoup(html,'lxml')
	return soup

def getcontent(content):
	