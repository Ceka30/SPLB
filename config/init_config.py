from datetime import datetime, timedelta
import time
import requests
import warnings
import os
import jwt
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad  # , unpad
from selenium import webdriver
from configparser import RawConfigParser
from pages.chile_pages.doble_pack_page import doble_pack_page
from pages.chile_pages.internet_hogar_page import internet_hogar_page
from pages.chile_pages.contratacion_page import contratacion_page
from pages.chile_pages.television_page import television_page
from pages.chile_pages.triple_pack_page import triple_pack_page
from pages.peru_pages.internet_hogar_page import peru_internet_hogar_page
from pages.chile_pages.recomendador_page import chile_recomendador_page
from pages.chile_pages.topo_fab_internet_hogar_page import (
    chile_topo_fab_internet_hogar_page,
)
from pages.peru_pages.planes_postpago_page import peru_planes_postpago_page
from pages.peru_pages.contratacion_movil_page import peru_contratacion_movil_page
from pages.chile_pages.planes_portabilidad_page import chile_planes_portabilidad_page
from pages.chile_pages.topo_fab_planes_portabilidad_page import (
    chile_topo_fab_planes_portabilidad_page,
)
from pages.chile_pages.planes_plan_adicional_page import (
    chile_planes_plan_adicional_page,
)
from pages.chile_pages.contratacion_movil_page import chile_contratacion_movil_page
from pages.chile_pages.ofertas_movil_page import chile_ofertas_movil_page
from pages.chile_pages.topo_fab_home_page import chile_topo_fab_home_page
from pages.peru_pages.topo_fab_home_page import peru_topo_fab_home_page
from pages.peru_pages.home_page import peru_home_page
from pages.chile_pages.home_page import chile_home_page
from pages.chile_pages.login_miportal_page import chile_login_miportal_page
from pages.chile_pages.contratacion_miportal_page import (
    chile_contratacion_miportal_page,
)
from pages.chile_pages.contratacion_appswls_page import chile_contratacion_appswls_page

# from config.browser_handler import browser_handler

warnings.filterwarnings(
    "ignore", category=UserWarning, module="selenium.webdriver.remote.remote_connection"
)


def encriptar_aes(texto, clave):
    iv = "D54Gsdf38vsW34B4"
    iv_bytes = iv.encode("utf-8")
    cifrador = AES.new(clave.encode("utf-8"), AES.MODE_CBC, iv_bytes)
    texto_aes = pad(texto.encode("utf-8"), AES.block_size)
    texto_cifrado = cifrador.encrypt(texto_aes)
    texto_encriptado = base64.b64encode(texto_cifrado).decode("utf-8")

    return texto_encriptado


# def descifrar_aes(texto_cifrado_base64, clave):
#     datos = base64.b64decode(texto_cifrado_base64)
#     iv_bytes = datos[:16]
#     texto_cifrado = datos[16:]
#     clave_bytes = clave.encode("utf-8")
#     descifrador = AES.new(clave_bytes, AES.MODE_CBC, iv=iv_bytes)
#     texto_plano = unpad(descifrador.decrypt(texto_cifrado), AES.block_size)

#     return texto_plano.decode("utf-8")


# def decodificar_jwt_y_descifrar(jwt_token, clave_jwt, clave_aes):
#     try:
#         payload = jwt.decode(jwt_token, clave_jwt, algorithms=["HS256"])
#         texto_encriptado = payload.get("key")
#         if not texto_encriptado:
#             raise ValueError("El campo 'key' no está en el JWT.")
#         texto_desencriptado = descifrar_aes(texto_encriptado, clave_aes)

#         return {"username_fecha": texto_desencriptado}
#     except jwt.ExpiredSignatureError:
#         raise ValueError("El JWT ha expirado.")
#     except jwt.InvalidTokenError as e:
#         raise ValueError(f"JWT inválido: {str(e)}")


def get_config():
    config = RawConfigParser()
    config_file = os.path.join(os.path.dirname(__file__), "config.cfg")

    if os.path.exists(config_file):
        config.read(config_file)
    else:
        print("Advertencia: No se encontró config.cfg, usando variables de entorno.")

    return {
        "user_name": os.getenv(
            "LT_USERNAME", config.get("Environment", "UserName", fallback=None)
        ),
        "access_key": os.getenv(
            "LT_ACCESS_KEY", config.get("Environment", "AccessKey", fallback=None)
        ),
        "os": os.getenv(
            "LT_OPERATING_SYSTEM",
            config.get("Environment", "OS", fallback="Windows 10"),
        ),
        "browser": os.getenv(
            "LT_BROWSER", config.get("Environment", "Browser", fallback="Chrome")
        ),
        "browser_version": os.getenv(
            "LT_BROWSER_VERSION",
            config.get("Environment", "BrowserVersion", fallback="latest"),
        ),
        "secret_key_user": os.getenv(
            "QA_SECRET_KEY_USER",
            config.get("Security", "SecretKeyUser", fallback=None),
        ),
        "secret_key_jwt": os.getenv(
            "QA_SECRET_KEY_JWT",
            config.get("Security", "SecretKeyJWT", fallback=None),
        ),
    }


