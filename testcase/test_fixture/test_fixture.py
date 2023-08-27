# *-* coding : utf-8 *-*
# @time : 2023/8/24 19:43
# @author : Mr_Li
# @file : test_fixture.py
# fixture概念：fixture是pytest用于将测试前后进行预备、清理工作的代码处理机制。fixture相对于setup和teardown来说
# 有以下几点优势：
# 1.fixture命名更加灵活，局限性比较小
# 2.conftest.py 配置里面可以实现数据共享，不需要import就能自动找到一些配置
'''fixture夹具的用法：   @pytest.fixture
(scop="function")每一个函数或方法都会调用
(scop="class")每一个类调用一次，一个类中可以有多个方法
(scop="module")每一个.py文件调用一次，该文件内又有多个function和class
(scop="session")多个文件调用一次，可以跨.py文件调用（通常这个级别会结合conftest.py文件使用）'''