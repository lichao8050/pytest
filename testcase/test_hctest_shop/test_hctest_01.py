# *-* coding : utf-8 *-*
# @time : 2023/8/28 12:18
# @author : Mr_Li
# @file : test_hctest_01.py

# 可以通过jsonpath获取json响应中某个key对应的value值：
# 两种方式1，$.key 如：{'msg': '登录成功', 'code': 0, 'data': {'body_html': ''}} >>  $.msg 将获取到“登录成功”这个值
# 2.$..key  递归获取方式  有多个则根据下标取值[]

# 加密接口的处理
# 1.执行命令 pip install pycryptodome
# 2.执行命令 pip install rsa
# 工作中，有些接口的参数是暴露在外面的。核心业务的处理，不安全。所以我们应该让对应的参数变成对应的密文
# 加密的领域有个概念：所有的加密和解密，都会有一个密钥的概念，将明文>>密码本>>输出为一段密文
import requests
import jsonpath


#
# def test_hctest_01():
#         url = "http://shop-xo.hctestedu.com/index.php?s=/api/user/login"
#         headers = {"application": "app", "application_client_type": "weixin"}
#         data = {"accounts": "huace_xm",
#                 "pwd": "123456",
#                 "type": "username"}
#         res = requests.post(url=url, headers=headers, data=data)
#         print(res.status_code)
#         print(res.text)
#         print(res.json())
#         token_list = jsonpath.jsonpath(res.json(), '$..token')
#         print(token_list)
#
