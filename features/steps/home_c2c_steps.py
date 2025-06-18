import time
from behave import then
from utils.utils import attach_screenshot


@then("se ingresa la solicitud")
def completo_con_mi_numero_de_contacto(context):
    try:
        texto_esperado = "¡Recibimos tu solicitud!"
        match context.modulo:
            case "home_peru":
                context.peru_home_page.send_keys_input_telefono("959595959")
                click_lo_quiero = context.peru_home_page.click_boton_lo_quiero
                texto_obtenido_solicitud = (
                    context.peru_home_page.get_text_titulo_solicitud_ingresada
                )

        time.sleep(1)
        attach_screenshot(context.driver)
        click_lo_quiero()
        time.sleep(2)
        assert texto_esperado in texto_obtenido_solicitud()
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
