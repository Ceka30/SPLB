from pages.base_page import base_page


class chile_cookies_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Titulo Cookies "Política de cookies"
        self.titulo_cookies = 'document.querySelector("#onetrust-policy-text > a")'

        # Boton Aceptar Cookies
        self.boton_aceptar_cookies = (
            'document.querySelector("#onetrust-accept-btn-handler")'
        )

    def get_text_titulo_cookies(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_cookies)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_aceptar_cookies(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_aceptar_cookies)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))
