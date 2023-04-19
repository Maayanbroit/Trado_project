from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.home_locators import Xpath_home
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    def trado_logo(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.trado_logo)))
        return title

    def click_trado_logo(self):
        Homepage.trado_logo(self).click()

    def search(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.search)))
        return title

    def click_search(self):
        Homepage.search(self).click()

    def first_prod_search(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.first_prod_search)))
        return title

    def click_first_prod_search(self):
        Homepage.first_prod_search(self).click()

    def log_in(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.log_in)))
        return title

    def click_log_in(self):
        Homepage.log_in(self).click()

    def upload_new_product(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.upload_new_product)))
        return title

    def click_upload_new_product(self):
        Homepage.upload_new_product(self).click()

    def sort(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.sort)))
        return title

    def click_sort(self):
        Homepage.sort(self).click()

    def product_list(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.product_list)))
        return title

    def click_product_list(self):
        Homepage.product_list(self).click()

    def product_squares(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.product_squares)))
        return title

    def click_product_squares(self):
        Homepage.product_squares(self).click()

    def link_max_ad_more_details(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.sort)))
        return title

    def click_link_max_ad_more_details(self):
        Homepage.link_max_ad_more_details(self).click()

    def link_all_questions(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.link_all_questions)))
        return title

    def click_link_all_questions(self):
        Homepage.link_all_questions(self).click()

    def link_contact_us(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.link_contact_us)))
        return title

    def click_link_contact_us(self):
        Homepage.link_contact_us(self).click()

    def link_more_details(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.link_more_details)))
        return title

    def click_link_more_details(self):
        Homepage.link_more_details(self).click()

    def link_who_we_are(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.link_who_we_are)))
        return title

    def click_link_who_we_are(self):
        Homepage.link_who_we_are(self).click()

    def link_personal_area(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.link_personal_area)))
        return title

    def click_link_personal_area(self):
        Homepage.link_personal_area(self).click()

    def link_etrado(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.link_etrado)))
        return title

    def click_link_etrado(self):
        Homepage.link_etrado(self).click()

    def link_business_interface(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.link_business_interface)))
        return title

    def click_link_business_interface(self):
        Homepage.link_business_interface(self).click()

    def link_common_questions(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.link_common_questions)))
        return title

    def click_link_common_questions(self):
        Homepage.link_common_questions(self).click()

    def link_how_does_shipping_work(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.link_how_does_shipping_work)))
        return title

    def click_link_how_does_shipping_work(self):
        Homepage.link_how_does_shipping_work(self).click()

    def link_payment_solutions(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.link_payment_solutions)))
        return title

    def click_link_payment_solutions(self):
        Homepage.link_payment_solutions(self).click()

    def link_max_for_business(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.link_max_for_business)))
        return title

    def max_for_business_text(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.max_for_business_text)))
        return title

    def click_link_max_for_business(self):
        Homepage.link_max_for_business(self).click()

    def link_facebook(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.link_facebook)))
        return title

    def click_link_facebook(self):
        Homepage.link_facebook(self).click()

    def link_instagram(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.link_instagram)))
        return title

    def click_link_instagram(self):
        Homepage.link_instagram(self).click()

    def link_twitter(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.link_twitter)))
        return title

    def click_link_twitter(self):
        Homepage.link_twitter(self).click()

    def language_changer(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.language_changer)))
        return title

    def click_language_changer(self):
        Homepage.language_changer(self).click()

    def popup_save(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.popup_save)))
        return title

    def click_popup_save(self):
        Homepage.popup_save(self).click()

    def popup_choose(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.popup_choose)))
        return title

    def click_popup_choose(self):
        Homepage.popup_choose(self).click()

    def header_sale(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.sale)))
        return title

    def header_snacks(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.snacks)))
        return title

    def header_cannabis(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.cannabis)))
        return title

    def header_drinks(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.drinks)))
        return title

    def size_of_product(self):
        element = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/a[1]')))
        size = element.size
        print(size)
        return size

    def filter_dropdown_price_high(self):
        drpfilter = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_home.sort)))
        select = Select(drpfilter)
        select.select_by_value('{"price":1}')

    def filter_dropdown_price_low(self):
        drpfilter = WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, Xpath_home.sort)))
        select = Select(drpfilter)
        select.select_by_value('{"price":-1}')


    # def test_sort_by_price(self):
    #     # Find all product elements under the productsList_list class
    #     product_elements = WebDriverWait(self.driver, 5).until(
    #         ec.visibility_of_element_located((By.CSS_SELECTOR, 'productsList_list .product')))
    #     # Create an empty list to store the prices
    #     prices = []
    #     # Loop over the product elements and extract the price
    #     for product_element in product_elements:
    #         # Get the price element
    #         price_element = WebDriverWait(self.driver, 5).until(
    #         ec.visibility_of_element_located((By.CSS_SELECTOR, '.productPrice_price')))
    #         # Extract the price text, which includes the currency symbol
    #         price_text = price_element.text
    #         # Remove the currency symbol and convert to a float
    #         price = float(price_text.replace('₪', ''))
    #         # Add the price to the list
    #         prices.append(price)
    #     # Check that the prices are sorted from low to high
    #     print(prices)
    #     assert prices == sorted(prices), "Product prices are not sorted from low to high"



