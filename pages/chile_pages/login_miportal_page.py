import time
from pages.base_page import base_page


class chile_login_miportal_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Titulo Login Mi Portal
        self.titulo_login_miportal = 'document.querySelector("#identification-div > div > div.row.justify-content-center > div > span")'

        # Boton Soy Cliente
        self.boton_soy_cliente = 'document.querySelector("#client")'

        # Boton Ingresar con contreseña
        self.boton_ingresar_con_contraseña = 'document.querySelector("#identification-div > div > div.row.justify-content-center > div > div.card.mb-3 > div > button.btn.btn-outline-primary.btn-block.fw-6.mb-3")'

        # Input Rut
        self.input_rut = 'document.querySelector("#identificationNumber")'

        # Input telefono
        self.input_telefono = 'document.querySelector("#phoneNumber")'

        # Input Contraseña
        self.input_contraseña = 'document.querySelector("#password")'

        # Boton Identificaion
        self.boton_identificacion = 'document.querySelector("#identification-div > div > div.row.justify-content-center > div > div.card.mb-4 > div > div.btn-con > button.default-button.btn-radius.rounded-pill.font-weight-bold.mb-4")'

        # loader
        self.loader = 'document.querySelector("#loader > div")'

    def get_text_titulo_login_miportal(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_login_miportal)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_soy_cliente(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_soy_cliente)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_ingresar_con_contraseña(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_ingresar_con_contraseña
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def send_keys_input_rut(self, texto):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.input_rut)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.send_keys(texto)
        except Exception as ex:
            raise Exception(str(ex))

    def send_keys_input_telefono(self, texto):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.input_telefono)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.send_keys(texto)
        except Exception as ex:
            raise Exception(str(ex))

    def send_keys_input_contraseña(self, texto):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.input_contraseña)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.send_keys(texto)
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_identificacion(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_identificacion)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def wait_loader(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.loader)
            while element.is_displayed():
                time.sleep(1)
        except Exception:
            pass
