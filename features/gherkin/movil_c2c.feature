@CHILE_PERU_B2C_C2C_MOVIL
Feature: CHILE PERU B2C Click to Call 

    @CHILE_B2C_C2C_MOVIL_Portabilidad
    Scenario Outline: CHILE B2C C2C Movil Portabilidad
        Given estoy en la pagina "<URL>"
        When selecciono el plan movil "<PLAN>"
        And selecciono Quiero que me llamen
        Then completo formulario de contacto

        @CHILE_B2C_C2C_MOVIL_Portabilidad_Plan_150_Gigas
        Examples:
            | URL                                | PLAN                  |
            | CHILE_URL_ENTEL_MOVIL_PORTABILIDAD | 150 Gigas             | 
        
        @CHILE_B2C_C2C_MOVIL_Portabilidad_Plan_450_Gigas
        Examples:
            | URL                                | PLAN                  |
            | CHILE_URL_ENTEL_MOVIL_PORTABILIDAD | 450 Gigas             |
        
        @CHILE_B2C_C2C_MOVIL_Portabilidad_Plan_Libre
        Examples:
            | URL                                | PLAN                  |
            | CHILE_URL_ENTEL_MOVIL_PORTABILIDAD | Libre                 |
        
        @CHILE_B2C_C2C_MOVIL_Portabilidad_Plan_Libre_Roaming
        Examples:
            | URL                                | PLAN                  |
            | CHILE_URL_ENTEL_MOVIL_PORTABILIDAD | Libre con Roaming     |

        # @CHILE_B2C_C2C_MOVIL_Portabilidad_Plan_Libre_Roaming_Pro
        # Examples:
        #     | URL                                | PLAN                  |
        #     | CHILE_URL_ENTEL_MOVIL_PORTABILIDAD | Libre con Roaming Pro |

    @CHILE_B2C_C2C_MOVIL_LineaAdicional
    Scenario Outline: CHILE B2C C2C Movil Linea Adicional
        Given estoy en la pagina "<URL>"
        When selecciono linea adicional
        And selecciono Contratar por telefono en el sidebar
        Then completo formulario de contacto

        Examples:
            | URL                                  | 
            | CHILE_URL_ENTEL_MOVIL_PLAN_ADICIONAL | 

    @PERU_Monitoring @PERU_B2C_C2C_MOVIL_Portabilidad
    Scenario Outline: PERU B2C C2C Movil Portabilidad
        Given estoy en la pagina "<URL>"
        When selecciono el plan movil "<PLAN>"
        And selecciono Quiero que me llamen
        # Then completo formulario de contacto

        @PERU_B2C_C2C_MOVIL_Portabilidad_Plan_Power_29_90
        Examples:
            | URL                  | PLAN                |
            | PERU_URL_ENTEL_MOVIL | Power 29.90         | 

        @PERU_B2C_C2C_MOVIL_Portabilidad_Plan_Power_39_90
        Examples:
            | URL                  | PLAN                |
            | PERU_URL_ENTEL_MOVIL | Power 39.90         |

        @PERU_B2C_C2C_MOVIL_Portabilidad_Plan_Power_Ilim_69_90
        Examples:
            | URL                  | PLAN                |
            | PERU_URL_ENTEL_MOVIL | Power Ilim 69.90    |

        @PERU_B2C_C2C_MOVIL_Portabilidad_Plan_Power_Ilim_79_90_SD
        Examples:
            | URL                  | PLAN                |
            | PERU_URL_ENTEL_MOVIL | Power Ilim 79.90 SD |

        @PERU_B2C_C2C_MOVIL_Portabilidad_Plan_Power_Ilim_99_90_SD
        Examples:
            | URL                  | PLAN                |
            | PERU_URL_ENTEL_MOVIL | Power Ilim 99.90 SD |

    @PERU_Monitoring @PERU_B2C_C2C_MOVIL_LineaAdicional
    Scenario Outline: PERU B2C C2C Movil Linea Adicional
        Given estoy en la pagina "<URL>"
        # And selecciono Soy cliente Entel
        When selecciono linea adicional
        Then completo formulario de contacto

        Examples:
            | URL                                     | 
            | PERU_URL_ENTEL_MOVIL_LINEAS_ADICIONALES | 