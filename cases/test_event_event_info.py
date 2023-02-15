import json
import unittest
import demjson3
import requests
from jsonpath import jsonpath
from loguru import logger
from unittestreport import ddt, list_data
from cases.token_common import APICase
from common.db_operation import DBHandler
from common.execl import read_excel
from setting import config

event_add_cases = read_excel(file=config.case_file, sheet_name='event_event_add')
event_transfer_cases = read_excel(file=config.case_file, sheet_name='event_event_transfer')
event_fallback_cases = read_excel(file=config.case_file, sheet_name='event_event_fallback')
event_escalation_cases = read_excel(file=config.case_file, sheet_name='event_event_escalation')
event_downsend_cases = read_excel(file=config.case_file, sheet_name='event_event_downsend')
event_finish_cases = read_excel(file=config.case_file, sheet_name='event_event_finish')
event_close_cases = read_excel(file=config.case_file, sheet_name='event_event_close')
event_selfclose_cases = read_excel(file=config.case_file, sheet_name='event_event_selfclose')


@ddt
class TestEventInfo(unittest.TestCase, APICase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.user_grid_token()
        cls.user_streetzfb_token()
        cls.user_streetzzzx_token()
        cls.user_areazzzx_token()

    def setUp(self) -> None:
        """数据库连接"""
        self.db = DBHandler()

    def tearDown(self) -> None:
        """数据库断开"""
        self.db.close()

    # 事件登记
    @list_data(event_add_cases)
    def test_event_acceptance_1(self, info):
        url = info['url']
        method = info['method']
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.grid_token)
        headers = json.loads(headers)
        json_data = json.loads(info['json_data'])
        # demjson3解析不规范的json字符串
        json_data = demjson3.encode(json_data)
        expected = json.loads(info['expected'])
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        logger.info(response.text)
        response_body = json.loads(response.text)
        add_event_id = jsonpath(response_body, '$..id')[0]
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])
        sql = f"SELECT ID_ FROM act_ru_task where PROC_INST_ID_ in (SELECT process_instance_id FROM event_event_info where id ='{str(add_event_id)}')"
        new_task_id = self.db.query_one(sql)[0]
        globals()['addTaskId'] = new_task_id
        globals()['addEventId'] = add_event_id

    # 事件转办
    @list_data(event_transfer_cases)
    def test_event_acceptance_2(self, info):
        global addTaskId, addEventId
        url = info['url']
        method = info['method']
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.streetzzzx_token)
        headers = json.loads(headers)
        json_data = info['json_data']
        if '#taskid#' in json_data:
            json_data = json_data.replace('#taskid#', str(addTaskId))
        if '#eventid#' in json_data:
            json_data = json_data.replace('#eventid#', str(addEventId))
        json_data = json.loads(json_data)
        transfer_event_id = json_data['eventInfoId']
        # demjson3解析不规范的json字符串
        json_data = demjson3.encode(json_data)
        expected = json.loads(info['expected'])
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])
        sql = f"SELECT ID_ FROM act_ru_task where PROC_INST_ID_ in (SELECT process_instance_id FROM event_event_info where id ='{str(transfer_event_id)}')"
        transfer_task_id = self.db.query_one(sql)[0]
        globals()['transferTaskId'] = transfer_task_id
        globals()['transferEventId'] = transfer_event_id

    # 事件回退
    @list_data(event_fallback_cases)
    def test_event_acceptance_3(self, info):
        global transferTaskId, transferEventId
        url = info['url']
        method = info['method']
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.streetzfb_token)
        headers = json.loads(headers)
        json_data = info['json_data']
        if '#taskid#' in json_data:
            json_data = json_data.replace('#taskid#', str(transferTaskId))
        if '#eventid#' in json_data:
            json_data = json_data.replace('#eventid#', str(transferEventId))
        json_data = json.loads(json_data)
        fallback_event_id = json_data['eventInfoId']
        # demjson3解析不规范的json字符串
        json_data = demjson3.encode(json_data)
        expected = json.loads(info['expected'])
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])
        sql = f"SELECT ID_ FROM act_ru_task where PROC_INST_ID_ in (SELECT process_instance_id FROM event_event_info where id ='{str(fallback_event_id)}')"
        fallback_task_id = self.db.query_one(sql)[0]
        globals()['fallbackTaskId'] = fallback_task_id
        globals()['fallbackEventId'] = fallback_event_id

    # 事件上报上级
    @list_data(event_escalation_cases)
    def test_event_acceptance_4(self, info):
        global fallbackTaskId, fallbackEventId
        url = info['url']
        method = info['method']
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.streetzzzx_token)
        headers = json.loads(headers)
        json_data = info['json_data']
        if '#taskid#' in json_data:
            json_data = json_data.replace('#taskid#', str(fallbackTaskId))
        if '#eventid#' in json_data:
            json_data = json_data.replace('#eventid#', str(fallbackEventId))
        json_data = json.loads(json_data)
        escalation_event_id = json_data['eventInfoId']
        # demjson3解析不规范的json字符串
        json_data = demjson3.encode(json_data)
        expected = json.loads(info['expected'])
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        print(response.text)
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])
        sql = f"SELECT ID_ FROM act_ru_task where PROC_INST_ID_ in (SELECT process_instance_id FROM event_event_info where id ='{str(escalation_event_id)}')"
        escalation_task_id = self.db.query_one(sql)[0]
        globals()['escalationTaskId'] = escalation_task_id
        globals()['escalationEventId'] = escalation_event_id

    # 事件下派
    @list_data(event_downsend_cases)
    def test_event_acceptance_5(self, info):
        global escalationTaskId, escalationEventId
        url = info['url']
        method = info['method']
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.areazzzx_token)
        headers = json.loads(headers)
        json_data = info['json_data']
        if '#taskid#' in json_data:
            json_data = json_data.replace('#taskid#', str(escalationTaskId))
        if '#eventid#' in json_data:
            json_data = json_data.replace('#eventid#', str(escalationEventId))
        json_data = json.loads(json_data)
        downsend_event_id = json_data['eventInfoId']
        # demjson3解析不规范的json字符串
        json_data = demjson3.encode(json_data)
        expected = json.loads(info['expected'])
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])
        sql = f"SELECT ID_ FROM act_ru_task where PROC_INST_ID_ in (SELECT process_instance_id FROM event_event_info where id ='{str(downsend_event_id)}')"
        downsend_task_id = self.db.query_one(sql)[0]
        globals()['downsendTaskId'] = downsend_task_id
        globals()['downsendEventId'] = downsend_event_id

    # 事件办结
    @list_data(event_finish_cases)
    def test_event_acceptance_6(self, info):
        global downsendTaskId, downsendEventId
        url = info['url']
        method = info['method']
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.streetzzzx_token)
        headers = json.loads(headers)
        json_data = info['json_data']
        if '#taskid#' in json_data:
            json_data = json_data.replace('#taskid#', str(downsendTaskId))
        if '#eventid#' in json_data:
            json_data = json_data.replace('#eventid#', str(downsendEventId))
        json_data = json.loads(json_data)
        finish_event_id = json_data['eventInfoId']
        # demjson3解析不规范的json字符串
        json_data = demjson3.encode(json_data)
        expected = json.loads(info['expected'])
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])
        sql = f"SELECT ID_ FROM act_ru_task where PROC_INST_ID_ in (SELECT process_instance_id FROM event_event_info where id ='{str(finish_event_id)}')"
        finish_task_id = self.db.query_one(sql)[0]
        globals()['finishTaskId'] = finish_task_id
        globals()['finishEventId'] = finish_event_id

    # 事件结案
    @list_data(event_close_cases)
    def test_event_acceptance_7(self, info):
        global finishTaskId, finishEventId
        url = info['url']
        method = info['method']
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.grid_token)
        headers = json.loads(headers)
        json_data = info['json_data']
        if '#taskid#' in json_data:
            json_data = json_data.replace('#taskid#', str(finishTaskId))
        if '#eventid#' in json_data:
            json_data = json_data.replace('#eventid#', str(finishEventId))
        json_data = json.loads(json_data)
        # demjson3解析不规范的json字符串
        json_data = demjson3.encode(json_data)
        expected = json.loads(info['expected'])
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])

    # 事件自办结
    @list_data(event_selfclose_cases)
    def test_event_acceptance_8(self, info):
        url = info['url']
        method = info['method']
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.grid_token)
        headers = json.loads(headers)
        json_data = json.loads(info['json_data'])
        # demjson3解析不规范的json字符串
        json_data = demjson3.encode(json_data)
        expected = json.loads(info['expected'])
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])
