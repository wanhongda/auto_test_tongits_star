import os
import time


def build_repott_name():
    temp = []
    reportName = os.path.dirname((os.path.dirname(__file__)))
    # print(reportName)
    # report目录，需要再此目录下打开powershell，输入anywhere，转发报告内容
    ps_location = '{}\\reports\\report'.format(reportName)
    temp.append(reportName)
    temp.append(ps_location)
    return temp


def generate_report_local(reportName, ps_location):
    # print(reportName)
    os.system("allure generate {}/reports/result/ -o {}/reports/report/ --clean".format(reportName, reportName))
    # 运行完后自动打开报告 与anywhere自动打开报告冲突
    os.system("allure open -h 127.0.0.1 -p 8883 {}/reports/report/".format(reportName))
    print("***执行完成，输出报告***")


def generate_report_to_anywhere(reportName, ps_location):
    # print(reportName)
    os.system("allure generate {}/reports/result/ -o {}/reports/report/ --clean".format(reportName, reportName))
    # 切换到指定路径下
    os.chdir(ps_location)
    # print(ps_location)
    # 执行完成，自动打开报告，以本机作为服务端，可直接发送   本机ip地址:8000  指定链接供别人查看报告，使用此命令前提是装好node.js
    os.system("anywhere")


if __name__ == '__main__':
    build_repott_name()
