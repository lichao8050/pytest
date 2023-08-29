# *-* coding : utf-8 *-*
# @time : 2023/8/28 16:52
# @author : Mr_Li
# @file : encryption_and_decryption_aes.py

"""
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
pip install 包名 -i http://pypi.douban.com/simple/
一、对称加密
对称加密是指加密和解密使用相同的密钥的一种加密方式。pycryptodome也提供了对称加密的相关功能。
1. AES加密
AES是目前最常用的对称加密算法之一。使用pycryptodome中的AES模块可以进行AES加密操作。
from Crypto.Cipher import AES
import base64

def aes_encrypt(key, data):
    key_bytes = key.encode('utf-8')
    data_bytes = data.encode('utf-8')
    iv = '0000000000000000'
    iv_bytes = iv.encode('utf-8')
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    cipher_data = cipher.encrypt(data_bytes)
    base64_cipher_data = base64.b64encode(cipher_data)
    return base64_cipher_data.decode('utf-8')
以上代码中，aes_encrypt方法接受两个参数，分别是加密密钥和要加密的数据。首先将密钥和数据转换成字节类型，
然后设置初始化向量iv（长度必须为16），接下来使用AES模块的new函数创建加密对象，并进行加密操作。
最后使用base64对加密后的数据进行编码，返回加密后的数据。

2. DES加密
DES加密是一种对称加密算法。使用pycryptodome中的DES模块可以进行DES加密操作。具体实现如下：
from Crypto.Cipher import DES
def des_encrypt(key, data):
    key_bytes = key.encode('utf-8')
    data_bytes = data.encode('utf-8')
    iv = '00000000'
    iv_bytes = iv.encode('utf-8')
    cipher = DES.new(key_bytes, DES.MODE_CBC, iv_bytes)
    cipher_data = cipher.encrypt(data_bytes)
    return cipher_data.hex()
以上代码中，des_encrypt方法接受两个参数，分别是加密密钥和要加密的数据。首先将密钥和数据转换成字节类型，
然后设置初始化向量iv（长度必须为8），接下来使用DES模块的new函数创建加密对象，并进行加密操作。最后返回加密后的十六进制字符串。

二、非对称加密
非对称加密是指加密和解密使用不同的密钥的一种加密方式。pycryptodome也提供了非对称加密的相关功能。
1. RSA加密
RSA是一种非对称加密算法。使用pycryptodome中的RSA模块可以进行RSA加密操作。
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_encrypt(public_key, data):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    data_bytes = data.encode('utf-8')
    cipher_data = cipher.encrypt(data_bytes)
    return cipher_data.hex()
以上代码中，rsa_encrypt方法接受两个参数，分别是公钥和要加密的数据。首先将公钥转换成RSA密钥对象，
然后使用PKCS1_OAEP模块的new函数创建加密对象，并进行加密操作。最后返回加密后的十六进制字符串。

2. ECC加密
ECC是一种非对称加密算法，它比RSA更加轻量级，安全性更高。使用pycryptodome中的ECC模块可以进行ECC加密操作。
from Crypto.PublicKey import ECC

def ecc_encrypt(public_key, data):
    key = ECC.import_key(public_key)
    cipher_data = key.encrypt(bytes(data, 'utf-8'), None)
    return cipher_data.hex()
以上代码中，ecc_encrypt方法接受两个参数，分别是公钥和要加密的数据。首先将公钥转换成ECC密钥对象，
然后使用密钥的encrypt方法进行加密操作。最后返回加密后的十六进制字符串。

三、摘要算法
摘要算法是一种将任意长度的消息压缩到某一固定长度的算法。pycryptodome也提供了多种摘要算法的相关功能。
1. MD5
使用pycryptodome中的Hash模块可以进行MD5摘要算法操作。
from Crypto.Hash import MD5
def md5(data):
    h = MD5.new()
    h.update(data.encode('utf-8'))
    return h.hexdigest()
以上代码中，md5方法接受一个参数，即要计算摘要的数据。使用MD5模块的new方法创建摘要对象，
并使用update方法更新摘要，最后使用hexdigest方法返回摘要结果。

2. SHA256
使用pycryptodome中的Hash模块可以进行SHA256摘要算法操作。
from Crypto.Hash import SHA256
def sha256(data):
    h = SHA256.new()
    h.update(data.encode('utf-8'))
    return h.hexdigest()
以上代码中，sha256方法接受一个参数，即要计算摘要的数据。使用SHA256模块的new方法创建摘要对象，
并使用update方法更新摘要，最后使用hexdigest方法返回摘要结果。
"""
import base64
from Crypto.Cipher import AES

# 自己定义一段秘钥--'123456789123456789'
# 对称加密


class EncryptDate:
    def __init__(self, key):
        self.key = key.encode("utf-8")  # 初始化秘钥格式
        self.length = AES.block_size  # 设置AES 加密数据块大小
        self.aes = AES.new(self.key, AES.MODE_ECB)  # 新建一个 AES 算法实例，使用 ECB（电子密码本）模式
        self.unpad = lambda date: date[0: -ord(date[-1])]

    def pad(self, text):  # 补齐长度
        count = len(text.encode("utf-8"))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):  # 加密函数
        res = self.aes.encrypt(self.pad(encrData).encode("utf-8"))
        # base64是网络上最常见的用于传输8bit字节码的编码方式之一
        msg = str(base64.b64encode(res), encoding="utf8")
        return msg

    def decrypt(self, decrData):  # 解密函数
        res = base64.decodebytes(decrData.encode("utf-8"))
        msg = self.aes.decrypt(res).decode("utf8")
        return self.unpad(msg)


if __name__ == '__main__':
    key = '12345678987456zs'  # 注意秘钥key只能为16位或者16位的倍数，否则报错
    username = '123456'
    print(50 * '-' + '数据加密' + 50 * '-')
    en = EncryptDate(key)
    res = en.encrypt(username)
    print('%s通过秘钥%s加密后得到的密文是:%s' % (username, key, res))
    print(50 * '-' + '数据解密' + 50 * '-')
    res2 = en.decrypt(res)
    print(f'{username}通过秘钥{key}解密密后得到的明文是:{res2}')
    assert res2 == username
