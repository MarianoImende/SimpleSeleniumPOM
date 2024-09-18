from BasePage import BasePage as bp

class LoginPage(bp):
    URL = "https://walletchallenge-front.onrender.com/"
    USERNAME_INPUT = (bp.XPATH, '//*[@id="username"]')
    PASSWORD_INPUT = (bp.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (bp.XPATH, '//*[@id="login-form"]/button')
    MSG_LOGIN = (bp.XPATH, '//*[@id="response"]')

    def navigate_to_login_page(self):
        self.navigate_to(self.URL)

    def login(self, username: str, password: str):
        self.set_text(self.USERNAME_INPUT, username)
        self.set_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def get_msg_login(self) -> str:
        return self.get_text(self.MSG_LOGIN)

    def get_caption_button_login(self):
        text = self.get_text(self.LOGIN_BUTTON)
        return text
    
    def get_color_button_login(self)-> str:
        return self.get_color_of_element(self.LOGIN_BUTTON)
    
    def password_field_type(self)-> str:
        return self.get_field_type(self.PASSWORD_INPUT)
    
    def username_field_type(self)-> str:
        return self.get_field_type(self.USERNAME_INPUT)
