# import json
# import yaml
from models.models import TestConfig, EnvironmentConfig,ButtonTests,FieldTests,HomeTest,LoginTest
import os
from typing import Union, Dict, List
import json
import yaml

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = ROOT_DIR + "\\data\\test_data.json"

def test_data() -> TestConfig:
    with open(DATA_DIR) as f:
        json_data = load_test_data(DATA_DIR)
    return create_test_config(json_data)

""" La función load_test_data retorna un objeto de tipo TestConfig
    lee un archivo JSON o YAML y lo deserializa en una estructura de 
    datos de Python (generalmente un diccionario o una lista). """
def load_test_data(file_path: str) -> Union[Dict, List]:
    """Carga datos de prueba desde un archivo JSON o YAML. por ese motivo, 
    la funcion devuelve un Union[Dict, List], puede ser un json o un yaml"""
    if file_path.endswith('.json'):
        with open(file=file_path, encoding='UTF-8') as f:
            return json.load(f)  # Retorna un dict
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file=file_path, encoding='UTF-8') as f:
            return yaml.safe_load(f)  # Retorna un list
    else:
        raise ValueError("El archivo debe ser .json o .yaml")

def create_test_config(json_data: Dict) -> TestConfig:
    # environment_config = {
    #     key: EnvironmentConfig(**value) for key, value in json_data.get('environment_config', {}).items()
    # }
    # Creamos un diccionario vacío para almacenar la configuración de entornos.
    environment_config = {}
    # Verificamos si el archivo JSON tiene una clave 'environment_config'.
    if 'environment_config' in json_data:
        # Iteramos sobre cada clave y su valor dentro de 'environment_config'.
        for key, value in json_data['environment_config'].items():
            # Creamos un objeto EnvironmentConfig con los valores específicos del entorno.
            env_config = EnvironmentConfig(
                url=value['url'],
                db_connection_string=value['db_connection_string'],
                api_key=value['api_key']
            )
            # Asignamos la configuración de este entorno al diccionario environment_config.
            environment_config[key] = env_config


    login_tests = [] #for tradicional:
    for test in json_data.get('login_tests', []):
        login_tests.append(LoginTest(**test))
        
    # button_tests = ButtonTests(**json_data.get('button_tests', {}))
    # Inicialización y verificación explícita
    login_button_text = ""
    login_button_color = ""

    if 'button_tests' in json_data:
        button_data = json_data['button_tests']
        
        if 'login_button_text' in button_data:
            login_button_text = button_data['login_button_text']
        
        if 'login_button_color' in button_data:
            login_button_color = button_data['login_button_color']

    button_tests = ButtonTests(
        login_button_text=login_button_text,
        login_button_color=login_button_color
    )

    field_tests = FieldTests(**json_data.get('field_tests', {}))
    home_tests = [HomeTest(**test) for test in json_data.get('home_tests', [])]

    return TestConfig(
        environment_config=environment_config,
        login_tests=login_tests,
        button_tests=button_tests,
        field_tests=field_tests,
        home_tests=home_tests
    )
    
