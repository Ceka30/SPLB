@CHILE_B2C_RECOMENDADOR
Feature: CHILE B2C Recomenador 

    @CHILE_B2C_RECOMENDADOR_DuoTriplePack
    Scenario Outline: Recomendador Duo Triple Pack 
        Given estoy en la pagina "<URL>"
        When selecciono el servicio "<SERVICIO>"
        And selecciono el tipo de hogar "<TIPO_HOGAR>"
        And selecciono los pisos del hogar "<PISOS_HOGAR>"
        And selecciono los espacios "<ESPACIOS>"
        And selecciono el numero de dispositivos "<DISPOSITIVOS>"
        And selecciono la utilizacion del internet "<UTILIZACION>"
        And selecciono TV simultaneas "<TVS>"
        Then me recomienda el plan ideal "<PLAN_IDEAL>"

        @CHILE_B2C_RECOMENDADOR_DuoTriplePack_Fibra600TVLite
        Examples:
            | URL                          | SERVICIO    | TIPO_HOGAR   | PISOS_HOGAR   | ESPACIOS         | DISPOSITIVOS              | UTILIZACION | TVS                  | PLAN_IDEAL          |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 1 espacio        | Menos de 8 dispositivos   | Basico      | 1 a 2 dispositivos   | Fibra 600 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 1 espacio        | Menos de 8 dispositivos   | Alto        | 1 a 2 dispositivos   | Fibra 600 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 3 espacios       | Menos de 8 dispositivos   | Basico      | 1 a 2 dispositivos   | Fibra 600 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 1 espacio        | Entre 8 y 16 dispositivos | Basico      | 1 a 2 dispositivos   | Fibra 600 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 1 espacio        | Entre 8 y 16 dispositivos | Alto        | 1 a 2 dispositivos   | Fibra 600 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 3 espacios       | Entre 8 y 16 dispositivos | Basico      | 1 a 2 dispositivos   | Fibra 600 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 1 espacio        | Mas de 16 dispositivos    | Basico      | 1 a 2 dispositivos   | Fibra 600 TV Lite   |

        @CHILE_B2C_RECOMENDADOR_DuoTriplePack_Fibra600TVFullPlus
        Examples:
            | URL                          | SERVICIO    | TIPO_HOGAR   | PISOS_HOGAR   | ESPACIOS         | DISPOSITIVOS              | UTILIZACION | TVS                  | PLAN_IDEAL          |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 1 espacio        | Menos de 8 dispositivos   | Basico      | 3 o mas dispositivos | Fibra 600 TV Full+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 1 espacio        | Menos de 8 dispositivos   | Alto        | 3 o mas dispositivos | Fibra 600 TV Full+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 3 espacios       | Menos de 8 dispositivos   | Basico      | 3 o mas dispositivos | Fibra 600 TV Full+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 1 espacio        | Entre 8 y 16 dispositivos | Basico      | 3 o mas dispositivos | Fibra 600 TV Full+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 1 espacio        | Entre 8 y 16 dispositivos | Alto        | 3 o mas dispositivos | Fibra 600 TV Full+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 3 espacios       | Entre 8 y 16 dispositivos | Basico      | 3 o mas dispositivos | Fibra 600 TV Full+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 1 espacio        | Mas de 16 dispositivos    | Basico      | 3 o mas dispositivos | Fibra 600 TV Full+  |

        @CHILE_B2C_RECOMENDADOR_DuoTriplePack_Fibra800TVLite
        Examples:
            | URL                          | SERVICIO    | TIPO_HOGAR   | PISOS_HOGAR   | ESPACIOS         | DISPOSITIVOS              | UTILIZACION | TVS                  | PLAN_IDEAL          |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 3 espacios       | Menos de 8 dispositivos   | Alto        | 1 a 2 dispositivos   | Fibra 800 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 5 o mas espacios | Menos de 8 dispositivos   | Basico      | 1 a 2 dispositivos   | Fibra 800 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 1 espacio        | Menos de 8 dispositivos   | Basico      | 1 a 2 dispositivos   | Fibra 800 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 1 espacio        | Menos de 8 dispositivos   | Alto        | 1 a 2 dispositivos   | Fibra 800 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 3 espacios       | Menos de 8 dispositivos   | Basico      | 1 a 2 dispositivos   | Fibra 800 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 3 espacios       | Menos de 8 dispositivos   | Alto        | 1 a 2 dispositivos   | Fibra 800 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 5 o mas espacios | Menos de 8 dispositivos   | Basico      | 1 a 2 dispositivos   | Fibra 800 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 3 espacios       | Entre 8 y 16 dispositivos | Alto        | 1 a 2 dispositivos   | Fibra 800 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 5 o mas espacios | Entre 8 y 16 dispositivos | Basico      | 1 a 2 dispositivos   | Fibra 800 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 1 espacio        | Entre 8 y 16 dispositivos | Basico      | 1 a 2 dispositivos   | Fibra 800 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 1 espacio        | Entre 8 y 16 dispositivos | Alto        | 1 a 2 dispositivos   | Fibra 800 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 3 espacios       | Entre 8 y 16 dispositivos | Basico      | 1 a 2 dispositivos   | Fibra 800 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 1 espacio        | Mas de 16 dispositivos    | Alto        | 1 a 2 dispositivos   | Fibra 800 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 3 espacios       | Mas de 16 dispositivos    | Basico      | 1 a 2 dispositivos   | Fibra 800 TV Lite   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 1 espacio        | Mas de 16 dispositivos    | Basico      | 1 a 2 dispositivos   | Fibra 800 TV Lite   |
            
            
        @CHILE_B2C_RECOMENDADOR_DuoTriplePack_Fibra800TVFullPlus
        Examples:
            | URL                          | SERVICIO    | TIPO_HOGAR   | PISOS_HOGAR   | ESPACIOS         | DISPOSITIVOS              | UTILIZACION | TVS                  | PLAN_IDEAL          |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 3 espacios       | Menos de 8 dispositivos   | Alto        | 3 o mas dispositivos | Fibra 800 TV Full+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 5 o mas espacios | Menos de 8 dispositivos   | Basico      | 3 o mas dispositivos | Fibra 800 TV Full+  |   
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 1 espacio        | Menos de 8 dispositivos   | Basico      | 3 o mas dispositivos | Fibra 800 TV Full+  | 
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 1 espacio        | Menos de 8 dispositivos   | Alto        | 3 o mas dispositivos | Fibra 800 TV Full+  | 
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 3 espacios       | Menos de 8 dispositivos   | Basico      | 3 o mas dispositivos | Fibra 800 TV Full+  | 
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 3 espacios       | Menos de 8 dispositivos   | Alto        | 3 o mas dispositivos | Fibra 800 TV Full+  | 
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 5 o mas espacios | Menos de 8 dispositivos   | Basico      | 3 o mas dispositivos | Fibra 800 TV Full+  | 
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 3 espacios       | Entre 8 y 16 dispositivos | Alto        | 3 o mas dispositivos | Fibra 800 TV Full+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 5 o mas espacios | Entre 8 y 16 dispositivos | Basico      | 3 o mas dispositivos | Fibra 800 TV Full+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 1 espacio        | Entre 8 y 16 dispositivos | Basico      | 3 o mas dispositivos | Fibra 800 TV Full+  | 
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 1 espacio        | Entre 8 y 16 dispositivos | Alto        | 3 o mas dispositivos | Fibra 800 TV Full+  | 
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 3 espacios       | Entre 8 y 16 dispositivos | Basico      | 3 o mas dispositivos | Fibra 800 TV Full+  | 
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 1 espacio        | Mas de 16 dispositivos    | Alto        | 3 o mas dispositivos | Fibra 800 TV Full+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 3 espacios       | Mas de 16 dispositivos    | Basico      | 3 o mas dispositivos | Fibra 800 TV Full+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 1 espacio        | Mas de 16 dispositivos    | Basico      | 3 o mas dispositivos | Fibra 800 TV Full+  |
            

        @CHILE_B2C_RECOMENDADOR_DuoTriplePack_FibraGigaTVLite
        Examples:
            | URL                          | SERVICIO    | TIPO_HOGAR   | PISOS_HOGAR   | ESPACIOS         | DISPOSITIVOS              | UTILIZACION | TVS                  | PLAN_IDEAL          |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 5 o mas espacios | Menos de 8 dispositivos   | Alto        | 1 a 2 dispositivos   | Fibra Giga TV Lite  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 5 o mas espacios | Menos de 8 dispositivos   | Alto        | 1 a 2 dispositivos   | Fibra Giga TV Lite  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 5 o mas espacios | Entre 8 y 16 dispositivos | Alto        | 1 a 2 dispositivos   | Fibra Giga TV Lite  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 3 espacios       | Entre 8 y 16 dispositivos | Alto        | 1 a 2 dispositivos   | Fibra Giga TV Lite  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 5 o mas espacios | Entre 8 y 16 dispositivos | Basico      | 1 a 2 dispositivos   | Fibra Giga TV Lite  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 5 o mas espacios | Entre 8 y 16 dispositivos | Alto        | 1 a 2 dispositivos   | Fibra Giga TV Lite  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 3 espacios       | Mas de 16 dispositivos    | Alto        | 1 a 2 dispositivos   | Fibra Giga TV Lite  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 5 o mas espacios | Mas de 16 dispositivos    | Basico      | 1 a 2 dispositivos   | Fibra Giga TV Lite  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 5 o mas espacios | Mas de 16 dispositivos    | Alto        | 1 a 2 dispositivos   | Fibra Giga TV Lite  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 1 espacio        | Mas de 16 dispositivos    | Alto        | 1 a 2 dispositivos   | Fibra Giga TV Lite  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 3 espacios       | Mas de 16 dispositivos    | Basico      | 1 a 2 dispositivos   | Fibra Giga TV Lite  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 3 espacios       | Mas de 16 dispositivos    | Alto        | 1 a 2 dispositivos   | Fibra Giga TV Lite  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 5 o mas espacios | Mas de 16 dispositivos    | Basico      | 1 a 2 dispositivos   | Fibra Giga TV Lite  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 5 o mas espacios | Mas de 16 dispositivos    | Alto        | 1 a 2 dispositivos   | Fibra Giga TV Lite  |

        @CHILE_B2C_RECOMENDADOR_DuoTriplePack_FibraGigaTVFullPlus
        Examples:
            | URL                          | SERVICIO    | TIPO_HOGAR   | PISOS_HOGAR   | ESPACIOS         | DISPOSITIVOS              | UTILIZACION | TVS                  | PLAN_IDEAL          |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 5 o mas espacios | Menos de 8 dispositivos   | Alto        | 3 o mas dispositivos | Fibra Giga TV Full+ | 
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 5 o mas espacios | Menos de 8 dispositivos   | Alto        | 3 o mas dispositivos | Fibra Giga TV Full+ | 
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 5 o mas espacios | Entre 8 y 16 dispositivos | Alto        | 3 o mas dispositivos | Fibra Giga TV Full+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 3 espacios       | Entre 8 y 16 dispositivos | Alto        | 3 o mas dispositivos | Fibra Giga TV Full+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 5 o mas espacios | Entre 8 y 16 dispositivos | Basico      | 3 o mas dispositivos | Fibra Giga TV Full+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 5 o mas espacios | Entre 8 y 16 dispositivos | Alto        | 3 o mas dispositivos | Fibra Giga TV Full+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 3 espacios       | Mas de 16 dispositivos    | Alto        | 3 o mas dispositivos | Fibra Giga TV Full+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 5 o mas espacios | Mas de 16 dispositivos    | Basico      | 3 o mas dispositivos | Fibra Giga TV Full+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Departamento | 1 piso        | 5 o mas espacios | Mas de 16 dispositivos    | Alto        | 3 o mas dispositivos | Fibra Giga TV Full+ |  
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 1 espacio        | Mas de 16 dispositivos    | Alto        | 3 o mas dispositivos | Fibra Giga TV Full+ |        
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 3 espacios       | Mas de 16 dispositivos    | Basico      | 3 o mas dispositivos | Fibra Giga TV Full+ |   
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 3 espacios       | Mas de 16 dispositivos    | Alto        | 3 o mas dispositivos | Fibra Giga TV Full+ |   
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 5 o mas espacios | Mas de 16 dispositivos    | Basico      | 3 o mas dispositivos | Fibra Giga TV Full+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Triple Pack | Casa         | 2 pisos o mas | 5 o mas espacios | Mas de 16 dispositivos    | Alto        | 3 o mas dispositivos | Fibra Giga TV Full+ |
            

    @CHILE_B2C_RECOMENDADOR_MonoPack_Television
    Scenario Outline: Recomendador Mono Pack Television
        Given estoy en la pagina "<URL>"
        When selecciono el servicio "<SERVICIO>"
        And selecciono mi compañia actual "<COMPANIA_ACTUAL>"
        And selecciono internet fuera del hogar "<INTERNET_FUERA_HOGAR>"
        And selecciono TV simultaneas "<TVS>"
        And selecciono el contenido de mi plan
        Then me recomienda el plan ideal "<PLAN_IDEAL>"

        @CHILE_B2C_RECOMENDADOR_MonoPack_Television_TV_Lite
        Examples:
            | URL                          | SERVICIO             | COMPANIA_ACTUAL                 | INTERNET_FUERA_HOGAR   | TVS                  | PLAN_IDEAL |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Television | Otra compañia                   | Si                     | 1 a 2 dispositivos   | TV Lite    |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Television | Otra compañia                   | No                     | 1 a 2 dispositivos   | TV Lite    |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Television | Otra compañia                   | No                     | 3 o mas dispositivos | TV Lite    |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Television | Utilizo internet de mi celular  | Si                     | 1 a 2 dispositivos   | TV Lite    |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Television | Utilizo internet de mi celular  | No                     | 1 a 2 dispositivos   | TV Lite    |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Television | Utilizo internet de mi celular  | No                     | 3 o mas dispositivos | TV Lite    |

        @CHILE_B2C_RECOMENDADOR_MonoPack_Television_TV_Full_Plus
        Examples:
            | URL                          | SERVICIO             | COMPANIA_ACTUAL                 | INTERNET_FUERA_HOGAR   | TVS                  | PLAN_IDEAL |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Television | Entel                           | Si                     | 1 a 2 dispositivos   | TV Full+   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Television | Entel                           | Si                     | 3 o mas dispositivos | TV Full+   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Television | Entel                           | No                     | 1 a 2 dispositivos   | TV Full+   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Television | Entel                           | No                     | 3 o mas dispositivos | TV Full+   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Television | Otra compañia                   | Si                     | 3 o mas dispositivos | TV Full+   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Television | Utilizo internet de mi celular  | Si                     | 3 o mas dispositivos | TV Full+   |

    @CHILE_B2C_RECOMENDADOR_MonoPack_Internet
    Scenario Outline: Recomendador Mono Pack Internet
        Given estoy en la pagina "<URL>"
        When selecciono el servicio "<SERVICIO>"
        And selecciono el tipo de hogar "<TIPO_HOGAR>"
        And selecciono los pisos del hogar "<PISOS_HOGAR>"
        And selecciono los espacios "<ESPACIOS>"
        And selecciono el numero de dispositivos "<DISPOSITIVOS>"
        And selecciono la utilizacion del internet "<UTILIZACION>"
        And selecciono Disney+ Premium "<DISNEY_PREMIUM>"
        Then me recomienda el plan ideal "<PLAN_IDEAL>"

        @CHILE_B2C_RECOMENDADOR_MonoPack_Internet_Fibra_600
        Examples:
            | URL                          | SERVICIO           | TIPO_HOGAR   | PISOS_HOGAR   | ESPACIOS         | DISPOSITIVOS              | UTILIZACION | DISNEY_PREMIUM | PLAN_IDEAL  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 1 espacio        | Menos de 8 dispositivos   | Basico      | No             | Fibra 600   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 1 espacio        | Menos de 8 dispositivos   | Alto        | No             | Fibra 600   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 3 espacios       | Menos de 8 dispositivos   | Basico      | No             | Fibra 600   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 3 espacios       | Menos de 8 dispositivos   | Alto        | No             | Fibra 800   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 1 espacio        | Entre 8 y 16 dispositivos | Basico      | No             | Fibra 600   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 1 espacio        | Entre 8 y 16 dispositivos | Alto        | No             | Fibra 600   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 3 espacios       | Entre 8 y 16 dispositivos | Basico      | No             | Fibra 600   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 1 espacio        | Mas de 16 dispositivos    | Basico      | No             | Fibra 600   |

        @CHILE_B2C_RECOMENDADOR_MonoPack_Internet_Fibra_600_Plus
        Examples:
            | URL                          | SERVICIO           | TIPO_HOGAR   | PISOS_HOGAR   | ESPACIOS         | DISPOSITIVOS              | UTILIZACION | DISNEY_PREMIUM | PLAN_IDEAL  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 1 espacio        | Menos de 8 dispositivos   | Basico      | Si             | Fibra 600+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 1 espacio        | Menos de 8 dispositivos   | Alto        | Si             | Fibra 600+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 3 espacios       | Menos de 8 dispositivos   | Basico      | Si             | Fibra 600+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 1 espacio        | Entre 8 y 16 dispositivos | Basico      | Si             | Fibra 600+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 1 espacio        | Entre 8 y 16 dispositivos | Alto        | Si             | Fibra 600+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 3 espacios       | Entre 8 y 16 dispositivos | Basico      | Si             | Fibra 600+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 1 espacio        | Mas de 16 dispositivos    | Basico      | Si             | Fibra 600+  |

        @CHILE_B2C_RECOMENDADOR_MonoPack_Internet_Fibra_800
        Examples:
            | URL                          | SERVICIO           | TIPO_HOGAR   | PISOS_HOGAR   | ESPACIOS         | DISPOSITIVOS              | UTILIZACION | DISNEY_PREMIUM | PLAN_IDEAL  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 3 espacios       | Menos de 8 dispositivos   | Alto        | No             | Fibra 800   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 5 o mas espacios | Menos de 8 dispositivos   | Basico      | No             | Fibra 800   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 1 espacio        | Menos de 8 dispositivos   | Basico      | No             | Fibra 800   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 1 espacio        | Menos de 8 dispositivos   | Alto        | No             | Fibra 800   |
            # RESULTADO DISTINTO AL QUE CORRESPONDE --> NO CORREGIDO
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 3 espacios       | Menos de 8 dispositivos   | Basico      | No             | Fibra 800   |
            # RESULTADO DISTINTO AL QUE CORRESPONDE --> NO CORREGIDO
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 3 espacios       | Menos de 8 dispositivos   | Alto        | No             | Fibra 800   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 5 o mas espacios | Menos de 8 dispositivos   | Basico      | No             | Fibra 800   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 3 espacios       | Entre 8 y 16 dispositivos | Alto        | No             | Fibra 800   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 5 o mas espacios | Entre 8 y 16 dispositivos | Basico      | No             | Fibra 800   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 1 espacio        | Entre 8 y 16 dispositivos | Basico      | No             | Fibra 800   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 1 espacio        | Entre 8 y 16 dispositivos | Alto        | No             | Fibra 800   |
            # RESULTADO DISTINTO AL QUE CORRESPONDE --> NO CORREGIDO
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 3 espacios       | Entre 8 y 16 dispositivos | Basico      | No             | Fibra 800   | 
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 1 espacio        | Mas de 16 dispositivos    | Alto        | No             | Fibra 800   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 3 espacios       | Mas de 16 dispositivos    | Basico      | No             | Fibra 800   |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 1 espacio        | Mas de 16 dispositivos    | Basico      | No             | Fibra 800   |

        @CHILE_B2C_RECOMENDADOR_MonoPack_Internet_Fibra_800_Plus
        Examples:
            | URL                          | SERVICIO           | TIPO_HOGAR   | PISOS_HOGAR   | ESPACIOS         | DISPOSITIVOS              | UTILIZACION | DISNEY_PREMIUM | PLAN_IDEAL  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 3 espacios       | Menos de 8 dispositivos   | Alto        | Si             | Fibra 800+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 5 o mas espacios | Menos de 8 dispositivos   | Basico      | Si             | Fibra 800+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 1 espacio        | Menos de 8 dispositivos   | Basico      | Si             | Fibra 800+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 1 espacio        | Menos de 8 dispositivos   | Alto        | Si             | Fibra 800+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 3 espacios       | Menos de 8 dispositivos   | Basico      | Si             | Fibra 800+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 3 espacios       | Menos de 8 dispositivos   | Alto        | Si             | Fibra 800+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 5 o mas espacios | Menos de 8 dispositivos   | Basico      | Si             | Fibra 800+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 3 espacios       | Entre 8 y 16 dispositivos | Alto        | Si             | Fibra 800+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 5 o mas espacios | Entre 8 y 16 dispositivos | Basico      | Si             | Fibra 800+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 1 espacio        | Entre 8 y 16 dispositivos | Basico      | Si             | Fibra 800+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 1 espacio        | Entre 8 y 16 dispositivos | Alto        | Si             | Fibra 800+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 3 espacios       | Entre 8 y 16 dispositivos | Basico      | Si             | Fibra 800+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 1 espacio        | Mas de 16 dispositivos    | Alto        | Si             | Fibra 800+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 3 espacios       | Mas de 16 dispositivos    | Basico      | Si             | Fibra 800+  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 1 espacio        | Mas de 16 dispositivos    | Basico      | Si             | Fibra 800+  |

        @CHILE_B2C_RECOMENDADOR_MonoPack_Internet_Fibra_Giga
        Examples:
            | URL                          | SERVICIO           | TIPO_HOGAR   | PISOS_HOGAR   | ESPACIOS         | DISPOSITIVOS              | UTILIZACION | DISNEY_PREMIUM | PLAN_IDEAL  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 5 o mas espacios | Menos de 8 dispositivos   | Alto        | No             | Fibra Giga  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 5 o mas espacios | Menos de 8 dispositivos   | Alto        | No             | Fibra Giga  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 5 o mas espacios | Entre 8 y 16 dispositivos | Alto        | No             | Fibra Giga  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 3 espacios       | Entre 8 y 16 dispositivos | Alto        | No             | Fibra Giga  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 5 o mas espacios | Entre 8 y 16 dispositivos | Basico      | No             | Fibra Giga  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 5 o mas espacios | Entre 8 y 16 dispositivos | Alto        | No             | Fibra Giga  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 3 espacios       | Mas de 16 dispositivos    | Alto        | No             | Fibra Giga  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 5 o mas espacios | Mas de 16 dispositivos    | Basico      | No             | Fibra Giga  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 5 o mas espacios | Mas de 16 dispositivos    | Alto        | No             | Fibra Giga  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 1 espacio        | Mas de 16 dispositivos    | Alto        | No             | Fibra Giga  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 3 espacios       | Mas de 16 dispositivos    | Basico      | No             | Fibra Giga  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 3 espacios       | Mas de 16 dispositivos    | Alto        | No             | Fibra Giga  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 5 o mas espacios | Mas de 16 dispositivos    | Basico      | No             | Fibra Giga  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 5 o mas espacios | Mas de 16 dispositivos    | Alto        | No             | Fibra Giga  |

        @CHILE_B2C_RECOMENDADOR_MonoPack_Internet_Fibra_Giga_Plus
        Examples:
            | URL                          | SERVICIO           | TIPO_HOGAR   | PISOS_HOGAR   | ESPACIOS         | DISPOSITIVOS              | UTILIZACION | DISNEY_PREMIUM | PLAN_IDEAL  |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 5 o mas espacios | Menos de 8 dispositivos   | Alto        | Si             | Fibra Giga+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 5 o mas espacios | Menos de 8 dispositivos   | Alto        | Si             | Fibra Giga+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 5 o mas espacios | Entre 8 y 16 dispositivos | Alto        | Si             | Fibra Giga+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 3 espacios       | Entre 8 y 16 dispositivos | Alto        | Si             | Fibra Giga+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 5 o mas espacios | Entre 8 y 16 dispositivos | Basico      | Si             | Fibra Giga+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 5 o mas espacios | Entre 8 y 16 dispositivos | Alto        | Si             | Fibra Giga+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 3 espacios       | Mas de 16 dispositivos    | Alto        | Si             | Fibra Giga+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 5 o mas espacios | Mas de 16 dispositivos    | Basico      | Si             | Fibra Giga+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Departamento | 1 piso        | 5 o mas espacios | Mas de 16 dispositivos    | Alto        | Si             | Fibra Giga+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 1 espacio        | Mas de 16 dispositivos    | Alto        | Si             | Fibra Giga+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 3 espacios       | Mas de 16 dispositivos    | Basico      | Si             | Fibra Giga+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 3 espacios       | Mas de 16 dispositivos    | Alto        | Si             | Fibra Giga+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 5 o mas espacios | Mas de 16 dispositivos    | Basico      | Si             | Fibra Giga+ |
            | CHILE_URL_ENTEL_RECOMENDADOR | Mono Pack Internet | Casa         | 2 pisos o mas | 5 o mas espacios | Mas de 16 dispositivos    | Alto        | Si             | Fibra Giga+ |