# import requests
# from lxml import etree
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
#     # 'Referer': 'https://fushun.gov.cn'
# }
#
# url = "http://www.jimei.gov.cn/ywkd/jmxw/index_41.htm" # ?categoryNum=001001&pageIndex=100
# response = requests.get(url, headers=headers)
# response.encoding = response.apparent_encoding
# html = etree.HTML(response.text)
# # element_a_text = html.xpath('//ul[@barrier-free-idx="127"]//text()')
# element_a_text = html.xpath('//div[@class="gl_list"]//a/text()')
# content = ''.join(element_a_text).strip()
# print(content)

a = './201801/t20180109_348399.htm'
print(a[2:])