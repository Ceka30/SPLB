@CHILE_B2C_C2C_OFERTAS_Movil
Feature: CHILE B2C Topo Fab 

    @CHILE_B2C_C2C_OFERTAS_Movil
    Scenario Outline: CHILE B2C C2C Ofertas Movil
        Given estoy en la pagina "<URL>"
        When selecciono click to call Quiero que me llamen
        Then completo formulario con mi numero de contacto

        Examples:
            | URL                           |
            | CHILE_URL_ENTEL_OFERTAS_MOVIL |