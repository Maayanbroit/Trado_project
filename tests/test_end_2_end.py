from utilities.setup_with_login_user import WebDriverSetup
from time import sleep


class TestOH(WebDriverSetup):

    def test_04_buy_prod_end2end_N_without_card_info(self):
        self.home_page.click_search()
        self.home_page.search().send_keys('אקדיה')
        self.home_page.click_search()
        self.home_page.search().clear()
        sleep(2)
        self.home_page.search().send_keys('אקדיה')
        self.home_page.click_search()
        self.home_page.click_first_prod_search()
        self.product_page.click_plus()
        self.your_cart_page.click_cart_payment()
        self.payment_page.bussines_name().send_keys('sdajk')
        self.payment_page.entrance().send_keys('6')
        self.payment_page.delivery_entrance().send_keys('6')
        self.payment_page.bn_number().send_keys('324234')
        self.payment_page.delivery_first_name().send_keys('sadbnsda')
        self.payment_page.click_delivery_purchase()
        self.payment_page.click_purchase()
        self.payment_page.click_back_home()


    def test_08_valid_sum_up_in_cart_total(self):
        self.home_page.click_search()
        self.home_page.search().send_keys('אקדיה')
        self.home_page.click_search()
        self.home_page.search().clear()
        sleep(2)
        self.home_page.search().send_keys('אקדיה')
        self.home_page.click_search()
        self.home_page.click_first_prod_search()
        text_product_1 = self.product_page.price().text
        price_product_1 = float(text_product_1.replace('₪', ''))
        self.product_page.click_plus()

        self.home_page.click_search()
        self.home_page.search().send_keys('גורילה גלו')
        self.home_page.click_search()
        self.home_page.search().clear()
        sleep(2)
        self.home_page.search().send_keys('גורילה גלו')
        self.home_page.click_search()
        self.home_page.click_first_prod_search()
        text_product_2 = self.product_page.price().text
        price_product_2 = float(text_product_2.replace('₪', ''))
        self.product_page.click_plus()

        text_total = self.your_cart_page.cart_sum_up_price_in_cart().text
        price_total = float(text_total.replace('₪', ''))

        self.assertEqual(price_product_1 + price_product_2, price_total)
