import json
import unittest
import demjson3
import requests
from loguru import logger
from unittestreport import ddt, list_data
from cases.token_common import APICase
from common.execl import read_excel
from setting import config

add_cases = read_excel(file=config.case_file, sheet_name='event_acceptance_add')
dispatch_cases = read_excel(file=config.case_file, sheet_name='event_acceptance_dispatch')
transfer_cases = read_excel(file=config.case_file, sheet_name='event_acceptance_transfer')
handle_cases = read_excel(file=config.case_file, sheet_name='event_acceptance_handle')
check_cases = read_excel(file=config.case_file, sheet_name='event_acceptance_check')
feedback_cases = read_excel(file=config.case_file, sheet_name='event_acceptance_feedback')
close_cases = read_excel(file=config.case_file, sheet_name='event_acceptance_closecase')


@ddt
class TestEventAcceptanceAdd(unittest.TestCase, APICase):
    # 前置夹具，获取token
    def setUp(self) -> None:
        self.login_token()
        self.user_management_token()
        self.user_transfer_token()

    # 事件登记
    @list_data(add_cases)
    def test_event_acceptance_1(self, info):
        url = info['url']
        method = info['method']
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.register_token)
        headers = json.loads(headers)
        json_data = json.loads(info['json_data'])
        # globals()['newToken'] = headers['accessToken']
        # demjson3解析不规范的json字符串
        json_data = demjson3.encode(json_data)
        logger.info(info['json_data'])
        expected = json.loads(info['expected'])
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        logger.info(response.text)
        actual = response.json()
        globals()['newid'] = actual['data']
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])

    # 事件派遣
    @list_data(dispatch_cases)
    def test_event_acceptance_2(self, info):
        global newid
        url = info['url']
        method = info['method']
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.register_token)
        headers = json.loads(headers)
        json_data = info['json_data']
        if '#id#' in json_data:
            json_data = json_data.replace('#id#', str(newid))
        json_data = json.loads(json_data)
        # demjson3解析不规范的json字符串
        json_data = demjson3.encode(json_data)
        logger.info(info['json_data'])
        expected = json.loads(info['expected'])
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        logger.info(response.text)
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])

    # 事件转办
    @list_data(transfer_cases)
    def test_event_acceptance_3(self, info):
        global newid
        url = info['url']
        method = info['method']
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.management_token)
        headers = json.loads(headers)
        json_data = info['json_data']
        if '#id#' in json_data:
            json_data = json_data.replace('#id#', str(newid))
        json_data = json.loads(json_data)
        # demjson3解析不规范的json字符串
        json_data = demjson3.encode(json_data)
        logger.info(info['json_data'])
        expected = json.loads(info['expected'])
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        logger.info(response.text)
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])

    # 事件处理
    @list_data(handle_cases)
    def test_event_acceptance_4(self, info):
        global newid
        url = info['url']
        method = info['method']
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.transfer_token)
        headers = json.loads(headers)
        json_data = info['json_data']
        if '#id#' in json_data:
            json_data = json_data.replace('#id#', str(newid))
        json_data = json.loads(json_data)
        # demjson3解析不规范的json字符串
        json_data = demjson3.encode(json_data)
        logger.info(info['json_data'])
        expected = json.loads(info['expected'])
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        logger.info(response.text)
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])

    # 事件核查
    @list_data(check_cases)
    def test_event_acceptance_5(self, info):
        global newid
        url = info['url']
        method = info['method']
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.register_token)
        headers = json.loads(headers)
        json_data = info['json_data']
        if '#id#' in json_data:
            json_data = json_data.replace('#id#', str(newid))
        json_data = json.loads(json_data)
        # demjson3解析不规范的json字符串
        json_data = demjson3.encode(json_data)
        logger.info(info['json_data'])
        expected = json.loads(info['expected'])
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        logger.info(response.text)
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])

    # 事件反馈
    @list_data(feedback_cases)
    def test_event_acceptance_6(self, info):
        global newid
        url = info['url']
        method = info['method']
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.register_token)
        headers = json.loads(headers)
        json_data = info['json_data']
        if '#id#' in json_data:
            json_data = json_data.replace('#id#', str(newid))
        json_data = json.loads(json_data)
        # demjson3解析不规范的json字符串
        json_data = demjson3.encode(json_data)
        logger.info(info['json_data'])
        expected = json.loads(info['expected'])
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        logger.info(response.text)
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])

    # 事件结案
    @list_data(close_cases)
    def test_event_acceptance_7(self, info):
        global newid
        url = info['url']
        method = info['method']
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.register_token)
        headers = json.loads(headers)
        json_data = info['json_data']
        if '#id#' in json_data:
            json_data = json_data.replace('#id#', str(newid))
        json_data = json.loads(json_data)
        # demjson3解析不规范的json字符串
        json_data = demjson3.encode(json_data)
        logger.info(info['json_data'])
        expected = json.loads(info['expected'])
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        logger.info(response.text)
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])