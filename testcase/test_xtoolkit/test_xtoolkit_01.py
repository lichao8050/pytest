# *-* coding : utf-8 *-*
# @time : 2023/8/30 11:44
# @author : Mr_Li
# @file : test_xtoolkit_01.py

# 用xtlookit插件读取Excel表格
# 读取Excel可以自己写代码，但是这个可读性不强，所以推荐使用增强插件库xtoolkit
# xtoolkit读取Excel会直接返回一个Excel的列表回来，要使用它必须先导入 from xToolkit import x

from xToolkit import xfile

xtoolkit_read = xfile.read("G:\pytest\excel\login_excel.xlsx").excel_to_dict(sheet=1)
print(xtoolkit_read)
