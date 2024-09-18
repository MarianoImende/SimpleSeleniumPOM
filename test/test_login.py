import pytest
from models.models import TestConfig
from utils.util import create_test_config,load_test_data, DATA_DIR
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pytest_html_reporter import attach

#La fixture test_data tiene un scope="module", (cada archivo .py es un módulo.) 
#lo que significa que los datos cargados desde el archivo JSON se inicializan
#una sola vez por cada módulo de prueba (archivo).cargarlos una única vez.
@pytest.fixture(scope="module")
def test_data()-> TestConfig:
    with open(DATA_DIR) as f:
        json_data = load_test_data(DATA_DIR)
    return create_test_config(json_data)

#La fixture se ejecuta una vez por cada prueba (función de prueba)
@pytest.fixture(scope="function")
def browser():
    loginPage = LoginPage(wait=120,driver_to_use='chrome')
    loginPage.sleep(2)
    yield loginPage
    loginPage.close_browser()

def test_successful_login_r(browser):
    browser.navigate_to_login_page()
    browser.login('prueba','challenge')
    attach(browser.get_screenshot_as_png())
    assert browser.get_msg_login() == 'Login Exitoso, redirigiendo a la página principal...'
    
def test_successful_login(browser, test_data):
    login_info = test_data.login_tests[0]
    browser.navigate_to_login_page()
    browser.login(login_info.username, login_info.password)
    attach(browser.get_screenshot_as_png())
    assert browser.get_msg_login() == login_info.expected_message
    
def test_failed_login_username(browser):
    browser.navigate_to_login_page()
    browser.login("usuariofake", "challenge")
    browser.sleep(2)
    attach(browser.get_screenshot_as_png())
    assert "Error: No se pudo validar las credenciales" in browser.get_msg_login()
    
def test_failed_login_password(browser):
    browser.navigate_to_login_page()
    browser.login("challenge", "clave")
    attach(browser.get_screenshot_as_png())
    assert "Error: No se pudo validar las credenciales" in browser.get_msg_login()
    
def test_label_boton_login_r(browser):
     browser.navigate_to_login_page()
     browser.login("prueba","challenge")
     attach(browser.get_screenshot_as_png())
     assert browser.get_caption_button_login() == "Iniciar Sesión", f"No se encuentra 'Iniciar Sesión' en el botón de login"
     
def test_color_button_login_r(browser):
     browser.navigate_to_login_page()
     browser.login("prueba","challenge")
     attach(browser.get_screenshot_as_png())
     assert browser.get_color_button_login() == "#0CAF50",'validación color botón login'
     
def test_type_field_username(browser):
     browser.navigate_to_login_page()
     browser.login("prueba","challenge")
     attach(browser.get_screenshot_as_png())
     assert browser.username_field_type() == "text",'validación tipo campo username'
     
def test_type_field_password(browser):
     browser.navigate_to_login_page()
     browser.login("prueba","challenge")
     attach(browser.get_screenshot_as_png())
     assert browser.password_field_type() == "password",'validación tipo campo password'
     
#     # set PYTHONPATH=D:\MisProyectos\CURSOS\Selenium && pytest test_login.py

#     pip install -m requirements.txt


# @pytest.fixture: Esto marca la función como un fixture. Los fixtures pueden ser utilizados en las pruebas para preparar datos, configurar conexiones a bases de datos, inicializar objetos, etc.

# scope="function": Este parámetro define el alcance (scope) del fixture. Aquí, el alcance es "function", lo que significa 
# que el fixture se ejecutará una vez por cada función de prueba que lo utilice. 
# Otros posibles valores para scope incluyen "module" (una vez por módulo), "class" (una vez por clase), y "session" (una vez por toda la sesión de pruebas).

# yield: Cuando yield es llamado, Python "pausa" la ejecución de la función browser
# y retorna el objeto page a la prueba que lo solicitó. Después de que la prueba 
# que usa este fixture termina su ejecución, la función browser reanuda la ejecución 
# desde donde se había pausado. Esto permite realizar tareas de limpieza o finalización.
#yield retorna temporalmente 

##How to invoke pytest##
    #test_*.py or \*_test.py 

##TRun tests in a module##
    #pytest test_mod.py
##TRun tests in a directory##
    #pytest testing/
    
##To run a specific test within a module:##T
    #pytest tests/test_mod.py::test_func

##To run all tests in a class:##T
    #pytest tests/test_mod.py::TestClass
    
##pecifying a specific test method:##
    #pytest tests/test_mod.py::TestClass::test_method

##Run tests by keyword expressions-Subcadenas en los nombres de las pruebas ##
    #En Windows: "" en Linux ''.
    #pytest test_login.py -k "test_successful_login or test_failed_login_password"
    #pytest test_login.py -k "_r"
    
##Specifying a specific parametrization of a test:##
    #pytest tests/test_mod.py::test_func[x1,y2]
    #pytest -k test_login.py::test_successful_login("prueba", "challenge")
