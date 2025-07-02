@CHILE_PERU_B2C_C2C_HOGAR
Feature: CHILE B2C Click to Call Hogar 

@CHILE_B2C_C2C_InternetHogar
Scenario Outline: CHILE C2C Internet Hogar
    Given estoy en la pagina "<URL>"
    And selecciono el plan "<PLAN>"
    When selecciono la velocidad "<VELOCIDAD>"
    And selecciono C2C
    Then ingreso la solicitud de contacto

    Examples:
        | URL                            | PLAN          | VELOCIDAD   | 
        # | Internet Hogar | Sin Disney+   | Fibra 600   |
        # | Internet Hogar | Con Disney+   | Fibra 600+  |
        # | Internet Hogar | Sin Disney+   | Fibra 800   |
        # | Internet Hogar | Con Disney+   | Fibra 800+  |
        # | Internet Hogar | Sin Disney+   | Fibra Giga  |
        | CHILE_URL_ENTEL_HOGAR_INTERNET | Con Disney+   | Fibra Giga+ |

@CHILE_B2C_C2C_DoblePack
Scenario Outline: CHILE C2C Doble Pack
    Given estoy en la pagina "<URL>"
    And selecciono el plan "<PLAN>"
    When selecciono el tipo de plan "<TIPO_PLAN>"
    And selecciono C2C
    Then ingreso la solicitud de contacto

    Examples:
        | URL        | PLAN        | TIPO_PLAN           | 
        # | Doble Pack | Fibra 600   | Fibra 600 TV Lite   |
        # | Doble Pack | Fibra 600   | Fibra 600 TV Full+  |
        # | Doble Pack | Fibra 800   | Fibra 800 TV Lite   |
        # | Doble Pack | Fibra 800   | Fibra 800 TV Full+  |
        # | Doble Pack | Fibra Giga  | Fibra Giga TV Lite  |
        | Doble Pack | Fibra Giga  | Fibra Giga TV Full+ |

@CHILE_B2C_C2C_TriplePack
Scenario Outline: CHILE C2C Triple Pack
    Given estoy en la pagina "<URL>"
    And selecciono el plan "<PLAN>"
    When selecciono el tipo de plan "<TIPO_PLAN>"
    And selecciono C2C
    Then ingreso la solicitud de contacto

    Examples:
        | URL         | PLAN        | TIPO_PLAN           | 
        | Triple Pack | Fibra 600   | Fibra 600 TV Lite   |
        | Triple Pack | Fibra 600   | Fibra 600 TV Full+  |
        | Triple Pack | Fibra 800   | Fibra 800 TV Lite   |
        | Triple Pack | Fibra 800   | Fibra 800 TV Full+  |
        | Triple Pack | Fibra Giga  | Fibra Giga TV Lite  |
        | Triple Pack | Fibra Giga  | Fibra Giga TV Full+ |

@CHILE_B2C_C2C_Television
Scenario Outline: CHILE C2C Television
    Given estoy en la pagina "<URL>"
    When selecciono el tipo de plan "<TIPO_PLAN>"
    And selecciono C2C
    Then ingreso la solicitud de contacto

    Examples:
        | URL        | TIPO_PLAN | 
        | Television | TV Full + |

@PERU_B2C_C2C_InternetHogar
Scenario Outline: PERU C2C Internet Hogar
    Given estoy en la pagina "<URL>"
    When selecciono el tipo de plan "<TIPO_PLAN>"
    Then ingreso la solicitud de contacto

    Examples:
        | URL                           | TIPO_PLAN       |
        | PERU_URL_ENTEL_HOGAR_INTERNET | Fibra 100 Mbps  |
        | PERU_URL_ENTEL_HOGAR_INTERNET | Fibra 200 Mbps  |