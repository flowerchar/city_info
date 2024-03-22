import requests
import time
from tqdm import tqdm
import os
import csv
import random
# TODO：这里填上具体城市的防盗链
headers = {'Referer': 'https://www.hegang.gov.cn/hegang/hgxw/list.shtml',
           'User-Agent': 'Mozilla/5.0 ('}
def filter_by_time(data: list) -> list:
    """
    过滤掉非2018年的数据
    :param data:
    :return:
    """
    return list(filter(lambda item: item[2][:4] == '2018', data))
def get_implicit_gov(pageBegin: int, pageEnd: int) -> list:
    """
    根据传入的起止页进行爬取
    :param pageBegin:
    :param pageEnd:
    :return: data是一个词条列表。内层元素分别是标题， URL， 日期
    """
    # 存放数据的列表
    data = []
    index = 1
    # TODO：填写城市名称
    city_name = "鹤岗"
    # 遍历[pageBegin, pageEnd]闭区间的数据
    for i in tqdm(range(pageBegin, pageEnd + 1)):
        # TODO：这里需要替换成实际城市的url
        url = f"https://www.hegang.gov.cn/common/search/5b047b82968247ad8715d5351678d992?_isAgg=false&_isJson=true&_pageSize=15&_template=index&_rangeTimeGte=&_channelName=&page={i}"
        # 发起请求
        response = requests.get(url, headers=headers)
        # 处理不同字符集的差异
        response.encoding = response.apparent_encoding
        # 将响应变成json数据方便处理
        json_data = response.json()
        # print(response.text)
        # exit(0)
        # 遍历json
        for j in json_data['data']['results']:
            try:
                # print(j)
                # TODO：从字典里去除标题
                title = j['title']
                # TODO：从字典里取出日期
                date = j['publishedTimeStr'].split()[0]
                # TODO：取出超链接
                href = j['url']
                # TODO：取出文本内容
                content = j['content']
                # 添加到大列表中
                data.append([index, title, date, date, f"{city_name}日报", href, content])
                # 生成1到10之间的随机浮点数
                random_number = random.random() * 10 + 1
                # 以防反爬，休眠1秒
                time.sleep(1)
                # ID自增
                index += 1
            except:
                continue
    # 返回大列表数据
    return data
def keep2csv(fileName: str, data: list) -> None:
    # 完整的文件名，加上时间戳是以防把之前的冲突而报错
    fileName = f"{fileName}_日报_2018-01-01_2018-12-31_{time.time()}.csv"
    # CSV表头信息
    tableHeader = ['id', '标题', '成文或生成日期', '发布或生效日期', '来源', 'URL源地址', '内容']
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
# TODO：填写具体的起止页
data1 = get_implicit_gov(498,569)
# 过滤非2018的数据
data2 = filter_by_time(data1)
# TODO：写全文件名，保存到csv
keep2csv("黑龙江-鹤岗", data2)