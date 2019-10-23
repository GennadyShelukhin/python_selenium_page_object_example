from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


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
