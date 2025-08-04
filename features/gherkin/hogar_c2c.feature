@CHILE_PERU_B2C_C2C_HOGAR
Feature: CHILE B2C Click to Call Hogar 

    @CHILE_Monitoring @CHILE_B2C_C2C_InternetHogar
    Scenario Outline: CHILE C2C Internet Hogar
        Given estoy en la pagina "<URL>"
        And selecciono el plan "<PLAN>"
        When selecciono la velocidad "<VELOCIDAD>"
        And selecciono C2C
        Then ingreso la solicitud de contacto

        @CHILE_B2C_C2C_InternetHogar_Fibra_600
        Examples:
            | URL                            | PLAN          | VELOCIDAD   | 
            | CHILE_URL_ENTEL_HOGAR_INTERNET | Sin Disney+   | Fibra 600   |

        @CHILE_B2C_C2C_InternetHogar_Fibra_600_Plus
        Examples:
            | URL                            | PLAN          | VELOCIDAD   | 
            | CHILE_URL_ENTEL_HOGAR_INTERNET | Con Disney+   | Fibra 600+  |
        
        @CHILE_B2C_C2C_InternetHogar_Fibra_800
        Examples:
            | URL                            | PLAN          | VELOCIDAD   |
            | CHILE_URL_ENTEL_HOGAR_INTERNET | Sin Disney+   | Fibra 800   |

        @CHILE_B2C_C2C_InternetHogar_Fibra_800_Plus
        Examples:
            | URL                            | PLAN          | VELOCIDAD   | 
            | CHILE_URL_ENTEL_HOGAR_INTERNET | Con Disney+   | Fibra 800+  |

        @CHILE_B2C_C2C_InternetHogar_Fibra_Giga
        Examples:
            | URL                            | PLAN          | VELOCIDAD   | 
            | CHILE_URL_ENTEL_HOGAR_INTERNET | Sin Disney+   | Fibra Giga  |

        @CHILE_B2C_C2C_InternetHogar_Fibra_Giga_Plus
        Examples:
            | URL                            | PLAN          | VELOCIDAD   |
            | CHILE_URL_ENTEL_HOGAR_INTERNET | Con Disney+   | Fibra Giga+ |

    @CHILE_Monitoring @CHILE_B2C_C2C_DoblePack
    Scenario Outline: CHILE C2C Doble Pack
        Given estoy en la pagina "<URL>"
        And selecciono el plan "<PLAN>"
        When selecciono el tipo de plan "<TIPO_PLAN>"
        And selecciono C2C
        Then ingreso la solicitud de contacto

        @CHILE_B2C_C2C_DoblePack_Fibra_600_TV_Lite
        Examples:
            | URL                             | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_DOBLEPACK | Fibra 600   | Fibra 600 TV Lite   |

        @CHILE_B2C_C2C_DoblePack_Fibra_600_TV_Full_Plus
        Examples:
            | URL                             | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_DOBLEPACK | Fibra 600   | Fibra 600 TV Full+  |

        @CHILE_B2C_C2C_DoblePack_Fibra_800_TV_Lite
        Examples:
            | URL                             | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_DOBLEPACK | Fibra 800   | Fibra 800 TV Lite   |

        @CHILE_B2C_C2C_DoblePack_Fibra_800_TV_Full_Plus
        Examples:
            | URL                             | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_DOBLEPACK | Fibra 800   | Fibra 800 TV Full+  |

        @CHILE_B2C_C2C_DoblePack_Fibra_Giga_TV_Lite
        Examples:
            | URL                             | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_DOBLEPACK | Fibra Giga  | Fibra Giga TV Lite  |

        @CHILE_B2C_C2C_DoblePack_Fibra_Giga_Tv_Full_Plus
        Examples:
            | URL                             | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_DOBLEPACK | Fibra Giga  | Fibra Giga TV Full+ |

    @CHILE_Monitoring @CHILE_B2C_C2C_TriplePack
    Scenario Outline: CHILE C2C Triple Pack
        Given estoy en la pagina "<URL>"
        And selecciono el plan "<PLAN>"
        When selecciono el tipo de plan "<TIPO_PLAN>"
        And selecciono C2C
        Then ingreso la solicitud de contacto

        @CHILE_B2C_C2C_TriplePack_Fibra_600_TV_Lite
        Examples:
            | URL                              | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_TRIPLEPACK | Fibra 600   | Fibra 600 TV Lite   |

        @CHILE_B2C_C2C_TriplePack_Fibra_600_TV_Full_Plus
        Examples:
            | URL                              | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_TRIPLEPACK | Fibra 600   | Fibra 600 TV Full+  |

        @CHILE_B2C_C2C_TriplePack_Fibra_800_TV_Lite
        Examples:
            | URL                              | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_TRIPLEPACK | Fibra 800   | Fibra 800 TV Lite   |

        @CHILE_B2C_C2C_TriplePack_Fibra_800_TV_Full_Plus
        Examples:
            | URL                              | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_TRIPLEPACK | Fibra 800   | Fibra 800 TV Full+  |

        @CHILE_B2C_C2C_TriplePack_Fibra_Giga_TV_Lite
        Examples:
            | URL                              | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_TRIPLEPACK | Fibra Giga  | Fibra Giga TV Lite  |
        
        @CHILE_B2C_C2C_TriplePack_Fibra_Giga_TV_Full_Plus
        Examples:
            | URL                              | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_TRIPLEPACK | Fibra Giga  | Fibra Giga TV Full+ |

    @CHILE_Monitoring @CHILE_B2C_C2C_Television
    Scenario Outline: CHILE C2C Television
        Given estoy en la pagina "<URL>"
        When selecciono el tipo de plan "<TIPO_PLAN>"
        And selecciono C2C
        Then ingreso la solicitud de contacto

        # @CHILE_B2C_C2C_Television_TV_Lite
        # Examples:
        #     | URL                      | TIPO_PLAN | 
        #     | CHILE_URL_ENTEL_HOGAR_TV | TV Lite   |

        @CHILE_B2C_C2C_Television_TV_Full_Plus
        Examples:
            | URL                      | TIPO_PLAN | 
            | CHILE_URL_ENTEL_HOGAR_TV | TV Full+  |

    @PERU_Monitoring @PERU_B2C_C2C_InternetHogar
    Scenario Outline: PERU C2C Internet Hogar
        Given estoy en la pagina "<URL>"
        When selecciono el tipo de plan "<TIPO_PLAN>"
        Then ingreso la solicitud de contacto

        @PERU_B2C_C2C_InternetHogar_Fibra_100_Mbps
        Examples:
            | URL                           | TIPO_PLAN       |
            | PERU_URL_ENTEL_HOGAR_INTERNET | Fibra 100 Mbps  |

        @PERU_B2C_C2C_InternetHogar_Fibra_300_Mbps
        Examples:
            | URL                           | TIPO_PLAN       |
            | PERU_URL_ENTEL_HOGAR_INTERNET | Fibra 300 Mbps  |
