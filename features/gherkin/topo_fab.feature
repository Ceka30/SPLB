@CHILE_B2C_TopoFab
Feature: CHILE B2C Topo Fab 

    @CHILE_B2C_TopoFab_InternetHogar
    Scenario Outline: CHILE B2C Topo Fab Internet Hogar
        Given estoy en la pagina "<URL>"
        When selecciono Topo/Fab ¿Quieres contratar?
        And selecciono contratar por telefono
        Then completo con mi numero de contacto

        Examples:
            | URL                            |
            | CHILE_URL_ENTEL_HOGAR_INTERNET |

    @CHILE_B2C_TopoFab_Portabilidad
    Scenario Outline: CHILE B2C Topo Fab Portabilidad
        Given estoy en la pagina "<URL>"
        When selecciono Topo/Fab ¿Quieres contratar?
        And selecciono contratar por telefono
        Then completo con mi numero de contacto

        Examples:
            | URL                                |
            | CHILE_URL_ENTEL_MOVIL_PORTABILIDAD |

    @CHILE_B2C_TopoFab_Home
    Scenario Outline: CHILE B2C Topo Fab Home
        Given estoy en la pagina "<URL>"
        When selecciono Topo/Fab ¿Quieres contratar?
        And selecciono contratar por telefono
        Then completo con mi numero de contacto

        Examples:
            | URL                  |
            | CHILE_URL_ENTEL_HOME |

    @PERU_Monitoring @PERU_B2C_TopoFab_Home
    Scenario Outline: PERU B2C Topo Fab Home
        Given estoy en la pagina "<URL>"
        When selecciono Topo/Fab ¿Quieres contratar?
        And selecciono contratar por telefono
        Then completo con mi numero de contacto

        Examples:
            | URL                 |
            | PERU_URL_ENTEL_HOME |