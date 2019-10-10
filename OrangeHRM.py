import unittest
from selenium import webdriver
import HtmlTestRunner

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="//Users/adik/Downloads/chromedriver")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        links = self.driver.find_elements_by_tag_name("a")
        print("Number of links present: ", len(links))
        self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
        self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//input[@id='btnLogin']").click()

    def test_search_2(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.save_screenshot("/Users/adik/Desktop/screen/photo.png")
        links = self.driver.find_elements_by_tag_name("a")
        print("Number of links present: ", len(links))
        self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
        self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//input[@id='btnLogin']").click()
        self.driver.find_element_by_xpath("//a[@id='welcome']").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
        links1 = self.driver.find_elements_by_tag_name("a")
        print("Number of links present: ", len(links))
        self.assertEqual(len(links), len(links1))
        self.driver.save_screenshot("/Users/adik/Desktop/screen/photo1.png")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=(HtmlTestRunner.HTMLTestRunner(output="/Users/adik/Desktop",verbosity=2)))

