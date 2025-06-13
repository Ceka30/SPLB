import time
from behave import step, when, then
from utils.utils import attach_screenshot


@when('selecciono el servicio "{servicio}"')
def selecciono_el_servicio(context, servicio):
    try:
        match servicio.strip().lower():
            case "triple pack":
                context.chile_recomendador_page.click_boton_checkbox_internet_fibra()
                context.chile_recomendador_page.click_boton_checkbox_television()
                context.chile_recomendador_page.click_boton_checkbox_telefonia()
                texto_esperado = "¿En qué tipo de hogar vives?"
                texto_obtenido = (
                    context.chile_recomendador_page.get_text_titulo_tipo_hogar
                )
                context.servicio = "triple pack"
            case "mono pack television":
                context.chile_recomendador_page.click_boton_checkbox_television()
                texto_esperado = "¿Cuál es tu actual compañía de internet?"
                texto_obtenido = (
                    context.chile_recomendador_page.get_text_titulo_compania_actual
                )
                context.servicio = "mono pack television"
            case "mono pack internet":
                context.chile_recomendador_page.click_boton_checkbox_internet_fibra()
                texto_esperado = "¿En qué tipo de hogar vives?"
                texto_obtenido = (
                    context.chile_recomendador_page.get_text_titulo_tipo_hogar
                )
                context.servicio = "mono pack internet"
            case _:
                raise ValueError(f"Servicio '{servicio}' no reconocido.")
        time.sleep(1)
        attach_screenshot(context.driver)
        context.chile_recomendador_page.click_boton_continuar()
        assert texto_esperado in texto_obtenido()
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@step('selecciono el tipo de hogar "{tipo_hogar}"')
def selecciono_el_tipo_de_hogar(context, tipo_hogar):
    try:
        match tipo_hogar.strip().lower():
            case "casa":
                context.chile_recomendador_page.click_boton_radio_casa()
            case "departamento":
                context.chile_recomendador_page.click_boton_radio_departamento()
            case _:
                raise ValueError(f"Hogar '{tipo_hogar}' no reconocido.")
        time.sleep(1)
        attach_screenshot(context.driver)
        context.chile_recomendador_page.click_boton_continuar()
        assert (
            "¿Cuántos pisos tiene tu hogar?"
            in context.chile_recomendador_page.get_text_titulo_pisos()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@step('selecciono los pisos del hogar "{pisos}"')
def selecciono_los_pisos_del_hogar(context, pisos):
    try:
        match pisos.strip().lower():
            case "2 pisos o mas":
                context.chile_recomendador_page.click_boton_radio_2_pisos_mas()
            case "1 piso":
                context.chile_recomendador_page.click_boton_radio_1_piso()
            case _:
                raise ValueError(f"Cantidad de pisos '{pisos}' no reconocido.")
        time.sleep(1)
        attach_screenshot(context.driver)
        context.chile_recomendador_page.click_boton_continuar()
        assert (
            "¿En cuántos espacios necesitas WiFi?"
            in context.chile_recomendador_page.get_text_titulo_espacios()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@step('selecciono los espacios "{espacios}"')
def selecciono_los_espacios(context, espacios):
    try:
        match espacios.strip().lower():
            case "5 o mas espacios":
                context.chile_recomendador_page.click_boton_radio_5_espacios_mas()
            case "3 espacios":
                context.chile_recomendador_page.click_boton_radio_3_espacios()
            case "1 espacio":
                context.chile_recomendador_page.click_boton_radio_1_espacio()
            case _:
                raise ValueError(f"Cantidad de espacios '{espacios}' no reconocido.")
        time.sleep(1)
        attach_screenshot(context.driver)
        context.chile_recomendador_page.click_boton_continuar()
        assert (
            "¿Cuántos dispositivos conectarás y utilizarás al mismo tiempo con WiFi?"
            in context.chile_recomendador_page.get_text_titulo_dispositivos()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@step('selecciono el numero de dispositivos "{dispositivos}"')
def selecciono_el_numero_de_dispositivos(context, dispositivos):
    try:
        match dispositivos.strip().lower():
            case "mas de 16 dispositivos":
                context.chile_recomendador_page.click_boton_radio_16_dispositivos_mas()
            case "entre 8 y 16 dispositivos":
                context.chile_recomendador_page.click_boton_radio_entre_8_16_dispositivos()
            case "menos de 8 dispositivos":
                context.chile_recomendador_page.click_boton_radio_menos_8_dispositivos()
            case _:
                raise ValueError(
                    f"Cantidad de dispositivos '{dispositivos}' no reconocido."
                )
        time.sleep(1)
        attach_screenshot(context.driver)
        context.chile_recomendador_page.click_boton_continuar()
        assert (
            "¿Para qué utilizas internet?"
            in context.chile_recomendador_page.get_text_titulo_utilizacion()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@step('selecciono la utilizacion del internet "{utilizacion}"')
def selecciono_la_utilizacion_del_internet(context, utilizacion):
    try:
        match utilizacion.strip().lower():
            case "alto":
                context.chile_recomendador_page.click_boton_radio_utilizacion_alto()
            case "basico":
                context.chile_recomendador_page.click_boton_radio_utilizacion_basico()
            case _:
                raise ValueError(f"Utilizacion '{utilizacion}' no reconocido.")
        time.sleep(1)
        attach_screenshot(context.driver)
        context.chile_recomendador_page.click_boton_continuar()

        match context.servicio.strip().lower():
            case "triple pack":
                texto_esperado = (
                    "¿En cuántos dispositivos reproducirás TV al mismo tiempo?"
                )
                texto_obtenido = (
                    context.chile_recomendador_page.get_text_titulo_tv_simultaneas
                )
            case "mono pack internet":
                texto_esperado = (
                    "¿Te interesa contratar internet con Disney+ Premium incluido?"
                )
                texto_obtenido = (
                    context.chile_recomendador_page.get_text_titulo_disney_plus_premium
                )

            case _:
                raise ValueError(f"Servicio '{context.servicio}' no reconocido.")
        assert texto_esperado in texto_obtenido()
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@step('selecciono TV simultaneas "{simultaneas}"')
def selecciono_tv_simultaneas(context, simultaneas):
    try:
        match simultaneas.strip().lower():
            case "3 o mas dispositivos":
                context.chile_recomendador_page.click_boton_radio_3_dispositivos_mas()
            case "1 a 2 dispositivos":
                context.chile_recomendador_page.click_boton_radio_1_2_dispositivos()
            case _:
                raise ValueError(f"Tvs simultaneas '{simultaneas}' no reconocido.")
        time.sleep(1)
        attach_screenshot(context.driver)
        context.chile_recomendador_page.click_boton_continuar()

        match context.servicio.strip().lower():
            case "triple pack":
                texto_esperado = "¡Felicitaciones!"
                texto_obtenido = (
                    context.chile_recomendador_page.get_text_titulo_recomendacion
                )
            case "mono pack television":
                texto_esperado = "¿Qué contenido te gustaría que tuviera tu plan de TV?"
                texto_obtenido = (
                    context.chile_recomendador_page.get_text_titulo_contenido
                )

            case _:
                raise ValueError(f"Servicio '{context.servicio}' no reconocido.")
        assert texto_esperado in texto_obtenido()
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@then('me recomienda el plan ideal "{plan_ideal}"')
def me_recomienda_el_plan_ideal(context, plan_ideal):
    try:
        texto_obtenido = context.chile_recomendador_page.get_text_titulo_plan_ideal()
        assert plan_ideal.strip() in texto_obtenido, (
            f"El plan recomendado no coincide.\n"
            f"Esperado: '{plan_ideal.strip()}'\n"
            f"Obtenido: '{texto_obtenido}'"
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@step('selecciono mi compañia actual "{compania_actual}"')
def selecciono_mi_compania_actual(context, compania_actual):
    try:
        match compania_actual.strip().lower():
            case "entel":
                context.chile_recomendador_page.click_boton_radio_compania_actual_entel()
            case "otra compañia":
                context.chile_recomendador_page.click_boton_radio_compania_actual_otra()
            case "utilizo internet de mi celular":
                context.chile_recomendador_page.click_boton_radio_compania_actual_internet_celular()
            case _:
                raise ValueError(f"Compañia '{compania_actual}' no reconocido.")
        time.sleep(1)
        attach_screenshot(context.driver)
        context.chile_recomendador_page.click_boton_continuar()
        assert (
            "¿Quieres disfrutar la televisión fuera de tu hogar?"
            in context.chile_recomendador_page.get_text_titulo_internet_fuera_hogar()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@step('selecciono internet fuera del hogar "{internet_fuera_del_hogar}"')
def selecciono_internet_fuera_del_hogar(context, internet_fuera_del_hogar):
    try:
        match internet_fuera_del_hogar.strip().lower():
            case "si":
                context.chile_recomendador_page.click_boton_radio_internet_fuera_hogar_si()
            case "no":
                context.chile_recomendador_page.click_boton_radio_internet_fuera_hogar_no()
            case _:
                raise ValueError(
                    f"Opcion Internet fuera del hogar '{internet_fuera_del_hogar}' no reconocido."
                )
        time.sleep(1)
        attach_screenshot(context.driver)
        context.chile_recomendador_page.click_boton_continuar()
        assert (
            "¿En cuántos dispositivos reproducirás TV al mismo tiempo?"
            in context.chile_recomendador_page.get_text_titulo_tv_simultaneas()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@step("selecciono el contenido de mi plan")
def selecciono_el_contenido_de_mi_plan(context):
    try:
        context.chile_recomendador_page.click_boton_checkbox_contenido_series_peliculas()
        context.chile_recomendador_page.click_boton_checkbox_contenido_noticias()
        context.chile_recomendador_page.click_boton_checkbox_contenido_deportes()
        context.chile_recomendador_page.click_boton_checkbox_contenido_streaming()
        time.sleep(1)
        attach_screenshot(context.driver)
        context.chile_recomendador_page.click_boton_continuar()
        assert (
            "¡Felicitaciones!"
            in context.chile_recomendador_page.get_text_titulo_recomendacion()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@step('selecciono Disney+ Premium "{disney_plus_premium}"')
def selecciono_disney_premium(context, disney_plus_premium):
    try:
        match disney_plus_premium.strip().lower():
            case "si":
                context.chile_recomendador_page.click_boton_radio_disney_plus_si()
            case "no":
                context.chile_recomendador_page.click_boton_radio_disney_plus_no()
            case _:
                raise ValueError(
                    f"Opcion Diensy+ Premium '{disney_plus_premium}' no reconocido."
                )
        time.sleep(1)
        attach_screenshot(context.driver)
        context.chile_recomendador_page.click_boton_continuar()
        assert (
            "¡Felicitaciones!"
            in context.chile_recomendador_page.get_text_titulo_recomendacion()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))
