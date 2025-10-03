import time
from behave import when, then
from utils.utils import attach_screenshot


@when("selecciono Quiero que me contacten")
def selecciono_quiero_que_me_contacten(context):
    try:
        context.peru_oferta_promociones_page.click_boton_quiero_que_me_llamen()
        time.sleep(5)
        assert (
            "Te ayudamos a contratar"
            in context.peru_oferta_promociones_page.get_text_titulo_formulario()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(ex)


@when('selecciono llama al numero "{numero}"')
def selecciono_llama_al_numero(context, numero):
    try:
        if context.device == "MOBILE":
            context.peru_oferta_promociones_page.click_boton_llama_al_numero_header()
        elif context.device == "DESKTOP":
            context.peru_oferta_promociones_page.click_boton_llama_al_numero()
        time.sleep(5)
        assert (
            "¡No te pierdas esta oferta!"
            in context.peru_oferta_promociones_page.get_text_titulo_formulario_modal()
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


@then("completo formulario Aun no te vayas")
def completo_formulario_aun_no_te_vayas(context):
    try:
        context.peru_oferta_promociones_page.send_keys_input_telefono_modal("959595959")
        time.sleep(1)
        attach_screenshot(context.driver)
        if context.device == "MOBILE":
            context.peru_oferta_promociones_page.click_boton_llamame_ahora_modal_mobile()
        elif context.device == "DESKTOP":
            context.peru_oferta_promociones_page.click_boton_llamame_ahora_modal_desktop()
        time.sleep(3)
        assert (
            "¡Tu solicitud ha sido registrada!"
            in context.peru_oferta_promociones_page.get_text_titulo_solicitud_ingresada_modal()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(ex)


@then("completo formulario para que me contacten del banner")
def completo_formulario_para_que_me_contacten_del_banner(context):
    try:
        context.peru_oferta_promociones_page.send_keys_input_telefono_banner(
            "959595959"
        )
        time.sleep(1)
        attach_screenshot(context.driver)
        context.peru_oferta_promociones_page.click_boton_llamame_ahora_banner()
        time.sleep(3)
        assert (
            "Nos contactaremos contigo"
            in context.peru_oferta_promociones_page.get_text_titulo_solicitud_ingresada()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(ex)
