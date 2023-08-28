# *-* coding : utf-8 *-*
# @time : 2023/8/28 16:52
# @author : Mr_Li
# @file : encryption_and_decryption.py
# 加密解密
"""可以通过jsonpath获取json响应中某个key对应的value值：
两种方式1，$.key 如：{'msg': '登录成功', 'code': 0, 'data': {'body_html': ''}} >>  $.msg 将获取到“登录成功”这个值
2.$..key  递归获取方式  有多个则根据下标取值[]

加密接口的处理
1.执行命令 pip install pycryptodome
2.执行命令 pip install rsa
工作中，有些接口的参数是暴露在外面的。核心业务的处理，不安全。所以我们应该让对应的参数变成对应的密文
加密的领域有个概念：所有的加密和解密，都会有一个密钥的概念，将明文>>密码本>>输出为一段密文
# 中科大镜像
pip install 包名 -i https://mirrors.ustc.edu.cn/pypi/web/simple
# 阿里源
pip install 包名 -i https://mirrors.aliyun.com/pypi/simple/
# 腾讯源
pip install 包名 -i http://mirrors.cloud.tencent.com/pypi/simple
# 豆瓣源
pip install 包名 -i http://pypi.douban.com/simple/"""
import jsonpath
import requests


def test_xiaomiao():
    print("小小秒秒登录")
    url = "http://miao.matrixdesign.cn/api/auth/login"
    json = {"loginId": "guoshuang",
            "password": "e10adc3949ba59abbe56e057f20f883e"}
    res = requests.post(url=url, json=json)
    print(res.status_code)
    print(res.json())
    token_list = jsonpath.jsonpath(res.json(), '$..access_token')
    print(token_list[0])
