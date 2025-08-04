import random
import time
from pages.base_page import base_page
from selenium.webdriver.common.action_chains import ActionChains


class chile_ofertas_movil_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Titulo Ofertas Movil
        self.titulo_ofertas_movil = 'document.querySelector("#planes-moviles-1-0-tab")'

        # Boton Modal "Quiero que me llamen"
        self.boton_modal_quiero_que_me_llamen = (
            'document.querySelector("#headerBtnC2C")'
        )

        # Titulo Modal
        self.titulo_modal = 'document.querySelector("#C2CModal > div > div.modal-content.medium-desk > div.modal-header > p")'

        # Input Telefono
        self.input_telefono = 'document.querySelector("#phoneC2C")'

        # Boton "Quiero que me llamen"
        self.boton_quiero_que_me_llamen = 'document.querySelector("#btnSubmitC2C")'

        # Titulo Soliocitud ingresada
        self.titulo_solicitud_ingresada = 'document.querySelector("#C2CModalSuccess > div > div.modal-content > div.modal-header > p")'

    def get_text_titulo_ofertas_movil(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_ofertas_movil)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            self.driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'})",
                element,
            )
            ActionChains(self.driver).move_to_element(element).pause(
                random.uniform(0.5, 2)
            ).perform()

            time.sleep(random.uniform(0.5, 2))
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_modal_quiero_que_me_llamen(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_modal_quiero_que_me_llamen
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            self.driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'})",
                element,
            )
            ActionChains(self.driver).move_to_element(element).pause(
                random.uniform(0.5, 2)
            ).click().perform()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_modal(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_modal)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            self.driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'})",
                element,
            )
            ActionChains(self.driver).move_to_element(element).pause(
                random.uniform(0.5, 2)
            ).perform()

            time.sleep(random.uniform(0.5, 2))
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
            self.driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'})",
                element,
            )
            ActionChains(self.driver).move_to_element(element).pause(
                random.uniform(0.5, 2)
            ).click().perform()

            # Escribir dígito por dígito con pausas
            for digito in telefono:
                element.send_keys(digito)
                time.sleep(random.uniform(0.5, 2))
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
            self.driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'})",
                element,
            )
            ActionChains(self.driver).move_to_element(element).pause(
                random.uniform(0.5, 2)
            ).click().perform()
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
            self.driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'})",
                element,
            )
            ActionChains(self.driver).move_to_element(element).pause(
                random.uniform(0.5, 2)
            ).perform()

            time.sleep(random.uniform(0.5, 2))
            return element.text
        except Exception as ex:
            raise Exception(str(ex))
