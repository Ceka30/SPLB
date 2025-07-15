from pages.base_page import base_page


class peru_internet_hogar_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Titulo Internet Hogar
        self.titulo_internet_hogar = 'document.querySelector("#custom > main > section:nth-child(6) > andino-banner-seccion-full > andino-text:nth-child(1) > h1 > span")'

        # Boton Fibra 100 Mbps
        self.boton_fibra_100_mbps = 'document.querySelector("#custom > main > section.bg-section-planes.py-5.mt-0.mb-0 > div > swiper-container > swiper-slide.swiper-slide-active > andino-card-planes-hibrida").shadowRoot.querySelector("div > div.header > andino-button")'

        # Boton Fibra 300 Mbps
        self.boton_fibra_300_mbps = 'document.querySelector("#custom > main > section.bg-section-planes.py-5.mt-0.mb-0 > div > swiper-container > swiper-slide.swiper-slide-next > andino-card-planes-hibrida").shadowRoot.querySelector("div > div.header > andino-button")'

        # Titulo Modal C2C
        self.titulo_modal_c2c = 'document.querySelector("#modal_card_planes_ecommerce > div > div > andino-text-styler")'

        # Input Numero
        self.input_numero = 'document.querySelector("#numero_celular").shadowRoot.querySelector("#andino-input-numero_celular")'

        # Boton Radio Aceptar Envio
        self.boton_radio_aceptar_envio = 'document.querySelector("#terminos_y_condiciones").shadowRoot.querySelector("#terminos_y_condiciones")'

        # Botoon Llamame
        self.boton_llamame = 'document.querySelector("#btn_quiero_que_me_llamen").shadowRoot.querySelector("#btn_quiero_que_me_llamen")'

        # Titulo Solicitud Ingresada
        self.titulo_solicitud_ingresada = 'document.querySelector("#modal-success-planes").shadowRoot.querySelector("div > div.eds-modal-passive__content.col-12.col-sm-12.col-md-9.col-lg-6.col-xl-6.col-xxl-6 > div.eds-modal-passive__content__heading-title > p")'

    def get_text_titulo_internet_hogar(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_internet_hogar)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_fibra_100_mbps(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_fibra_100_mbps)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_fibra_300_mbps(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_fibra_300_mbps)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_modal_c2c(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_modal_c2c)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def send_keys_input_numero(self, num):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.input_numero)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.send_keys(num)
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_aceptar_envio(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_radio_aceptar_envio)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_llamame(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_llamame)
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
