# *-* coding : utf-8 *-*
# @time : 2023/9/1 0:31
# @author : Mr_Li
# @file : test_string_template_01.py

"""
template: 如果碰到字符串有特殊符号${}
它会自动进行替换
用法：Template(需要替换的对象).substitute(进行替换的内容)
接口自动化自定义框架封装；
用封装的思想来解决问题
一旦准备封装--首先思考，哪些地方可以封装，把重复的东西抽离，让它变成一个公共的东西
**自动化应该包括以下几个模块：核心执行器、断言、测试报告、无人值守**
"""

import jsonpath
import pytest
import requests
from xToolkit import xfile
from string import Template
from commons.get_value import Get_Value

s_string = {"token": "accesss_token"}
url = "http://www.baidu.com?token=${token}"
url2 = "http://miao.matrixdesign.cn/supplychain/api/shone/oridata/addEntityData?access_token=${token}"
print("打印替换后的URL", Template(url2).substitute(s_string))


@pytest.mark.parametrize("test_data", xfile.read('G:\\pytest\\excel\\xiaomiao_add_test.xlsx').excel_to_dict())
def test_jiekouchuandi(test_data):
    print("打印传入的test_data数据：", test_data)
    url = test_data["请求地址"]
    dic_t = Get_Value().show_dict()
    if '$' in url:
        url = Template(url).substitute(dic_t)
        print(url)
    res = requests.request(
        url=url,
        method=test_data["请求方法"],
        json=eval(test_data["json请求参数"]),
        data=test_data['data请求参数'],
        headers=eval(test_data['请求头部'])
    )
    print(res.status_code)
    print(res.json())

    if test_data["提取参数"] is not None or test_data["提取参数"] != '':
        # 参数提取，使用jsonpath方法，提取后是一个列表
        lis = jsonpath.jsonpath(res.json(), '$..' + test_data["提取参数"])
        # 保存参数，很多接口会有不同参数，所以可以创建一个类，设计对应的方法保存提取共有变量
        print(type(lis))
        Get_Value().set_dict(test_data["提取参数"], lis[0])
        print("打印保存后的字典", Get_Value().show_dict())
    else:
        print(Exception)
    assert res.status_code == test_data["预期响应码"]
    assert res.json()['msg'] in test_data["预期结果"]
