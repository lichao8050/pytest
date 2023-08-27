# *-* coding : utf-8 *-*
# @time : 2023/6/12 8:47
# @author : Mr_Li
# @file : test_parametrize_01.py
import pytest
import unittest


# 单参数通过parametrize方法传递
@pytest.mark.parametrize("name", ["哈哈哈"])
def test_parametrize_01(name):
    print("我是" + name)
    assert name == "哈哈哈"


# 多个参数通过parametrize方法传递
@pytest.mark.parametrize("name, age", [["无敌", "18"], ["王大拿", "25"], ["潇洒哥", "44"]])
def test_parametrize_02(name, age):
    print(f"我叫{name},我今年{age}岁")


if __name__ == '__main__':
    pytest.main(['-s', 'G:\\pytest\\test_parametrize\\test_parametrize_01.py'])
