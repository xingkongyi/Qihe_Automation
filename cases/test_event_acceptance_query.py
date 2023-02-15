import json
import unittest
import requests
from unittestreport import ddt, list_data
from cases.token_common import APICase
from common.execl import read_excel
from setting import config

cases = read_excel(file=config.case_file, sheet_name='event_acceptance_query')


@ddt
class TestEventAcceptanceQuery(unittest.TestCase, APICase):
    # 前置夹具，获取token
    def setUp(self) -> None:
        self.login_token()

    @list_data(cases)
    def test_event_acceptance_query(self, info):
        url = info['url']
        method = info['method']
        params = json.loads(info['params'])
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.register_token)
        headers = json.loads(headers)
        expected = json.loads(info['expected'])
        response = requests.request(url=url, params=params, method=method, headers=headers)
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])
