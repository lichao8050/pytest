# *-* coding : utf-8 *-*
# @time : 2023/9/1 0:31
# @author : Mr_Li
# @file : test_string_template_01.py

"""
template: 如果碰到字符串有特殊符号${}
它会自动进行替换
用法：Template(需要替换的对象).substitute(进行替换的内容)
"""
from string import Template

import jsonpath
import pytest
import requests
from xToolkit import xfile


s_string = {"token": "accesss_token"}
url = "http://www.baidu.com?token=${token}"
print(Template(url).substitute(s_string))


@pytest.mark.parametrize("test_data", xfile.read('G:\\pytest\\excel\login_excel.xlsx').excel_to_dict())
def test_jiekouchuandi(test_data):
    print(test_data)
    url = test_data["请求地址"]
    method = test_data["请求方法"]
    json = test_data["请求参数"]
    res = requests.request(
        url=url,
        method=method,
        json=eval(json)
    )
    print(res.status_code)
    print(res.json())

    if test_data["提取参数"] is not None or test_data["提取参数"] != '':
        # 参数提取，使用jsonpath方法，提取后是一个列表
        lis = jsonpath.jsonpath(res.json(), '$..' + test_data["提取参数"])
        # 保存参数，很多接口会有不同参数，所以可以创建一个类，设计对应的方法保存提取共有变量
        print(lis)
    assert res.status_code == test_data["预期响应码"]
