import time
from behave import step, then
from utils.utils import attach_screenshot


@step("selecciono contratar online movil")
def step_selecciono_contratar_online_movil(context):
    try:
        context.chile_contratacion_movil_page.click_boton_contratar_en_linea()
        time.sleep(1)
        assert (
            "Selecciona tipo de cliente y completa tu compra"
            in context.chile_login_miportal_page.get_text_titulo_login_miportal()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@then('ingreso como cliente y recibo el resumen de contratacion del plan "{plan}"')
def step_ingreso_como_cliente_y_recibo_el_resumen_de_contratacion_del_plan(
    context, plan
):
    try:
        context.chile_login_miportal_page.click_boton_soy_cliente()
        time.sleep(1)
        context.chile_login_miportal_page.click_boton_ingresar_con_contraseña()
        time.sleep(1)
        context.chile_login_miportal_page.send_keys_input_rut("16557432k")
        time.sleep(1)
        context.chile_login_miportal_page.send_keys_input_telefono("940530329")
        time.sleep(1)
        context.chile_login_miportal_page.send_keys_input_contraseña("1603")
        time.sleep(1)
        attach_screenshot(context.driver)
        context.chile_login_miportal_page.click_boton_identificacion()
        time.sleep(1)
        context.chile_login_miportal_page.wait_loader()
        assert (
            plan.strip()
            in context.chile_contratacion_miportal_page.get_text_titulo_contratacion_miportal()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))
