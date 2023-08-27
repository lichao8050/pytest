# *-* coding : utf-8 *-*
# @time : 2023/8/24 19:20
# @author : Mr_Li
# @file : test_setup_teardown_class.py
# 方法级  ：setup_method/teardown_method  开始方法始末（在类中）
import requests


class TestXiaoMiaoA:

    def setup_method(self):
        print("类级的前置--准备测试数据")

    def teardown_method(self):
        print("类级的后置--清理测试数据")

    def test_xiaomiao(self):
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

    def test_xiaomiao_2(self):
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
