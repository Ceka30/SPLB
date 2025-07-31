@CHILE_PERU_B2C_Flujo_Digital_InternetHogar
Feature: CHILE PERU Flujo Digital Internet Hogar

    @CHILE_B2C_Flujo_Digital_InternetHogar
    Scenario Outline: CHILE C2C Internet Hogar
        Given estoy en la pagina "<URL>"
        And selecciono el plan "<PLAN>"
        When selecciono la velocidad "<VELOCIDAD>"
        And selecciono contratar online hogar para la velocidad "<VELOCIDAD>"
        Then completo formulario de factibilidad para la velocidad "<VELOCIDAD>"

        @CHILE_B2C_Flujo_Digital_InternetHogar_Fibra_600
        Examples:
            | URL                            | PLAN          | VELOCIDAD   | 
            | CHILE_URL_ENTEL_HOGAR_INTERNET | Sin Disney+   | Fibra 600   |

        @CHILE_B2C_Flujo_Digital_InternetHogar_Fibra_600_Plus
        Examples:
            | URL                            | PLAN          | VELOCIDAD   | 
            | CHILE_URL_ENTEL_HOGAR_INTERNET | Con Disney+   | Fibra 600+  |

        @CHILE_B2C_Flujo_Digital_InternetHogar_Fibra_800
        Examples:
            | URL                            | PLAN          | VELOCIDAD   |
            | CHILE_URL_ENTEL_HOGAR_INTERNET | Sin Disney+   | Fibra 800   |

        @CHILE_B2C_Flujo_Digital_InternetHogar_Fibra_800_Plus
        Examples:
            | URL                            | PLAN          | VELOCIDAD   | 
            | CHILE_URL_ENTEL_HOGAR_INTERNET | Con Disney+   | Fibra 800+  |

        @CHILE_B2C_Flujo_Digital_InternetHogar_Fibra_Giga
        Examples:
            | URL                            | PLAN          | VELOCIDAD   | 
            | CHILE_URL_ENTEL_HOGAR_INTERNET | Sin Disney+   | Fibra Giga  |

        @CHILE_B2C_Flujo_Digital_InternetHogar_Fibra_Giga_Plus
        Examples:
            | URL                            | PLAN          | VELOCIDAD   |
            | CHILE_URL_ENTEL_HOGAR_INTERNET | Con Disney+   | Fibra Giga+ |

    @CHILE_B2C_Flujo_Digital_DoblePack
    Scenario Outline: CHILE C2C Internet Hogar
        Given estoy en la pagina "<URL>"
        And selecciono el plan "<PLAN>"
        When selecciono la velocidad "<VELOCIDAD>"
        And selecciono contratar online hogar para la velocidad "<VELOCIDAD>"
        Then completo formulario de factibilidad para la velocidad "<VELOCIDAD>"

        @CHILE_B2C_Flujo_Digital_DoblePack_Fibra_600_TV_Lite
        Examples:
            | URL                             | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_DOBLEPACK | Fibra 600   | Fibra 600 TV Lite   |

        @CHILE_B2C_Flujo_Digital_DoblePack_Fibra_600_TV_Full_Plus
        Examples:
            | URL                             | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_DOBLEPACK | Fibra 600   | Fibra 600 TV Full+  |

        @CHILE_B2C_Flujo_Digital_DoblePack_Fibra_800_TV_Lite
        Examples:
            | URL                             | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_DOBLEPACK | Fibra 800   | Fibra 800 TV Lite   |

        @CHILE_B2C_Flujo_Digital_DoblePack_Fibra_800_TV_Full_Plus
        Examples:
            | URL                             | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_DOBLEPACK | Fibra 800   | Fibra 800 TV Full+  |

        @CHILE_B2C_Flujo_Digital_DoblePack_Fibra_Giga_TV_Lite
        Examples:
            | URL                             | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_DOBLEPACK | Fibra Giga  | Fibra Giga TV Lite  |

        @CHILE_B2C_Flujo_Digital_DoblePack_Fibra_Giga_Tv_Full_Plus
        Examples:
            | URL                             | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_DOBLEPACK | Fibra Giga  | Fibra Giga TV Full+ |

    @CHILE_B2C_Flujo_Digital_TriplePack
    Scenario Outline: CHILE C2C Internet Hogar
        Given estoy en la pagina "<URL>"
        And selecciono el plan "<PLAN>"
        When selecciono la velocidad "<VELOCIDAD>"
        And selecciono contratar online hogar para la velocidad "<VELOCIDAD>"
        Then completo formulario de factibilidad para la velocidad "<VELOCIDAD>"

        @CHILE_B2C_Flujo_Digital_TriplePack_Fibra_600_TV_Lite
        Examples:
            | URL                              | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_TRIPLEPACK | Fibra 600   | Fibra 600 TV Lite   |

        @CHILE_B2C_Flujo_Digital_TriplePack_Fibra_600_TV_Full_Plus
        Examples:
            | URL                              | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_TRIPLEPACK | Fibra 600   | Fibra 600 TV Full+  |

        @CHILE_B2C_Flujo_Digital_TriplePack_Fibra_800_TV_Lite
        Examples:
            | URL                              | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_TRIPLEPACK | Fibra 800   | Fibra 800 TV Lite   |

        @CHILE_B2C_Flujo_Digital_TriplePack_Fibra_800_TV_Full_Plus
        Examples:
            | URL                              | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_TRIPLEPACK | Fibra 800   | Fibra 800 TV Full+  |

        @CHILE_B2C_Flujo_Digital_TriplePack_Fibra_Giga_TV_Lite
        Examples:
            | URL                              | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_TRIPLEPACK | Fibra Giga  | Fibra Giga TV Lite  |

        @CHILE_B2C_Flujo_Digital_TriplePack_Fibra_Giga_Tv_Full_Plus
        Examples:
            | URL                              | PLAN        | TIPO_PLAN           | 
            | CHILE_URL_ENTEL_HOGAR_TRIPLEPACK | Fibra Giga  | Fibra Giga TV Full+ |