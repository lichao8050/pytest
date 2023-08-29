# *-* coding : utf-8 *-*
# @time : 2023/8/29 12:21
# @author : Mr_Li
# @file : test_jsonpath_01.py

# jsonpath
# 可以通过jsonpath获取json响应中某个key对应的value值：
# 两种方式1，$.key 如：{'msg': '登录成功', 'code': 0, 'data': {'body_html': ''}} >>  $.msg 将获取到“登录成功”这个值
# 2.$..key  递归获取方式  有多个则根据下标取值[]
import jsonpath
import requests


def test_xiaomiao_login():
    url = 'http://miao.matrixdesign.cn/api/auth/login'
    json = {"loginId": "guoshuang",
            "password": "e10adc3949ba59abbe56e057f20f883e"}
    res = requests.post(url=url, json=json)
    print(res.status_code)
    print(res.json())
    json_token_list1 = jsonpath.jsonpath(res.json(), '$..access_token')  # 递归获取方式
    json_token_list2 = jsonpath.jsonpath(res.json(), '$.data.access_token')  # 路径获取
    print(json_token_list1[0])
    print(json_token_list2[0])
