from pages.base_page import base_page


class chile_planes_plan_adicional_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Titulo Planes Plan Adicional
        self.titulo_planes_plan_adicional = 'document.querySelector("#custom > main > section.contenedor-banner-seccion-transversal > div > andino-banner-seccion > andino-text:nth-child(1)")'

        # Boton "Conocer mi oferta"
        self.boton_conocer_mi_oferta = 'document.querySelector("#cardHorizontalPlan").shadowRoot.querySelector("#btn-open-modal-contratar-planes-adicionales").shadowRoot.querySelector("#btn-open-modal-contratar-planes-adicionales")'

        # Titulo Side Bar
        self.titulo_side_bar = 'document.querySelector("#modal-title")'

        # Boton Contratar por telefono
        self.boton_contratar_por_telefono = (
            'document.querySelector("#linea-nueva-2-0 > eds-card-small > div")'
        )

        # Titulo Formulario
        self.titulo_formulario = (
            'document.querySelector("#section-contratar-ejecutivo > p.body_2-xs.mb-3")'
        )

        # Input Telefono
        self.input_telefono = 'document.querySelector("#numeric02-conecta")'

        # Boton quiero que me llamen
        self.boton_quiero_que_me_llamen = (
            'document.querySelector("#eds-btn-llamen-conecta")'
        )

        # Titulo Solicitud Ingresada
        self.titulo_solicitud_ingresada = (
            'document.querySelector("#succes-view-c2c > h3")'
        )

    def get_text_titulo_planes_plan_adicional(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.titulo_planes_plan_adicional
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_conocer_mi_oferta(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_conocer_mi_oferta)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_side_bar(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_side_bar)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_contratar_por_telefono(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_contratar_por_telefono
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_formulario(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_formulario)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
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
            # element.location_once_scrolled_into_view
            element.send_keys(telefono)
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
