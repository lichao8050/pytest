# *-* coding : utf-8 *-*
# @time : 2023/8/25 16:00
# @author : Mr_Li
# @file : test_cs_test.py


# 冒泡排序：
def test_maopao():
    list_01 = [43, 11,3,42,56,21,12,35]
    for i in range(len(list_01)-1, 0, -1):
        for j in range(i):
            # 小于就是从小到大，大于就是从大到小
            if list_01[j] < list_01[j + 1]:
                list_01[j], list_01[j + 1] = list_01[j + 1], list_01[j]
    print(list_01)


# 打印99乘法表：
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%2d' % (j, i, i * j), end=' ')
    print('')
