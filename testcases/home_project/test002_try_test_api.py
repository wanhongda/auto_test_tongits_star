"""
author:wanhongda
time:2022.02.17
function:
    tongits star 公告接口测试
"""
import pytest
import time
import os
import requests
from assertpy import assert_that
import allure

from utils import *


@allure.feature("Tongits Star登录接口")
class Test_study:
    # 接口yaml所在路径，后面可做成配置文件，依据文件目录、命名来设定yaml所在地址与名称
    data_path = os.path.dirname(os.path.dirname((os.path.dirname(__file__))))
    file_name_cases = "{}/data/home_project/cases/test002_try_test_api.yaml".format(data_path)
    # file_name_apis = "{}/data/home_project/csses/test002_try_test_api.yaml".format(data_path)

    # 处理用例数据
    data = yaml_control.get_yaml_data(file_name_cases)
    # url = yaml_control.get_one_yaml_data(file_name_apis)
    print("-----------------------------", data, "*****************************")
    """
    data:
    [('https://itest.tongitsstar.com/data/handleMsg.do', 8201, 0), ('https://itest.tongitsstar.com/data/handleMsg.do', '-0x1001 -0 -"" -auth_register_test', 0)]
    """

    # 参数化处理测试用例，发送请求
    @allure.story("测试用例")
    @allure.title("测试用例001")
    @allure.description("尝试用allure生成美观的测试报告")
    @pytest.mark.parametrize("url,params,status", data)
    def test_run_simple(self, url, params, status):
        # 加个判断 判断是否有数组、字典
        # 预处理用例信息
        print("--------------url-----------------", url)
        print("--------------params-----------------", params)
        print("--------------status-----------------", status)
        body = pre_build_data.pre_build(params)
        print("--------------------------------", body)
        res = requests.get(url=url, params=body)
        response_tracker = ByteTracker.ByteTracker("little")
        # 读取响应数据
        # print("res.text2",res.text)
        response_tracker.load(res.text)
        # print("响应内容解析后为：",response_tracker.load(res.text))
        # 获取响应的status
        response_status = response_tracker.get_int()
        print("登录请求的response_status:", response_status)
        assert_that(response_status).is_equal_to(status)
        if response_status == status:
            print("登录请求响应成功！")


if __name__ == '__main__':
    # 报告所在路径及名称
    reportName = after_operation.build_report_name()[0]
    ps_location = after_operation.build_report_name()[1]
    print(ps_location)
    pytest.main(["test002_try_test_api.py", '--alluredir', '{}/reports/result/'.format(reportName),
                 '--clean-alluredir'])  #
    after_operation.generate_report_to_anywhere(reportName, ps_location)
