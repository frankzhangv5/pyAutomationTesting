import os
import sys
import logging
from datetime import datetime


class Log:
    _instance = None
    _console_print = True

    def __init__(self, log_dir=os.path.join(os.getcwd(), "result"), log_level=logging.DEBUG):
        if os.path.exists(log_dir):
            try:
                os.removedirs(log_dir)
            except Exception as e:
                pass

        try:
            os.mkdir(log_dir)
        except Exception as e:
            pass

        log_path = os.path.join(log_dir, "log_" + str(datetime.now().strftime("%Y%m%d_%H%M%S")) + ".txt")

        self.logger = logging.getLogger()
        self.logger.setLevel(log_level)

        # defined handler
        handler = logging.FileHandler(log_path)
        # defined formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)-8s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self._print_level_log('INFO', "log path: " + log_path)

    def _print_level_log(self, level, msg):
        print_func = None
        if level == 'DEBUG':
            print_func = self.logger.debug
        elif level == 'INFO':
            print_func = self.logger.info
        elif level == 'ERROR':
            print_func = self.logger.error
        else:
            print_func = self.logger.debug

        module_name = os.path.basename(sys._getframe().f_back.f_back.f_code.co_filename)
        func_name = os.path.basename(sys._getframe().f_back.f_back.f_code.co_name)
        line_num = sys._getframe().f_back.f_back.f_lineno

        if func_name == '<module>':
            func_name = '__main__'

        if print_func is not None:
            print_func("%-10s(%-10s:%d): %s" % (module_name, func_name, line_num, msg))

        if Log._console_print:
            print("%s - %-5s - %-10s(%-10s:%d): %s" % (str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")), level,
                                                       str(module_name), func_name, line_num, str(msg)))

    def _print_action_log(self, action, msg):
        self._print_level_log('INFO', "[%-5s] -> [%s]" % (action, msg))

    @classmethod
    def _get_instance(cls):
        if cls._instance is None:
            cls._instance = Log()
        return cls._instance

    @classmethod
    def enter(cls, msg):
        cls._get_instance()._print_action_log('enter', msg)

    @classmethod
    def exit(cls, msg):
        cls._get_instance()._print_action_log('exit', msg)

    @classmethod
    def d(cls, msg):
        cls._get_instance()._print_level_log('DEBUG', msg)

    @classmethod
    def i(cls, msg):
        cls._get_instance()._print_level_log('INFO', msg)

    @classmethod
    def e(cls, msg):
        cls._get_instance()._print_level_log('ERROR', msg)


if __name__ == "__main__":
    Log.d("debug level message")
    Log.i("info level message")
    Log.e("error level message")
    Log.enter("test")
    Log.exit("test")
