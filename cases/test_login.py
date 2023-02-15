import hashlib
import json
import unittest

import requests
from unittestreport import ddt, list_data
from common.execl import read_excel
from setting import config

cases = read_excel(file=config.case_file, sheet_name='Login')


@ddt
class TestLogin(unittest.TestCase):

    @list_data(cases)
    def test_login_1(self, info):
        """步骤：
        1. 准备测试数据
        2. 发送接口请求，得到实际结果
        3. 预期结果和实际结果的断言。
        """
        # 1. 准备测试数据
        url = info['url']
        json_data = json.loads(info['json_data'])
        # 转换MD5
        m2 = hashlib.md5()
        m2.update(json_data['password'].encode("utf8"))
        data_password = m2.hexdigest()
        json_data['password'] = data_password
        headers = info['headers']
        method = info['method']
        # 转化成字典类型
        headers = json.loads(headers)
        expected = json.loads(info['expected'])
        # 2. 发送接口请求，得到实际结果
        response = requests.request(url=config.host+url, method=method, headers=headers, data=json_data)
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])
