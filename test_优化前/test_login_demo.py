import hashlib
import json
import unittest
import requests
from unittestreport import ddt, list_data
from common.execl import read_excel
from setting import config

cases = read_excel(file=config.case_file, sheet_name='Login')
print(cases)


@ddt
class TestRegister(unittest.TestCase):

    def test_register_1(self):
        """步骤：
        1. 准备测试数据
        2. 发送接口请求，得到实际结果
        3. 预期结果和实际结果的断言。
        """
        # 1. 准备测试数据
        url = 'http://10.12.107.159:9000/oauth2/login'
        method = 'post'
        headers = {"content-type": "application/x-www-form-urlencoded"}
        src = '888888'
        m2 = hashlib.md5()
        m2.update(src.encode("utf8"))
        json_data1 = m2.hexdigest()
        json_data = {"username": "yuxy", "password": json_data1}
        # json_data = json.dumps(json_data_dict)
        expected = {
            "code": "200",
            "message": "登陆成功",
            "data": None
        }
        # 2. 发送接口请求，得到实际结果
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])
