from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


hn = 'https://thehackernews.com/'
silicon = 'https://www.siliconvalley.com/news/'
rp = 'https://hackspace.raspberrypi.org/articles'


hn_list = []
hackspace_news = []
silicon_news = []



def get_hn():
    r = requests.get(hn).text
    soup = BeautifulSoup(r, 'lxml')
    posts = soup.find_all('div', class_='body-post clear')
    for post in posts:
        title = post.find('h2', class_='home-title').text
        url = post.find('a').get('href')
        data = {'title':title,
                'url':url}
        hn_list.append(data)


def get_silicon_news():
    r = requests.get(silicon).text
    soup = BeautifulSoup(r, "lxml")
    posts = soup.find_all("article")
    for post in posts:
        title = post.find("a", class_="article-title").get('title')
        url = post.find("a", class_="article-title").get("href")

        data = {'title': title,
                'url': url,
                }

        silicon_news.append(data)

def get_hspace_news():
    r = requests.get(rp).text
    soup = BeautifulSoup(r, "lxml")
    posts = soup.find_all("article")
    for post in posts:
        title = post.find("p", class_="o-type-sub-heading u-weight-bold rspec-article-card--heading").text
        url = post.find("a").get("href")

        data = {'title': title,
                'url': url,
                }

        hackspace_news.append(data)





get_hn()
get_silicon_news()
get_hspace_news()



def home(requests):
    context = {
        'hn_list':hn_list,
        'hackspace_news':hackspace_news,
        'silicon_news':silicon_news,
    }
    return render(requests, 'news_app/home.html', context)