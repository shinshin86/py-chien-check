import requests
from bs4 import BeautifulSoup

# エリア番号は下記の通り
# 2 : 北海道
# 3 : 東北
# 4 : 関東
# 5 : 中部
# 6 : 近畿
# 8 : 中国
# 9 : 四国
# 7 : 九州
area = 4

url = "https://transit.yahoo.co.jp/traininfo/area/" + str(area) + "/"
r = requests.get(url)
if(r.status_code != 200):
    print("not status code 200")
    exit()

soup = BeautifulSoup(r.text, 'lxml')
items = soup.find_all("tr")
for item in items:
    if(item.span is not None):
        print("--------------")
        print(item.text)

