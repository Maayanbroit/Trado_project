import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.home_page import Homepage
from pages.product_page import Products
from pages.log_in_page import Loginpage
from pages.your_cart_page import Yourcart
from pages.payment_page import Paymentpage


class WebDriverSetup(unittest.TestCase):
    def setUp(self) -> None:
        try:
            chromedriver_path = "C:/Webdriver/chromedriver.exe"
            service = Service(executable_path=chromedriver_path)
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-extensions")
            self.driver = webdriver.Chrome(service=service,options=options)
            self.driver.maximize_window()
            self.driver.set_page_load_timeout(30)
            self.driver.get("https://qa.trado.co.il/")
            self.home_page = Homepage(self.driver)
            self.product_page = Products(self.driver)
            self.log_in_page = Loginpage(self.driver)
            self.your_cart_page = Yourcart(self.driver)
            self.payment_page = Paymentpage(self.driver)
            self.home_page.click_popup_choose()
            self.home_page.click_popup_save()

        except AssertionError:
            self.driver.quit()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
