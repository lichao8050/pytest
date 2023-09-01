# *-* coding : utf-8 *-*
# @time : 2023/8/24 16:17
# @author : Mr_Li
# @file : test_post_json.py
import requests


# data = {"loginId": "guoshuang",
#         "password": "e10adc3949ba59abbe56e057f20f883e"}
# json_data = {"loginId": "guoshuang",
#              "password": "e10adc3949ba59abbe56e057f20f883e"}

def test_xiaomiao():
    res = requests.post(url="http://miao.matrixdesign.cn/api/auth/login", json={"loginId": "guoshuang",
                                                                                "password": "e10adc3949ba59abbe56e057f20f883e"})
    print(res.status_code)
    assert res.status_code == 200
    result = res.json()
    print(result)
    print(result['msg'])
    assert result['msg'] == '操作成功'
    assert result['code'] == 200
    assert result['data']['access_token'] is not None


def test_xiaomiao_1():
    res = requests.post(url="http://miao.matrixdesign.cn/api/auth/login", data={"loginId": "guoshuang",
                                                                                "password": "e10adc3949ba59abbe56e057f20f883e"})
    print(res.status_code)
    assert res.status_code == 200
    result = res.json()
    print(result)
    print(result['msg'])
    assert result['msg'] == '操作成功'
    assert result['code'] == 200
    assert result['data']['access_token'] is not None

# url = 'https://search.douban.com/movie/subject_search'
# params = {"search_text": "太平洋",
#           "cat": 1002}
# headers = {"User-Agent":
# "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
#

# url = 'https://search.douban.com/movie/subject_search' params = {"search_text": "太平洋", "cat": 1002} headers = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0
# Safari/537.36"} res2 = requests.get(url=url, params=params, headers=headers) assert res2.status_code == 200 print(
# res2.status_code) print(res2.text)