def init_config(context, scenario):
    config = get_config()

    if not config["user_name"] or not config["access_key"]:
        raise ValueError("Error: Faltan las credenciales de LambdaTest.")

    if not config["secret_key_user"] or not config["secret_key_jwt"]:
        raise ValueError("Error: Faltan SecretKeys.")

    if scenario.tags:
        ultimo_tag = scenario.tags[-1]
        scenario.name = ultimo_tag
    else:
        ultimo_tag = scenario.name

    if "CHILE" in ultimo_tag:
        context.pais = "CHILE"
    elif "PERU" in ultimo_tag:
        context.pais = "PERU"
    else:
        raise ValueError(
            "Error: No se ha definido un país válido en el TAG del escenario."
        )

    # Generar Encriptacion
    fecha_hora = (datetime.now() + timedelta(hours=-3)).strftime("%Y-%m-%d-%H:%M")
    build_name = f"Ejecucion {ultimo_tag} --- {fecha_hora}"

    mensaje = f"{config['user_name']}@@@{fecha_hora}"
    user_encriptado = encriptar_aes(mensaje, config["secret_key_user"])

    payload = {
        "origin": "Lambdatest",
        "key": user_encriptado,
        "iat": int(time.time()),
        "exp": int(time.time() + 3600),  # 5 min
    }
    jwt_token = jwt.encode(payload, config["secret_key_jwt"], algorithm="HS256")
    custom_headers = {"X-Test-Agent": jwt_token}

    # print(
    #     decodificar_jwt_y_descifrar(
    #         jwt_token, config["secret_key_jwt"], config["secret_key_user"]
    #     )
    # )

    # Configurar navegador
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--log-level=3")
    options.add_argument("--incognito")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    # Configuracion de Lambdatest
    options.set_capability("platform", config["os"])
    options.set_capability("browserName", config["browser"])
    options.set_capability("browserVersion", config["browser_version"])
    options.set_capability("name", build_name)
    options.set_capability("build", build_name)
    options.set_capability("project", f"Automatizacion {context.pais} QA")
    # Activar Herramientas de depuración
    options.set_capability("video", True)
    options.set_capability("network", True)
    options.set_capability("console", "info")
    # options.set_capability("terminal", True)
    # options.set_capability("performance", True)
    # options.set_capability("w3c", True)
    options.set_capability("customHeaders", custom_headers)

    remote_url = f"https://{config['user_name']}:{config['access_key']}@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(command_executor=remote_url, options=options)

    session_id = driver.session_id
    LAMBDA_API_URL = "https://api.lambdatest.com/automation/api/v1/sessions"
    session_api_url = f"{LAMBDA_API_URL}/{session_id}"

    time.sleep(5)

    response = requests.get(
        session_api_url, auth=(config["user_name"], config["access_key"])
    )

    data = response.json()
    public_url = data["data"]["public_url"]
    video_url = data["data"]["video_url"]
    flujo_name = ultimo_tag

    context.flujo_name = flujo_name
    context.build_name = build_name
    context.session_id = session_id
    context.public_url = public_url
    context.video_url = video_url

    context.driver = driver
    context.chile_internet_hogar_page = internet_hogar_page(driver)
    context.chile_contratacion_page = contratacion_page(driver)
    context.chile_doble_pack_page = doble_pack_page(driver)
    context.chile_triple_pack_page = triple_pack_page(driver)
    context.chile_television_page = television_page(driver)
    context.peru_internet_hogar_page = peru_internet_hogar_page(driver)
    context.chile_recomendador_page = chile_recomendador_page(driver)
    context.chile_topo_fab_internet_hogar_page = chile_topo_fab_internet_hogar_page(
        driver
    )
    context.peru_planes_postpago_page = peru_planes_postpago_page(driver)
    context.peru_contratacion_movil_page = peru_contratacion_movil_page(driver)
    context.chile_planes_portabilidad_page = chile_planes_portabilidad_page(driver)
    context.chile_planes_plan_adicional_page = chile_planes_plan_adicional_page(driver)
    context.chile_topo_fab_planes_portabilidad_page = (
        chile_topo_fab_planes_portabilidad_page(driver)
    )
    context.chile_contratacion_movil_page = chile_contratacion_movil_page(driver)
    context.chile_ofertas_movil_page = chile_ofertas_movil_page(driver)
    context.chile_topo_fab_home_page = chile_topo_fab_home_page(driver)
    context.peru_topo_fab_home_page = peru_topo_fab_home_page(driver)
    context.peru_home_page = peru_home_page(driver)
    context.chile_home_page = chile_home_page(driver)
    context.chile_login_miportal_page = chile_login_miportal_page(driver)
    context.chile_contratacion_miportal_page = chile_contratacion_miportal_page(driver)
    context.chile_contratacion_appswls_page = chile_contratacion_appswls_page(driver)
