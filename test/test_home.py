import pytest
from models.models import TestConfig
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from utils.util import test_data

#La fixture test_data tiene un scope="module", (cada archivo .py es un módulo.) 
#lo que significa que los datos cargados desde el archivo JSON se inicializan
#una sola vez por cada módulo de prueba (archivo).cargarlos una única vez.
@pytest.fixture(scope="module")
def data() -> TestConfig:
     return test_data()

@pytest.fixture(scope="function")
def page(data):
    
    login_page = LoginPage(wait=60, driver_to_use='chrome')
    user = data.login_tests[0]
    login_page.navigate_to_login_page()
    login_page.login(user.username, user.password)
    login_page.sleep(2)
    yield login_page
    login_page.close_browser()

def test_welcome_message_home_after_login(page,data):    
    home_info = data.home_tests[0]
    home_page = HomePage(page.get_driver_current())# Usa el driver de la 
    home_page.navigate_to_home()                   # sesión existente
    assert home_page.get_welcome_message() == home_info.welcome_message

def test_click_btn_cuentas_home(page,data):
    home_info = data.home_tests[0]
    home_page = HomePage(page.get_driver_current())  
    home_page.navigate_to_home()
    home_page.set_Tarjeta(home_info.tarjeta_number)
    home_page.click_btn_cuentas()
    home_page.sleep(2)

# def test_click_btn_cuentas_home(page):
#     home_page = HomePage(page.get_driver_current())  
#     home_page.navigate_to_home()
#     home_page.set_Tarjeta("437123768444")
#     home_page.click_btn_cuentas()
#     home_page.sleep(2)