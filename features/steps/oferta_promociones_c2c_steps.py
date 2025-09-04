import time
from behave import when, then
from utils.utils import attach_screenshot


@when("selecciono Quiero que me contacten")
def selecciono_quiero_que_me_contacten(context):
    try:
        context.peru_oferta_promociones_page.click_boton_quiero_que_me_contacten()
        time.sleep(5)
        assert (
            "Te ayudamos a contratar"
            in context.peru_oferta_promociones_page.get_text_titulo_formulario()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(ex)


@then("completo formulario para que me contacten")
def completo_formulario_para_que_me_contacten(context):
    try:
        context.peru_oferta_promociones_page.send_keys_input_telefono("959595959")
        time.sleep(1)
        attach_screenshot(context.driver)
        context.peru_oferta_promociones_page.click_boton_llamame_ahora()
        time.sleep(3)
        assert (
            "Nos contactaremos contigo"
            in context.peru_oferta_promociones_page.get_text_titulo_solicitud_ingresada()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(ex)
