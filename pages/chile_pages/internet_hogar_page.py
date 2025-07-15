from pages.base_page import base_page


class internet_hogar_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Titulo Internet Hogar
        self.titulo_internet_hogar = 'document.querySelector("#banner-seccion-principal-1 > andino-text:nth-child(1) > h1 > span")'

        # Radio Button Sin Disney+
        self.boton_radio_sin_disney_plus = 'document.querySelector("#radio-planes-1").shadowRoot.querySelector("div > andino-input-label")'

        # Radio Button Con Disney+
        self.boton_radio_con_disney_plus = 'document.querySelector("#radio-planes-2").shadowRoot.querySelector("div > andino-input-label > andino-radio-button")'

        # Titulo Con Disney+
        self.titulo_con_disney_plus = 'document.querySelector("#banner-seccion-principal").shadowRoot.querySelector("div > div.container > div > div > div.channels > div.channels-text > p")'

        # Boton Fibra 600
        self.boton_fibra_600 = 'document.querySelector("#swiper-planes-section-1 > swiper-slide.swiper-slide-active > andino-card-planes-hibrida").shadowRoot.querySelector("div > div.header > andino-button")'

        # Boton Fibra 600+
        self.boton_fibra_600_plus = 'document.querySelector("#swiper-planes-section-2 > swiper-slide.swiper-slide-active > andino-card-planes-hibrida").shadowRoot.querySelector("div > div.header > andino-button")'

        # Boton Fibra 800
        self.boton_fibra_800 = 'document.querySelector("#swiper-planes-section-1 > swiper-slide.swiper-slide-next > andino-card-planes-hibrida").shadowRoot.querySelector("div > div.header > andino-button")'

        # Boton Fibra 800+
        self.boton_fibra_800_plus = 'document.querySelector("#swiper-planes-section-2 > swiper-slide.swiper-slide-next > andino-card-planes-hibrida").shadowRoot.querySelector("div > div.header > andino-button")'

        # Boton Fibra Giga
        self.boton_fibra_giga = 'document.querySelector("#swiper-planes-section-1 > swiper-slide:nth-child(3) > andino-card-planes-hibrida").shadowRoot.querySelector("div > div.header > andino-button")'

        # Boton Fibra Giga+
        self.boton_fibra_giga_plus = 'document.querySelector("#swiper-planes-section-2 > swiper-slide:nth-child(3) > andino-card-planes-hibrida").shadowRoot.querySelector("div > div.header > andino-button")'

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

    def click_boton_radio_sin_disney_plus(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_radio_sin_disney_plus
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_con_disney_plus(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_radio_con_disney_plus
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_con_disney_plus(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_con_disney_plus)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_fibra_600(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_fibra_600)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_fibra_600_plus(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_fibra_600_plus)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_fibra_800(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_fibra_800)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_fibra_800_plus(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_fibra_800_plus)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_fibra_giga(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_fibra_giga)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_fibra_giga_plus(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_fibra_giga_plus)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))
