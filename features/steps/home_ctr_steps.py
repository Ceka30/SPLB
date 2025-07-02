import time
from behave import then, when
from utils.utils import attach_screenshot

CARPETA_SALIDA = "Reportes"
ARCHIVO_SALIDA = "eventos_datalayer.xlsx"


@when("navego hasta el final de la pagina")
def navego_hasta_el_final_de_la_pagina(context):
    try:
        # context.chile_home_page.click_boton_banner_1()
        time.sleep(1)
        context.chile_home_page.click_boton_slider_carrusel_next()
        time.sleep(2)
        context.chile_home_page.click_boton_banner_2()
        time.sleep(3)
        # context.chile_home_page.click_boton_banner_3()
        # context.chile_home_page.click_boton_banner_4()
        # context.chile_home_page.click_boton_banner_5()
        # context.chile_home_page.click_boton_banner_6()
        attach_screenshot(context.driver)
    except Exception as ex:
        attach_screenshot(context.driver)
        raise Exception(ex)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(ex)


@then("obtengo las marcas de CTR")
def obtengo_las_marcas_de_CTR(context):
    try:
        df = context.chile_home_page.obtener_marcas_ctr()
        context.chile_home_page.guardar_en_excel(df, CARPETA_SALIDA, ARCHIVO_SALIDA)
        attach_screenshot(context.driver)
    except Exception as ex:
        attach_screenshot(context.driver)
        raise Exception(ex)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(ex)
