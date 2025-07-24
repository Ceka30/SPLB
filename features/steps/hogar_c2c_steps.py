import time
from behave import given, step, when, then
from utils.utils import attach_screenshot
from config.settings import (
    CHILE_URL_ENTEL_HOGAR_INTERNET,
    CHILE_URL_ENTEL_HOGAR_DOBLEPACK,
    CHILE_URL_ENTEL_HOGAR_TRIPLEPACK,
    CHILE_URL_ENTEL_HOGAR_TV,
    PERU_URL_ENTEL_HOGAR_INTERNET,
    CHILE_URL_ENTEL_RECOMENDADOR,
    CHILE_URL_ENTEL_MOVIL_PORTABILIDAD,
    PERU_URL_ENTEL_MOVIL,
    CHILE_URL_ENTEL_MOVIL_PLAN_ADICIONAL,
    CHILE_URL_ENTEL_OFERTAS_MOVIL,
    CHILE_URL_ENTEL_HOME,
    PERU_URL_ENTEL_HOME,
    PERU_URL_ENTEL_MOVIL_LINEAS_ADICIONALES,
)

sitios = {
    CHILE_URL_ENTEL_HOME: [
        "Explora Mundo Móvil y Hogar",
        lambda context: context.chile_topo_fab_home_page.get_text_titulo_home(),
        "chile",
    ],
    PERU_URL_ENTEL_HOME: [
        "Quiero ser cliente",
        lambda context: context.peru_topo_fab_home_page.get_text_titulo_home(),
        "peru",
    ],
    CHILE_URL_ENTEL_HOGAR_INTERNET: [
        "Planes Internet Hogar",
        lambda context: context.chile_internet_hogar_page.get_text_titulo_internet_hogar(),
        "chile",
    ],
    CHILE_URL_ENTEL_HOGAR_DOBLEPACK: [
        "Planes Internet Hogar + Televisión",
        lambda context: context.chile_doble_pack_page.get_text_titulo_doble_pack(),
        "chile",
    ],
    CHILE_URL_ENTEL_HOGAR_TRIPLEPACK: [
        "Internet Hogar + TV y Telefonía",
        lambda context: context.chile_triple_pack_page.get_text_titulo_triple_pack(),
        "chile",
    ],
    CHILE_URL_ENTEL_HOGAR_TV: [
        "TV Online: Planes de Televisión",
        lambda context: context.chile_television_page.get_text_titulo_television_hogar(),
        "chile",
    ],
    PERU_URL_ENTEL_HOGAR_INTERNET: [
        "Internet Hogar",
        lambda context: context.peru_internet_hogar_page.get_text_titulo_internet_hogar(),
        "peru",
    ],
    CHILE_URL_ENTEL_RECOMENDADOR: [
        "Encuentra tu plan ideal",
        lambda context: context.chile_recomendador_page.get_text_titulo_recomendador(),
        "chile",
    ],
    CHILE_URL_ENTEL_MOVIL_PORTABILIDAD: [
        "Quiero ser cliente",
        lambda context: context.chile_planes_portabilidad_page.get_text_titulo_planes_oferta_portabilidad(),
        "chile",
    ],
    PERU_URL_ENTEL_MOVIL: [
        "¿Cuántas líneas deseas adquirir?",
        lambda context: context.peru_planes_postpago_page.get_text_titulo_planes_postpago_portabilidad(),
        "peru",
    ],
    PERU_URL_ENTEL_MOVIL_LINEAS_ADICIONALES: [
        "Líneas Adicionales",
        lambda context: context.peru_planes_postpago_page.get_text_titulo_planes_postpago_linea_adicional(),
        "peru",
    ],
    CHILE_URL_ENTEL_MOVIL_PLAN_ADICIONAL: [
        "Plan adicional con descuento",
        lambda context: context.chile_planes_portabilidad_page.get_text_titulo_planes_oferta_portabilidad(),
        "chile",
    ],
    CHILE_URL_ENTEL_OFERTAS_MOVIL: [
        "Portabilidad con plan",
        lambda context: context.chile_planes_portabilidad_page.get_text_titulo_planes_oferta_portabilidad(),
        "chile",
    ],
}


