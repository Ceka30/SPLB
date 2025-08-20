from pages.base_page import base_page


class chile_contratacion_movil_linea_nueva_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Titulo Acceso Contratacion Online
        self.titulo_contratacion_movil = 'document.querySelector("#root > section > div > div > div.plan-container.bg-white.col-12.col-lg-5.p-0 > div > div > div > h2")'

        # Boton C2C
        self.boton_C2C = 'document.querySelector("#linea-nueva-1-1 > div > div.c2c-flow.mb-3 > andino-card-sm").shadowRoot.querySelector("div > div.content > andino-text-styler.title").shadowRoot.querySelector("p > span")'

        # Boton Contratar en linea
        self.boton_contratar_en_linea = 'document.querySelector("#linea-nueva-1-1 > div > div.digital-flow.mb-3 > andino-card-sm").shadowRoot.querySelector("div > div.content > andino-text-styler.title").shadowRoot.querySelector("p > span")'

        # Titulo Formulario
        self.titulo_formulario = 'document.querySelector("#root > section > div > div > div.flow-container.bg-neutral-050.col-12.col-lg-7.p-0 > div > div > div.form-c2c.mb-4 > p")'

        # Input telefono
        self.input_telefono = 'document.querySelector("#phoneC2c")'

        # Boton "Quiero que me llamen"
        self.boton_quiero_que_me_llamen = 'document.querySelector("#formC2C > eds-btn")'

        # Titulo solicitud ingresada
        self.titulo_solicitud_ingresada = 'document.querySelector("#root > section > div > div > div.flow-container.bg-neutral-050.col-12.col-lg-7.p-0 > div > div > div > div > h3")'

    def get_text_titulo_contratacion_movil(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_contratacion_movil)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
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
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_contratar_en_linea(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_contratar_en_linea)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
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
            element.location_once_scrolled_into_view
            return element.text
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
            element.location_once_scrolled_into_view
            element.send_keys(texto)
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_boton_quiero_que_me_llamen(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_quiero_que_me_llamen
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
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
            element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))
