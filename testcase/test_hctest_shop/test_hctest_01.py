# *-* coding : utf-8 *-*
# @time : 2023/8/28 12:18
# @author : Mr_Li
# @file : test_hctest_01.py

# 可以通过jsonpath获取json响应中某个key对应的value值：
# 两种方式1，$.key 如：{'msg': '登录成功', 'code': 0, 'data': {'body_html': ''}} >>  $.msg 将获取到“登录成功”这个值
# 2.$..key  递归获取方式  有多个则根据下标取值[]

import requests
import jsonpath


def test_hctest_01():
    url = "http://shop-xo.hctestedu.com/index.php?s=/api/user/login"
    headers = {"application": "app", "application_client_type": "weixin"}
    data = {"accounts": "huace_xm",
            "pwd": "123456",
            "type": "username"}
    res = requests.post(url=url, headers=headers, data=data)
    print(res.status_code)
    print(res.text)
    print(res.json())
    token_list = jsonpath.jsonpath(res.json(), '$..token')
    print(token_list)


'''
def test_xiaomiao():
    print("小小秒秒登录")
    url = "http://miao.matrixdesign.cn/api/auth/login"
    json = {"loginId": "guoshuang",
            "password": "e10adc3949ba59abbe56e057f20f883e"}
    res = requests.post(url=url, json=json)
    print(res.status_code)
    print(res.json())
    token_list = jsonpath.jsonpath(res.json(), '$..access_token')
    print(token_list[0])'''
