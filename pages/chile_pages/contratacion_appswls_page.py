from selenium.webdriver.support.ui import Select
from pages.base_page import base_page


class chile_contratacion_appswls_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Titulo Contratacion Appswls
        self.titulo_contratacion_appswls = 'document.querySelector("#step")'

        # Titulo Velocidad Plan
        self.titulo_velocidad_plan = 'document.querySelector("#form_datos > div > div.d-block.d-lg-flex > div.col-lg-3.col-md-5.col-12.px-md-0.px-2.mx-auto.mb-2.jqFlujoPlan > div > div:nth-child(1) > div.rediseño_nombrePlan.mx-auto > div > div > div:nth-child(1) > h3 > p")'

        # Lista Region
        self.lista_region = 'document.querySelector("#selReg")'

        # Lista Comuna
        self.lista_comuna = 'document.querySelector("#selCom")'

        # Lista Direccion
        self.lista_direccion = 'document.querySelector("#selDir")'

        # Lista Numero
        self.lista_numero = 'document.querySelector("#selNum")'

        # Lista Oficina
        self.lista_oficina = 'document.querySelector("#depaCasa")'

        # Input Telefono
        self.input_telefono = 'document.querySelector("#numcontact")'

        # Boton Continuar
        self.boton_continuar = 'document.querySelector("#buttonDireccion")'

        # Titulo Resumen Contratacion
        self.titulo_resumen_contratacion = 'document.querySelector("#container-header > div > div.col-12.col-md-12.mt-4.align-items-center.ps-4 > div > p")'

    def get_text_titulo_contratacion_appswls(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.titulo_contratacion_appswls
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_velocidad_plan(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_velocidad_plan)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def select_lista_region(self, texto):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.lista_region)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            select_element = Select(element)
            select_element.select_by_visible_text(texto)
        except Exception as ex:
            raise Exception(str(ex))

    def select_lista_comuna(self, texto):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.lista_comuna)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            select_element = Select(element)
            select_element.select_by_visible_text(texto)
        except Exception as ex:
            raise Exception(str(ex))

    def select_lista_direccion(self, texto):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.lista_direccion)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            select_element = Select(element)
            select_element.select_by_visible_text(texto)
        except Exception as ex:
            raise Exception(str(ex))

    def select_lista_numero(self, texto):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.lista_numero)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            select_element = Select(element)
            select_element.select_by_visible_text(texto)
        except Exception as ex:
            raise Exception(str(ex))

    def select_lista_oficina(self, texto):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.lista_oficina)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            select_element = Select(element)
            select_element.select_by_visible_text(texto)
        except Exception as ex:
            raise Exception(str(ex))

    def send_keys_input_telefono(self, texto):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.input_telefono)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.send_keys(texto)
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_continuar(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_continuar)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_resumen_contratacion(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.titulo_resumen_contratacion
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            return element.text
        except Exception as ex:
            raise Exception(str(ex))
