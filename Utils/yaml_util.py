import yaml
import os
from string import Template
import json

class YamlUtil():
    # 读取yaml文件并返回对应参数名的值

    def read_extract_yaml(self, key):
        with open(os.getcwd() + '/extract.yml', mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]
    # 写入yaml文件对应参数以及值
    def write_extract_yaml(self, data):
        with open(os.getcwd() + '/extract.yml', mode='a', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)
    # 清除yaml已经存在的值
    def clear_extract_yaml(self):
        with open(os.getcwd() + '/extract.yml', mode='w', encoding='utf-8') as f:
            f.truncate()
    # 读取测试用例对应yml文件的值(通常为字典/列表/元组格式)
    def read_testcase_yaml(self, yaml_name):
        with open(os.getcwd() + '/data/' + yaml_name, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value
    # 写入yaml文件对应参数以及值
    def write_testcase_yaml(self,yaml_name, data):
        with open(os.getcwd() + '/data/' + yaml_name, mode='a', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)
    # 清除yaml已经存在的值
    def clear_testcase_yaml(self, yaml_name):
        with open(os.getcwd() + '/data/' + yaml_name, mode='w', encoding='utf-8') as f:
            f.truncate()
    # 修改yaml文件下对应参数的值
    def alter_testcase_yaml(self, yaml_name):
        with open(os.getcwd() + '/data/' + yaml_name, mode='r', encoding='utf-8') as f:
            doc = yaml.safe_load(f)
            print(doc['request']['data']['csrf_token'])
            f.close()
    def set_state_yaml(self, yaml_name, token):
        with open(os.getcwd() + '/data/' + yaml_name, mode='r', encoding='utf-8') as f:
            read_yaml_str = f.read()
            template1 = Template(read_yaml_str)
            c = template1.safe_substitute({'token': token})
            with open(os.getcwd() + '/data/' + yaml_name[0:-4] + 'result.yml', mode='w', encoding='utf-8') as g:
                g.write(c)
                g.close()
        f.close()


