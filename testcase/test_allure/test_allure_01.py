# *-* coding : utf-8 *-*
# @time : 2023/8/26 16:17
# @author : Mr_Li
# @file : test_allure_01.py

# # allure 用例描述
# 使用方法                        参数值                参数说明
# @allure.epic()                 epic描述              定义项目、当有多个项目时使用。往下是feature
# @allure.feature()              模块名称              用例按照模块区分，有多个模块时给每个起名字
# @allure.story()                用例名称              一个用例的描述
# @allure.title(用例的标题)       用例标题              一个用例的标题
# @allure.testcase()             测试用例的连接地址     自动化用例对应的功能用例存放的系统地址
# @allure.issue()                缺陷地址              对应缺陷管理系统里面的缺陷地址
# @allure.description()          用例描述              对测试用例的详细描述
# @allure.step()                 操作步骤              测试用例的操作步骤
# @allure.severity()             用例等级              blocker、critical、normal、minor、trivial
# @allure.link()                 定义连接              用于定义一个需要在测试报告中展示的连接
# @allure.attachment()           附件                  添加测试报告的附件


# 使用allure报告必须配置pytest.ini文件 即添加如下行  addopts = -vs --alluredir ./report   ./report指在当前目录下生成执行文件
# 打开allure报告：
# 1.allure serve ./report
# 2.allure generate report + allure open allure-report