@given('estoy en la pagina "{URL}"')
def step_ingreso_a_la_pagina(context, URL):
    try:
        datos = sitios.get(globals()[URL])
        if not datos:
            raise ValueError(f"La URL del sitio '{URL}' no existe.")

        match URL:
            case "CHILE_URL_ENTEL_HOGAR_INTERNET":
                context.modulo = "internet_hogar"
            case "CHILE_URL_ENTEL_MOVIL_PORTABILIDAD":
                context.modulo = "portabilidad"
            case "CHILE_URL_ENTEL_HOME":
                context.modulo = "home_chile"
            case "PERU_URL_ENTEL_HOME":
                context.modulo = "home_peru"

        texto_esperado, get_titulo, pais = datos
        context.pais = pais
        context.driver.get(globals()[URL])
        time.sleep(2)
        # context.driver.execute_script("document.body.style.zoom='70%'")
        assert texto_esperado in get_titulo(context)
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@step('selecciono el plan "{plan}"')
def step_selecciono_el_plan(context, plan):
    try:
        planes = {
            "sin disney+": context.chile_internet_hogar_page.click_boton_radio_sin_disney_plus,
            "con disney+": context.chile_internet_hogar_page.click_boton_radio_con_disney_plus,
            "fibra 600": context.chile_doble_pack_page.click_boton_radio_fibra_600,
            "fibra 800": context.chile_doble_pack_page.click_boton_radio_fibra_800,
            "fibra giga": context.chile_doble_pack_page.click_boton_radio_fibra_giga,
        }
        click_plan = planes.get(plan.strip().lower())

        if not click_plan:
            raise ValueError(f"El plan '{plan}' no es válida")

        click_plan()
        time.sleep(1)
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@when('selecciono la velocidad "{velocidad}"')
def step_selecciono_plan(context, velocidad):
    try:
        velocidades = {
            "fibra 600": context.chile_internet_hogar_page.click_boton_fibra_600,
            "fibra 600+": context.chile_internet_hogar_page.click_boton_fibra_600_plus,
            "fibra 800": context.chile_internet_hogar_page.click_boton_fibra_800,
            "fibra 800+": context.chile_internet_hogar_page.click_boton_fibra_800_plus,
            "fibra giga": context.chile_internet_hogar_page.click_boton_fibra_giga,
            "fibra giga+": context.chile_internet_hogar_page.click_boton_fibra_giga_plus,
        }

        click_velocidad = velocidades.get(velocidad.strip().lower())

        if not click_velocidad:
            raise ValueError(f"La velocidad '{velocidad}' no es válido")

        click_velocidad()
        time.sleep(5)
        assert (
            velocidad.strip()
            in context.chile_contratacion_page.get_text_titulo_contratacion_hogar()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@when('selecciono el tipo de plan "{tipo_plan}"')
def step_selecciono_el_tipo_de_plan(context, tipo_plan):
    try:
        key_plan = tipo_plan.strip().lower()
        texto_esperado = tipo_plan.strip()
        get_titulo = context.chile_contratacion_page.get_text_titulo_contratacion_hogar

        clicks = {
            "fibra 600 tv lite": context.chile_doble_pack_page.click_boton_fibra_600_tv_lite,
            "fibra 600 tv full+": context.chile_doble_pack_page.click_boton_fibra_600_tv_full_plus,
            "fibra 800 tv lite": context.chile_doble_pack_page.click_boton_fibra_800_tv_lite,
            "fibra 800 tv full+": context.chile_doble_pack_page.click_boton_fibra_800_tv_full_plus,
            "fibra giga tv lite": context.chile_doble_pack_page.click_boton_fibra_giga_tv_lite,
            "fibra giga tv full+": context.chile_doble_pack_page.click_boton_fibra_giga_tv_full_plus,
            "tv full +": context.chile_television_page.click_boton_tv_full_plus,
            "fibra 100 mbps": context.peru_internet_hogar_page.click_boton_fibra_100_mbps,
            "fibra 300 mbps": context.peru_internet_hogar_page.click_boton_fibra_300_mbps,
        }

        sitio_peru = {
            "fibra 100 mbps": {
                "texto_esperado": "¡Contrata Internet\npara tu Hogar!",
                "get_titulo": context.peru_internet_hogar_page.get_text_titulo_modal_c2c,
            },
            "fibra 300 mbps": {
                "texto_esperado": "¡Contrata Internet\npara tu Hogar!",
                "get_titulo": context.peru_internet_hogar_page.get_text_titulo_modal_c2c,
            },
        }

        if key_plan not in clicks:
            raise ValueError(f"El tipo de plan '{tipo_plan}' no es válido")

        click_tipo_plan = clicks[key_plan]

        peru = sitio_peru.get(key_plan) or {}
        texto_esperado = peru.get("texto_esperado", texto_esperado)
        get_titulo = peru.get("get_titulo", get_titulo)

        click_tipo_plan()
        time.sleep(3)
        assert texto_esperado in get_titulo()
        attach_screenshot(context.driver)

    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@step("selecciono C2C")
def step_selecciono(context):
    try:
        context.chile_contratacion_page.click_boton_C2C()
        assert (
            "Te ayudamos a contratar"
            in context.chile_contratacion_page.get_text_titulo_formulario()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@then("ingreso la solicitud de contacto")
def step_ingreso_solicitud_contacto(context):
    try:
        paises = {
            "chile": {
                "ingresar_telefono": lambda: context.chile_contratacion_page.send_keys_input_telefono(
                    "959595959"
                ),
                "ingresar_correo": lambda: context.chile_contratacion_page.send_keys_input_correo(
                    "prueba@prueba.cl"
                ),
                "enviar_solicitud": context.chile_contratacion_page.click_boton_enviarSolcitud,
                "solicitud_ingresada": lambda: "¡Recibimos tu solicitud!"
                in context.chile_contratacion_page.get_text_solicitud_ingresada(),
            },
            "peru": {
                "ingresar_telefono": lambda: context.peru_internet_hogar_page.send_keys_input_numero(
                    "959595959"
                ),
                "seleccionar_aceptar_envio": context.peru_internet_hogar_page.click_boton_radio_aceptar_envio,
                "enviar_solicitud": context.peru_internet_hogar_page.click_boton_llamame,
                "solicitud_ingresada": lambda: "Te llamaremos pronto"
                in context.peru_internet_hogar_page.get_text_titulo_solicitud_ingresada(),
            },
        }

        steps = paises.get(context.pais)
        if not steps:
            raise ValueError(f"País no soportado: {context.pais}")

        steps["ingresar_telefono"]()

        if "ingresar_correo" in steps:
            steps["ingresar_correo"]()

        if "seleccionar_aceptar_envio" in steps:
            steps["seleccionar_aceptar_envio"]()
            time.sleep(1)

        attach_screenshot(context.driver)

        steps["enviar_solicitud"]()
        time.sleep(5)

        assert steps["solicitud_ingresada"]()
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))
