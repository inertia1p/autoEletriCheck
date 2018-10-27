import requests
from lxml import html

def getData(url):
    response = requests.get(url).content
    selector = html.fromstring(response)
    data = selector.xpath("//div[@class='w_n_lis2']/p/text()")[0]
    data = data.encode('utf-8').decode().replace(" 度","")
    return float(data)

