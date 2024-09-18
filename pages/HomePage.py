from BasePage import BasePage as bp

class HomePage(bp):
    
    URL = "https://walletchallenge-front.onrender.com/home.html"
    WELCOME_MESSAGE = (bp.XPATH, '/html/body/p')
    LOGOUT_BUTTON = (bp.XPATH, "//button[@id='logout']")
    NRO_TARJETA = (bp.XPATH, '//*[@id="tarjeta"]')
    CUENTAS_BUTTON = (bp.XPATH, "/html/body/button[1]")

    def navigate_to_home(self):
        self.navigate_to(self.URL)

    def get_welcome_message(self) -> str:
        return self.get_text(self.WELCOME_MESSAGE)
    
    def set_Tarjeta(self, nro_tarjeta:str):
        self.set_text(self.NRO_TARJETA, nro_tarjeta)

    def click_btn_cuentas(self):
        self.click_element(self.CUENTAS_BUTTON)
        
    def logout(self):
        self.click_element(self.LOGOUT_BUTTON)

