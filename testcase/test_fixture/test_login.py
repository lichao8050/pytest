# *-* coding : utf-8 *-*
# @time : 2023/6/12 10:34
# @author : Mr_Li
# @file : test_login.py
import pytest
import requests
import self as self

from commons.yaml_until import YamlUntil


#
# @pytest.mark.parametrize("username, password", YamlUntil.read_testcase_yaml(self, yaml_path="G:\\pytest\\data\\test_yaml_00.yml"))
# def test_login_01(self, username, password):
#     res = requests.post(url=r'https://erpapi.matrixdesign.cn/pmtapi/base_Account/login', params={
#         "username": username, "password": password
#     })
#     print(res.json())
#
# if __name__ == '__main__':
#     pytest.main(['-s', 'G:\\pytest\\test_parametrize\\test_login'])
# res = YamlUntil('./test_yaml_00.yml').read_yaml_data()
# print(res)
@pytest.fixture(scope='session', autouse=True)
def test_setup_session():
    print("这是前置夹具，它的作用范围是session")


@pytest.fixture(scope='session', autouse=True)
def test_setup_class():
    print("这是前置夹具，它的作用范围是class")


class TestTest:

    def test_01(self):
        print("测试1")

    def test_02(self):
        print("测试2")
