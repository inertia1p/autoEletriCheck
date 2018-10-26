import requests
from lxml import html
url='https://wxschool.lsmart.cn/electric/electric_index.shtml?openId=oujX2w6dzwgLOXs012-qhiM0IlPQ&wxArea=10354'

def getData():
    response = requests.get(url).content
    selector = html.fromstring(response)
    data = selector.xpath("//div[@class='w_n_lis2']/p/text()")[0]
    data = data.encode('utf-8').decode().replace(" 度","")
    return float(data)

