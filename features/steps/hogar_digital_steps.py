import time
from behave import step, then
from utils.utils import attach_screenshot


@step('selecciono contratar online hogar para la velocidad "{velocidad}"')
def step_selecciono_contratar_online_hogar_para_la_velocidad(context, velocidad):
    try:
        context.chile_contratacion_page.click_boton_contratar_online()
        time.sleep(1)
        assert (
            "Revisa tu Factibilidad"
            in context.chile_contratacion_appswls_page.get_text_titulo_contratacion_appswls()
        )
        assert (
            velocidad.strip()
            in context.chile_contratacion_appswls_page.get_text_titulo_velocidad_plan()
        )
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@then('completo formulario de factibilidad para la velocidad "{velocidad}"')
def step_completar_formulario_de_factibilidad_para_la_velocidad(context, velocidad):
    try:
        context.chile_contratacion_appswls_page.select_lista_region(
            "METROPOLITANA DE SANTIAGO"
        )
        time.sleep(4)
        context.chile_contratacion_appswls_page.select_lista_comuna("LAS CONDES")
        time.sleep(4)
        context.chile_contratacion_appswls_page.select_lista_direccion("ENCOMENDEROS")
        time.sleep(4)
        context.chile_contratacion_appswls_page.select_lista_numero("200")
        time.sleep(4)
        context.chile_contratacion_appswls_page.select_lista_oficina("1001")
        time.sleep(4)
        context.chile_contratacion_appswls_page.send_keys_input_telefono("959595959")
        time.sleep(1)
        attach_screenshot(context.driver)
        context.chile_contratacion_appswls_page.click_boton_continuar()
        time.sleep(5)
        assert (
            f"Estás contratando Internet {velocidad.strip()}"
            in context.chile_contratacion_appswls_page.get_text_titulo_resumen_contratacion()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))
