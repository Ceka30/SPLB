import time
from behave import step, when, then
from utils.utils import attach_screenshot


@when('selecciono el plan movil "{plan}"')
def selecciono_el_plan_movil(context, plan):
    try:
        planes = {
            "power 29.90": context.peru_planes_postpago_page.click_boton_plan_power_29_90,
            "power 39.90": context.peru_planes_postpago_page.click_boton_plan_power_39_90,
            "power ilim 69.90": context.peru_planes_postpago_page.click_boton_plan_power_ilim_69_90,
            "power ilim 79.90 sd": context.peru_planes_postpago_page.click_boton_plan_power_ilim_79_90_sd,
            "power ilim 99.90 sd": context.peru_planes_postpago_page.click_boton_plan_power_ilim_99_90_sd,
            "150 gigas": context.chile_planes_portabilidad_page.click_boton_plan_150_gigas,
            "plan 350 gigas": context.chile_planes_portabilidad_page.click_boton_plan_350_gigas,
            "plan libre": context.chile_planes_portabilidad_page.click_boton_plan_libre,
            "plan libre con roaming": context.chile_planes_portabilidad_page.click_boton_plan_libre_con_roaming,
            "plan libre con roaming pro": context.chile_planes_portabilidad_page.click_boton_plan_libre_con_roaming_pro,
        }
        context.plan_movil = "portabilidad"
        if plan.strip().lower() == "power ilim 99.90 sd":
            context.peru_planes_postpago_page.click_boton_next_slide_swiper()
            time.sleep(1)
        elif plan.strip().lower() == "plan libre con roaming pro":
            context.chile_planes_portabilidad_page.click_boton_next_slide_swiper()
            time.sleep(1)

        click_plan = planes.get(plan.strip().lower())

        if not click_plan:
            raise ValueError(f"La velocidad '{plan}' no es válido")

        click_plan()
        time.sleep(2)

        match context.pais:
            case "chile":
                get_titulo = context.chile_contratacion_movil_page.get_text_titulo_contratacion_movil
            case "peru":
                get_titulo = context.peru_internet_hogar_page.get_text_titulo_modal_c2c

        assert plan.strip() in get_titulo()
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@step("selecciono Quiero que me llamen")
def selecciono_quiero_que_me_llamen(context):
    try:
        match context.pais:
            case "chile":
                click_C2C = context.chile_contratacion_movil_page.click_boton_C2C
                get_titulo = (
                    context.chile_contratacion_movil_page.get_text_titulo_formulario
                )
            case "peru":
                click_C2C = context.peru_contratacion_movil_page.click_boton_C2C
                get_titulo = (
                    context.peru_contratacion_movil_page.get_text_titulo_formulario
                )

        click_C2C()
        time.sleep(1)
        assert "Un ejecutivo te contactará lo antes posible" in get_titulo()
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@step("selecciono Soy cliente Entel")
def selecciono_soy_cliente_entel(context):
    try:
        context.peru_planes_postpago_page.click_boton_soy_cliente_entel()
        assert (
            "Líneas Adicionales"
            in context.peru_planes_postpago_page.get_text_titulo_planes_postpago_linea_adicional()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@when("selecciono linea adicional")
def selecciono_linea_adiccional(context):
    try:
        match context.pais:
            case "chile":
                click_linea_adicional = context.chile_planes_plan_adicional_page.click_boton_conocer_mi_oferta
                texto_esperado = "¿Como quieres contratar?"
                texto_obtenido = (
                    context.chile_planes_plan_adicional_page.get_text_titulo_side_bar
                )
            case "peru":
                click_linea_adicional = (
                    context.peru_planes_postpago_page.click_boton_linea_adicional
                )
                texto_esperado = "Un ejecutivo te contactará lo antes posible"
                texto_obtenido = (
                    context.peru_planes_postpago_page.get_text_titulo_formulario
                )
        context.plan_movil = "linea_adicional"

        click_linea_adicional()
        time.sleep(2)
        assert texto_esperado in texto_obtenido()
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@step("selecciono Contratar por telefono en el sidebar")
def selecciono_contratar_por_telefono_en_el_sidebar(context):
    try:
        context.chile_planes_plan_adicional_page.click_boton_contratar_por_telefono()
        time.sleep(2)
        assert (
            "Un ejecutivo te contactará lo antes posible"
            in context.chile_planes_plan_adicional_page.get_text_titulo_formulario()
        )
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))


@then("completo formulario de contacto")
def completo_formulario_de_contacto(context):
    try:
        match context.pais:
            case "chile":
                modalidad = {
                    "portabilidad": {
                        "ingresar_telefono": lambda: context.chile_contratacion_movil_page.send_keys_input_telefono(
                            "995959595"
                        ),
                        "enviar_solicitud": context.chile_contratacion_movil_page.click_boton_boton_quiero_que_me_llamen,
                        "solicitud_ingresada": lambda: "¡Recibimos tu solicitud!"
                        in context.chile_contratacion_movil_page.get_text_titulo_solicitud_ingresada(),
                    },
                    "linea_adicional": {
                        "ingresar_telefono": lambda: context.chile_planes_plan_adicional_page.send_keys_input_telefono(
                            "959595959"
                        ),
                        "enviar_solicitud": context.chile_planes_plan_adicional_page.click_boton_quiero_que_me_llamen,
                        "solicitud_ingresada": lambda: "¡Recibimos tu solicitud!"
                        in context.chile_planes_plan_adicional_page.get_text_titulo_solicitud_ingresada(),
                    },
                }

            case "peru":
                modalidad = {
                    "portabilidad": {
                        "ingresar_telefono": lambda: context.peru_contratacion_movil_page.send_keys_input_telefono(
                            "995959595"
                        ),
                        "enviar_solicitud": context.peru_contratacion_movil_page.click_boton_llamenme_ahora,
                        "solicitud_ingresada": lambda: "Te llamaremos pronto"
                        in context.peru_contratacion_movil_page.get_text_titulo_solicitud_ingresada(),
                    },
                    "linea_adicional": {
                        "ingresar_telefono": lambda: context.peru_planes_postpago_page.send_keys_input_telefono(
                            "959595959"
                        ),
                        "enviar_solicitud": context.peru_planes_postpago_page.click_boton_llamenme_ahora,
                        "solicitud_ingresada": lambda: "Te llamaremos pronto"
                        in context.peru_planes_postpago_page.get_text_titulo_solicitud_ingresada(),
                    },
                }

        steps = modalidad.get(context.plan_movil)
        if not steps:
            raise ValueError(f"Modalidad no soportada: {context.plan_movil}")

        steps["ingresar_telefono"]()
        time.sleep(1)
        attach_screenshot(context.driver)

        steps["enviar_solicitud"]()
        time.sleep(2)

        assert steps["solicitud_ingresada"]()
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))
