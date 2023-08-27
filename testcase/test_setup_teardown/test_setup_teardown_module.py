# *-* coding : utf-8 *-*
# @time : 2023/8/24 18:46
# @author : Mr_Li
# @file : test_setup_teardown_module.py

# 模块级  ：setup_module/teardown_module  开始于模块始末，执行一次
# 函数级  ：setup_function/teardown_function  对每条函数用例生效，不在类中
# 类级  ：setup_class/teardown_class  只在类前后执行一次（在类中）
# 方法级  ：setup_method/teardown_method  开始方法始末（在类中）
import requests


def setup_module():
    print("模块级的前置--准备测试数据")


def teardown_module():
    print("模块级的后置--清理测试数据")


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
