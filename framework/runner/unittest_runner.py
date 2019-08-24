import os
import unittest
import traceback
from framework.runner.beautiful_report import BeautifulReport

from framework.util.config import Config
from framework.util.email import Email
from framework.util.log import Log


class UnitTestRunner:
    _instance = None

    def __init__(self):
        pass

    @classmethod
    def _get_instance(cls):
        if cls._instance is None:
            cls._instance = UnitTestRunner()
        return cls._instance

    @staticmethod
    def run(case_dir=os.path.join(os.getcwd(), "cases_unittest"), description='接口测试', pattern='test*.py'):
        Log.i("********UNITTEST START********")
        fp = None
        try:
            report_dir = Config.get("UNITTEST", "report_dir")
            if report_dir is None:
                report_dir = os.path.join(os.getcwd(), "result")
            else:
                if os.path.exists(report_dir) and os.path.isdir(report_dir):
                    try:
                        os.removedirs(report_dir)
                        Log.i("remove dir: " + report_dir)
                    except Exception as e:
                        Log.e("remove failed: " + report_dir + ", exception: " + str(e))
                try:
                    os.mkdir(report_dir)
                except Exception as e:
                    Log.e("mkdir failed: " + report_dir + ", exception: " + str(e))

            report_file = Config.get("UNITTEST", "report_file")
            if report_file is None:
                report_file = "unittest_report.html"

            test_suite_ = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py')
            result_ = BeautifulReport(test_suite_, report_dir)
            result_.report(filename=report_file, description=description)
        except Exception as ex:
            traceback.print_exc()
        finally:
            Log.i("********UNITTEST END**********")


if __name__ == '__main__':
    UnitTestRunner.run()
