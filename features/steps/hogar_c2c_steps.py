import time
from behave import step, when, then
from utils.utils import attach_screenshot


@step('selecciono el plan "{plan}"')
def step_selecciono_el_plan(context, plan):
    try:
        plan = plan.strip().lower()

        planes_generales = {
            "sin disney+": context.chile_internet_hogar_page.click_boton_radio_sin_disney_plus,
            "con disney+": context.chile_internet_hogar_page.click_boton_radio_con_disney_plus,
        }

        planes_por_modulo = {
            "doble_pack": {
                "fibra 600": context.chile_doble_pack_page.click_boton_radio_fibra_600,
                "fibra 800": context.chile_doble_pack_page.click_boton_radio_fibra_800,
                "fibra giga": context.chile_doble_pack_page.click_boton_radio_fibra_giga,
            },
            "triple_pack": {
                "fibra 600": context.chile_triple_pack_page.click_boton_radio_fibra_600,
                "fibra 800": context.chile_triple_pack_page.click_boton_radio_fibra_800,
                "fibra giga": context.chile_triple_pack_page.click_boton_radio_fibra_giga,
            },
        }

        if plan in planes_generales:
            click_plan = planes_generales[plan]
        elif plan in ["fibra 600", "fibra 800", "fibra giga"]:
            modulo = context.modulo.strip().lower()
            if modulo not in planes_por_modulo:
                raise ValueError(f"Módulo '{context.modulo}' no reconocido.")
            click_plan = planes_por_modulo[modulo].get(plan)
            if not click_plan:
                raise ValueError(
                    f"Plan '{plan}' no disponible para el módulo '{modulo}'"
                )
        else:
            raise ValueError(f"El plan '{plan}' no es válido")

        click_plan()
        time.sleep(1)
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@when('selecciono la velocidad "{velocidad}"')
def step_selecciono_plan(context, velocidad):
    try:
        velocidades = {
            "fibra 600": context.chile_internet_hogar_page.click_boton_fibra_600,
            "fibra 600+": context.chile_internet_hogar_page.click_boton_fibra_600_plus,
            "fibra 800": context.chile_internet_hogar_page.click_boton_fibra_800,
            "fibra 800+": context.chile_internet_hogar_page.click_boton_fibra_800_plus,
            "fibra giga": context.chile_internet_hogar_page.click_boton_fibra_giga,
            "fibra giga+": context.chile_internet_hogar_page.click_boton_fibra_giga_plus,
        }

        click_velocidad = velocidades.get(velocidad.strip().lower())

        if not click_velocidad:
            raise ValueError(f"La velocidad '{velocidad}' no es válida")

        click_velocidad()
        time.sleep(5)
        assert (
            velocidad.strip()
            in context.chile_contratacion_page.get_text_titulo_contratacion_hogar()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@when('selecciono el tipo de plan "{tipo_plan}"')
def step_selecciono_el_tipo_de_plan(context, tipo_plan):
    try:
        key_plan = tipo_plan.strip().lower()
        texto_esperado = tipo_plan.strip()
        get_titulo = context.chile_contratacion_page.get_text_titulo_contratacion_hogar

        planes_generales = {
            "tv full+": context.chile_television_page.click_boton_tv_full_plus,
            "fibra 100 mbps": context.peru_internet_hogar_page.click_boton_fibra_100_mbps,
            "fibra 300 mbps": context.peru_internet_hogar_page.click_boton_fibra_300_mbps,
        }

        planes_por_modulo = {
            "doble_pack": {
                "fibra 600 tv lite": context.chile_doble_pack_page.click_boton_fibra_600_tv_lite,
                "fibra 600 tv full+": context.chile_doble_pack_page.click_boton_fibra_600_tv_full_plus,
                "fibra 800 tv lite": context.chile_doble_pack_page.click_boton_fibra_800_tv_lite,
                "fibra 800 tv full+": context.chile_doble_pack_page.click_boton_fibra_800_tv_full_plus,
                "fibra giga tv lite": context.chile_doble_pack_page.click_boton_fibra_giga_tv_lite,
                "fibra giga tv full+": context.chile_doble_pack_page.click_boton_fibra_giga_tv_full_plus,
            },
            "triple_pack": {
                "fibra 600 tv lite": context.chile_triple_pack_page.click_boton_fibra_600_tv_lite,
                "fibra 600 tv full+": context.chile_triple_pack_page.click_boton_fibra_600_tv_full_plus,
                "fibra 800 tv lite": context.chile_triple_pack_page.click_boton_fibra_800_tv_lite,
                "fibra 800 tv full+": context.chile_triple_pack_page.click_boton_fibra_800_tv_full_plus,
                "fibra giga tv lite": context.chile_triple_pack_page.click_boton_fibra_giga_tv_lite,
                "fibra giga tv full+": context.chile_triple_pack_page.click_boton_fibra_giga_tv_full_plus,
            },
        }

        sitio_peru = {
            "fibra 100 mbps": {
                "texto_esperado": "¡Contrata Internet\npara tu Hogar!",
                "get_titulo": context.peru_internet_hogar_page.get_text_titulo_modal_c2c,
            },
            "fibra 300 mbps": {
                "texto_esperado": "¡Contrata Internet\npara tu Hogar!",
                "get_titulo": context.peru_internet_hogar_page.get_text_titulo_modal_c2c,
            },
        }

        if key_plan in planes_generales:
            click_tipo_plan = planes_generales[key_plan]
        else:
            modulo = context.modulo.strip().lower()
            if modulo not in planes_por_modulo:
                raise ValueError(
                    f"Módulo '{context.modulo}' no reconocido para el plan '{tipo_plan}'"
                )
            click_tipo_plan = planes_por_modulo[modulo].get(key_plan)
            if not click_tipo_plan:
                raise ValueError(
                    f"Tipo de plan '{tipo_plan}' no disponible en módulo '{modulo}'"
                )

        if key_plan in sitio_peru:
            texto_esperado = sitio_peru[key_plan]["texto_esperado"]
            get_titulo = sitio_peru[key_plan]["get_titulo"]

        click_tipo_plan()
        time.sleep(3)
        assert texto_esperado in get_titulo()
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@step("selecciono C2C")
def step_selecciono(context):
    try:
        context.chile_contratacion_page.click_boton_C2C()
        assert (
            "Te ayudamos a contratar"
            in context.chile_contratacion_page.get_text_titulo_formulario()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@then("ingreso la solicitud de contacto")
def step_ingreso_solicitud_contacto(context):
    try:
        paises = {
            "chile": {
                "ingresar_telefono": lambda: context.chile_contratacion_page.send_keys_input_telefono(
                    "959595959"
                ),
                "ingresar_correo": lambda: context.chile_contratacion_page.send_keys_input_correo(
                    "prueba@prueba.cl"
                ),
                "enviar_solicitud": context.chile_contratacion_page.click_boton_enviarSolcitud,
                "solicitud_ingresada": lambda: "¡Recibimos tu solicitud!"
                in context.chile_contratacion_page.get_text_solicitud_ingresada(),
            },
            "peru": {
                "ingresar_telefono": lambda: context.peru_internet_hogar_page.send_keys_input_numero(
                    "959595959"
                ),
                "seleccionar_aceptar_envio": context.peru_internet_hogar_page.click_boton_radio_aceptar_envio,
                "enviar_solicitud": context.peru_internet_hogar_page.click_boton_llamame,
                "solicitud_ingresada": lambda: "Te llamaremos pronto"
                in context.peru_internet_hogar_page.get_text_titulo_solicitud_ingresada(),
            },
        }

        steps = paises.get(context.pais)
        if not steps:
            raise ValueError(f"País no soportado: {context.pais}")

        steps["ingresar_telefono"]()

        if "ingresar_correo" in steps:
            steps["ingresar_correo"]()

        if "seleccionar_aceptar_envio" in steps:
            steps["seleccionar_aceptar_envio"]()
            time.sleep(1)

        attach_screenshot(context.driver)

        steps["enviar_solicitud"]()
        time.sleep(5)

        assert steps["solicitud_ingresada"]()
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))
