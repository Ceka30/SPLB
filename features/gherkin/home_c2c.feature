@CHILE_PERU_B2C_C2C_Banner_HOME
Feature: CHILE B2C Click to Call Home

    @PERU_Monitoring @PERU_B2C_C2C_Banner_Home
    Scenario Outline: PERU B2C C2C Banner Home
        Given estoy en la pagina "<URL>"
        Then se ingresa la solicitud

        Examples:
            | URL                 |
            | PERU_URL_ENTEL_HOME |