import time
from behave import given
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
    CHILE_URL_ENTEL_MOVIL_LINEA_NUEVA,
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
        "Portabilidad",
        lambda context: context.chile_planes_portabilidad_page.get_text_titulo_planes_oferta_portabilidad(),
        "chile",
    ],
    CHILE_URL_ENTEL_MOVIL_LINEA_NUEVA: [
        "Línea nueva",
        lambda context: context.chile_planes_linea_nueva_page.get_text_titulo_planes_linea_nueva(),
        "chile",
    ],
    PERU_URL_ENTEL_MOVIL: [
        "¿Cuántos planes deseas adquirir?",
        lambda context: context.peru_planes_postpago_page.get_text_titulo_planes_postpago_portabilidad(),
        "peru",
    ],
    PERU_URL_ENTEL_MOVIL_LINEAS_ADICIONALES: [
        "Líneas Adicionales",
        lambda context: context.peru_planes_postpago_page.get_text_titulo_planes_postpago_linea_adicional(),
        "peru",
    ],
    CHILE_URL_ENTEL_MOVIL_PLAN_ADICIONAL: [
        "Soy Cliente Entel",
        lambda context: context.chile_planes_plan_adicional_page.get_text_titulo_planes_plan_adicional(),
        "chile",
    ],
    CHILE_URL_ENTEL_OFERTAS_MOVIL: [
        "Planes móviles",
        lambda context: context.chile_ofertas_movil_page.get_text_titulo_ofertas_movil(),
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
            case "CHILE_URL_ENTEL_MOVIL_LINEA_NUEVA":
                context.modulo = "linea_nueva"
            case "CHILE_URL_ENTEL_HOME":
                context.modulo = "home_chile"
            case "PERU_URL_ENTEL_HOME":
                context.modulo = "home_peru"
            case "CHILE_URL_ENTEL_HOGAR_DOBLEPACK":
                context.modulo = "doble_pack"
            case "CHILE_URL_ENTEL_HOGAR_TRIPLEPACK":
                context.modulo = "triple_pack"

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
