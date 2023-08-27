# _*_ coding: utf-8 _*_
# @Time     : 2022/9/26 16:14
# @Author   : Mr_Li
# @FileName : test_new_action.py
from commons.read_excel_until import ExcelReader
from commons.request_page import HttpRequest
import pytest


class TestAddNewActionApi:
    @pytest.mark.actiontest
    def test_add_new_action(self, get_session):
        res, excel, url1 = get_session
        count_row = excel.get_case_count()
        for row in range(0, count_row):
            case_describe = excel.get_test_case_describe(row)
            print("用例描述：%s" % case_describe)
            method = excel.get_method(row)
            print("接口请求方法：%s" % method)
            url = url1 + excel.get_url(row)
            print("接口请求地址：%s" % url)
            data = eval(excel.get_request_data(row))  # 此处参数类型不是字符串，所以用eval转换为字典类型
            print("接口请求数据：%s" % data)
            res = HttpRequest().send_all_request(method=method, url=url, json=data)

            if res.status_code != int(excel.get_start_code(row)):  # 判断响应代码是否等于预期值
                # 不等于就将该用例测试结果写上“FAIL”
                excel.set_pass_or_fail(row, 9, "FAIL")
            else:
                # 等于就将该用例测试结果写上“PASS”
                excel.set_pass_or_fail(row, 9, "PASS")
            excel.set_pass_or_fail(row, 8, res.text)  # 将服务器返回信息写入该用例“接口响应”一栏中
            excel.save_file(r"D:\untitled\excel\test_add_new_action.xlsx")  # 保存写入结果
            print("接口响应代码：%s" % res.status_code)
            print("接口响应数据：%s" % res.json())
            print(200 * '*')

    @pytest.mark.cttest
    def test_print_excel_url(self, get_session):
        res, excel, url1 = get_session
        count_row = excel.get_case_count()
        for row in range(0, count_row):
            case_describe = excel.get_test_case_describe(row)
            print("用例描述：%s" % case_describe)
            url = url1 + excel.get_url(row)
            print("接口请求地址：%s" % url)

    @pytest.mark.acctest
    def test_erp_url(self, ERP_login):
        res1, excel, url1 = ERP_login
        count_row = excel.get_case_count()
        for row in range(0, count_row):
            case_describe = excel.get_test_case_describe(row)
            print("用例描述：%s" % case_describe)
            url = url1 + excel.get_url(row)
            print("接口请求地址：%s" % url)
            method = excel.get_method(row)
            print("接口请求方法：%s" % method)
            res1 = HttpRequest().send_all_request(method=method, url=url)
            #
            # if res.status_code != int(excel.get_start_code(row)):  # 判断响应代码是否等于预期值
            #     # 不等于就将该用例测试结果写上“FAIL”
            #     excel.set_pass_or_fail(row, 9, "FAIL")
            # else:
            #     # 等于就将该用例测试结果写上“PASS”
            #     excel.set_pass_or_fail(row, 9, "PASS")
            # excel.set_pass_or_fail(row, 8, res.text)  # 将服务器返回信息写入该用例“接口响应”一栏中
            # excel.save_file(r"D:\untitled\excel\test_add_new_action.xlsx")  # 保存写入结果
            print("接口响应代码：%s" % res1.status_code)
            print("接口响应数据：%s" % res1.text)
            print(200 * '*')
