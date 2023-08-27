# *-* coding : utf-8 *-*
# @time : 2023/8/25 12:21
# @author : Mr_Li
# @file : test_session.py
import pytest
import requests

'''可以通过设置函数方法然后后面的函数写入该方法实现前置夹具的调用，填写了就调用夹具，没填的就不会调用
    也可通过pytest.fixture(scope="session", autouse=True)设置所有用例自动执行该夹具'''


# @pytest.fixture(scope="function", autouse=True)
@pytest.fixture(scope="class", autouse=True)
def sessio():
    print("这是session前置夹具，多个文件调用一次，可以跨.py文件调用（通常这个级别会结合conftest.py文件使用")


class TestLogin:
    def test_xiaomiao(self):
        print("小小秒秒登录")
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

    def test_xiaomiao_1(self):
        print("小小秒秒登录2")
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
