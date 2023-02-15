import json
import unittest
import demjson3
import requests
from loguru import logger
from unittestreport import ddt, list_data
from cases.token_common import APICase
from common.db_operation import DBHandler
from common.execl import read_excel
from setting import config

building_cases = read_excel(file=config.case_file, sheet_name='basic_building')
population_basic_cases = read_excel(file=config.case_file, sheet_name='population_basic_add')
building_operation_cases = read_excel(file=config.case_file, sheet_name='basic_building_operation')


@ddt
class TestBasicBuilding(unittest.TestCase, APICase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login_token()

    def setUp(self) -> None:
        """数据库连接"""
        self.db = DBHandler()

    def tearDown(self) -> None:
        """数据库断开"""
        self.db.close()

    @list_data(building_cases)
    def test_basic_building_1(self, info):
        url = info['url']
        method = info['method']
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.register_token)
        headers = json.loads(headers)
        json_data = json.loads(info['json_data'])
        new_house_name = json_data['houseName']
        # demjson3解析不规范的json字符串
        json_data = demjson3.encode(json_data)
        logger.info(json_data)
        expected = json.loads(info['expected'])
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])
        sql = f"select id,specific_address,pos_x,pos_y from element_basic_house where house_name='{str(new_house_name)}'"
        new_id = self.db.query_one(sql)[0]
        new_specific_address = self.db.query_one(sql)[1]
        new_pos_x = self.db.query_one(sql)[2]
        new_pos_y = self.db.query_one(sql)[3]
        globals()['houseId'] = new_id
        globals()['newSpecificAddress'] = new_specific_address
        globals()['newPosX'] = new_pos_x
        globals()['newPosY'] = new_pos_y

    @list_data(population_basic_cases)
    def test_basic_building_2(self, info):
        global houseId, newSpecificAddress, newPosX, newPosY
        url = info['url']
        method = info['method']
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.register_token)
        headers = json.loads(headers)
        json_data = info['json_data']
        if'#id#' in json_data:
            json_data = json_data.replace('#id#', str(houseId))
        if '#specific_address#' in json_data:
            json_data = json_data.replace('#specific_address#', str(newSpecificAddress))
        if '#pos_x#' in json_data:
            json_data = json_data.replace('#pos_x#', str(newPosX))
        if '#pos_y#' in json_data:
            json_data = json_data.replace('#pos_y#', str(newPosY))
        json_data = json.loads(json_data)
        # demjson3解析不规范的json字符串
        json_data = demjson3.encode(json_data)
        logger.info(json_data)
        expected = json.loads(info['expected'])
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        actual = response.json()
        globals()['userId'] = actual['data']
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])

    @list_data(building_operation_cases)
    def test_basic_building_3(self, info):
        global houseId, userId, newSpecificAddress, newPosX, newPosY
        url = info['url']
        if '#houseid#' in url:
            url = url.replace('#houseid#', str(houseId))
        elif '#userid#' in url:
            url = url.replace('#userid#', str(userId))
        method = info['method']
        headers = info['headers']
        # 替换请求头的token
        if '#token#' in headers:
            headers = headers.replace('#token#', self.register_token)
        headers = json.loads(headers)
        json_data = info['json_data']
        if '#specific_address#' in json_data:
            json_data = json_data.replace('#specific_address#', str(newSpecificAddress))
        if '#pos_x#' in json_data:
            json_data = json_data.replace('#pos_x#', str(newPosX))
        if '#pos_y#' in json_data:
            json_data = json_data.replace('#pos_y#', str(newPosY))
        json_data = json.loads(json_data)
        # demjson3解析不规范的json字符串
        json_data = demjson3.encode(json_data)
        logger.info(json_data)
        expected = json.loads(info['expected'])
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        actual = response.json()
        # 3. 预期结果和实际结果的断言。
        for key, value in expected.items():
            self.assertEqual(value, actual[key])
