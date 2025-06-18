@CHILE_PERU_B2C_C2C_HOME
Feature: CHILE PERU B2C Click to Call Home

@PERU_B2C_C2C_Home
Scenario Outline: PERU B2C C2C Home
    Given estoy en la pagina "<URL>"
    Then se ingresa la solicitud

    Examples:
        | URL                 |
        | PERU_URL_ENTEL_HOME |