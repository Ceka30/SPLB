@CHILE_PERU_B2C_Flujo_Digital_Hogar
Feature: CHILE PERU Flujo Digital Hogar

    @CHILE_B2C_Flujo_Digital_Hogar
    Scenario Outline: CHILE C2C Internet Hogar
        Given estoy en la pagina "<URL>"
        And selecciono el plan "<PLAN>"
        When selecciono la velocidad "<VELOCIDAD>"
        And selecciono contratar online hogar para la velocidad "<VELOCIDAD>"
        Then completo formulario de factibilidad para la velocidad "<VELOCIDAD>"

        Examples:
            | URL                            | PLAN          | VELOCIDAD   | 
            # | Internet Hogar | Sin Disney+   | Fibra 600   |
            # | Internet Hogar | Con Disney+   | Fibra 600+  |
            # | Internet Hogar | Sin Disney+   | Fibra 800   |
            # | Internet Hogar | Con Disney+   | Fibra 800+  |
            # | Internet Hogar | Sin Disney+   | Fibra Giga  |
            | CHILE_URL_ENTEL_HOGAR_INTERNET | Con Disney+   | Fibra Giga+ |