from pages.base_page import base_page
# from selenium.webdriver.common.action_chains import ActionChains


class peru_oferta_promociones_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Titulo Oferta Promociones
        self.titulo_oferta_promociones = 'document.querySelector("#content > main > div > div.container.text-center > h2")'

        # Boton "Quiero que me llamen"
        self.boton_quiero_que_me_llamen = 'document.querySelector("#content > main > div > section.py-3 > div > div > andino-card-sm.mt-2.cardSmModal").shadowRoot.querySelector("div")'

        # Boton "Llama al numero"
        self.boton_llama_al_numero = 'document.querySelector("#content > main > div > section.py-3 > div > div > andino-card-sm:nth-child(1)").shadowRoot.querySelector("div > a")'

        # Boton "Llama al numero" Header
        self.boton_llama_al_numero_header = 'document.querySelector("#content > main > andino-header-simple").shadowRoot.querySelector("#mi_id")'

        # Titulo Formulario
        self.titulo_formulario = 'document.querySelector("#modalContratacionOYP").shadowRoot.querySelector("div > div.eds-modal-passive__content.col-12.col-sm-12.col-md-10.col-lg-5.col-xl-5.col-xxl-4 > div > p")'

        # Titulo Formulario Modal
        self.titulo_formulario_modal = 'document.querySelector("#modalContratacionInactividadOYP > div > div > div > div.modal-content > div.title > p")'

        # Input Telefono
        self.input_telefono = 'document.querySelector("#inputPhoneModalContratacionmodalContratacionOYP").shadowRoot.querySelector("#andino-input-inputPhoneModalContratacionmodalContratacionOYP")'

        # Input Telefono Modal
        self.input_telefono_modal = 'document.querySelector("#inputPhoneModalContratacionInactividad").shadowRoot.querySelector("#andino-input-inputPhoneModalContratacionInactividad")'

        # Input Telefono Banner
        self.input_telefono_banner = 'document.querySelector("#phoneInput").shadowRoot.querySelector("#andino-input-phoneInput")'

        # Boton "Llamame ahora"
        self.boton_llamame_ahora = 'document.querySelector("#btnLlamameAhoramodalContratacionOYP").shadowRoot.querySelector("#btnLlamameAhoramodalContratacionOYP")'

        # Boton "Llamame ahora" Modal
        self.boton_llamame_ahora_modal_mobile = 'document.querySelector("#btnMobileLlamameAhoraInactividad").shadowRoot.querySelector("#btnMobileLlamameAhoraInactividad")'
        self.boton_llamame_ahora_modal_desktop = 'document.querySelector("#btnLlamameAhoraInactividad").shadowRoot.querySelector("#btnLlamameAhoraInactividad")'

        # Boton "Llamame ahora" Banner
        self.boton_llamame_ahora_banner = 'document.querySelector("#btnLlamameForm").shadowRoot.querySelector("#btnLlamameForm")'

        # Titulo solicitud ingresada
        self.titulo_solicitud_ingresada = 'document.querySelector("#modalSuccess").shadowRoot.querySelector("div > div.eds-modal-passive__content.col-12.col-sm-12.col-md-10.col-lg-6.col-xl-6.col-xxl-5 > div > p")'

        # Titulo solicitud ingresada Modal
        self.titulo_solicitud_ingresada_modal = 'document.querySelector("#modalSuccessInactividad").shadowRoot.querySelector("div > div.eds-modal-passive__content.col-12.col-sm-12.col-md-10.col-lg-10.col-xl-7.col-xxl-5 > div > p")'

    def get_text_titulo_oferta_promociones(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_oferta_promociones)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
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
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_llama_al_numero(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_llama_al_numero)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_llama_al_numero_header(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_llama_al_numero_header
            )
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

    def get_text_titulo_formulario_modal(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_formulario_modal)
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

    def send_keys_input_telefono_modal(self, telefono):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.input_telefono_modal)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.send_keys(telefono)
        except Exception as ex:
            raise Exception(str(ex))

    def send_keys_input_telefono_banner(self, telefono):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.input_telefono_banner)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.send_keys(telefono)
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_llamame_ahora(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_llamame_ahora)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_llamame_ahora_modal_mobile(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_llamame_ahora_modal_mobile
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_llamame_ahora_modal_desktop(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_llamame_ahora_modal_desktop
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_llamame_ahora_banner(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_llamame_ahora_banner
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

    def get_text_titulo_solicitud_ingresada_modal(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.titulo_solicitud_ingresada_modal
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))
