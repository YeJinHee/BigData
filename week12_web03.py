import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime

shops = list() #비어있는 리스트 만들기

for i in range(1, 52):
    url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store="
    print(url)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    tbody = soup.find('tbody') #tbody 안에 있는 데이터 가져옴
    trs = tbody.find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        shop_name = tds[1].string #매장명
        shop_addr = tds[3].string #주소
        shop_phone = tds[5].string #번호

        shops.append([shop_phone]+[shop_name]+[shop_addr]+[datetime.datetime.now()])

#print(shops)

hollsy_df = pd.DataFrame(shops, columns=('매장명', '주소', 'Tel', '일시')) #판다스 사용해 리스트 저장
hollsy_df.to_csv('hollsy.csv', mode='w', encoding='cp949') #.csv 파일에 저장
