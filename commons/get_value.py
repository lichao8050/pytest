# *-* coding : utf-8 *-*
# @time : 2023/9/1 11:55
# @author : Mr_Li
# @file : get_value.py


class Get_Value(object):
    # 创建一个公共类，并在类中定义一个字典‘_globle_dict = {}’，并在类中加入，set，get方法
    _globle_dict = {}

    # 加入set方法：设置字典中每个key对应的value值
    def set_dict(self, key, value):
        self._globle_dict[key] = value

    # 加入get方法，通过对应key获取值value
    def get_dict(self, key):
        return self._globle_dict[key]

    # 查看字典信息
    def show_dict(self):
        return self._globle_dict
