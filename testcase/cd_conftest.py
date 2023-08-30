# _*_ coding: utf-8 _*_
# @Time     : 2022/9/26 16:15
# @Author   : Mr_Li
# @FileName : cd_conftest.py
import pytest
from commons.request_page import HttpRequest
from commons.read_excel_until import ExcelReader


# 使用pytest夹具定义前置、后置
# @pytest.fixture(scope='session')
def test_session():
    print(50 * '*' + '测试环境，开始测试' + 50 * '*')
    excel = ExcelReader(r"D:\pytest\excel\test_add_new_action.xlsx")
    url = r'http://kbs.matrixdesign.cn/api/pmtapi/base_Account/login'
    url1 = r'http://kbs.matrixdesign.cn'
    data = {
        "username": "heqiangming",
        "password": "abc123456"
    }
    method = 'post'
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    res = HttpRequest().send_all_request(method=method, url=url, params=data)
    print("登录获取session：%s" % res.headers['set-Cookie'])
    yield res, excel, url1
    print(50 * '*' + '结束测试' + 50 * '*')
    excel.close_file()


'''
@pytest.fixture(scope='session', autouse=True)
def ERP_login():
    """正式环境"""
    print(50 * '*' + '开始测试' + 50 * '*')
    excel = ExcelReader(r"G:\pytest\excel\test_erp_login.xlsx")
    url = r'https://erpapi.matrixdesign.cn/pmtapi/base_Account/login'
    url1 = r'https://erpapi.matrixdesign.cn'
    data = {
        "username": "heqiangming",
        "password": "abc147258369",
        "authType": "adm-u",
        "validateCode": "",
        "rememberme": "true"
    }
    method = 'post'
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    res1 = HttpRequest().send_all_request(method=method, url=url, params=data)

    print("登录获取session：%s" % res1.headers['set-Cookie'])
    yield res1, excel, url1
    print(50 * '*' + '正式环境结束测试' + 50 * '*')
    excel.close_file()


"""Fixture作用域
Unittest框架中setup的作用是每条测试用例执行之前都会执行一次，setupclass的作用是每个测试用例类执行之前都会执行一次。
pytest的fixture同样有这样的作用域，且使用更广泛更灵活。
​关键代码：@pytest.fixture(scope='作用范围')，参数如下：
function：默认作用域，每个测试用例都运行一次
class：每个测试类只执行一次
module：每个模块只执行一次(模块:一个.py文件)
package：每个python包只执行一次
session：整个会话只执行一次，即运行项目时整个过程只执行一次
Fixture后面的括号不加任何参数，就代表默认作用域，与function作用一样。

'''