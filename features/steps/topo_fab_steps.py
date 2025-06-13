import time
from behave import step, when, then
from utils.utils import attach_screenshot


@when("selecciono Topo/Fab ¿Quieres contratar?")
def selecciono_topo_fab_quieres_contratar(context):
    try:
        match context.modulo:
            case "portabilidad":
                click_quieres_contratar = context.chile_topo_fab_planes_portabilidad_page.click_boton_quieres_contratar
                texto_obtenido = context.chile_topo_fab_planes_portabilidad_page.get_text_titulo_fab_planes_portabilidad
            case "internet_hogar":
                click_quieres_contratar = context.chile_topo_fab_internet_hogar_page.click_boton_quieres_contratar
                texto_obtenido = context.chile_topo_fab_internet_hogar_page.get_text_titulo_fab_internet_hogar
            case "home":
                click_quieres_contratar = (
                    context.chile_topo_fab_home_page.click_boton_quieres_contratar
                )
                texto_obtenido = (
                    context.chile_topo_fab_home_page.get_text_titulo_fab_home
                )

        click_quieres_contratar()
        time.sleep(1)
        assert "Te ayudamos a contratar" in texto_obtenido()
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(ex)


@step("selecciono contratar por telefono")
def selecciono_contratar_por_telefono(context):
    try:
        texto_esperado = "Contratar por teléfono"
        match context.modulo:
            case "portabilidad":
                click_contratar_por_telefono = context.chile_topo_fab_planes_portabilidad_page.click_boton_contratar_por_telefono
                texto_obtenido = context.chile_topo_fab_planes_portabilidad_page.get_text_titulo_te_ayudamos_a_contratar
                texto_esperado = "Te ayudamos a contratar"
            case "internet_hogar":
                click_contratar_por_telefono = context.chile_topo_fab_internet_hogar_page.click_boton_quieres_contratar
                texto_obtenido = context.chile_topo_fab_internet_hogar_page.get_text_titulo_te_ayudamos_a_contratar
            case "home":
                click_contratar_por_telefono = (
                    context.chile_topo_fab_home_page.click_boton_contratar_por_telefono
                )
                texto_obtenido = context.chile_topo_fab_home_page.get_text_titulo_te_ayudamos_a_contratar

        click_contratar_por_telefono()
        time.sleep(1)
        assert texto_esperado in texto_obtenido()
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(ex)


@then("completo con mi numero de contacto")
def completo_con_mi_numero_de_contacto(context):
    try:
        match context.modulo:
            case "portabilidad":
                context.chile_topo_fab_planes_portabilidad_page.send_keys_input_telefono(
                    "959595959"
                )
                click_quiero_que_me_llamen = context.chile_topo_fab_planes_portabilidad_page.click_boton_quiero_que_me_llamen
                texto_obtenido_solicitud = context.chile_topo_fab_planes_portabilidad_page.get_text_titulo_te_ayudamos_a_contratar
            case "internet_hogar":
                context.chile_topo_fab_internet_hogar_page.send_keys_input_telefono(
                    "959595959"
                )
                click_quiero_que_me_llamen = context.chile_topo_fab_internet_hogar_page.click_boton_quiero_que_me_llamen
                texto_obtenido_solicitud = context.chile_topo_fab_internet_hogar_page.get_text_titulo_solicitud_ingresada
            case "home":
                context.chile_topo_fab_home_page.send_keys_input_telefono("959595959")
                click_quiero_que_me_llamen = (
                    context.chile_topo_fab_home_page.click_boton_quiero_que_me_llamen
                )
                texto_obtenido_solicitud = (
                    context.chile_topo_fab_home_page.get_text_titulo_solicitud_ingresada
                )

        time.sleep(1)
        attach_screenshot(context.driver)
        click_quiero_que_me_llamen()
        time.sleep(2)
        assert "¡Recibimos tu solicitud!" in texto_obtenido_solicitud()
        # assert "¡Recibimos tu solicitud!" in texto_obtenido_solicitud(), (
        #     f"Error al enviar Solcitud.\n"
        #     f"Esperado: '¡Recibimos tu solicitud!\n"
        #     f"Obtenido: '{texto_obtenido_solicitud}'"
        # )
        attach_screenshot(context.driver)
    except Exception as ex:
        attach_screenshot(context.driver)
        raise Exception(ex)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(ex)
