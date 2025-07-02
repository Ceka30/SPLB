import os
import pandas as pd
from pages.base_page import base_page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class chile_home_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.TIPOS_EVENTO = {"load", "go_to", "click_to_action", "interaction"}

        # Titulo Home
        self.titulo_home = 'document.querySelector("#contenedorMundoEntel > div.col-12.text-sm-center > h2")'

        # Boton Slider Carrusel Next
        self.boton_slider_carrusel_next = 'document.querySelector("#contenedorBanner > andino-banner-hero").shadowRoot.querySelector("swiper-container").shadowRoot.querySelector("div > div.swiper-button-next")'

        # Boton Slider Carrusel Prev
        self.boton_slider_carrusel_prev = 'document.querySelector("#contenedorBanner > andino-banner-hero").shadowRoot.querySelector("swiper-container").shadowRoot.querySelector("div > div.swiper-button-prev")'

        # Boton Banner 1
        self.boton_banner_1 = 'document.querySelector("#section-nav-home > andino-navigationbar-accesos-directos").shadowRoot.querySelector("div > div > a.item.dots")'

        # Boton banner 2
        self.boton_banner_2 = 'document.querySelector("#contenedorBanner > andino-banner-hero").shadowRoot.querySelector("swiper-container > swiper-slide.swiper-slide-active > div > div.body.no-second-body > div.second-content.mb-custom > andino-button")'

        # Boton banner 3
        self.boton_banner_3 = 'document.querySelector("#contenedorBanner > andino-banner-hero").shadowRoot.querySelector("swiper-container > swiper-slide.swiper-slide-active > div > div.body.no-second-body > div.second-content.mb-custom > andino-button")'

        # Boton banner 4
        self.boton_banner_4 = 'document.querySelector("#contenedorBanner > andino-banner-hero").shadowRoot.querySelector("swiper-container > swiper-slide.swiper-slide-active > div > div.body.no-second-body > div.second-content.mb-custom > andino-button")'

        # Boton banner 5
        self.boton_banner_5 = 'document.querySelector("#contenedorBanner > andino-banner-hero").shadowRoot.querySelector("swiper-container > swiper-slide.swiper-slide-active > div > div.body.no-second-body > div.second-content.mb-custom > andino-button")'

        # Boton banner 6
        self.boton_banner_6 = 'document.querySelector("#contenedorBanner > andino-banner-hero").shadowRoot.querySelector("swiper-container > swiper-slide.swiper-slide-active > div > div.body.no-second-body > div.second-content.mb-custom > andino-button")'

    def obtener_marcas_ctr(self):
        data_layer = self.driver.execute_script("return window.dataLayer || []")
        filas = []

        for item in data_layer:
            if not isinstance(item, dict):
                continue

            ev = item.get("event")
            if ev not in self.TIPOS_EVENTO:
                continue

            if not (item.get("location") and item.get("section")):
                continue

            if ev == "load" and item.get("variant_1"):
                continue

            identificador = item.get("title") or item.get("event_label") or ""

            filas.append(
                {
                    "event": ev,
                    "location": item["location"],
                    "section": item["section"],
                    "identificador": identificador,
                }
            )

        return pd.DataFrame(filas)

    def guardar_en_excel(self, df, carpeta, archivo):
        os.makedirs(carpeta, exist_ok=True)
        ruta = os.path.join(carpeta, archivo)
        df.to_excel(ruta, index=False)

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

    def click_boton_slider_carrusel_next(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_slider_carrusel_next
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(
                Keys.CONTROL
            ).perform()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_slider_carrusel_prev(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_slider_carrusel_prev
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(
                Keys.CONTROL
            ).perform()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_banner_1(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_banner_1)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(
                Keys.CONTROL
            ).perform()
            # element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_banner_2(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_banner_2)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(
                Keys.CONTROL
            ).perform()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_banner_3(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_banner_3)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(
                Keys.CONTROL
            ).perform()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_banner_4(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_banner_4)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(
                Keys.CONTROL
            ).perform()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_banner_5(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_banner_5)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(
                Keys.CONTROL
            ).perform()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_banner_6(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_banner_6)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(
                Keys.CONTROL
            ).perform()
        except Exception as ex:
            raise Exception(str(ex))
