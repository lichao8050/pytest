# *-* coding : utf-8 *-*
# @time : 2023/8/25 18:12
# @author : Mr_Li
# @file :  ./
import pytest
import requests
from commons.yaml_until import YamlUntil


#  读取yaml 文件，获取‘login_data’这个类中的数据，并通过url, loginId, password, cod, eq这些参数传递到用例中：
@pytest.mark.parametrize("url, loginId, password, cod, eq", YamlUntil('../test_yaml_00.yml').
                         read_yaml_data()["login_data"])
def test_xiaomiao_login_1(url, loginId, password, cod, eq):
    print("测试小秒正常登录")
    url = url
    json = {"loginId": loginId, "password": password}
    res = requests.post(url=url, json=json)
    print(res.status_code)
    assert res.status_code == cod
    result = res.json()
    print(result)
    print(result['msg'])
    assert result['msg'] == eq
    assert result['code'] == cod
    assert result['data']['access_token'] is not None

# def test_yaml():
#     a = YamlUntil('../../data/test_yaml_00.yml').read_yaml_data()["login_data"]
#     print(a)


#  读取yaml 文件，获取‘login_data’这个类中的数据，并通过data直接将所有参数传递到用例中：
@pytest.mark.parametrize("data", YamlUntil('../../data/test_yaml_00.yml').read_yaml_data()["login_data"])
def test_xiaomiao_login_2(data):
    print("测试小秒正常登录")
    print(data)
    url = data['url']
    json = {"loginId": data['loginid'], "password": data['password']}
    print(data['password'])
    method = data['method']
    headers1 = data['headers']
    print(headers1)
    headers = {'Content-Type': 'application/json'}
    print(headers)
    res = requests.request(url=url, headers=headers1, method=method, json=json)
    print(res.status_code)
    print(res.json())
    assert res.status_code == data['cod']
    result = res.json()
    print(result)
    print(result['msg'])
    assert result['msg'] == data['asser_eq']
    assert result['code'] == data['cod']
    assert result['data']['access_token'] is not None


@pytest.mark.parametrize("data", YamlUntil('../../data/test_yaml_00.yml').read_yaml_data()["login_data"])
def test_xiaomiao_login_3(data):
    url = data['url']
    print(url)
    method = data['method']
    print(method)
    json = {"loginId": data['loginid'], "password": data['password']}
    print(json)
    headers = data['headers']
    print(headers)
    print(type(headers))
    print(type(json))
    res = requests.request(url=url, headers=headers, method=method, json=json)
    print(res.json())
