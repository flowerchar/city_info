import requests
from lxml import etree
import time
from tqdm import tqdm
header1 = {'User-Agent': 'Mozilla/5.0 (Windows NT'}
header2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
 # 268 375
# 单个跑
url = "https://www.xlgl.gov.cn/eportal/ui?pageId=9172fd9416a74102a1c1c5d1b1cb7a87&currentPage=280&moduleId=11a6765c3ab0406e874bd3f994dc88ce&staticRequest=yes"
response = requests.get(url, headers=header1)
response.encoding = response.apparent_encoding
html = etree.HTML(response.text)  # //*[@id="11a6765c3ab0406e874bd3f994dc88ce"]/div[2]/ul/li[1]/a  /html/body/div[6]/div[2]/div[2]/div[2]/div/div[2]/ul/li[1]/a
element_a_text = html.xpath('//ul//a/text()')[8:-11:]
element_a_href = html.xpath('//ul//a/@href')[27:-11:]
element_span = html.xpath('//ul//span/text()')[11::]
# print(response.text)
print(len(element_a_href))
data = []
for a_text, a_href, span in zip(element_a_text, element_a_href, element_span):
    data.append([a_text, a_href, span])
print(data)

# 循环
data = []
    # 遍历[pageBegin, pageEnd]闭区间的数据
for i in tqdm(range(278, 280)):
    # TODO：这里需要替换成实际城市的url
    url = f"https://www.xlgl.gov.cn/eportal/ui?pageId=9172fd9416a74102a1c1c5d1b1cb7a87&currentPage={i}&moduleId=11a6765c3ab0406e874bd3f994dc88ce&staticRequest=yes"
    # 发起请求
    response = requests.get(url, headers=header2)
    # 处理不同字符集的差异
    response.encoding = response.apparent_encoding
    # 转换成lxml类型的解析树
    html = etree.HTML(response.text)
    # TODO：这里替换成实际的词条文本内容__已完成
    # element_a_text = html.xpath('//*[@id="11a6765c3ab0406e874bd3f994dc88ce"]/div[2]/ul/li[2]/a/text()')
    element_a_text = html.xpath('//ul//a/text()')[8:-11:]
    # TODO：替换成实际词条的href属性__已完成
    # element_a_href = html.xpath('//*[@id="11a6765c3ab0406e874bd3f994dc88ce"]/div[2]/ul/li[2]/a/@href')
    element_a_href = html.xpath('//ul//a/@href')[27:-11:]
    # TODO：替换成实际日期的xpath路径__已完成
    # element_span = html.xpath('//*[@id="11a6765c3ab0406e874bd3f994dc88ce"]/div[2]/ul/li[2]/span/text()')
    element_span = html.xpath('//ul//span/text()')[11::]
    for a_text, a_href, span in zip(element_a_text, element_a_href, element_span):
        data.append([a_text, a_href, span])
        # 以防反爬，休眠1秒
        time.sleep(1)
print(data)
