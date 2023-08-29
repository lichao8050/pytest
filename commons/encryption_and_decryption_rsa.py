# *-* coding : utf-8 *-*
# @time : 2023/8/29 22:51
# @author : Mr_Li
# @file : encryption_and_decryption_rsa.py

# 非对称加密
import base64
import rsa
# 秘钥的位数，可以自定义指定，列如：128,256,512 2的倍数
(pubkey, privkey) = rsa.newkeys(512)
# 生成公钥
pub = pubkey.save_pkcs1()
with open('public.pem', 'wb') as f:
    f.write(pub)

# 生成私钥
pri = privkey.save_pkcs1()
with open('private.pem', 'wb') as f:
    f.write(pri)

with open("./private.pem", "r") as f:
    priv_str = f.read()

with open("./public.pem", "r") as f:
    pub_str = f.read()


class Rsa:

    def __init__(self):
        self.pub_key = rsa.PublicKey.load_pkcs1(pub_str)
        self.priv_key = rsa.PrivateKey.load_pkcs1(priv_str)

    def encrypt(self, text):
        #  rsa加密  最后把加密字符串转为base64
        text = text.encode("utf-8")
        cryto_info = rsa.encrypt(text, self.pub_key)
        cipher_base64 = base64.b64encode(cryto_info)
        cipher_base64 = cipher_base64.decode()
        return cipher_base64

    def decrypt(self, text):
        #  RSA解密
        cryto_info = base64.b64decode(text)
        talk_real = rsa.decrypt(cryto_info, self.priv_key)
        res = talk_real.decode("utf-8")
        return res


if __name__ == '__main__':
    encr = Rsa()
    tex = encr.encrypt("小明")
    a = encr.decrypt(tex)
    print("这是加密后的结果：", tex)
    print("这是解密后的结果：", a)













