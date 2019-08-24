import os
import pytest
import traceback

from framework.util.config import Config
from framework.util.email import Email
from framework.util.log import Log


class PyTestRunner:
    _instance = None

    def __init__(self):
        pass

    @classmethod
    def _get_instance(cls):
        if cls._instance is None:
            cls._instance = PyTestRunner()
        return cls._instance

    @staticmethod
    def run(case_dir=os.path.join(os.getcwd(), "cases_pytest")):
        Log.i("********PYTEST START********")
        fp = None
        try:
            report_dir = Config.get("PYTEST", "report_dir")
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

            report_file = Config.get("PYTEST", "report_file")
            if report_file is None:
                report_file = "pytest_report.html"

            pytest.main(
                ["-q",
                 os.path.abspath(case_dir),
                 "--html",
                 os.path.join(report_dir, report_file),
                 "--self-contained-html"])
        except Exception as ex:
            traceback.print_exc()
        finally:


            Log.i("********PYTEST END**********")


if __name__ == '__main__':
    PyTestRunner.run()