def html_encode(texto: str) -> str:
    
    diccionario = {
    '"': "&quot;",
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    "¡": "&iexcl;",
    "¢": "&cent;",
    "£": "&pound;",
    "¤": "&curren;",
    "¥": "&yen;",
    "¦": "&brvbar;",
    "§": "&sect;",
    "¨": "&uml;",
    "©": "&copy;",
    "(c,": "&copy;",
    "(C,": "&copy;",
    "ª": "&ordf;",
    "«": "&laquo;",
    "¬": "&not;",
    "®": "&reg;",
    "(r,": "&reg;",
    "(R,": "&reg;",
    "¯": "&macr;",
    "°": "&deg;",
    "±": "&plusmn;",
    "²": "&sup2;",
    "³": "&sup3;",
    "´": "&acute;",
    "µ": "&micro;",
    "¶": "&para;",
    "·": "&middot;",
    "¸": "&cedil;",
    "¹": "&sup1;",
    "º": "&ordm;",
    "»": "&raquo;",
    "¼": "&frac14;",
    "½": "&frac12;",
    "¾": "&frac34;",
    "¿": "&iquest;",
    "À": "&Agrave;",
    "Á": "&Aacute;",
    "Â": "&Acirc;",
    "Ã": "&Atilde;",
    "Ä": "&Auml;",
    "Å": "&Aring;",
    "Æ": "&AElig;",
    "Ç": "&Ccedil;",
    "È": "&Egrave;",
    "É": "&Eacute;",
    "Ê": "&Ecirc;",
    "Ë": "&Euml;",
    "Ì": "&Igrave;",
    "Í": "&Iacute;",
    "Î": "&Icirc;",
    "Ï": "&Iuml;",
    "Ð": "&ETH;",
    "Ñ": "&Ntilde;",
    "Ò": "&Ograve;",
    "Ó": "&Oacute;",
    "Ô": "&Ocirc;",
    "Õ": "&Otilde;",
    "Ö": "&Ouml;",
    "×": "&times;",
    "Ø": "&Oslash;",
    "Ù": "&Ugrave;",
    "Ú": "&Uacute;",
    "Û": "&Ucirc;",
    "Ü": "&Uuml;",
    "Ý": "&Yacute;",
    "Þ": "&THORN;",
    "ß": "&szlig;",
    "à": "&agrave;",
    "á": "&aacute;",
    "â": "&acirc;",
    "ã": "&atilde;",
    "ä": "&auml;",
    "å": "&aring;",
    "æ": "&aelig;",
    "ç": "&ccedil;",
    "è": "&egrave;",
    "é": "&eacute;",
    "ê": "&ecirc;",
    "ë": "&euml;",
    "ì": "&igrave;",
    "í": "&iacute;",
    "î": "&icirc;",
    "ð": "&eth;",
    "ñ": "&ntilde;",
    "ò": "&ograve;",
    "ó": "&oacute;",
    "ô": "&ocirc;",
    "õ": "&otilde;",
    "ö": "&ouml;",
    "÷": "&divide;",
    "ø": "&oslash;",
    "ù": "&ugrave;",
    "ú": "&uacute;",
    "û": "&ucirc;",
    "ü": "&uuml;",
    "ý": "&yacute;",
    "þ": "&thorn;",
    "ÿ": "&yuml;",
    "Α": "&Alpha;",
    "α": "&alpha;",
    "Β": "&Beta;",
    "β": "&beta;",
    "Γ": "&Gamma;",
    "γ": "&gamma;",
    "Δ": "&Delta;",
    "δ": "&delta;",
    "Ε": "&Epsilon;",
    "ε": "&epsilon;",
    "Ζ": "&Zeta;",
    "ζ": "&zeta;",
    "Η": "&Eta;",
    "η": "&eta;",
    "Θ": "&Theta;",
    "θ": "&theta;",
    "Ι": "&Iota;",
    "ι": "&iota;",
    "Κ": "&Kappa;",
    "κ": "&kappa;",
    "Λ": "&Lambda;",
    "λ": "&lambda;",
    "Μ": "&Mu;",
    "μ": "&mu;",
    "Ν": "&Nu;",
    "ν": "&nu;",
    "Ξ": "&Xi;",
    "ξ": "&xi;",
    "Ο": "&Omicron;",
    "ο": "&omicron;",
    "Π": "&Pi;",
    "π": "&pi;",
    "Ρ": "&Rho;",
    "ρ": "&rho;",
    "Σ": "&Sigma;",
    "ς": "&sigmaf;",
    "σ": "&sigma;",
    "Τ": "&Tau;",
    "τ": "&tau;",
    "Υ": "&Upsilon;",
    "υ": "&upsilon;",
    "Φ": "&Phi;",
    "φ": "&phi;",
    "Χ": "&Chi;",
    "χ": "&chi;",
    "Ψ": "&Psi;",
    "ψ": "&psi;",
    "Ω": "&Omega;",
    "ω": "&omega;",
    "ϑ": "&thetasym;",
    "ϒ": "&upsih;",
    "ϖ": "&piv;",
    "∀": "&forall;",
    "∂": "&part;",
    "∃": "&exist;",
    "∅": "&empty;",
    "∇": "&nabla;",
    "∈": "&isin;",
    "∉": "&notin;",
    "∋": "&ni;",
    "∏": "&prod;",
    "∑": "&sum;",
    "−": "&minus;",
    "∗": "&lowast;",
    "√": "&radic;",
    "∝": "&prop;",
    "∞": "&infin;",
    "∠": "&ang;",
    "∧": "&and;",
    "∨": "&or;",
    "∩": "&cap;",
    "∪": "&cup;",
    "∫": "&int;",
    "∴": "&there4;",
    "∼": "&sim;",
    "≅": "&cong;",
    "≈": "&asymp;",
    "≠": "&ne;",
    "≡": "&equiv;",
    "≤": "&le;",
    "≥": "&ge;",
    "⊂": "&sub;",
    "⊃": "&sup;",
    "⊄": "&nsub;",
    "⊆": "&sube;",
    "⊇": "&supe;",
    "⊕": "&oplus;",
    "⊗": "&otimes;",
    "⊥": "&perp;",
    "⋅": "&sdot;",
    "◊": "&loz;",
    "⌈": "&lceil;",
    "⌉": "&rceil;",
    "⌊": "&lfloor;",
    "⌋": "&rfloor;",
    "⟨": "&lang;",
    "⟩": "&rang;",
    "←": "&larr;",
    "↑": "&uarr;",
    "→": "&rarr;",
    "↓": "&darr;",
    "↔": "&harr;",
    "↵": "&crarr;",
    "⇐": "&lArr;",
    "⇑": "&uArr;",
    "⇒": "&rArr;",
    "⇓": "&dArr;",
    "⇔": "&hArr;",
    "•": "&bull;",
    "′": "&prime;",
    "″": "&Prime;",
    "‾": "&oline;",
    "⁄": "&frasl;",
    "℘": "&weierp;",
    "ℑ": "&image;",
    "ℜ": "&real;",
    "™": "&trade;",
    "(TM,": "&trade;",
    "(tm,": "&trade;",
    "€": "&euro;",
    "ℵ": "&alefsym;",
    "♠": "&spades;",
    "♣": "&clubs;",
    "♥": "&hearts;",
    "♦": "&diams;",
    "Œ": "&OElig;",
    "œ": "&oelig;",
    "Š": "&Scaron;",
    "š": "&scaron;",
    "ƒ": "&fnof;",
    "–": "&ndash;",
    "—": "&mdash;",
    "‘": "&lsquo;",
    "’": "&rsquo;",
    "‚": "&sbquo;",
    "“": "&ldquo;",
    "”": "&rdquo;",
    "„": "&bdquo;",
    "†": "&dagger;",
    "‡": "&Dagger;",
    "…": "&hellip;",
    "‰": "&permil;",
    "‹": "&lsaquo;",
    "›": "&rsaquo;",
    "ˆ": "&circ;",
    "˜": "&tilde;"
    }
    for clave in diccionario.keys():
        texto = texto.replace(clave, diccionario[clave])
        
    return texto

   
   