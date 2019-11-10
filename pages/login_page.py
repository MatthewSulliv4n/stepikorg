from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/accounts/login/" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REG_FORM), "Reg form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_input.send_keys(email)

        password_input = self.browser.find_element(
            *LoginPageLocators.REG_PASSWORD)
        password_input.send_keys(password)

        confirm_password = self.browser.find_element(
            *LoginPageLocators.REG_PASSWORD_CONFIRM)
        confirm_password.send_keys(password)

        reg_btn = self.browser.find_element(*LoginPageLocators.REG_BTN)
        reg_btn.click()
