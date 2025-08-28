@CHILE_PERU_B2C_FlujoDigital_Movil
Feature: CHILE PERU Flujo Digital Movil

    @CHILE_Monitoring @CHILE_B2C_FlujoDigital_MOVIL_Portabilidad
    Scenario Outline: CHILE Flujo Digital Movil Portabilidad
        Given estoy en la pagina "<URL>"
        When selecciono el plan movil "<PLAN>"
        And selecciono contratar online movil
        Then ingreso como cliente y recibo el resumen de contratacion del plan "<PLAN>"

        @CHILE_B2C_FlujoDigital_MOVIL_Portabilidad_150_Gigas
        Examples:
            | URL                                | PLAN                  |
            | CHILE_URL_ENTEL_MOVIL_PORTABILIDAD | 150 Gigas             | 

        @CHILE_B2C_FlujoDigital_MOVIL_Portabilidad_450_Gigas
        Examples:
            | URL                                | PLAN                  |
            | CHILE_URL_ENTEL_MOVIL_PORTABILIDAD | 450 Gigas             |

        @CHILE_B2C_FlujoDigital_MOVIL_Portabilidad_Libre
        Examples:
            | URL                                | PLAN                  |
            | CHILE_URL_ENTEL_MOVIL_PORTABILIDAD | Libre                 |

        @CHILE_B2C_FlujoDigital_MOVIL_Portabilidad_Libre_Roaming
        Examples:
            | URL                                | PLAN                  |
            | CHILE_URL_ENTEL_MOVIL_PORTABILIDAD | Libre con Roaming     |

        @CHILE_B2C_FlujoDigital_MOVIL_Portabilidad_Libre_Roaming_Pro
        Examples:
            | URL                                | PLAN                  |
            | CHILE_URL_ENTEL_MOVIL_PORTABILIDAD | Libre con Roaming Pro |