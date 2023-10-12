import urllib.request
import urllib.parse

api : 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

station_id = input('지역코드 : ')
values = {'stnId':station_id}
parameters = urllib.parse.urlencode(values)
url = api + '?' + parameters

urls = urllib.request.urlopen(url).read()
texts = urls.decode('utf-8')
print(texts)

# 다운로드를 하고 수집되는 데이터에 따라 출력?