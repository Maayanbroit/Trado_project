from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.log_in_locators import Xpath_log_in
from utilities import mongoscrape


class Loginpage:

    def __init__(self, driver):
        self.driver = driver

    def log_in_option(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_log_in.log_in_option)))
        return title

    def click_log_in_option(self):
        Loginpage.log_in_option(self).click()

    def log_in_facebook(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_log_in.log_in_facebook)))
        return title

    def click_log_in_facebook(self):
        Loginpage.log_in_facebook(self).click()

    def log_in_google(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_log_in.log_in_google)))
        return title

    def click_log_in_google(self):
        Loginpage.log_in_google(self).click()

    def log_in_twitter(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_log_in.log_in_twitter)))
        return title

    def click_log_in_twitter(self):
        Loginpage.log_in_twitter(self).click()

    def input_cell_phone_number(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_log_in.input_cell_phone_number)))
        return title

    def click_input_cell_phone_number(self):
        Loginpage.input_cell_phone_number(self).click()

    def checkbox_remember_me(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_log_in.checkbox_remember_me)))
        return title

    def click_checkbox_remember_me(self):
        Loginpage.checkbox_remember_me(self).click()

    def log_in_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_log_in.log_in_btn)))
        return title

    def click_log_in_btn(self):
        Loginpage.log_in_btn(self).click()

    def register_option(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_log_in.register_option)))
        return title

    def click_register_option(self):
        Loginpage.register_option(self).click()

    def input_business_number(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_log_in.input_business_number)))
        return title

    def click_input_business_number(self):
        Loginpage.input_business_number(self).click()

    def form_submit_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_log_in.form_submit_btn)))
        return title

    def click_form_submit_btn(self):
        Loginpage.form_submit_btn(self).click()


    def re_send_sms(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_log_in.re_send_sms)))
        return title

    def click_re_send_sms(self):
        Loginpage.re_send_sms(self).click()




