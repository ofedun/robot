"""Component API for Login form."""
# from Lib.elements import BaseElement
from Lib.page_components import BaseComponent
from Lib.elements import InputField, Button


ELEMENTMAP = {
    'username': ('xpath', '//input[@name="user"]'),
    'password': ('xpath', '//input[@name="pass"]'),
    'login_button': ('xpath', '//input[@type="submit"]')
}

class LoginForm(BaseComponent):
    """Functionality for the AddressBook Login Panel."""

    def __init__(self, driver):
        super(BaseComponent, self).__init__()
        self.driver = driver

        self.username = InputField(self.driver, ELEMENTMAP['username'])
        self.password = InputField(self.driver, ELEMENTMAP['password'])
        self.login_button = Button(self.driver, ELEMENTMAP['login_button'])

    def login(self, username, password):
        """Attempt to log in to the system with AddressBook account credentials.

        Args:
            username (str): the username of the AddressBook user
            password (str): the password of the AddressBook user
        """
        self.username.set_value(username)
        self.password.set_value(password)
        self.login_button.click()

        # self.driver.find_element_by_name(
        #     ELEMENTMAP['username']).first.fill(username)
        # self.driver.find_element_by_name(
        #     ELEMENTMAP['password']).first.fill(password)
        # login_button = self.driver.find_by_text(
        #     ELEMENTMAP['login_button'])
        # login_button.click()

    def enter_username(self, username):
        self.username.set_value(username)
        # self.driver.find_element_by_name(
        #     ELEMENTMAP['username']).send_keys(username)

    def enter_password(self, password):
        self.password.set_value(password)
        # self.driver.find_element_by_name(
        #     ELEMENTMAP['password']).send_keys(password)

    def click_submit_button(self):
        # login_button = self.driver.find_element_by_xpath(
        #     ELEMENTMAP['login_button'])
        # login_button.click()
        self.login_button.click()
