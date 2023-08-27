# *-* coding : utf-8 *-*
# @time : 2023/6/12 8:21
# @author : Mr_Li
# @file : read_data.py
import yaml

f = open("../testcase/config/data.yaml", encoding="utf-8")
data = yaml.safe_load(f)
print(data)
print(data['hero'])
print(data['heros1'])
print(data['heros_name'])
print(data['heros'])
print(data['heros_name_list'])