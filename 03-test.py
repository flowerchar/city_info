import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://fushun.gov.cn'
}
params = {
"categoryNum":"001001",
    "pageIndex":"100"
}
url = "https://fushun.gov.cn/ywdt/001001/moreinfo.html" # ?categoryNum=001001&pageIndex=100
response = requests.get(url, params=params, headers=headers)
response.encoding = response.apparent_encoding
html = etree.HTML(response.text)
# element_a_text = html.xpath('//*[@id="list"]/li/a/text()')
element_a_text = html.xpath('//li[@class="sec-right-item"]/a/text()')
print(element_a_text)