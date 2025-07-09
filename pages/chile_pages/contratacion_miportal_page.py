from pages.base_page import base_page


class chile_contratacion_miportal_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Titulo Contratacion Mi Portal
        self.titulo_contratacion_miportal = 'document.querySelector("#resumen-div > div > div > div.row.mb-14.mb-md-0.d-flex.justify-content-center > div.col-12.col-md-7.mb-2 > div.card.borders.mb-3.p-4 > div > div > div > div.col-4.col-md-7.text-left > span.d-block.fw-6.font-small.font-md-large")'

    def get_text_titulo_contratacion_miportal(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.titulo_contratacion_miportal
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))
