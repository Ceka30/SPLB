from pages.base_page import base_page
# from selenium.webdriver.common.action_chains import ActionChains


class peru_home_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Titulo Home
        self.titulo_home = 'document.querySelector("#tabs_opciones").shadowRoot.querySelector("#tab-portabilidad-quiero-ser-cliente-1-tab > span")'

        # Titulo Banner C2C
        # self.titulo_banner_c2c = 'document.querySelector("#banner-formulario").shadowRoot.querySelector("#check_ad_2").shadowRoot.querySelector("div > div > andino-input-label").shadowRoot.querySelector("label > div.body_2-xs > andino-text > span > span")'

        # Input Telefono
        self.input_telefono = 'document.querySelector("#my_phone_id_2").shadowRoot.querySelector("#andino-input-my_phone_id_2")'

        # Boton "Lo quiero"
        self.boton_lo_quiero = 'document.querySelector("#acept_btn_primary_2").shadowRoot.querySelector("#acept_btn_primary_2")'

        # Titulo solicitud ingresada
        self.titulo_solicitud_ingresada = 'document.querySelector("#modal").shadowRoot.querySelector("div > div.eds-modal-passive__content.col-12.col-sm-12.col-md-9.col-lg-6.col-xl-6.col-xxl-6 > div.eds-modal-passive__content__heading-title > p")'
        self.titulo_solicitud_errada = 'document.querySelector("#modal-error-transversal > div > div.modal-content > div.modal-header > p")'

    def get_text_titulo_home(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_home)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    # def get_text_titulo_banner_c2c(self):
    #     try:
    #         super().carga_pagina()
    #         element = self.wait_until_element_is_visible(self.titulo_banner_c2c)
    #         if not super().is_displayed(element):
    #             print("Elemento no Desplegado.")
    #         if not super().is_enabled(element):
    #             print("Elemento no Disponible.")
    #         # element.location_once_scrolled_into_view
    #         return element.text
    #     except Exception as ex:
    #         raise Exception(str(ex))

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

    def click_boton_lo_quiero(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_lo_quiero)
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
