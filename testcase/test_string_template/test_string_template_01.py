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

问题：>>代码量大（修改，给别人）>>减少代码量（重复的工作一起处理）>>分解思路>>流程中统一的东西提取出来
>>一个接口请求无非就是：发送/接收

自定义封装的问题：
问题一：链接中token会变，用变量去定义
问题二：如果有多个变量我们该怎么办
问题三：变量应该保存在哪
问题四：如果每个接口对弈的响应的对应的东西都需要去提取，我们怎么保存
运行安装 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/

Pytest常⽤插件
　　pytest单元测试框架有很丰富的插件，下⾯分别介绍这些插件的应⽤。
　（1）Pytest-sugar   Pytest-sugar在执⾏的时候显示进度条，即使有失败的也会⽴刻显示出来，安装命令为：）
　　       pip3 install pytest-sugar
"""
import os
from string import Template
import allure
import jsonpath
import pytest
import requests
from xToolkit import xfile

from commons.get_value import Get_Value

s_string = {"token": "accesss_token"}
url = "http://www.baidu.com?token=${token}"
url2 = "http://miao.matrixdesign.cn/supplychain/api/shone/oridata/addEntityData?access_token=${token}"
print("打印替换后的URL", Template(url2).substitute(s_string))


@pytest.mark.parametrize("test_data", xfile.read('G:\\pytest\\excel\\xiaomiao_add_test.xlsx').excel_to_dict())
def test_jiekouchuandi(test_data):
    allure.title(test_data['用例编号'])
    allure.description(test_data['用例描述'])
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
    # 断言：机器帮助我们校验结果
    # 期望返回数据里有什么东西，包含某些必要的返回值
    # 不应该只关注状态码200，还应该关注其他关键数据是否正确
    assert res.status_code == 200
    assert res.status_code == test_data["预期响应码"]
    # assert res.json()['msg'] in test_data["预期结果"]
    for lis_t in eval(test_data["预期结果"]):
        print(lis_t)
        assert lis_t in res.text


if __name__ == '__main__':
    pytest.main(['-s', 'test_string_template_01.py', '--alluredir', './temp'])
    os.system('allure generate ./temp -o ./reports')
    # 报告写入pycharm本地目录，自动生成对应的文件夹
    # pytest.main(["-s", "test_RomweIos_run.py", "--alluredir", "./temp"])
    # os.system("allure generate ./temp -o ./reports --clean")
