import os
from framework.util.log import Log
from framework.util.xml import Xml
from framework.util.email import Email
from framework.util.config import Config
from framework.runner.unittest_runner import UnitTestRunner
from framework.runner.pytest_runner import PyTestRunner

if __name__ == "__main__":
    Log.d(Xml.get_children_by_attr(os.path.join(os.getcwd(), "config", "api.xml"), "url", "name", "login"))
    UnitTestRunner.run()
    PyTestRunner.run()
    # send test report by email
    email_switch = Config.get("EMAIL", "switch")
    if email_switch == 'on':
        Email.send()
    else:
        Log.i("Do not send report via email")
