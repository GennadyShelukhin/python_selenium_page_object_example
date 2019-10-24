from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")
    EMAIL_LOGIN_FIELD = (By.ID, "id_login-username")
    PASSWORD_LOGIN_FIELD = (By.ID, "id_login-password")
    EMAIL_REG_FIELD = (By.ID, "id_registration-email")
    PASSWORD_REG_FIELD = (By.ID, "id_registration-password1")
    PASSWORD_CONFIRM_REG_FIELD = (By.ID, "id_registration-password2")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REG_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success .alertinner")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner p")
