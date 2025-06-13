from pages.base_page import base_page


class doble_pack_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Titulo Doble Pack
        self.titulo_doble_pack = 'document.querySelector("#banner-seccion-principal > andino-text:nth-child(1)")'

        # Radio Plan Fibra 600
        self.boton_radio_fibra_600 = 'document.querySelector("#radio-planes-1").shadowRoot.querySelector("div > andino-input-label > andino-radio-button")'

        # Radio Plan Fibra 800
        self.boton_radio_fibra_800 = 'document.querySelector("#radio-planes-2").shadowRoot.querySelector("div > andino-input-label > andino-radio-button")'

        # Radio Plan Fibra Giga
        self.boton_radio_fibra_giga = 'document.querySelector("#radio-planes-3").shadowRoot.querySelector("div > andino-input-label > andino-radio-button")'

        # Boton Fibra 600 TV Lite
        self.boton_fibra_600_tv_lite = 'document.querySelector("#swiper-planes-section-1 > swiper-slide.swiper-slide-next > andino-card-planes-hibrida").shadowRoot.querySelector("div > div.header > andino-button")'

        # Boton 600 TV Full+
        self.boton_fibra_600_tv_full_plus = 'document.querySelector("#swiper-planes-section-1 > swiper-slide.swiper-slide-active > andino-card-planes-hibrida").shadowRoot.querySelector("div > div.header > andino-button")'

        # Boton Fibra 800 TV Lite
        self.boton_fibra_800_tv_lite = 'document.querySelector("#swiper-planes-section-2 > swiper-slide.swiper-slide-next > andino-card-planes-hibrida").shadowRoot.querySelector("div > div.header > andino-button")'

        # Boton Fibra 800 TV Full+
        self.boton_fibra_800_tv_full_plus = 'document.querySelector("#swiper-planes-section-2 > swiper-slide.swiper-slide-active > andino-card-planes-hibrida").shadowRoot.querySelector("div > div.header > andino-button")'

        # Boton Fibra Giga TV Lite
        self.boton_fibra_giga_tv_lite = 'document.querySelector("#swiper-planes-section-3 > swiper-slide.swiper-slide-next > andino-card-planes-hibrida").shadowRoot.querySelector("div > div.header > andino-button")'

        # Boton Fibra Giga TV Full+
        self.boton_fibra_giga_tv_full_plus = 'document.querySelector("#swiper-planes-section-3 > swiper-slide.swiper-slide-active > andino-card-planes-hibrida").shadowRoot.querySelector("div > div.header > andino-button")'

    def get_text_titulo_doble_pack(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_doble_pack)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_fibra_600(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_radio_fibra_600)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_fibra_800(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_radio_fibra_800)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_fibra_giga(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_radio_fibra_giga)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_fibra_600_tv_lite(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_fibra_600_tv_lite)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_fibra_600_tv_full_plus(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_fibra_600_tv_full_plus
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_fibra_800_tv_lite(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_fibra_800_tv_lite)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_fibra_800_tv_full_plus(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_fibra_800_tv_full_plus
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_fibra_giga_tv_lite(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_fibra_giga_tv_lite)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_fibra_giga_tv_full_plus(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_fibra_giga_tv_full_plus
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))
