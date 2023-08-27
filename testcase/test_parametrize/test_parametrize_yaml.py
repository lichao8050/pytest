# *-* coding : utf-8 *-*
# @time : 2023/8/25 18:12
# @author : Mr_Li
# @file :  ./
import pytest
import requests
from commons.yaml_until import YamlUntil


@pytest.mark.parametrize("url, loginId, password, cod, eq", YamlUntil('../../data/test_yaml.yml').read_yaml_data()["login_data"])
def test_xiaomiao_login(url, loginId, password, cod, eq):
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
#     a = YamlUntil('../../data/test_yaml.yml').read_yaml_data()["login_data"]
#     print(a)
