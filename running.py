import unittest
import unittestreport

# 收集用例
suite = unittest.defaultTestLoader.discover('cases')
# 运行用例
# 写法一：
# runner = unittest.TextTestRunner()
# runner.run(suite)

# 写法二：
runner = unittestreport.TestRunner(suite,
                                   report_dir="./reports",
                                   title='齐河项目测试报告',
                                   tester='测试员',
                                   desc="齐河项目测试生成的报告",
                                   templates=2)
runner.run()
