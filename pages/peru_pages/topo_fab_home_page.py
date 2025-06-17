from pages.base_page import base_page
# from selenium.webdriver.common.action_chains import ActionChains


class peru_topo_fab_home_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Titulo Home
        self.titulo_home = 'document.querySelector("#tabs_opciones").shadowRoot.querySelector("#tab-portabilidad-quiero-ser-cliente-1-tab > span")'

        # Boton "¿Quieres contratar?" Topo Fab"
        self.boton_quieres_contratar = 'document.querySelector("#fabHomeDinamic")'

        # Titulo Fab Internet Hogar
        self.titulo_fab_home = 'document.querySelector("#modalPrincipalDinamic").shadowRoot.querySelector("div > div.eds-modal-passive__content.col-12.col-sm-12.col-md-6.col-lg-4.col-xl-4.col-xxl-4 > div.eds-modal-passive__content__heading-title > p")'

        # Boton "Contratar por telefono"
        self.boton_planes_moviles = 'document.querySelector("#modalPrincipalDinamic").shadowRoot.querySelector("div > div.eds-modal-passive__content.col-12.col-sm-12.col-md-6.col-lg-4.col-xl-4.col-xxl-4 > div.eds-modal-passive__content__channels.small > andino-card-sm:nth-child(1)")'

        # Titulo "Te ayudamos a contratar"
        self.titulo_te_ayudamos_a_contratar = 'document.querySelector("#modalMovilDinamic").shadowRoot.querySelector("div > div.eds-modal-passive__content.col-12.col-sm-12.col-md-12.col-lg-10.col-xl-4.col-xxl-4 > div > p")'

        # Input Telefono
        self.input_telefono = 'document.querySelector("#inputMovilForm").shadowRoot.querySelector("#andino-input-inputMovilForm")'

        # Boton "Quiero que me llamen"
        self.boton_quiero_que_me_llamen = (
            'document.querySelector("#contratarMovilDinamic")'
        )

        # Titulo solicitud ingresada
        self.titulo_solicitud_ingresada = 'document.querySelector("#modalExitoRequest").shadowRoot.querySelector("div > div.eds-modal-passive__content.col-12.col-sm-12.col-md-9.col-lg-6.col-xl-6.col-xxl-6 > div.eds-modal-passive__content__heading-title > p")'
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

    def click_boton_quieres_contratar(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_quieres_contratar)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_fab_home(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_fab_home)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_planes_moviles(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_planes_moviles)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_te_ayudamos_a_contratar(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.titulo_te_ayudamos_a_contratar
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
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

    def click_boton_quiero_que_me_llamen(self):
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
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))
