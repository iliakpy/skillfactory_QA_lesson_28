import re
import time

import pytest
from selenium.common.exceptions import ElementClickInterceptedException

from base.selenium_base import Base


@pytest.mark.usefixtures('setup')
class TestWebUi:

    def test_home_page(self):
        """Get name of director from main page and check what this name equal necessary"""
        test_object = Base(driver=self.driver)
        director_name = test_object.is_visible('class_name', 'middle-navigation__director-name').text.lower()
        assert director_name == 'fedor savchuk'

    def test_main_categories(self):
        """Test number of main categories on main page"""
        test_object = Base(driver=self.driver)
        assert 3 == len(test_object.are_visible('class_name', 'top-category-slider__item'))

    def test_naming_of_main_categories(self):
        """Get all buttons of main category and check text content"""
        test_object = Base(driver=self.driver)
        naming_of_categories = ['ninebot kickscooter', 'ninebot gokart', 'accessories']
        buttons = test_object.are_visible('class_name', 'top-category-slider__item')
        for i in range(len(buttons)):
            assert buttons[i].text.lower() == naming_of_categories[i]

    def test_categories_in_head(self):
        """Check number of categories in head of main page"""
        test_object = Base(driver=self.driver)
        assert 4 == len(test_object.are_visible('class_name', 'top-nav__item'))

    def test_naming_categories_in_head(self):
        """Check naming of categories in head of main page"""
        test_object = Base(driver=self.driver)
        naming_of_categories = ['catalog', 'shipping and payment', 'wholesale', 'contacts']
        buttons = test_object.are_visible('class_name', 'top-nav__item')
        for i in range(len(buttons)):
            assert buttons[i].text.lower() == naming_of_categories[i]

    def test_shopping_cart(self):
        """Click on shopping cart and check title of pop up window"""
        test_object = Base(driver=self.driver)
        test_object.is_visible('xpath', '//*[@id="__next"]/div[1]/div/div[1]/button/div/span/img').click()
        title = test_object.is_visible('class_name', 'product-modal__top-title').text.lower()
        assert title == 'added to cart'

    def test_tabs_info_about_company(self):
        """Check number of buttons with info about company"""
        test_object = Base(driver=self.driver)
        assert 4 == len(test_object.are_visible('class_name', 'tabs__tab'))

    def test_naming_tabs_info_about_company(self):
        """Check naming of buttons with info about company"""
        test_object = Base(driver=self.driver)
        naming_of_buttons = ['deliverywithin1businessday', 'basic1yearwarranty', 'aftersalessupport', 'appcontroll']
        buttons = test_object.are_visible('class_name', 'tabs__tab-text')
        for i in range(len(buttons)):
            assert re.sub(r'[\n ]', '', buttons[i].text.lower()) == naming_of_buttons[i]

    def test_click_on_tabs_with_info_about_company(self):
        """Click on buttons with info about company"""
        test_object = Base(driver=self.driver)
        self.driver.execute_script(f"window.scrollTo(0, {2200})")
        time.sleep(0.5)
        buttons = test_object.are_present('class_name', 'tabs__tab')
        for button in buttons:
            button.click()

    def test_icons_with_social_network_links(self):
        """Check number of icons with social network links"""
        test_object = Base(driver=self.driver)
        assert 4 == len(test_object.are_visible('class_name', 'footer__socials-link'))

    def test_addresses_of_social_networks(self):
        """Check addresses from href of icons social network"""
        test_object = Base(driver=self.driver)
        items = test_object.are_visible('class_name', 'footer__socials-link')
        for i in range(len(items)):
            assert items[i].get_attribute('href') == 'https://segway.vercel.app/'

    def test_items_in_end_of_page(self):
        """Check text content categories in end of page"""
        test_object = Base(driver=self.driver)
        naming = ['social media', 'about us', 'contact us']
        items = test_object.are_visible('class_name', 'footer__columns-item-title')
        for i in range(len(items)):
            assert items[i].text.lower() == naming[i]

    def test_number_of_links_in_category(self):
        """Check number of links in end of page from category 'About as'"""
        test_object = Base(driver=self.driver)
        assert 6 == len(test_object.are_visible('class_name', 'footer__website-links-item'))

    def test_naming_of_links_in_category(self):
        """Check naming of links in end of page from category 'About as'"""
        test_object = Base(driver=self.driver)
        naming = ['catalog', 'shipping and payment', 'wholesale', 'contacts', 'terms and conditions', 'privacy policy']
        elements = test_object.are_visible('class_name', 'footer__website-links-item')
        for i in range(len(elements)):
            assert elements[i].text.lower() == naming[i]

    def test_addresses_of_links_in_category(self):
        """Check addresses of links in end of page from category 'About as'"""
        test_object = Base(driver=self.driver)
        address = ['', 'shipping-and-payment', 'wholesale', 'contacts', 'terms-and-conditions', 'privacy-policy']
        elements = test_object.are_visible('class_name', 'footer__website-links-item')
        for i in range(len(elements)):
            assert elements[i].get_attribute('href') == 'https://segway.vercel.app/' + address[i]

    def test_number_of_cards_in_first_category(self):
        """Check number cards in first category 'KICKSCOOTER'"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        assert 18 == len(test_object.are_visible('class_name', 'category-slider__img-with-content'))

    def test_number_of_cards_in_second_category(self):
        """Check number cards in second category 'GOKARTS'"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[1].click()
        assert 2 == len(test_object.are_visible('class_name', 'category-slider__img-with-content'))

    def test_number_of_cards_in_third_category(self):
        """Check number cards in third category 'ACCESSORIES'"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[2].click()
        assert 9 == len(test_object.are_visible('class_name', 'accessories-block__img-wrapper'))

    def test_addresses_of_cards_in_first_category(self):
        """Check all cards links"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        elements = test_object.are_visible('class_name', 'category-slider__overlay-link')
        links = [element.get_attribute('href') for element in elements]
        domains = [
            'kickscooter-max',
            'kickscooter-e-22',
            'kickscooter-e-45',
            'kickscooter-f30',
            'kickscooter-zing-e8-pink',
            'kickscooter-zing-c8',
            'kickscooter-e-25a',
            'kickscooter-p65',
            'kickscooter-p100',
            'kickscooter-gt2',
            'kickscooter-es-4',
            'kickscooter-zing-e12',
            'kickscooter-air-t15',
            'kickscooter-es-2',
            'kickscooter-es-3',
            'kickscooter-es-1l',
            'kickscooter-zing-e10',
            'kickscooter-gt1'
        ]
        addresses = ['https://segway.vercel.app/kickscooters/' + domain for domain in domains]
        assert links == addresses

    def test_addresses_of_cards_in_second_category(self):
        """Check all cards links"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[1].click()
        elements = test_object.are_visible('class_name', 'category-slider__overlay-link')
        links = [element.get_attribute('href') for element in elements]
        domains = [
            'gokart-pro',
            'gokart-kit'
        ]
        addresses = ['https://segway.vercel.app/gokarts/' + domain for domain in domains]
        assert links == addresses

    def test_colors_in_first_category(self):
        """Check colors buttons in first category"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        test_object.is_visible('class_name', 'category-slider__overlay-link').click()
        colors = test_object.are_present('class_name', 'form-colors__item-link')[:2]
        link = ''
        for color in colors:
            color.click()
            self.driver.implicitly_wait(5)
            assert link != self.driver.current_url
            link = self.driver.current_url

    def test_extended_warranty_in_first_category(self):
        """Click all warranty buttons and check what price changed"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        test_object.is_visible('class_name', 'category-slider__overlay-link').click()
        buttons = test_object.are_visible('class_name', 'form-with-warrancy__form-button')[:3]
        price = test_object.is_visible('class_name', 'form-with-warrancy__form-price-new').text
        for button in buttons:
            time.sleep(0.2)
            button.click()
            time.sleep(0.2)
            assert price != test_object.is_visible('class_name', 'form-with-warrancy__form-price-new').text
            price = test_object.is_visible('class_name', 'form-with-warrancy__form-price-new').text

    def test_calculation_extended_warranty_in_first_category(self):
        """Take from warranty button price and check value on which price was changed"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        test_object.is_visible('class_name', 'category-slider__overlay-link').click()
        # get all buttons and prices from the buttons
        buttons = test_object.are_visible('class_name', 'form-with-warrancy__form-button')[:3]
        elements_of_prices = test_object.are_visible('class_name', 'form-with-warrancy__form-button-price')[:3]
        text_prices = [float(re.sub(r'[$]', '', price.text)) for price in elements_of_prices]
        price = test_object.is_visible('class_name', 'form-with-warrancy__form-price-new').text
        for i in range(len(buttons)):
            time.sleep(0.2)
            buttons[i].click()
            time.sleep(0.2)
            # check calculation of price
            new_price = test_object.is_visible('class_name', 'form-with-warrancy__form-price-new').text
            assert float(re.sub(r'[$]', '', price)) + text_prices[i] == float(re.sub(r'[$]', '', new_price))

    def test_button_by_it_now_in_first_category(self):
        """Click on buttons 'by it now' and check new url"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        test_object.is_visible('class_name', 'category-slider__overlay-link').click()
        self.driver.execute_script(f"window.scrollTo(0, {300})")
        time.sleep(0.5)
        # click on button 'by it now'
        test_object.is_visible('class_name', 'form-with-warrancy__form-action').click()
        assert 'https://segway.vercel.app/payment' == self.driver.current_url

    def test_button_add_to_card_in_first_category(self):
        """Click on buttons 'add to card' and check new url"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        test_object.is_visible('class_name', 'category-slider__overlay-link').click()
        self.driver.execute_script(f"window.scrollTo(0, {300})")
        time.sleep(0.5)
        # click on button 'add to card'
        test_object.are_visible('class_name', 'form-with-warrancy__form-action')[1].click()
        title_of_shopping_cart = test_object.is_visible('class_name', 'product-modal__top-title').text
        assert 'added to cart' == title_of_shopping_cart.lower()

    def test_button_plus_in_first_card_of_first_category(self):
        """Click on button + in shop cart"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        test_object.is_visible('class_name', 'category-slider__overlay-link').click()
        self.driver.execute_script(f"window.scrollTo(0, {300})")
        time.sleep(1)
        # click on button 'add to card'
        test_object.are_visible('class_name', 'form-with-warrancy__form-action')[1].click()
        # get price before
        price = float(re.sub(r'[ $]', '', test_object.is_visible('class_name', 'product-modal__summ-total').text))

        for number_of in range(2, 10):
            # click on + button and check new price
            test_object.is_visible('class_name', 'products__product-count-plus').click()
            # delete from string unnecessary characters
            new_price = re.sub(r'[ $]', '', test_object.is_visible('class_name', 'product-modal__summ-total').text)
            new_price = float(new_price)
            assert int(price * number_of) == int(new_price)

    def test_button_minus_in_first_card_of_first_category(self):
        """Click on button - in shop cart and check price"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        test_object.is_present('class_name', 'category-slider__overlay-link').click()
        self.driver.execute_script(f"window.scrollTo(0, {300})")
        time.sleep(0.5)
        # click on button 'add to card'
        test_object.are_visible('class_name', 'form-with-warrancy__form-action')[1].click()
        # get price before
        price = test_object.is_visible('class_name', 'product-modal__summ-total').text
        # click on - button and check new price
        test_object.is_visible('class_name', 'products__product-count-minus').click()
        assert price != test_object.is_visible('class_name', 'product-modal__summ-total').text

    def test_clear_button_in_first_card_of_first_category(self):
        """Click on clear button in shop cart and check new price"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        test_object.is_visible('class_name', 'category-slider__overlay-link').click()
        self.driver.execute_script(f"window.scrollTo(0, {300})")
        time.sleep(0.5)
        # click on button 'add to card'
        test_object.are_visible('class_name', 'form-with-warrancy__form-action')[1].click()
        # get price before
        price = test_object.is_visible('class_name', 'product-modal__summ-total').text
        # click on 'clear cart' button and check new price
        test_object.is_visible('class_name', 'product-modal__clear').click()
        assert price != test_object.is_visible('class_name', 'product-modal__summ-total').text

    def test_extend_buttons_in_first_card_of_first_category(self):
        """Click on extend buttons and check changing of price"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        test_object.is_visible('class_name', 'category-slider__overlay-link').click()
        self.driver.execute_script(f"window.scrollTo(0, {300})")
        time.sleep(0.5)
        # click on button 'add to card'
        test_object.are_visible('class_name', 'form-with-warrancy__form-action')[1].click()
        # get price before
        price = test_object.is_visible('class_name', 'product-modal__summ-total').text
        test_object.is_visible('class_name', 'products__product-warrancy').click()

        assert price != test_object.is_visible('class_name', 'product-modal__summ-total').text

    def test_hide_order_summary_in_first_category(self):
        """Click on 'hide_order_summary' in shop cart and check info"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        test_object.is_visible('class_name', 'category-slider__overlay-link').click()
        self.driver.execute_script(f"window.scrollTo(0, {300})")
        time.sleep(1)
        # click on button 'add to card'
        test_object.are_visible('class_name', 'form-with-warrancy__form-action')[1].click()
        # click on 'hide order summary'
        test_object.is_visible('class_name', 'product-modal__summ-title').click()
        assert test_object.is_not_present('class_name', 'inline-flex-center products__product-count-plus')

    def test_bonus_price_in_shop_cart(self):
        """Click on button 'check out' and check changing of url"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        test_object.is_present('class_name', 'category-slider__overlay-link').click()
        self.driver.execute_script(f"window.scrollTo(0, {300})")
        time.sleep(0.5)
        # click on button 'add to card'
        test_object.are_visible('class_name', 'form-with-warrancy__form-action')[1].click()
        assert '1 x $0' == test_object.are_visible('class_name', 'products__product-price')[1].text

    def test_back_button_in_shop_cart(self):
        """Click on button 'cross' and check access to not existing element representation"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        test_object.is_visible('class_name', 'category-slider__overlay-link').click()
        self.driver.execute_script(f"window.scrollTo(0, {300})")
        time.sleep(0.5)
        # click on button 'add to card'
        test_object.are_visible('class_name', 'form-with-warrancy__form-action')[1].click()
        # click on button 'cross'
        test_object.is_visible('xpath', '//*[@id="__next"]/div[29]/div/button/div/span/img').click()
        assert test_object.is_not_present('class_name', 'product-modal__top-title')

    def test_logo_click(self):
        """Click on logo and check what logo back to main page"""
        test_object = Base(driver=self.driver)
        # swipe to end of page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
        # click on logo image in the end of page
        test_object.are_visible('xpath', '//*[@id="__next"]/footer/div/div/div[1]/div/a/span/img')
        # assertion what element exist on page
        assert test_object.are_visible('class_name', 'category-slider__title')

    def test_logo_in_first_card(self):
        """Click on logo in first card of first category"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        test_object.is_visible('class_name', 'category-slider__overlay-link').click()
        try:
            test_object.is_present('xpath', '//*[@id="__next"]/footer/div/div/div[1]/div/a/span/img').click()
        except ElementClickInterceptedException:
            time.sleep(0.5)
            # click on logo image in the end of page
            test_object.is_present('xpath', '//*[@id="__next"]/footer/div/div/div[1]/div/a/span/img').click()
        # assertion what element exist on page
        assert test_object.is_present('class_name', 'category-slider__title')

    def test_scroll_button_in_first_page(self):
        """Click on page up button in first category 'KICKSCOOTER'"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        # swipe to end of page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        # click on button for return to head of page in the end of page
        test_object.are_visible('xpath', '//*[@id="__next"]/button/div/span/img')
        # assertion what element exist on page
        assert test_object.are_visible('class_name', 'category-slider__title')

    def test_number_of_payment_variables_methods(self):
        """Check number of payment variables in first card"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        test_object.is_visible('class_name', 'category-slider__overlay-link').click()
        # swipe page
        self.driver.execute_script(f"window.scrollTo(0, {300})")
        time.sleep(0.5)
        # check number of methods to pay
        assert 16 == len(test_object.are_visible('class_name', 'payments-methods__payments-method')) // 2

    def test_add_to_card_in_compare_specification(self):
        """Test button add to card in compare specification from first card"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        test_object.is_visible('class_name', 'category-slider__overlay-link').click()
        # swipe page
        try:
            test_object.is_present('class_name', 'main-slide__buy-btn').click()
        except ElementClickInterceptedException:
            test_object.is_present('class_name', 'main-slide__buy-btn').click()
        # assert what element exist
        assert test_object.is_visible('class_name', 'product-modal__top-title')

    def test_in_second_category_bundle_buttons(self):
        """Click on bundle buttons and check changing of price"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[1].click()
        test_object.are_visible('class_name', 'category-slider__overlay-link')[1].click()
        # swipe page
        self.driver.execute_script(f"window.scrollTo(0, {400})")
        time.sleep(1)
        bundle_buttons = test_object.are_present('class_name', 'bundle-toggler__item')[:2]
        price = ''
        for button in bundle_buttons:
            time.sleep(0.2)
            button.click()
            time.sleep(0.2)
            assert price != test_object.is_present('class_name', 'form-with-warrancy__form-price-new')

    def test_navigation_button_catalog(self):
        """Click on 'catalog' button and check new content"""
        test_object = Base(driver=self.driver)
        # click on catalog button
        test_object.are_visible('class_name', 'top-nav__item')[0].click()
        # check existence of element
        assert test_object.is_present('class_name', 'category-slider__title')

    def test_navigation_button_shipping_and_payment(self):
        """Click on 'shipping and payment' button and check new content"""
        test_object = Base(driver=self.driver)
        # click on catalog button
        test_object.are_visible('class_name', 'top-nav__item')[1].click()
        # check existence of element
        assert test_object.is_present('class_name', 'hide-991')

    def test_navigation_button_wholesale(self):
        """Click on 'whole sale' button and check new content"""
        test_object = Base(driver=self.driver)
        # click on catalog button
        test_object.are_visible('class_name', 'top-nav__item')[2].click()
        # check existence of element
        assert test_object.is_present('class_name', 'hide-991')

    def test_navigation_button_contacts(self):
        """Click on 'contacts' button and check new content"""
        test_object = Base(driver=self.driver)
        # click on catalog button
        test_object.are_visible('class_name', 'top-nav__item')[3].click()
        # check existence of element
        assert test_object.is_present('class_name', 'hide-991')

    def test_button_see_details(self):
        """Click on button see details and check new content"""
        test_object = Base(driver=self.driver)
        # swipe page
        self.driver.execute_script(f"window.scrollTo(0, {500})")
        time.sleep(0.5)
        # click on button see details
        test_object.is_visible('class_name', 'category-slider__see-more').click()
        # check existence of element
        assert test_object.is_present('class_name', 'welcome__title')

    def test_see_more_button_in_first_category(self):
        """Click on button 'see more details in first category'"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[0].click()
        # swipe page
        self.driver.execute_script(f"window.scrollTo(0, {300})")
        time.sleep(0.5)
        test_object.are_present('class_name', 'category-slider__see-more')[0].click()
        # swipe page
        self.driver.execute_script(f"window.scrollTo(0, {300})")
        time.sleep(0.5)
        assert test_object.is_present('class_name', 'welcome__title')

    def test_see_more_button_in_second_category(self):
        """Click on button 'see more details' in second category"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[1].click()
        test_object.are_visible('class_name', 'category-slider__see-more')[1].click()
        assert test_object.is_present('class_name', 'welcome__title')

    def test_see_more_button_in_third_category(self):
        """Click on button 'see more details in third category'"""
        test_object = Base(driver=self.driver)
        test_object.are_visible('class_name', 'top-category-slider__item')[2].click()
        # swipe page
        self.driver.execute_script(f"window.scrollTo(0, {300})")
        time.sleep(0.5)
        test_object.are_visible('class_name', 'accessories-block__add-cart')[0].click()
        # swipe page
        self.driver.execute_script(f"window.scrollTo(0, {300})")
        time.sleep(0.5)
        assert test_object.is_visible('class_name', 'product-modal__top-title')

    def test_slider_in_main_menu_right_button(self):
        """Click on slider button in main menu"""
        test_object = Base(driver=self.driver)
        for _ in range(4):
            test_object.is_visible('xpath', '//*[@id="__next"]/div[6]/div[1]/div/div[2]/div[2]/span/img').click()

    def test_slider_in_main_left_button(self):
        """Click on slider button in main menu"""
        test_object = Base(driver=self.driver)
        for _ in range(4):
            test_object.is_visible('xpath', '//*[@id="__next"]/div[6]/div[1]/div/div[2]/div[1]/span/img').click()

    def test_next_slider_on_main_page(self):
        """Click on slider button for comments"""
        test_object = Base(driver=self.driver)
        # swipe page
        self.driver.execute_script(f"window.scrollTo(0, {2000})")
        time.sleep(0.5)
        test_object.is_visible('xpath', '//*[@id="__next"]/div[6]/div[3]/div/div/div/div[2]/div[2]/span/img').click()

    def test_next_slider_on_main_page_back(self):
        """Click on slider button for comments and then on back slider button"""
        test_object = Base(driver=self.driver)
        # swipe page
        self.driver.execute_script(f"window.scrollTo(0, {2000})")
        time.sleep(0.5)
        test_object.is_visible('xpath', '//*[@id="__next"]/div[6]/div[3]/div/div/div/div[2]/div[2]/span/img').click()
        test_object.is_visible('xpath', '//*[@id="__next"]/div[6]/div[3]/div/div/div/div[2]/div[1]/span/img').click()
