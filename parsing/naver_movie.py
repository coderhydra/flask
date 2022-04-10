import requests
from bs4 import BeautifulSoup
import movie_class
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84"
r = requests.get(url)
response = r.text
soup = BeautifulSoup(response, 'html.parser')
parsing_titles = soup.find_all("strong",{"class","name"})
parsing_img_urls = soup.select('div.thumb > img ')
naver_movies=[]
for i in range(10):
    index = i
    title = parsing_titles[i].text
    img_url = str(parsing_img_urls[i]).split(" ")[-2][5:-1]
    naver_movies.append(movie_class.movie(index,title,img_url))

for movie in naver_movies:
    print(movie.rank,movie.title,movie.img_url)