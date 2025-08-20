from pages.base_page import base_page


class chile_planes_linea_nueva_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Titulo Planes Oferta Línea Nueva
        self.titulo_planes_linea_nueva = 'document.querySelector("#section-cards-movil > andino-tabs").shadowRoot.querySelector("#tab-portabilidad-linea-nueva-2-tab > span.body_2")'

        # Boton Plan 150 Gigas
        self.boton_plan_150_gigas = 'document.querySelector("#card-planes").shadowRoot.querySelector("swiper-container > swiper-slide.swiper-slide-active > div > div.footer > andino-button:nth-child(1)")'

        # Boton Plan 450 Gigas
        self.boton_plan_450_gigas = 'document.querySelector("#card-planes").shadowRoot.querySelector("swiper-container > swiper-slide.swiper-slide-next > div > div.footer > andino-button:nth-child(1)")'

        # Boton Plan Libre
        self.boton_plan_libre = 'document.querySelector("#card-planes").shadowRoot.querySelector("swiper-container > swiper-slide:nth-child(3) > div > div.footer > andino-button:nth-child(1)")'

        # Boton Plan Libre con Roaming
        self.boton_plan_libre_con_roaming = 'document.querySelector("#card-planes").shadowRoot.querySelector("swiper-container > swiper-slide:nth-child(4) > div > div.footer > andino-button:nth-child(1)")'

        # Boton Plan Libre con Roaming Pro
        self.boton_plan_libre_con_roaming_pro = 'document.querySelector("#card-planes").shadowRoot.querySelector("swiper-container > swiper-slide:nth-child(5) > div > div.footer > andino-button:nth-child(1)")'

        # Boton Next Slide Swiper
        self.boton_next_slide_swiper = 'document.querySelector("#card-planes").shadowRoot.querySelector("swiper-container").shadowRoot.querySelector("div > div.swiper-button-next")'

    def get_text_titulo_planes_linea_nueva(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_planes_linea_nueva)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_plan_150_gigas(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_plan_150_gigas)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_plan_450_gigas(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_plan_450_gigas)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_plan_libre(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_plan_libre)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_plan_libre_con_roaming(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_plan_libre_con_roaming
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_plan_libre_con_roaming_pro(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_plan_libre_con_roaming_pro
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_next_slide_swiper(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_next_slide_swiper)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))
