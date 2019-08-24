import os
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from framework.runner.beautiful_report import BeautifulReport


class UiAutoTestCase(unittest.TestCase):
    """ 测试报告的基础用例Sample """
    driver = None
    img_path = os.path.join(os.getcwd(), "result", "Screenshots")

    def save_img(self, img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        if not os.path.exists(self.img_path):
            os.mkdir(self.img_path)
        self.driver.get_screenshot_as_file('{}{}{}.png'.format(os.path.abspath(self.img_path), os.sep, img_name))

    @classmethod
    def setUpClass(cls):
        """ set Up method """
        cls.driver = webdriver.Firefox()
        cls.test_page = 'https://cn.bing.com/'

    def tearDown(self):
        """ tear Down method """

    @classmethod
    def tearDownClass(cls):
        """ tear Down method """
        cls.driver.close()

    def test_1_home_page_is_ok(self):
        """
        测试访问首页正常, 并使用title进行断言
        """
        self.driver.get(self.test_page)
        try:
            element = self.driver.find_element(By.LINK_TEXT, "图片")
            self.assertEqual(element.text, "图片")
        except NoSuchElementException as e:
            self.fail(str(e))
            pass


    @BeautifulReport.add_test_img('打开首页', '点击地图')
    def test_2_save_img_and_view(self):
        """
            打开首页, 截图, 在截图后点击第一篇文章连接, 跳转页面完成后再次截图
        """
        self.driver.get(self.test_page)
        self.save_img('打开首页')
        element = self.driver.find_element(By.ID, "scpl4")
        element.click()
        self.save_img('点击地图')
        print('跳转与保存截图完成')
        element = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul[2]/li[1]/a/span')
        self.driver.implicitly_wait(3)
        self.assertEqual(
            element.text,
            '路线'
        )

    @BeautifulReport.add_test_img('test_errors_save_imgs')
    def test_3_errors_save_imgs(self):
        """
            如果在测试过程中, 出现不确定的错误, 程序会自动截图, 并返回失败, 如果你需要程序自动截图, 则需要咋测试类中定义 save_img方法
        """
        self.driver.get(self.test_page)
        try:
            self.driver.find_element_by_xpath('//abc')
            self.assertEqual("OK", "OK")
        except NoSuchElementException as e:
            self.fail(str(e))

    @BeautifulReport.add_test_img('test_success_case_img')
    def test_4_success_case_img(self):
        """
            如果case没有出现错误, 即使使用了错误截图装饰器, 也不会影响case的使用
        """
        self.driver.get(self.test_page)
        try:
            self.driver.find_element_by_xpath('//li/a[@id="scpl3"]')
            self.assertEqual("OK", "OK")
        except NoSuchElementException as e:
            self.fail(str(e))


if __name__ == '__main__':
    unittest.main()
