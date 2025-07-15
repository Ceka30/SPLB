@CHILE_PERU_B2C_Flujo_Digital_Movil
Feature: CHILE PERU Flujo Digital Movil

    @CHILE_PERU_B2C_Flujo_Digital_Movil_Portabilidad
    Scenario Outline: CHILE PERU Flujo Digital Movil Portabilidad
        Given estoy en la pagina "<URL>"
        When selecciono el plan movil "<PLAN>"
        And selecciono contratar online movil
        Then ingreso como cliente y recibo el resumen de contratacion del plan "<PLAN>"

        Examples:
            | URL                                | PLAN                  |
            | CHILE_URL_ENTEL_MOVIL_PORTABILIDAD | 150 Gigas             | 
            # | CHILE_URL_ENTEL_MOVIL_PORTABILIDAD | 350 Gigas             |
            # | CHILE_URL_ENTEL_MOVIL_PORTABILIDAD | Libre                 |
            # | CHILE_URL_ENTEL_MOVIL_PORTABILIDAD | Libre con Roaming     |
            # | CHILE_URL_ENTEL_MOVIL_PORTABILIDAD | Libre con Roaming Pro |