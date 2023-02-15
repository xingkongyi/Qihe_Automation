"""配置选项"""
import os

# 获取 config.py当前文件的路径
current_path = os.path.abspath(__file__)

# 配置文件目录的路径  setting/ 的路径
config_dir = os.path.dirname(current_path)

# 项目的根目录
root_dir = os.path.dirname(config_dir)

# 测试数据的目录路径 data/
data_dir = os.path.join(root_dir, 'data')

# 测试用例文件路径
case_file = os.path.join(data_dir, 'qihe_case.xlsx')

# host 域名
host = 'http://10.12.107.159:9000'

# token接口
token_host = 'http://10.12.107.158:8060/social/api/oauth/unite/v1/login'