import json
import requests
from setting import config
from jsonpath import jsonpath


class APICase:

    @classmethod
    def login_token(cls):
        """步骤：
            1. 准备测试数据
            2. 发送接口请求，得到实际结果
            3. 预期结果和实际结果的断言。
            """
        # 1. 准备测试数据
        url = config.token_host
        method = "post"
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        json_data = r'''{"userName": "yuxy",
                             "password": "21218cca77804d2ba1922c33e0151105",
                             "flag": "4"
                             }'''
        # 2. 发送接口请求，得到实际结果
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        response_body = json.loads(response.text)
        cls.register_token = jsonpath(response_body, '$..accessToken')[0]

    @classmethod
    def user_management_token(cls):
        """步骤：
            1. 准备测试数据
            2. 发送接口请求，得到实际结果
            3. 预期结果和实际结果的断言。
            """
        # 1. 准备测试数据
        url = config.token_host
        method = "post"
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        json_data = r'''{"userName": "ZFHCXJSJ1",
                             "password": "e10adc3949ba59abbe56e057f20f883e",
                             "flag": "4"
                             }'''
        # 2. 发送接口请求，得到实际结果
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        response_body = json.loads(response.text)
        cls.management_token = jsonpath(response_body, '$..accessToken')[0]

    @classmethod
    def user_transfer_token(cls):
        """步骤：
            1. 准备测试数据
            2. 发送接口请求，得到实际结果
            3. 预期结果和实际结果的断言。
            """
        # 1. 准备测试数据
        url = config.token_host
        method = "post"
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        json_data = r'''{"userName": "TTGS01",
                             "password": "e10adc3949ba59abbe56e057f20f883e",
                             "flag": "4"
                             }'''
        # 2. 发送接口请求，得到实际结果
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        response_body = json.loads(response.text)
        cls.transfer_token = jsonpath(response_body, '$..accessToken')[0]

    # 网格员
    @classmethod
    def user_grid_token(cls):
        """步骤：
            1. 准备测试数据
            2. 发送接口请求，得到实际结果
            3. 预期结果和实际结果的断言。
            """
        # 1. 准备测试数据
        url = config.token_host
        method = "post"
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        json_data = r'''{"userName": "YC10400401",
                             "password": "e10adc3949ba59abbe56e057f20f883e",
                             "flag": "6"
                             }'''
        # 2. 发送接口请求，得到实际结果
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        response_body = json.loads(response.text)
        cls.grid_token = jsonpath(response_body, '$..accessToken')[0]

    # 晏城街道执法办
    @classmethod
    def user_streetzfb_token(cls):
        """步骤：
            1. 准备测试数据
            2. 发送接口请求，得到实际结果
            3. 预期结果和实际结果的断言。
            """
        # 1. 准备测试数据
        url = config.token_host
        method = "post"
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        json_data = r'''{"userName": "ycjdzfb01",
                             "password": "e10adc3949ba59abbe56e057f20f883e",
                             "flag": "6"
                             }'''
        # 2. 发送接口请求，得到实际结果
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        response_body = json.loads(response.text)
        cls.streetzfb_token = jsonpath(response_body, '$..accessToken')[0]

    # 晏城街道综治中心
    @classmethod
    def user_streetzzzx_token(cls):
        """步骤：
            1. 准备测试数据
            2. 发送接口请求，得到实际结果
            3. 预期结果和实际结果的断言。
            """
        # 1. 准备测试数据
        url = config.token_host
        method = "post"
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        json_data = r'''{"userName": "YCJ01",
                             "password": "96e79218965eb72c92a549dd5a330112",
                             "flag": "6"
                             }'''
        # 2. 发送接口请求，得到实际结果
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        response_body = json.loads(response.text)
        cls.streetzzzx_token = jsonpath(response_body, '$..accessToken')[0]

    # 区县综治中心
    @classmethod
    def user_areazzzx_token(cls):
        """步骤：
            1. 准备测试数据
            2. 发送接口请求，得到实际结果
            3. 预期结果和实际结果的断言。
            """
        # 1. 准备测试数据
        url = config.token_host
        method = "post"
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        json_data = r'''{"userName": "QHX01",
                             "password": "08aea5306baf9db9323c58547c040338",
                             "flag": "6"
                             }'''
        # 2. 发送接口请求，得到实际结果
        response = requests.request(url=url, method=method, headers=headers, data=json_data)
        response_body = json.loads(response.text)
        cls.areazzzx_token = jsonpath(response_body, '$..accessToken')[0]