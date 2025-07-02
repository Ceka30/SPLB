@CHILE_CTR_Monitoring
Feature: CHILE Monitoreo CTR

@CHILE_CTR_Monitoring_Home
Scenario Outline: CHILE CTR Mopnitoring Home
    Given estoy en la pagina "<URL>"
    When navego hasta el final de la pagina
    Then obtengo las marcas de CTR

    Examples:
        | URL                  |
        | CHILE_URL_ENTEL_HOME |