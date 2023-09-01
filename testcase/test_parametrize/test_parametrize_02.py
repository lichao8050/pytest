# *-* coding : utf-8 *-*
# @time : 2023/8/25 16:25
# @author : Mr_Li
# @file : test_parametrize_02.py
# pytest 学习
# 参数化学习：parametrize


"""
多次循环
@pytest.mark.parametrize("a, b", [["c", "d"],["e", "f"]])------parametrize("key1, key2", [["value1", "value2"],
这里的key1,key2必须跟后面的一组值[value1,value2]对应                           ["value1", "value2"]])
def test_parametrize(a, b):
print(a, b)
"""

import pytest
from commons.yaml_until import YamlUntil
# 数组的形式
# 多参数单次循环就只给一组值，多参数多次循环就同时给多组值@pytest.mark.parametrize("key1，key2", [["vaule1", "vaule2"],["vaule1","vaule2"])
import requests


@pytest.mark.parametrize("name, world", [["黄忠", "周日都得给我熄火！"], ["小鲁班", "不作是不会死的！"], ["蒙犽", "跟我的浑天讲去吧！"]])
def test_paramrtrize(name, world):
    print("测试parametrize数组形式，多参数，您选择的英雄的名字是%s,他常说的一句话是%s" % (name, world))
    assert name == "黄忠" or "小鲁班" or "蒙犽"
    assert name is not None


# # 元组的形式
# # 多参数单次循环就只给一组值，多参数多次循环就同时给多组值@pytest.mark.parametrize("key1，key2", [["vaule1", "vaule2"],["vaule1","vaule2"])
@pytest.mark.parametrize("name, world", [("黄忠", "周日都得给我熄火！"), ("小鲁班", "不作是不会死的！"), ("蒙犽", "跟我的浑天讲去吧！")])
def test_paramrtrize_1(name, world):
    print("测试parametrize元组形式，多参数，您选择的英雄的名字是%s,他常说的一句话是%s" % (name, world))
    assert name == "黄忠" or "小鲁班" or "蒙犽"
    assert name is not None


@pytest.mark.parametrize("url, loginId, password, cod, eq", YamlUntil('../../testcase/test_yaml_00.yml').read_yaml_data()["login_data"])
def test_xiaomiao_login(url, loginId, password, cod, eq):
    print("小小秒秒登录1")
    url = url
    json = {"loginId": loginId, "password": password}
    res = requests.post(url=url, json=json)
    print(res.status_code)
    assert res.status_code == cod
    result = res.json()
    assert result['code'] == cod
    print(result)
    print(result['msg'])
    assert eq in result['msg']
    assert result['data']['access_token'] is not None
