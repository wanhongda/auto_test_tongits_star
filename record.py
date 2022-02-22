"""
各目录含义
1. apis 存放接口信息
2. utils 存放公共方法类
3. logs 存放日志文件
4. data 存放数据驱动文件
5. reports 存放测试报告
6. testcases 存放测试用例
7. tools 存放使用的测试工具
"""

"""
开发里程碑
1. 创建各目录，搭建框架
2. 使用tongits的公告接口尝试运行
3. 编写common公共方法类
4. 集成allure产出测试报告
5. 集成jekins，加入每日轮询与代码监控
"""

"""
2022.02.17
1. 搭建框架
2. 尝试以框架运行简单的测试用例
3. 尝试参数化注入用例
......
"""

"""
2022.02.19
1. pytest.ini配置文件处理命令（未完成）
2. yaml存储用例格式设计（实现50%）
3. 把加解密方式封装成预处理方法
......
下期计划：
1. 接口yaml所在路径，后面可做成配置文件，依据文件目录、命名来设定yaml所在地址与名称
2. yaml数据处理方法批量化，可以在一个yaml文件中写复数条用例

"""


"""
yaml存放测试用例
1. url
2. params
3. 预期结果-响应状态码
4. 用例级别（是否冒烟等）


"""