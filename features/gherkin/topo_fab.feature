@CHILE_PERU_B2C_TopoFab
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


    @PERU_B2C_TopoFab
    Scenario Outline: PERU B2C Topo Fab
        Given estoy en la pagina "<URL>"
        When selecciono Topo/Fab ¿Quieres contratar?
        And selecciono contratar por telefono
        Then completo con mi numero de contacto

        @PERU_B2C_TopoFab_Home
        Examples:
            | URL                                     |
            | PERU_URL_ENTEL_HOME                     |

        @PERU_B2C_TopoFab_Hogar_Internet
        Examples:
            | URL                                     |
            | PERU_URL_ENTEL_HOGAR_INTERNET           |

        @PERU_B2C_TopoFab_Movil
        Examples:
            | URL                                     |
            | PERU_URL_ENTEL_MOVIL                    |

        @PERU_B2C_TopoFab_Movil_Lineas_Adicionales
        Examples:
            | URL                                     |
            | PERU_URL_ENTEL_MOVIL_LINEAS_ADICIONALES |

        @PERU_B2C_TopoFab_Telefonia_Fija
        Examples:
            | URL                                     |
            | PERU_URL_ENTEL_TELEFONIA_FIJA           |

        @PERU_B2C_TopoFab_Prepago_Bolsas
        Examples:
            | URL                                     |
            | PERU_URL_ENTEL_PREPAGO_BOLSAS           |

        @PERU_B2C_TopoFab_Prepago_Planes
        Examples:
            | URL                                     |
            | PERU_URL_ENTEL_PREPAGO_PLANES           |

        @PERU_B2C_TopoFab_Prepago_Recargas
        Examples:
            | URL                                     |
            | PERU_URL_ENTEL_PREPAGO_RECARGAS         |

        @PERU_B2C_TopoFab_Prepago_Beneficios
        Examples:
            | URL                                     |
            | PERU_URL_ENTEL_PREPAGO_BENEFICIOS       |

        @PERU_B2C_TopoFab_Recambiopower
        Examples:
            | URL                                     |
            | PERU_URL_ENTEL_RECAMBIOPOWER            |

        @PERU_B2C_TopoFab_Seguros
        Examples:
            | URL                                     |
            | PERU_URL_ENTEL_SEGUROS                  |

        @PERU_B2C_TopoFab_Chip_Autoactivado
        Examples:
            | URL                                     |
            | PERU_URL_ENTEL_CHIP_AUTOACTIVADO        |

        @PERU_B2C_TopoFab_Apple
        Examples:
            | URL                                     |
            | PERU_URL_ENTEL_APPLE                    |

        @PERU_B2C_TopoFab_Ayuda
        Examples:
            | URL                                     |
            | PERU_URL_ENTEL_AYUDA                    |

        @PERU_B2C_TopoFab_Tiendas
        Examples:
            | URL                                     |
            | PERU_URL_ENTEL_TIENDAS                  |

        @PERU_B2C_TopoFab_Info_Abonados
        Examples:
            | URL                                     |
            | PERU_URL_ENTEL_INFO_ABONADOS            |


    @PERU_B2C_TopoFab_OFERTA_PROMOCIONES
    Scenario Outline: PERU B2C Topo Fab Ofertas y Promociones
        Given estoy en la pagina "<URL>"
        When selecciono Quiero que me contacten
        Then completo formulario para que me contacten

        @PERU_B2C_TopoFab_OFERTA_PROMOCIONES_googlesem_landingoyp_marcaexacta
        Examples:
            | URL                                   |
            | PERU_URL_ENTEL_OFERTAS_PROMOCIONES_01 |

        @PERU_B2C_TopoFab_OFERTA_PROMOCIONES_googlesem_landingoyp_porta_lima
        Examples:
            | URL                                   |
            | PERU_URL_ENTEL_OFERTAS_PROMOCIONES_02 |

        @PERU_B2C_TopoFab_OFERTA_PROMOCIONES_googlesem_landingoyp_competencia
        Examples:
            | URL                                   |
            | PERU_URL_ENTEL_OFERTAS_PROMOCIONES_03 |
        
        @PERU_B2C_TopoFab_OFERTA_PROMOCIONES_bing_oyp_performance
        Examples:
            | URL                                   |
            | PERU_URL_ENTEL_OFERTAS_PROMOCIONES_04 |

        @PERU_B2C_TopoFab_OFERTA_PROMOCIONES_google
        Examples:
            | URL                                   |
            | PERU_URL_ENTEL_OFERTAS_PROMOCIONES_05 |

        @PERU_B2C_TopoFab_OFERTA_PROMOCIONES_google_provincias
        Examples:
            | URL                                   |
            | PERU_URL_ENTEL_OFERTAS_PROMOCIONES_06 |
        
        @PERU_B2C_TopoFab_OFERTA_PROMOCIONES_google_postpago
        Examples:
            | URL                                   |
            | PERU_URL_ENTEL_OFERTAS_PROMOCIONES_07 |

        @PERU_B2C_TopoFab_OFERTA_PROMOCIONES_google_incentivos
        Examples:
            | URL                                   |
            | PERU_URL_ENTEL_OFERTAS_PROMOCIONES_08 |