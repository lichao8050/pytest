# *-* coding : utf-8 *-*
# @time : 2023/8/25 16:25
# @author : Mr_Li
# @file : test_parametrize_01.py
# pytest 学习
# 参数化学习：parametrize


"""
单次循环：
@pytest.mark.parametrize("a", ["b"])
def test_parametrize(a):
print(a)
此处打印a将会显示a对应的值b
"""

import pytest


# 单参数单次循环就只给一个值，单参数多次循环就同时给多个值@pytest.mark.parametrize("key", ["vaule1", "vaule2", "vaule3"])
@pytest.mark.parametrize("name", ["黄忠", "小鲁班", "蒙犽"])
def test_paramrtrize(name):
    print("测试parametrize单参数，您选择的英雄的名字是%s" % name)
    assert name == "黄忠" or "小鲁班" or "蒙犽"
