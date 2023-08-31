# *-* coding : utf-8 *-*
# @time : 2023/8/30 11:44
# @author : Mr_Li
# @file : test_xtoolkit_01.py

# 用xtlookit插件读取Excel表格
# 读取Excel可以自己写代码，但是这个可读性不强，所以推荐使用增强插件库xtoolkit
# xtoolkit读取Excel会直接返回一个Excel的列表回来，要使用它必须先导入 from xToolkit import x
# 接口关联怎么处理？
"""
解决第一个问题：怎么给这个token赋值
Template可以自动去替换值
解决第二个问题：关联接口+
我在第一个接口请求完毕后，要知道我需要提取出一个对应的值出来
第二个是我在后续接口运行的时候，我要知道我需要对应的前面保存的值
"""
import pytest
import requests
from xToolkit import xfile

xtoolkit_read = xfile.read('G:\\pytest\\excel\login_excel.xlsx').excel_to_dict()
print("读取表格后返回的数据是：", xtoolkit_read)


@pytest.mark.parametrize('case_data', xtoolkit_read)
def test_kbs_login(case_data):
    print(50 * '*' + "开始执行测试" + 50 * '*')
    print("传入parametrize后的数据是：", case_data)
    print(case_data['用例编号'])
    print("用例名称是：", case_data['用例描述'])
    print(case_data['用例名称'])
    print(case_data['请求方式'])
    print(case_data['请求地址'])
    print(case_data['请求头部'])
    print(case_data['请求参数'])
    url = case_data['请求地址']
    headers = case_data['请求头部']
    method = case_data['请求方式']
    json = case_data['请求参数']
    # headers = eval(headers)
    # json = eval(json)
    # print(headers)
    # print(type(headers))
    # print(type(json))
    #  由于传入的参数是str格式所以要用eval()将其转换成字典格式
    res = requests.request(url=url, headers=eval(headers), json=eval(json), method=method)
    print("登录请求响应状态码是：", res.status_code)
    print("登录请求响应信息是：", res.json())
    assert res.status_code == case_data['预期响应码']
    print(50 * '*' + "本用例执行完毕" + 50 * '*')


if __name__ == '__main__':
    pytest.main(['-p no:warnings'])
