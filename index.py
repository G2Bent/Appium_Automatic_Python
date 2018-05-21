import os,unittest,time
from Report.HTMLTestRunner3 import HTMLTestRunner
import sys
def create_suite():
    TestSuite = unittest.TestSuite()#测试集
    test_dir = os.getcwd()+'\\TestCase\\'

    discover = unittest.defaultTestLoader.discover(
        start_dir=test_dir,
        pattern='Register.py',
        top_level_dir=None
    )

    # print (discover)

    for test_case in discover:
        TestSuite.addTests(test_case)
    return TestSuite

def report():
    if len(sys.argv) > 1:
        report_name = os.getcwd() + '\\Report\\' + sys.argv[1] + '_result.html'
    else:
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        report_name = os.getcwd()+'\\Report\\result.html'
    return report_name


if __name__ == '__main__':
    TestSuite = create_suite()
    fp = open(report(), 'wb')
    Runner = HTMLTestRunner(
        stream=fp,
        title='测试报告',
        description='测试用例执行情况'
    )
    Runner.run(TestSuite)
    fp.close()