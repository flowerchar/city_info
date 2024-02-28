本项目以**地方政府网站**作为第一优先级

以2018年漳州市人民政府网为例：

1. 先找到城市对应的人民政府网url
2. 找到**漳州要闻**栏目
3. 在选项里找到2018年对应的起止条数，此时903页为最开始的时间，762页为截至时间![image-20240227162707839](README.assets/image-20240227162707839.png)
4. F12选择最右边的小箭头，点开任意条目，查看a元素的href属性并点击![image-20240228194218214](README.assets/image-20240228194218214.png)
5. 那么红圈内的前缀跟4中的href就组成了详情页的链接。记住这个baseUrl![image-20240228194433133](README.assets/image-20240228194433133.png)
6. 在详情页F12打开开发者工具，选择此页内容，可以看见所有文本都是包含在id为Content的div中![image-20240228195534976](README.assets/image-20240228195534976.png)

"D:\Program Files\Python37\python.exe" D:\Users\heychar\PycharmProjects\city_info\01-get_city_info.py 
100%|██████████| 142/142 [20:09<00:00,  8.51s/it]
Traceback (most recent call last):
  File "D:\Program Files\Python37\lib\site-packages\urllib3\connection.py", line 207, in _new_conn
    socket_options=self.socket_options,
  File "D:\Program Files\Python37\lib\site-packages\urllib3\util\connection.py", line 60, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
  File "D:\Program Files\Python37\lib\socket.py", line 748, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "D:\Program Files\Python37\lib\site-packages\urllib3\connectionpool.py", line 803, in urlopen
    **response_kw,
  File "D:\Program Files\Python37\lib\site-packages\urllib3\connectionpool.py", line 492, in _make_request
    raise new_e
  File "D:\Program Files\Python37\lib\site-packages\urllib3\connectionpool.py", line 468, in _make_request
    self._validate_conn(conn)
  File "D:\Program Files\Python37\lib\site-packages\urllib3\connectionpool.py", line 1097, in _validate_conn
    conn.connect()
  File "D:\Program Files\Python37\lib\site-packages\urllib3\connection.py", line 611, in connect
    self.sock = sock = self._new_conn()
  File "D:\Program Files\Python37\lib\site-packages\urllib3\connection.py", line 210, in _new_conn
    raise NameResolutionError(self.host, self, e) from e
urllib3.exceptions.NameResolutionError: <urllib3.connection.HTTPSConnection object at 0x000002A3C11264C8>: Failed to resolve 'www.zhangzhou.gov.cnhttp' ([Errno 11001] getaddrinfo failed)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "D:\Program Files\Python37\lib\site-packages\requests\adapters.py", line 497, in send
    chunked=chunked,
  File "D:\Program Files\Python37\lib\site-packages\urllib3\connectionpool.py", line 846, in urlopen
    method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
  File "D:\Program Files\Python37\lib\site-packages\urllib3\util\retry.py", line 515, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='www.zhangzhou.gov.cnhttp', port=443): Max retries exceeded with url: //toupiao.www.gov.cn/100dudian/index.htm (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x000002A3C11264C8>: Failed to resolve 'www.zhangzhou.gov.cnhttp' ([Errno 11001] getaddrinfo failed)"))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\Users\heychar\PycharmProjects\city_info\01-get_city_info.py", line 60, in <module>
    data3 = get_detail_content(data2)
  File "D:\Users\heychar\PycharmProjects\city_info\01-get_city_info.py", line 41, in get_detail_content
    response = requests.get(url=url)
  File "D:\Program Files\Python37\lib\site-packages\requests\api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
  File "D:\Program Files\Python37\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "D:\Program Files\Python37\lib\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "D:\Program Files\Python37\lib\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "D:\Program Files\Python37\lib\site-packages\requests\adapters.py", line 519, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='www.zhangzhou.gov.cnhttp', port=443): Max retries exceeded with url: //toupiao.www.gov.cn/100dudian/index.htm (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x000002A3C11264C8>: Failed to resolve 'www.zhangzhou.gov.cnhttp' ([Errno 11001] getaddrinfo failed)"))

Process finished with exit code 1