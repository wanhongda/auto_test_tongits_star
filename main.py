# import pytest, os
# from utils.yaml_control import get_yaml_data_to_main
# from utils import *

# if __name__ == '__main__':
#     # 获取配置文件数据
#     res = get_yaml_data_to_main('./config.yml')
#
#     # print(res)
#     # print(res['runParams'])
#     # print(res['reportParams'])
#     # 报告所在路径及名称
#     reportName = after_operation.build_repott_name()[0]
#     ps_location = after_operation.build_repott_name()[1]
#     # print(reportName)
#     # print(ps_location)
#     # pytest.main(["test002_try_test_api.py", "-s", '--alluredir', '{}/reports/result/'.format(reportName),
#     #              '--clean-alluredir'])  #
#     pytest.main(res['runParams'],'{}/reports/result/'.format(reportName))
#     after_operation.generate_report_to_anywhere(reportName, ps_location)
#     #
