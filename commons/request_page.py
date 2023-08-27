# *-* coding : utf-8 *-*
# @time : 2023/5/18 20:17
# @author : Mr_Li
# @file : request_page.py
import requests
import time
import json
import jsonpath


class HttpRequest:
    session = requests.session()

    def send_all_request(self, method, url, **kwargs):

        method = str(method).lower()
        res = ""
        if method == 'get':
            res = HttpRequest.session.request(method, url, **kwargs)
        elif method == 'post':
            res = HttpRequest.session.request(method, url, **kwargs)
        return res

    # 基于jsonpath获取数据的关键字，用于提取所需要的内容
    def get_json_txt(self, data, key):
        """jsonpath获取数据的表达式：成功则返回list，失败则返回false
        loads是将JSON格式的内容转换为字典格式
        jsonpath接受的是dict字典类型的数据"""
        dict_data = json.loads(data)
        value = jsonpath.jsonpath(dict_data, '$..{0}'.format(key))
        return value[0]

    def get_random(self):
        return str(int(time.time()))
