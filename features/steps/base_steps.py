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
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_01,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_02,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_03,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_04,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_05,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_06,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_07,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_08,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_09,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_10,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_11,
    PERU_URL_ENTEL_TELEFONIA_FIJA,
    PERU_URL_ENTEL_PREPAGO_BOLSAS,
    PERU_URL_ENTEL_PREPAGO_PLANES,
    PERU_URL_ENTEL_PREPAGO_RECARGAS,
    PERU_URL_ENTEL_PREPAGO_BENEFICIOS,
    PERU_URL_ENTEL_RECAMBIOPOWER,
    PERU_URL_ENTEL_SEGUROS,
    PERU_URL_ENTEL_CHIP_AUTOACTIVADO,
    PERU_URL_ENTEL_APPLE,
    PERU_URL_ENTEL_AYUDA,
    PERU_URL_ENTEL_TIENDAS,
    PERU_URL_ENTEL_INFO_ABONADOS,
)

SITIOS_PERU_PROMOCIONES = [
    "Descubre el plan que va contigo",
    lambda context: context.peru_oferta_promociones_page.get_text_titulo_oferta_promociones(),
    "peru",
]

PROMOCIONES_PERU_URLS = [
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_01,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_02,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_03,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_04,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_05,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_06,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_07,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_08,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_09,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_10,
    PERU_URL_ENTEL_OFERTAS_PROMOCIONES_11,
]

sitios = {
    CHILE_URL_ENTEL_HOME: [
        "Explora Mundo Móvil y Hogar",
        lambda context: context.chile_topo_fab_home_page.get_text_titulo_home(),
        "chile",
    ],
    PERU_URL_ENTEL_HOME: [
        "Quiero ser cliente",
        lambda context: context.peru_topo_fab_page.get_text_titulo_home(),
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
    PERU_URL_ENTEL_TELEFONIA_FIJA: [
        "Telefonía Fija Inalámbrica",
        lambda context: context.peru_topo_fab_page.get_text_titulo_telefonia_fija(),
        "peru",
    ],
    PERU_URL_ENTEL_PREPAGO_BOLSAS: [
        "Bolsas que se ajustan a ti!",
        lambda context: context.peru_topo_fab_page.get_text_titulo_prepago_bolsas(),
        "peru",
    ],
    PERU_URL_ENTEL_PREPAGO_PLANES: [
        "Descubre tu plan prepago ideal",
        lambda context: context.peru_topo_fab_page.get_text_titulo_prepago_planes(),
        "peru",
    ],
    PERU_URL_ENTEL_PREPAGO_RECARGAS: [
        "Recarga al toque a través de nuestros canales Entel",
        lambda context: context.peru_topo_fab_page.get_text_titulo_prepago_recargas(),
        "peru",
    ],
    PERU_URL_ENTEL_PREPAGO_BENEFICIOS: [
        "¡Prestaluca al rescate!",
        lambda context: context.peru_topo_fab_page.get_text_titulo_prepago_beneficios(),
        "peru",
    ],
    PERU_URL_ENTEL_RECAMBIOPOWER: [
        "Recambio Power",
        lambda context: context.peru_topo_fab_page.get_text_titulo_recambiopower(),
        "peru",
    ],
    PERU_URL_ENTEL_SEGUROS: [
        "Mi Equipo Protegido",
        lambda context: context.peru_topo_fab_page.get_text_titulo_seguros(),
        "peru",
    ],
    PERU_URL_ENTEL_CHIP_AUTOACTIVADO: [
        "Actívalo tu mismo",
        lambda context: context.peru_topo_fab_page.get_text_titulo_chip_autoactivado(),
        "peru",
    ],
    PERU_URL_ENTEL_APPLE: [
        "Asegura tu iPhone",
        lambda context: context.peru_topo_fab_page.get_text_titulo_apple(),
        "peru",
    ],
    PERU_URL_ENTEL_AYUDA: [
        "Resolvamos juntos todas tus dudas",
        lambda context: context.peru_topo_fab_page.get_text_titulo_ayuda(),
        "peru",
    ],
    PERU_URL_ENTEL_TIENDAS: [
        "Conoce tu tienda más cercana y todo lo que te ofrecemos",
        lambda context: context.peru_topo_fab_page.get_text_titulo_tiendas(),
        "peru",
    ],
    PERU_URL_ENTEL_INFO_ABONADOS: [
        "Tu consulta en un solo lugar",
        lambda context: context.peru_topo_fab_page.get_text_titulo_info_abonados(),
        "peru",
    ],
}

sitios.update({url: SITIOS_PERU_PROMOCIONES for url in PROMOCIONES_PERU_URLS})


@given('estoy en la pagina "{URL}"')
def step_ingreso_a_la_pagina(context, URL):
    try:
        datos = sitios.get(globals()[URL])
        if not datos:
            raise ValueError(f"La URL del sitio '{URL}' no existe.")

        if "OFERTAS_PROMOCIONES" in URL:
            context.modulo = "oyf_peru"
        elif "PERU" in URL:
            context.modulo = "topofab_peru"
        else:
            match URL:
                case "CHILE_URL_ENTEL_HOGAR_INTERNET":
                    context.modulo = "internet_hogar"
                case "CHILE_URL_ENTEL_MOVIL_PORTABILIDAD":
                    context.modulo = "portabilidad"
                case "CHILE_URL_ENTEL_MOVIL_LINEA_NUEVA":
                    context.modulo = "linea_nueva"
                case "CHILE_URL_ENTEL_HOME":
                    context.modulo = "home_chile"
                case "CHILE_URL_ENTEL_HOGAR_DOBLEPACK":
                    context.modulo = "doble_pack"
                case "CHILE_URL_ENTEL_HOGAR_TRIPLEPACK":
                    context.modulo = "triple_pack"

        texto_esperado, get_titulo, pais = datos
        context.pais = pais
        context.driver.get(globals()[URL])
        time.sleep(2)
        assert texto_esperado in get_titulo(context), (
            f"El título no coincide.\n"
            f"Esperado (contiene): {texto_esperado}\n"
            f"Obtenido: {get_titulo(context)}"
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))
