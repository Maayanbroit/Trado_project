from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.products_locators import Xpath_products


class Products:

    def __init__(self, driver):
        self.driver = driver

    def name(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_products.name)))
        return title

    def click_name(self):
        Products.name(self).click()


    def price(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_products.price)))
        return title

    def click_price(self):
        Products.price(self).click()


    def minus(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_products.minus)))
        return title

    def click_minus(self):
        Products.minus(self).click()


    def amount_counter(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_products.amount_counter)))
        return title

    def click_amount_counter(self):
        Products.amount_counter(self).click()


    def plus(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_products.plus)))
        return title

    def click_plus(self):
        Products.plus(self).click()

