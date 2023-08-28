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
加密的领域有个概念：所有的加密和解密，都会有一个密钥的概念，将明文>>密码本>>输出为一段密文"""
