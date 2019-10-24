from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_success_message_with_correct_product_name(self):
        product_name = self.get_product_name()
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text
        assert product_name == product_name_in_basket, f"Названия товаров не совпадают. Добавлялся товар " \
                                                       f"{product_name}, а в корзине {product_name_in_basket}"

    def should_be_product_price_in_basket(self):
        price = self.get_product_price()
        info_message = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert price in info_message, f"Цены товара {price} нету в информационном сообщении {info_message}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успешном добавлении товара в корзину присутствует, но его не должно быть на странице"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успешном добавлении товара в корзину не исчезло, но должно было исчезнуть"
