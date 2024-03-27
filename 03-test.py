import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}
# #

url = "http://szb.shaoyangnews.net/syrb/html/2018-01/31/node_3.htm" # ?categoryNum=001001&pageIndex=100
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
html = etree.HTML(response.text)
# print(response.text)
element_a_text = html.xpath('//table[@cellpadding="1"]//tr/td[2]/a/div/text()')
# print(element_a_text)
# element_a_text = list(filter(lambda x: x != '\xa0', element_a_text))
# element_a_date = html.xpath('//table[@width="96%"]//td[@width="80"]/a/text()')
# element_a_href = html.xpath('//table[@width="96%"]//td[@width="70"]/a/@href')
# element_a_text = html.xpath('//li//a/text()')
# content = ''.join(element_a_text).strip()
# print(content)
print(element_a_text)
# from tqdm import tqdm
# from time import sleep
# for i in tqdm(range(100)):
#     sleep(0.1)
#     pass
# print("[2023-05-23] 第六届进博会英国推介会在伦敦举行")
# print("[2023-05-23] 中刚（金）元首宣布将两国合作共赢的战略伙伴关系提升为全面战略合作伙伴关系")
# print("[2023-05-23] 2023数博会聚焦数字经济未来高质量发展")
# print("[2023-05-23] 提升中小企业科技创新力 十部门发文开展专项行动")
# print("[2023-05-23] 精准发力为中小企业赋智")
# print("[2023-05-23] 九部门：力争到2025年新增相关领域中小企业公共服务平台1000家以上")
# print("[2023-05-23] 推动科学技术更好造福各国人民——习近平主席致2023中关村论坛的贺信激励各界携手促进科技创新")
# print("[2023-05-23] 小微企业金融服务再加力")

# li = ['[2019-01-01]', '[2019-01-01]', '[2019-01-01]', '[2019-01-01]', '[2019-01-01]', '[2019-01-01]', '[2019-01-01]', '[2019-01-01]', '[2018-12-30]', '[2018-12-30]', '[2018-12-30]', '[2018-12-30]', '[2018-12-29]', '[2018-12-29]', '[2018-12-29]', '[2018-12-29]', '[2018-12-29]', '[2018-12-28]', '[2018-12-28]', '[2018-12-27]']
# li2 = list(map(lambda x:x[1:-1:], li))
# print(li2)

# resp = requests.get('http://www.donganqu.gov.cn/list.asp?class=278&page=61')
