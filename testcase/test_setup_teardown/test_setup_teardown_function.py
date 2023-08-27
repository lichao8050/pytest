# *-* coding : utf-8 *-*
# @time : 2023/8/24 19:09
# @author : Mr_Li
# @file : test_setup_teardown_function.py
# 函数级  ：setup_function/teardown_function  对每条函数用例生效，不在类中，用例不在某个类里面
import requests


def setup_function():
    print("函数级的前置--准备测试数据")


def teardown_function():
    print("函数级的后置--清理测试数据")


def test_xiaomiao():
    url = "http://miao.matrixdesign.cn/api/auth/login"
    json = {"loginId": "guoshuang",
            "password": "e10adc3949ba59abbe56e057f20f883e"}
    res = requests.post(url=url, json=json)
    print(res.status_code)
    assert res.status_code == 200
    result = res.json()
    print(result)
    print(result['msg'])
    assert result['msg'] == '操作成功'
    assert result['code'] == 200
    assert result['data']['access_token'] is not None


def test_xiaomiao_1():
    url = "http://miao.matrixdesign.cn/api/auth/login"
    json = {"loginId": "guoshuang",
            "password": "e10adc3949ba59abbe56e057f20f883e"}
    res = requests.post(url=url, json=json)
    print(res.status_code)
    assert res.status_code == 200
    result = res.json()
    print(result)
    print(result['msg'])
    assert result['msg'] == '操作成功'
    assert result['code'] == 200
    assert result['data']['access_token'] is not None
