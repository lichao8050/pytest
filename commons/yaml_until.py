# *-* coding : utf-8 *-*
# @time : 2023/5/18 21:27
# @author : Mr_Li
# @file : yaml_until.py
import os
import yaml


# 1.创建类 文件调用：YamlUntil('当前目录的相对路径找到想要读取的yaml文件').读取/写入/清空方法
class YamlUntil:

    # 2.初始化,检查文件是否存在
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("文件不存在")
        self.yml_data = None
        self.yml_datas = None

    # 3.读取单个文件
    def read_yaml_data(self):
        # 第一次调用方法读取yaml文档，如果不是则直接返回之前保存的数据
        if not self.yml_data:
            with open(self.yamlf, mode="r", encoding='UTF-8') as yml:
                self.yml_data = yaml.safe_load(stream=yml)
                return self.yml_data

    # 读取多个文件
    def read_yaml_datas(self):
        # 第一次调用方法读取yaml文档，如果不是则直接返回之前保存的数据
        if not self.yml_datas:
            with open(self.yamlf, mode='r', encoding='UTF-8') as yml:
                self.yml_datas = list(yaml.safe_load_all(stream=yml))
                return self.yml_datas

    # 3.读取文件
    # def read_yaml_data(self):
    #     # 第一次调用方法读取yaml文档，如果不是则直接返回之前保存的数据
    #     if not self.yml_data:
    #         with open(self.yamlf, mode='r', encoding='UTF-8') as yml:
    #             value = yaml.load(stream=yml, Loader=yaml.FullLoader)
    #             return value
    # 写
    def write_yaml(self, data):
        with open(os.getcwd() + "./yaml/extract.yaml", mode='a', encoding='UTF-8') as yml:
            yaml.dump(data, stream=yml, allow_unicode=True)

    # 清空
    def clear_yaml(self):
        with open(os.getcwd() + "./yaml/extract.yaml", 'w', encoding='UTF-8') as yml:
            yml.truncate()
