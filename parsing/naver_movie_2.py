import requests
from bs4 import BeautifulSoup as bs
import re
import movie_class as movie

r = requests.get('http://movie.naver.com/movie/sdb/rank/rmovie.naver')
response = r.text
soup = bs(response, 'html.parser')
 # 네이버 영화순위 top50_제목 리스트
tit3_list = soup.find_all(class_="tit3")
title_list=[]
for i in tit3_list:
    title_list.append(i.text.strip())
# 이미지 가져오기 ver.navermovie:: requset 50times slow -> naver open api! 네이버 무비코드
a_list = soup.select("div.tit3 > a")
img_list=[]
for i in range(len(a_list)):
    movie_link = str(a_list[i])#.split('code=')[1]
    naver_code = re.findall(r'\d+',movie_link)[0]
    img_link = 'http://movie.naver.com/movie/bi/mi/photoViewPopup.naver?movieCode='+naver_code
    img_list.append(img_link)

movie_list=[]
for i in range(len(title_list)):
    movie_list.append(movie.movie(i,title_list[i],img_list[i]))
    print(movie_list[i].rank, movie_list[i].title, movie_list[i].img_url)