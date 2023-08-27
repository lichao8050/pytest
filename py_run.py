# _*_ coding: utf-8 _*_
# @Time     : 2022/9/15 11:34
# @Author   : Mr_Li
# @FileName : py_run.py
from commons.yaml_until import YamlUntil
"""import pytest

if __name__ == '__main__':
    # pytest.main(['D:/untitled/testcase/test_add_action_case.py', '-q', '-m cttest'])
    # pytest.main(['D:/untitled/test_login/testlogin.py', '-q'])
    # pytest.main(['D:/untitled/testcase/test_add_new_action.py', '-q'])
    pytest.main(['G:/pytest/testcase/test_new_action.py', '-m acctest'])
"""

"""pytest.main()的使用
1. pytest的两种运行模式，一种是命令行运行，另外一种是调用pytest.main() 运行
2. pytest.main() 运行模式时，不添加任何参数，表示运行当前目录下的所有的测试文件；
　　2.1 main()方法中不填写任何参数，表示运行当前目录下的所有的测试文件；
　　2.2 添加参数：pytest.main(['-s','-v','-k "print"',''])
　　　　（1）'-s'：关闭捕捉，输出打印信息；----就是运行的时候是否出入代码里边的一些打印信息，比如你的测试代码里边包含了print语句，
        则print的内容会显示出来；如果不填写该参数，则print语句的值不会打印出来
　　　　（2）'-v':用于增加测试用例的冗长。---没太看懂到底代表啥意思，等看懂了再补充上，这是复制的别人的
　　　　（3）'-k' ：运行包含某个字符串的测试用例。如：pytest -k add XX.py 表示运行XX.py中包含add的测试用例。
　　　　（4）'q':减少测试的运行冗长。
　　　　（5）'-x':出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例
        （6）'-m ' 打上标记，'-m +标记名'
        用法pytest.main(['D:/untitled/testcase/test_add_action_case.py', '-m cttest'])
　　2.3 要执行测试用例的过滤方法：
　　　　（1）指定某个测试类或测试方法，用“::”隔开。
        如：命令格式：pytest 文件名.py::测试方法 ，pytest.main([模块.py::类或方法])
        ，pytest 文件名.py::测试类::测试方法 ，pytest.main([模块.py::类::方法])
3. python文件中包含如下代码，则可运行当前目录下，的测试类或者测试方法（以test_开头或者以test结尾的类.py文件，
    以test_开头的测试方法,具体可参照配置文件），同时使用到多个参数时，格式如下：
    pytest.main(['D:/untitled/testcase/test_add_action_case.py::TestApi::test_add_new_action', '-q'])
4.pytest配置文件相关参数
    -v：显示更详细的信息
    -vs：这两个参数一起用
    -n ：支持多线程或者分布式运行测试用例
     如：pytest -vs ./testcase/test_login.py -n 2
    --html : 测试报告位置
    --reruns ： 失败重跑
    -p no:warnings  ： 取消警告
    --ff ： 先执行上次失败的用例
    --lf ： 只执行上次失败的用例
    -x ： 遇到测试用例fail，就结束测试
    --maxfail=num：遇到num条测试用例fail, 就结束测试
    -k ：根据测试用例的部分字符串指定测试用例
    """