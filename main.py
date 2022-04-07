import pytest, os
from utils.yaml_control import get_yaml_data_to_main
from utils import *

if __name__ == '__main__':
    # 报告所在路径及名称
    reportName = after_operation.build_report_name()[0]
    ps_location = after_operation.build_report_name()[1]
    # print(reportName)
    # print(ps_location)

    pytest.main(['--alluredir', '{}/reports/result/'.format(reportName), '--clean-alluredir'])
    after_operation.generate_report_local(reportName)
    # after_operation.generate_report_to_anywhere(reportName, ps_location)
