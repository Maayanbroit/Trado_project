from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.your_cart_locators import Xpath_cart


class Yourcart:

    def __init__(self, driver):
        self.driver = driver

    def cart_plus(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_cart.plus)))
        return title

    def click_cart_plus(self):
        Yourcart.cart_plus(self).click()

    def cart_minus(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_cart.minus)))
        return title

    def click_cart_minus(self):
        Yourcart.cart_minus(self).click()

    def cart_payment(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_cart.payment)))
        return title

    def click_cart_payment(self):
        Yourcart.cart_payment(self).click()

    def cart_sum_up_price_in_cart(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_cart.cart_sum_up_price_in_cart)))
        return title
