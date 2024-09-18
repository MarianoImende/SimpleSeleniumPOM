from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class EnvironmentConfig:
    url: str
    db_connection_string: str
    api_key: str

@dataclass
class LoginTest:
    username: str
    password: str
    expected_message: str

@dataclass
class ButtonTests:
    variable = {"nombre":"Pedro",
                "apellido":"Gomez"}
    
    login_button_text: str
    login_button_color: str

@dataclass
class FieldTests:
    username_field_type: str
    password_field_type: str

@dataclass
class HomeTest:
    welcome_message: str
    tarjeta_number: str

@dataclass
class TestConfig:
    environment_config: Dict[str, EnvironmentConfig] = field(default_factory=dict)
    login_tests: List[LoginTest] = field(default_factory=list)
    button_tests: ButtonTests = field(default_factory=ButtonTests)
    field_tests: FieldTests = field(default_factory=FieldTests)
    home_tests: List[HomeTest] = field(default_factory=list)
