from pages.base_page import base_page


class television_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Titulo Internet Hogar
        self.titulo_television_hogar = 'document.querySelector("#banner-seccion-entel-tv > andino-text:nth-child(1)")'

        # Boton TV Full+
        self.boton_tv_full_plus = 'document.querySelector("#tab-planes-hogar-entel-tv-4 > div > div > div > section > div > swiper-container > swiper-slide.swiper-slide-next > andino-card-planes-hibrida").shadowRoot.querySelector("div > div.header > andino-button")'

        # Boton TV Lite
        self.boton_tv_lite = 'document.querySelector("#tab-planes-hogar-entel-tv-4 > div > div > div > section > div > swiper-container > swiper-slide.swiper-slide-active > andino-card-planes-hibrida").shadowRoot.querySelector("div > div.header > andino-button")'

    def get_text_titulo_television_hogar(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_television_hogar)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_tv_full_plus(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_tv_full_plus)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_tv_lite(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_tv_lite)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))
