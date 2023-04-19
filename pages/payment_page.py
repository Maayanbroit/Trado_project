from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.payment_locators import Xpath_payment
from locators.payment_locators import Xpath_delivery
from locators.payment_locators import Xpath_my_wallet

class Paymentpage:

    def __init__(self, driver):
        self.driver = driver

    def bussines_name(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_payment.bussines_name)))
        return title

    def click_bussines_name(self):
        Paymentpage.bussines_name(self).click()

    def bn_number(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_payment.bn_number)))
        return title

    def click_bn_number(self):
        Paymentpage.bn_number(self).click()

    def email(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_payment.email)))
        return title

    def click_email(self):
        Paymentpage.email(self).click()

    def city(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_payment.city)))
        return title

    def click_city(self):
        Paymentpage.city(self).click()

    def street(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_payment.street)))
        return title

    def click_street(self):
        Paymentpage.street(self).click()

    def number(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_payment.number)))
        return title

    def click_number(self):
        Paymentpage.number(self).click()

    def entrance(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_payment.entrance)))
        return title

    def click_entrance(self):
        Paymentpage.entrance(self).click()

    def floor(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_payment.floor)))
        return title

    def click_floor(self):
        Paymentpage.entrance(self).click()

    def delivery_city(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_delivery.city)))
        return title

    def click_delivery_city(self):
        Paymentpage.city(self).click()

    def delivery_street(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_delivery.street)))
        return title

    def click_delivery_street(self):
        Paymentpage.city(self).click()

    def delivery_number(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_delivery.number)))
        return title

    def click_delivery_number(self):
        Paymentpage.number(self).click()

    def delivery_entrance(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_delivery.entrance)))
        return title

    def click_delivery_entrance(self):
        Paymentpage.entrance(self).click()

    def delivery_floor(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_delivery.floor)))
        return title

    def click_delivery_floor(self):
        Paymentpage.floor(self).click()

    def delivery_contact(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_delivery.contact)))
        return title

    def click_delivery_contact(self):
        Paymentpage.delivery_contact(self).click()

    def delivery_first_name(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_delivery.first_name)))
        return title

    def click_delivery_first_name(self):
        Paymentpage.delivery_first_name(self).click()

    def delivery_last_name(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_delivery.last_name)))
        return title

    def click_delivery_last_name(self):
        Paymentpage.delivery_last_name(self).click()

    def delivery_cellphone(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_delivery.cellphone)))
        return title

    def click_delivery_cellphone(self):
        Paymentpage.delivery_cellphone(self).click()

    def delivery_purchase(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_delivery.purchase)))
        return title

    def click_delivery_purchase(self):
        Paymentpage.delivery_purchase(self).click()

    def new_card(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_my_wallet.new_card)))
        return title

    def click_new_card(self):
        Paymentpage.new_card(self).click()

    def card_number(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_my_wallet.card_number)))
        return title

    def click_card_number(self):
        Paymentpage.new_card(self).click()

    def id(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_my_wallet.id)))
        return title

    def click_id(self):
        Paymentpage.id(self).click()


    def month(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_my_wallet.month)))
        return title

    def click_month(self):
        Paymentpage.month(self).click()


    def year(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_my_wallet.year)))
        return title

    def click_year(self):
        Paymentpage.year(self).click()

    def cvv(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_my_wallet.cvv)))
        return title

    def click_cvv(self):
        Paymentpage.cvv(self).click()

    def purchase(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_my_wallet.purchase)))
        return title

    def click_purchase(self):
        Paymentpage.purchase(self).click()

    def back_home(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_my_wallet.back_home)))
        return title

    def click_back_home(self):
        Paymentpage.back_home(self).click()

    def v_icon(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_my_wallet.v_icon)))
        return title