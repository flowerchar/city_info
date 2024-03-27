import csv
import os
import requests
import random
from lxml import etree
import time
from tqdm import tqdm
from typing import List

# TODO: 城市名
CITYNAME = "牡丹江-东安"
proxy = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
def sort_info_by_time(data: list) -> list:
    """
    按照列表第二项时间进行升序排序
    :param data:
    :return:
    """
    # 第一个list的date在2， 第二个list的date在2
    return sorted(data, key=lambda item: item[2])


def filter_by_time(data: list) -> list:
    """
    过滤掉非2018年的数据
    :param data:
    :return:
    """
    return list(filter(lambda item: item[2][:4] == '2018', data))


def get_common_gov(pageBegin: int, pageEnd: int) -> list:
    """
    根据传入的起止页进行爬取
    :param pageBegin:
    :param pageEnd:
    :return: data是一个词条列表。内层元素分别是标题， URL， 日期
    """
    # 存放数据的列表
    data = []
    # 遍历[pageBegin, pageEnd]闭区间的数据
    for i in tqdm(range(pageBegin, pageEnd + 1)):
        # TODO：这里需要替换成实际城市的url
        # url = f"https://www.zhangzhou.gov.cn/cms/sitemanage/index.shtml?siteId=620416813021630000&page={i}"
        url = f"http://www.donganqu.gov.cn/list.asp?class=278&page={i}"
        # 发起请求
        response = requests.get(url, headers=headers)
        # 处理不同字符集的差异
        response.encoding = response.apparent_encoding
        # 转换成lxml类型的解析树
        html = etree.HTML(response.text)
        # TODO：这里替换成实际的词条文本内容
        # element_a_text = html.xpath('//*[@id="resources"]/li/a/text()')  /html/body/div[4]/div[2]/div[2]/div/div[2]/ul/li[1]/a
        element_a_text = html.xpath('//table[@width="96%"]//td[@height="35"]/a/text()')
        element_a_text = list(filter(lambda x: x != '\xa0', element_a_text))
        # TODO：替换成实际词条的href属性
        # element_a_href = html.xpath('//*[@id="resources"]/li/a/@href')
        element_a_href = html.xpath('//table[@width="96%"]//td[@width="70"]/a/@href')
        # TODO：替换成实际日期的xpath路径
        # element_span = html.xpath('//*[@id="resources"]/li/span/text()') //*[@id="main"]/div[2]/div[2]/div[3]/table[1]/tbody/tr[9]/td[3]
        element_span = html.xpath('//table[@width="96%"]//td[@width="80"]/a/text()')
        # element_span = list(map(lambda x: x[1:-1:], element_span))
        # 同时遍历这三个列表，组成一个包含全部的大列表
        for a_text, a_href, span in zip(element_a_text, element_a_href, element_span):
            # 追加元素进大列表
            data.append([a_text, a_href, span])
            # 生成1到10之间的随机浮点数
            random_number = random.random() * 10 + 1
            # 以防反爬，休眠1秒
            time.sleep(random_number)
    # 返回大列表数据
    return data


def get_detail_content(data: list) -> list:
    """
    根据get_common_gov()中的url爬取详情页具体信息
    :param data: get_common_gov()返回的数据类型
    :return: 返回格式为：['id', '标题', '成文或生成日期', '发布或生效日期', '来源', 'URL源地址', '内容']的数据
    """
    # TO：此处改写成你所爬取的城市名
    # cityName = "漳州"
    # cityName = "牡丹江-林口"
    # 存放进CSV的列表数据
    fullData: list = []
    # TODO：参见README中获得baseUrl的方法
    # baseUrl = 'https://www.zhangzhou.gov.cn'
    baseUrl = 'http://www.donganqu.gov.cn/'
    # 遍历原列表中的数据
    for index, value in tqdm(enumerate(data)):
        # print(value)
        # exit(0)
        url = value[1]
        # 拼接成完整的详情页url
        url = baseUrl + url
        try:
            # 对详情页发起请求
            response = requests.get(url=url, headers=headers)
            # 处理字符集编码
            response.encoding = response.apparent_encoding
            # 转换成lxml解析树
            html = etree.HTML(response.text)
            # TODO：这里替换成实际城市中的xpath
            # element_div_content = html.xpath('//*[@id="Content"]//text()')
            element_div_content = html.xpath('//span[@class="aa"]//text()')
            # 清洗数据，把空白符剔除掉
            content = ''.join(element_div_content).strip()
            # 将所有元素组成一个csv列表
            fullData.append([index + 1, value[0], value[2], value[2], f"{CITYNAME}日报", url, content])
            # 生成1到10之间的随机浮点数
            random_number = random.random() * 10 + 1
            # 程序休眠，防止封IP
            time.sleep(random_number)
        except:
            print(f"{url}有误")
            continue
    # 返回csv列表
    return fullData


def keep2csv(fileName: str, data: list) -> None:
    # 完整的文件名，加上时间戳是以防把之前的冲突而报错
    fileName = f"{fileName}_日报_2018-01-01_2018-12-31_{time.time()}.csv"
    # CSV表头信息
    tableHeader: List[str] = ['id', '标题', '成文或生成日期', '发布或生效日期', '来源', 'URL源地址', '内容']
    # 检查文件是否已存在
    if not os.path.exists(fileName):
        # 文件不存在，创建并写入数据
        with open(fileName, 'w', newline='', encoding='utf-8') as fp:
            writer = csv.writer(fp)
            # 写入表头
            writer.writerow(tableHeader)
            # 写入数据行
            writer.writerows(data)
        print(f"CSV文件已创建：{fileName}")
    else:
        # 文件已存在，跳过写入操作
        print(f"CSV文件已存在：{fileName}，请先确认删除")


# 得到总览页的数据信息 TODO：这里改写成实际的城市起止页
# data = get_common_gov(762, 903)
data = get_common_gov(61, 71)#71
# data1 = sort_info_by_time(data)
# 过滤掉非2018年的数据
data2 = filter_by_time(data)
# 获取详情页的文本数据
data3 = get_detail_content(data2)
# 按照日期时间升序
data4 = sort_info_by_time(data3)
# 保存文件到csv TODO：这里替换成实际的省份-城市名
# keep2csv("福建_漳州", data4)
keep2csv(f"黑龙江-{CITYNAME}", data4)
