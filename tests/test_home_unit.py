from utilities.setup_with_login_user import WebDriverSetup
from time import sleep


class TestOH(WebDriverSetup):

    def test_01_valid_logo_is_valid_home_btn(self):
        self.home_page.click_trado_logo()
        #Check if the current URL is correct
        assert self.driver.current_url == "https://qa.trado.co.il/"

    def test_02_link_all_questions_sidebar_valid(self):
        self.home_page.click_link_all_questions()
        assert self.driver.current_url == "https://qa.trado.co.il/questions"

    def test_03_link_contact_us_valid(self):
        self.home_page.click_link_contact_us()
        assert self.driver.current_url == "https://qa.trado.co.il/contact"

    def test_04_link_more_details(self):
        self.home_page.click_link_more_details()
        assert self.driver.current_url == "https://qa.trado.co.il/shipment"

    def test_05_link_who_we_are(self):
        self.home_page.click.link_who_we_are()
        assert self.driver.current_url == "https://www.trado.co.il/page"

    def test_06_link_personal_area(self):
        self.home_page.click_link_personal_area()
        assert self.driver.current_url == "https://qa.trado.co.il/user/personalArea"

    def test_07_link_etrado(self):
        self.home_page.click_link_etrado()
        assert self.driver.current_url == "https://qa.trado.co.il/etrado"

    def test_08_link_business_interface(self):
        self.home_page.click_link_business_interface()
        assert self.driver.current_url == "https://qa.trado.co.il/joinUs"

    def test_09_link_link_payment_solutions(self):
        self.home_page.click_link_payment_solutions()
        assert self.driver.current_url == "https://www.max.co.il/cards/card/8649"

    def test_10_link_max_for_business(self):
        self.home_page.click_link_max_for_business()
        assert self.driver.current_url == "https://www.max.co.il/cards/card/8649"

    def test_11_link_facebook(self):
        self.home_page.click_link_facebook()
        assert self.driver.current_url == "https://www.facebook.com/trado"

    def test_12_link_instagram(self):
        self.home_page.click_link_instagram()
        assert self.driver.current_url == "https://www.instagram.com/trado"

    def test_13_link_twitter(self):
        self.home_page.click_link_twitter()
        assert self.driver.current_url == "https://www.twitter.com/trado"

    def test_14_search_valid_product(self):
        self.home_page.click_search()
        self.home_page.search().send_keys('אקדיה')
        self.home_page.click_search()
        result = self.home_page.click_first_prod_search()
        assert result.text == 'אקדיה'
        self.home_page.click_first_prod_search()
        result = self.product_page.name()
        assert result.text == 'אקדיה'

    def test_15_search_valid_product(self):
        self.home_page.click_search()
        self.home_page.search().send_keys('אקדיה')
        self.home_page.click_search()
        self.home_page.search().clear()
        sleep(2)
        self.home_page.search().send_keys('אקדיה')
        self.home_page.click_search()
        self.home_page.click_first_prod_search()
        result = self.product_page.name()
        assert result.text == 'אקדיה'

    def test_16_sort_by_change_size_of_prod_view(self):
        self.home_page.click_product_list()
        size_list = self.home_page.size_of_product()
        self.home_page.click_product_squares()
        size_squares = self.home_page.size_of_product()
        self.assertNotEqual(size_list, size_squares)

    def test_17_Max_ad_more_details(self):
        element = self.home_page.link_max_ad_more_details()
        link = element.get_attribute("href")
        self.assertEqual(link, 'https://www.max.co.il/cards/card/8649/')

    # def test_18_valid_sort_by_price_high(self):
    #     self.home_page.click_sort()
    #     self.home_page.filter_dropdown_price_high()
    #     self.home_page.click_product_list()
    #     self.home_page.test_sort_by_price()

    def test_19_language_changer_valid(self):
        text1 = self.home_page.header_cannabis().text
        text2 = self.home_page.header_sale().text
        text3 = self.home_page.header_snacks().text
        text4 = self.home_page.header_drinks().text
        list_bc = [text1,text2,text3,text4]
        self.home_page.click_language_changer()
        text1_ac = self.home_page.header_cannabis().text
        text2_ac = self.home_page.header_sale().text
        text3_ac = self.home_page.header_snacks().text
        text4_ac = self.home_page.header_drinks().text
        list_ac = [text1_ac,text2_ac,text3_ac,text4_ac]
        self.assertNotEqual(list_ac,list_bc)







