# import requests
# from lxml import etree
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
# }
# #
# url = "https://www.gov.cn/yaowen/liebiao/home_301.htm" # ?categoryNum=001001&pageIndex=100
# response = requests.get(url, headers=headers)
# response.encoding = response.apparent_encoding
# html = etree.HTML(response.text)
# # element_a_text = html.xpath('//ul[@barrier-free-idx="127"]//text()')
# element_a_text = html.xpath('//li//a/text()')
# content = ''.join(element_a_text).strip()
# print(content)
#
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

li = ['[2019-01-01]', '[2019-01-01]', '[2019-01-01]', '[2019-01-01]', '[2019-01-01]', '[2019-01-01]', '[2019-01-01]', '[2019-01-01]', '[2018-12-30]', '[2018-12-30]', '[2018-12-30]', '[2018-12-30]', '[2018-12-29]', '[2018-12-29]', '[2018-12-29]', '[2018-12-29]', '[2018-12-29]', '[2018-12-28]', '[2018-12-28]', '[2018-12-27]']
li2 = list(map(lambda x:x[1:-1:], li))
print(li2)