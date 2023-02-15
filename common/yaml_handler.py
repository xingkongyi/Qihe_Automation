import yaml


def read_yaml(file):
    """读取yaml文件"""
    with open(file, encoding='utf-8') as f:
        # 安装加载
        data = yaml.safe_load(f)
    return data
