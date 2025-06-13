from pages.base_page import base_page


class chile_recomendador_page(base_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        #################### SELECTORES GENERALES ####################

        # Titulo Acceso Recomendador
        self.titulo_recomendador = (
            'document.querySelector("#root > main > div > div > div > div > h1")'
        )

        # Boton Continuar
        self.boton_continuar = 'document.querySelector("#root > main > div > div > div > div > div.row.justify-content-center > div.col-10.col-lg-8.pt-4 > andino-button")'

        # Titulo Recomendacion
        self.titulo_recomendacion = 'document.querySelector("#root > main > div > div > andino-banner-seccion-full > andino-text:nth-child(1)")'

        # Titulo Plan Ideal
        self.titulo_plan_ideal = 'document.querySelector("#root > main > div > div > andino-banner-seccion-full").shadowRoot.querySelector("div > div.container > div > andino-card-planes-horizontal").shadowRoot.querySelector("div > div > div.header > div.type > andino-text-styler").shadowRoot.querySelector("p > span:nth-child(3)")'

        # Boton radio Internet Fibra
        self.boton_checkbox_internet_fibra = 'document.querySelector("#servicios-INT").shadowRoot.querySelector("#servicios-INT")'

        # Boton radio Television
        self.boton_checkbox_television = 'document.querySelector("#servicios-TV").shadowRoot.querySelector("#servicios-TV")'

        # Boton radio Telefonia
        self.boton_checkbox_telefonia = 'document.querySelector("#servicios-TLF").shadowRoot.querySelector("#servicios-TLF")'

        #################### SELECTORES TRIPLE PACK ####################

        # Titulo Tipo Hogar
        self.titulo_tipo_hogar = 'document.querySelector("#root > main > div > div > div > div > div.pb-2 > andino-text")'

        # Boton radio casa
        self.boton_radio_casa = 'document.querySelector("#casa").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Boton radio departamento
        self.boton_radio_departamento = 'document.querySelector("#depto").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Titulo Pisos
        self.titulo_pisos = 'document.querySelector("#root > main > div > div > div > div > div.pb-2 > andino-text")'

        # Boton radio 1 piso
        self.boton_radio_1_piso = r'document.querySelector("#\\31 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Boton radio 2 pisos o mas
        self.boton_radio_2_pisos_mas = r'document.querySelector("#\\32 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Titulo Espacios
        self.titulo_espacios = 'document.querySelector("#root > main > div > div > div > div > div.pb-2 > andino-text")'

        # Boton radio 1 espacio
        self.boton_radio_1_espacio = r'document.querySelector("#\\31 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Boton radio 2 espacios
        # self.boton_radio_2_espacios = r'document.querySelector("#\\31 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Boton radio 3 espacios
        self.boton_radio_3_espacios = r'document.querySelector("#\\32 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Boton radio 4 espacios
        # self.boton_radio_4_espacios = r'document.querySelector("#\\32 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Boton radio 5 espacios o mas
        self.boton_radio_5_espacios_mas = r'document.querySelector("#\\33 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Titulo Dispositivos
        self.titulo_dispositivos = 'document.querySelector("#root > main > div > div > div > div > div.pb-2 > andino-text")'

        # Boton radio menos 8 dispositvos
        self.boton_radio_menos_8_dispositivos = r'document.querySelector("#\\31 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Boton radio entre 8 y 16 dispositivos
        self.boton_radio_entre_8_16_dispositivos = r'document.querySelector("#\\32 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Boton radio 16 dispositivos o mas
        self.boton_radio_16_dispositivos_mas = r'document.querySelector("#\\33 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Titulo Utilizacion
        self.titulo_utilizacion = 'document.querySelector("#root > main > div > div > div > div > div.pb-2 > andino-text")'

        # Boton radio utilizacion basico
        self.boton_radio_utilizacion_basico = r'document.querySelector("#\\31 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Boton radio utilizacion medio
        # self.boton_radio_utilizacion_medio = r'document.querySelector("#\\31 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Boton radio utilizacion alto
        self.boton_radio_utilizacion_alto = r'document.querySelector("#\\32 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Titulo TV simultaneas
        self.titulo_tv_simultaneas = 'document.querySelector("#root > main > div > div > div > div > div.pb-2 > andino-text")'

        # Boton radio 1 a 2 dispositivos
        self.boton_radio_1_2_dispositivos = r'document.querySelector("#\\31 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Boton radio 3 o mas dispositivos
        self.boton_radio_3_dispositivos_mas = r'document.querySelector("#\\32 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        #################### SELECTORES MONO PACK TELEVISION - INTERNET ####################

        # Titulo Compania Actual
        self.titulo_compania_actual = 'document.querySelector("#root > main > div > div > div > div > div.pb-2 > andino-text")'

        # Boton radio compañia actual Entel
        self.boton_radio_compania_actual_entel = r'document.querySelector("#\\31 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Boton radio compañia actual Otra compañia
        self.boton_radio_compania_actual_otra = r'document.querySelector("#\\32 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Boton radio compañia actual Utilizo internet de mi celular
        self.boton_radio_compania_actual_internet_celular = r'document.querySelector("#\\33 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Titulo Internet fuera del hogar
        self.titulo_internet_fuera_hogar = 'document.querySelector("#root > main > div > div > div > div > div.pb-2 > andino-text")'

        # Boton radio internet fuera del hogar si
        self.boton_radio_internet_fuera_hogar_si = r'document.querySelector("#\\31 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Boton radio internet fuera del hogar no
        self.boton_radio_internet_fuera_hogar_no = r'document.querySelector("#\\32 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Titulo Contenido
        self.titulo_contenido = 'document.querySelector("#root > main > div > div > div > div > div.pb-2 > andino-text")'

        # Boton checkbox contenido series y peliculas
        self.boton_checkbox_contenido_series_peliculas = 'document.querySelector("#contenido-1").shadowRoot.querySelector("#contenido-1")'

        # Boton checkbox contenido noticias
        self.boton_checkbox_contenido_noticias = 'document.querySelector("#contenido-2").shadowRoot.querySelector("#contenido-2")'

        # Boton checkbox contenido deportes
        self.boton_checkbox_contenido_deportes = 'document.querySelector("#contenido-3").shadowRoot.querySelector("#contenido-3")'

        # Boton checkbox contenido streaming
        self.boton_checkbox_contenido_streaming = 'document.querySelector("#contenido-4").shadowRoot.querySelector("#contenido-4")'

        # Titulo Disney+ Premium
        self.titulo_disney_plus_premium = 'document.querySelector("#root > main > div > div > div > div > div.pb-2 > andino-text")'

        # Boton radio Disney+ Premium Si
        self.boton_checkbox_contenido_disney_plus_si = r'document.querySelector("#\\31 ").shadowRoot.querySelector("div > label > input[type=radio]")'

        # Boton radio Disney+ Premium No
        self.boton_checkbox_contenido_disney_plus_no = r'document.querySelector("#\\32 ").shadowRoot.querySelector("div > label > input[type=radio]")'

    #################### FUNCIONES GENERALES ####################

    def get_text_titulo_recomendador(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_recomendador)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_continuar(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_continuar)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_recomendacion(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_recomendacion)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_plan_ideal(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_plan_ideal)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_checkbox_internet_fibra(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_checkbox_internet_fibra
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_checkbox_television(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_checkbox_television)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_checkbox_telefonia(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_checkbox_telefonia)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    #################### FUNCIONES DUO TRIPLE PACK ####################

    def get_text_titulo_tipo_hogar(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_tipo_hogar)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_casa(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_radio_casa)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_departamento(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_radio_departamento)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_pisos(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_pisos)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_1_piso(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_radio_1_piso)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_2_pisos_mas(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_radio_2_pisos_mas)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_espacios(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_espacios)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_1_espacio(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_radio_1_espacio)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_3_espacios(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_radio_3_espacios)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_5_espacios_mas(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_radio_5_espacios_mas
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_dispositivos(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_dispositivos)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_menos_8_dispositivos(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_radio_menos_8_dispositivos
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_entre_8_16_dispositivos(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_radio_entre_8_16_dispositivos
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_16_dispositivos_mas(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_radio_16_dispositivos_mas
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_utilizacion(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_utilizacion)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_utilizacion_basico(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_radio_utilizacion_basico
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_utilizacion_medio(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_radio_utilizacion_medio
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_utilizacion_alto(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_radio_utilizacion_alto
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_tv_simultaneas(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_tv_simultaneas)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_1_2_dispositivos(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_radio_1_2_dispositivos
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_3_dispositivos_mas(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_radio_3_dispositivos_mas
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    #################### FUNCIONES MONO PACK TELEVISION - INTERNET ####################

    def get_text_titulo_compania_actual(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_compania_actual)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_compania_actual_entel(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_radio_compania_actual_entel
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_compania_actual_otra(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_radio_compania_actual_otra
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_compania_actual_internet_celular(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_radio_compania_actual_internet_celular
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_internet_fuera_hogar(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.titulo_internet_fuera_hogar
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_internet_fuera_hogar_si(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_radio_internet_fuera_hogar_si
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_internet_fuera_hogar_no(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_radio_internet_fuera_hogar_no
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_contenido(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_contenido)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_checkbox_contenido_series_peliculas(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_checkbox_contenido_series_peliculas
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_checkbox_contenido_noticias(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_checkbox_contenido_noticias
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_checkbox_contenido_deportes(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_checkbox_contenido_deportes
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_checkbox_contenido_streaming(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_checkbox_contenido_streaming
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def get_text_titulo_disney_plus_premium(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.titulo_disney_plus_premium
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            # element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_disney_plus_si(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_checkbox_contenido_disney_plus_si
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))

    def click_boton_radio_disney_plus_no(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(
                self.boton_checkbox_contenido_disney_plus_no
            )
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))
