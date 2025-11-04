from pages.base_page import base_page
# from selenium.webdriver.common.action_chains import ActionChains


class peru_topo_fab_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Titulo Home
        self.titulo_home = 'document.querySelector("#tabs_opciones").shadowRoot.querySelector("#tab-portabilidad-quiero-ser-cliente-1-tab > span")'

        # Titulo telefonia fija
        self.titulo_telefonia_fija = 'document.querySelector("#custom > main > section.contenedor-banner-telefonia-hogar > div > div:nth-child(1) > andino-text-styler").shadowRoot.querySelector("h2 > span")'

        # Titulo Prepago Bolsas
        self.titulo_prepago_bolsas = 'document.querySelector("#custom > main > section.pt-md-5.pb-md-5.pt-4.pb-4.seccion_tabs_bolsas > div > div > div.col-12.pb-4 > div > andino-text-styler").shadowRoot.querySelector("h3")'

        # Titulo Prepago Planes
        self.titulo_prepago_planes = 'document.querySelector("#custom > main > div.container.py-3 > div > div > andino-banner-small-image").shadowRoot.querySelector("div > div.header-content.false > div.title-content > andino-text-styler").shadowRoot.querySelector("p > span")'

        # Titulo Prepago Recargas
        self.titulo_prepago_recargas = 'document.querySelector("#custom > main > div:nth-child(5) > div > div > h3")'

        # Titulo Prepago Beneficios
        self.titulo_prepago_beneficios = 'document.querySelector("#custom > main > div.container.py-3 > div > div > andino-banner-small-image").shadowRoot.querySelector("div > div.header-content.false > div.title-content > andino-text-styler").shadowRoot.querySelector("p > span")'

        # Titulo RecambioPower
        # self.titulo_recambiopower = 'document.querySelector("#custom > main > div.container.py-3 > div > div > andino-banner-small-image").shadowRoot.querySelector("div > div.header-content.false > div.title-content > andino-text-styler").shadowRoot.querySelector("p > span")'
        self.titulo_recambiopower = 'document.querySelector("#custom > main > div.container.py-md-5.py-4 > div > div.col-lg-4.offset-lg-1 > h3")'
        # Titulo Seguros
        self.titulo_seguros = 'document.querySelector("#banner-seccion-principal > andino-text:nth-child(1) > p > span")'

        # Titulo Chip Autoactivado
        self.titulo_chip_autoactivado = 'document.querySelector("#custom > main > div.container.py-3 > div > div > andino-banner-small-image").shadowRoot.querySelector("div > div.header-content.false > div.title-content > andino-text-styler").shadowRoot.querySelector("p > span")'

        # Titulo Apple
        # self.titulo_apple = 'document.querySelector("#custom > main > div:nth-child(8) > div > div > andino-banner-complementario-imagen").shadowRoot.querySelector("div > div.header-content > slot:nth-child(2) > andino-text-styler").shadowRoot.querySelector("p > span")'
        self.titulo_apple = 'document.querySelector("#custom > main > div:nth-child(8) > div > div > div > div > andino-banner-complementario-imagen").shadowRoot.querySelector("div > div.header-content > slot:nth-child(2) > andino-text-styler").shadowRoot.querySelector("p > span")'

        # Titulo Ayuda
        self.titulo_ayuda = 'document.querySelector("#banner-seccion-principal > andino-text:nth-child(2) > p > span")'

        # Titulo Tiendas
        self.titulo_tiendas = 'document.querySelector("#custom > main > section:nth-child(3) > andino-banner-seccion-full > andino-text > p > span")'

        # Titulo Info Abonados
        self.titulo_info_abonados = 'document.querySelector("#custom > main > section:nth-child(7) > div > h2 > b")'

        # Boton "¿Quieres contratar?" Topo Fab"
        self.boton_quieres_contratar = 'document.querySelector("#fabHomeDinamic")'

        # Boton "¿Quieres contratar?" Topo Fab OFERTAS Y PROMOCIONES"
        self.boton_quieres_contratar_ofertas_promociones = (
            'document.querySelector("#fabOYP")'
        )

        # Titulo Fab Internet Hogar
        self.titulo_fab_home = 'document.querySelector("#modalPrincipalDinamic").shadowRoot.querySelector("div > div.eds-modal-passive__content.col-12.col-sm-12.col-md-6.col-lg-4.col-xl-4.col-xxl-4 > div.eds-modal-passive__content__heading-title > p")'

        # Boton "Contratar por telefono"
        self.boton_planes_moviles = 'document.querySelector("#modalPrincipalDinamic").shadowRoot.querySelector("div > div.eds-modal-passive__content.col-12.col-sm-12.col-md-6.col-lg-4.col-xl-4.col-xxl-4 > div.eds-modal-passive__content__channels.small > andino-card-sm:nth-child(1)")'

        # Titulo "Te ayudamos a contratar"
        self.titulo_te_ayudamos_a_contratar = 'document.querySelector("#modalMovilDinamic").shadowRoot.querySelector("div > div.eds-modal-passive__content.col-12.col-sm-12.col-md-12.col-lg-10.col-xl-4.col-xxl-4 > div > p")'

        # Input Telefono
        self.input_telefono = 'document.querySelector("#inputMovilFormFab").shadowRoot.querySelector("#andino-input-inputMovilFormFab")'

        # Boton "Quiero que me llamen"
        self.boton_quiero_que_me_llamen = (
            'document.querySelector("#contratarMovilDinamic")'
        )

        # Titulo solicitud ingresada
        self.titulo_solicitud_ingresada = 'document.querySelector("#modalExitoRequest").shadowRoot.querySelector("div > div.eds-modal-passive__content.col-12.col-sm-12.col-md-9.col-lg-6.col-xl-6.col-xxl-6 > div.eds-modal-passive__content__heading-title > p")'
        self.titulo_solicitud_errada = 'document.querySelector("#modal-error-transversal > div > div.modal-content > div.modal-header > p")'

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

    def get_text_titulo_telefonia_fija(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_telefonia_fija)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_prepago_bolsas(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_prepago_bolsas)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_prepago_planes(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_prepago_planes)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_prepago_recargas(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_prepago_recargas)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_prepago_beneficios(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_prepago_beneficios)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_recambiopower(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_recambiopower)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_seguros(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_seguros)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_chip_autoactivado(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_chip_autoactivado)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_apple(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_apple)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_ayuda(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_ayuda)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_tiendas(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_tiendas)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_info_abonados(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_info_abonados)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_quieres_contratar(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_quieres_contratar)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_quieres_contratar_ofertas_promociones(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_quieres_contratar_ofertas_promociones
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_fab_home(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_fab_home)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_planes_moviles(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_planes_moviles)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_te_ayudamos_a_contratar(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.titulo_te_ayudamos_a_contratar
            )
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
            element.location_once_scrolled_into_view
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
