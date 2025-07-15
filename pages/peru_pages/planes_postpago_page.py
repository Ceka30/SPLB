from pages.base_page import base_page


class peru_planes_postpago_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Titulo Planes Postpago Portabilidad
        self.titulo_planes_postpago_portabilidad = 'document.querySelector("#custom > main > section.mb-5.pt-4.pt-md-4.container.o-hidden > p")'

        # Boton Soy Cliente Entel
        self.boton_soy_cliente_entel = 'ddocument.querySelector("#tabs_opciones").shadowRoot.querySelector("#tab-portabilidad-soy-cliente-entel-2-tab")'

        # Titulo Planes Postpago Linaa Adicional
        self.titulo_planes_postpago_linea_adicional = 'document.querySelector("#banner-small-image-principal").shadowRoot.querySelector("div > div.header-content.false > div.epigraph-content > andino-text-styler").shadowRoot.querySelector("p > span")'

        # Boton Plan Power 29.90
        self.boton_plan_power_29_90 = 'document.querySelector("#card-planes").shadowRoot.querySelector("#plan-simple")'

        # Boton Plan Power 39.90
        self.boton_plan_power_39_90 = 'document.querySelector("#card-planes").shadowRoot.querySelector("#plan-basico")'

        # Boton Plan Power Ilim 69.90
        self.boton_plan_power_ilim_69_90 = 'document.querySelector("#card-planes").shadowRoot.querySelector("#plan-premium")'

        # Boton Plan Power Ilim 79.90 SD
        self.boton_plan_power_ilim_79_90_sd = 'document.querySelector("#card-planes").shadowRoot.querySelector("#plan-ilimitado-basico")'

        # Boton Plan Power Ilim 99.90 HD
        self.boton_plan_power_ilim_99_90_sd = 'document.querySelector("#card-planes").shadowRoot.querySelector("#plan-ilimitado-plus")'

        # Boton Next Slide Swiper
        self.boton_next_slide_swiper = 'document.querySelector("#card-planes").shadowRoot.querySelector("swiper-container").shadowRoot.querySelector("div > div.swiper-button-next")'

        # Boton Linea Adicional
        self.boton_linea_adicional = 'document.querySelector("#plan-linea-adicional-destacado").shadowRoot.querySelector("#btn-contratar-soy-cliente")'

        # Titulo Formulario
        self.titulo_formulario = 'document.querySelector("#modalLineasAdicionales > p")'

        # Input Telefono
        self.input_telefono = 'document.querySelector("#input-lineas-adicionales").shadowRoot.querySelector("#andino-input-input-lineas-adicionales")'

        # Boton "Llamenme Ahora"
        self.boton_llamenme_ahora = 'document.querySelector("#btn-lineas-adicionales")'

        # Titulo Solicitud Ingresada
        self.titulo_solicitud_ingresada = 'document.querySelector("#modal-success-planes").shadowRoot.querySelector("div > div.eds-modal-passive__content.col-12.col-sm-12.col-md-9.col-lg-6.col-xl-6.col-xxl-6 > div.eds-modal-passive__content__heading-title > p")'

    def get_text_titulo_planes_postpago_portabilidad(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.titulo_planes_postpago_portabilidad
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_soy_cliente_entel(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_soy_cliente_entel)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_planes_postpago_linea_adicional(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.titulo_planes_postpago_linea_adicional
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_plan_power_29_90(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_plan_power_29_90)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_plan_power_39_90(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_plan_power_39_90)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_plan_power_ilim_69_90(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_plan_power_ilim_69_90
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_plan_power_ilim_79_90_sd(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_plan_power_ilim_79_90_sd
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_plan_power_ilim_99_90_sd(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_plan_power_ilim_99_90_sd
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
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
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_linea_adicional(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_linea_adicional)
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

    def click_boton_llamenme_ahora(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_llamenme_ahora)
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
