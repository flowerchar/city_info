import csv

import requests
from lxml import etree
import time
from tqdm import tqdm


def sort_info_by_time(data: list)->list:
    return sorted(data, key=lambda item: item[2]) #第一个list的date在2， 第二个list的date在2

def filter_by_time(data: list)->list:
    return list(filter(lambda item:item[2][:4] == '2018', data))

def get_common_gov(pageBegin: int, pageEnd: int)->list:
    """

    :param govUrl: government website address
    :return: data: [title, time, href]
    """
    data = []
    for i in tqdm(range(pageBegin, pageEnd+1)):
        url = f"https://www.zhangzhou.gov.cn/cms/sitemanage/index.shtml?siteId=620416813021630000&page={i}"
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        html = etree.HTML(response.text)
        element_a_text = html.xpath('//*[@id="resources"]/li/a/text()')
        element_a_href = html.xpath('//*[@id="resources"]/li/a/@href')
        element_span = html.xpath('//*[@id="resources"]/li/span/text()')
        for a_text, a_href, span in zip(element_a_text, element_a_href, element_span):
            data.append([a_text, a_href, span])
            time.sleep(0.5)
    return data

def get_detail_content(data: list) -> list:
    cityName = "漳州"
    fullData: list = []
    baseUrl = 'https://www.zhangzhou.gov.cn'
    for index, value in enumerate(data):
        url = baseUrl + value[1]
        response = requests.get(url=url)
        response.encoding = response.apparent_encoding
        html = etree.HTML(response.text)
        element_div_content = html.xpath('//*[@id="Content"]/p/text()')
        content = ''.join(element_div_content).strip()
        fullData.append([index + 1, value[0], value[2], value[2],f"{cityName}日报", url, content])
    return fullData


def keep2csv(fileName: str, data: list) -> None:
    tableHeader = ['id', '标题', '成文或生成日期', '发布或生效日期', '来源', 'URL源地址', '内容']
    with open(f"{fileName}.csv", 'w', newline='', encoding='utf-8') as fp:
        writer = csv.writer(fp)
        writer.writerow(tableHeader)
        writer.writerows(data)

data = get_common_gov(762, 903)
data1 = sort_info_by_time(data)
data2 = filter_by_time(data)
data3 = get_detail_content(data2)
data4 = filter_by_time(data3)
keep2csv("福建-漳州", data3)

# get_detail_content("1")

