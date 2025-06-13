import time
from behave import when, then
from utils.utils import attach_screenshot


@when("selecciono click to call Quiero que me llamen")
def selecciono_click_to_call_quiero_que_me_llamen(context):
    try:
        context.chile_ofertas_movil_page.click_boton_modal_quiero_que_me_llamen()
        time.sleep(1)
        assert (
            "Te ayudamos a contratar"
            in context.chile_ofertas_movil_page.get_text_titulo_modal()
        )
        attach_screenshot(context.driver)

    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(ex)


@then("completo formulario con mi numero de contacto")
def completo_formulario_con_mi_numero_de_contacto(context):
    try:
        context.chile_ofertas_movil_page.send_keys_input_telefono("959595959")
        time.sleep(1)
        attach_screenshot(context.driver)
        context.chile_ofertas_movil_page.click_boton_quiero_que_me_llamen()
        time.sleep(2)
        assert (
            "¡Recibimos tu solicitud!"
            in context.chile_ofertas_movil_page.get_text_titulo_solicitud_ingresada()
        )
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
