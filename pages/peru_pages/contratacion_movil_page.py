from pages.base_page import base_page


class peru_contratacion_movil_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Titulo Contratacion
        self.titulo_contratacion = 'document.querySelector("#root > section.lp-modalidad__plans > div > div.content-info-plans > div.info-plan > p.name-plan")'

        # Boton "Quiero que me llamen"
        self.boton_C2C = 'document.querySelector("#root > section.lp-modalidad__plans > div > div.content-actions-plans > div > div > a.call-me")'

        # Titulo Formulario
        self.titulo_formulario = (
            'document.querySelector("#modalForm > div.lp-modalidad__form__titulo > p")'
        )

        # Input telefono
        self.input_telefono = 'document.querySelector("#lead_phone")'

        # Boton Check Box "Acepto Envio de Comunicaciones Comerciales"
        self.check_box_acepto_envio_comunicaciones = 'document.querySelector("#entelFormModal > div.lp-modalidad__form__checkbox > input[type=checkbox]")'

        # Boton "LLamenme Ahora"
        self.boton_llamenme_ahora = 'document.querySelector("#send-c2c")'

        # Titulo solicitud ingresada
        self.titulo_solicitud_ingresada = 'document.querySelector("#root > section.lp-modalidad__modal > div.lp-modalidad__success > div.lp-modalidad__success__title")'

    def get_text_titulo_contratacion(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_contratacion)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_C2C(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_C2C)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_formulario(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_formulario)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_llamenme_ahora(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_llamenme_ahora)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def send_keys_input_telefono(self, telefono):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.input_telefono)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.send_keys(telefono)
        except Exception as ex:
            raise Exception(str(ex))

    def click_check_box_acepto_envio_comunicaciones(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.check_box_acepto_envio_comunicaciones
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_solicitud_ingresada(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.titulo_solicitud_ingresada
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))
