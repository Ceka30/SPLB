import json
import os
import requests
from requests.auth import HTTPBasicAuth

# Configuracion JIRA
JIRA_BASE_URL = "https://cg-externo-entel.atlassian.net"
JIRA_USERNAME = "mut_cgomez@externos.entel.cl"
# JIRA_TOKEN = "ATATT3xFfGF0KI77ReEdTDUgki8obmYwwrwbEckIiT4knfmybFvvOxgnQQXwwubL-NJbBG7V_VfUc005xeHTZ6cXeHq_wke7RQAm0FOV33Bmm90eJzo8RK2HsvzHz9J-m3IU_WAUgWGu6Z2bcmyvpmlMBy4C8SJUSrFsmnfyt76B9X9nbxNB5yU=F8292112"
JIRA_TOKEN = "ATATT3xFfGF0Tcj66fMGQKVanuua6MJXn89cbp4MzI_Gu1siht47YqOhzZmThCmh1MgkFICpZvzCt03yCeP_33nfbX8Nv_2ur1WhGnfw21sbaSUscmxDOIUFj_Oa5nyek1pFw0BoHhpywhc2QlcOOz-9phDqvOEcNsQL9WEdedVz49tJhC71ZZ0=AD36F18F"
TEAMS_TOKEN = "https://prod-144.westus.logic.azure.com:443/workflows/dd5d62cd9f944280b8c4b1a4917de149/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=6tIyI-Mu_dvh76NQlDH8meS8EwAXyh4z7HhWekinzRY"


def generar_informe(report_name):
    try:
        print("Generando informe Allure...")
        os.system(
            "allure generate allure-results --clean -o allure-report --single-file"
        )
        print(os.curdir)
        os.rename("allure-report/index.html", f"allure-report/{report_name}.html")
        print("Informe generado correctamente.")
    except Exception as e:
        print(f"Error al generar el informe: {e}")
        raise


def enviar_informe_jira(JIRA_ISSUE_KEY, estado, report_name, public_url, video_url):
    archivo = f"allure-report/{report_name}.html"
    try:
        if not os.path.exists(archivo):
            raise FileNotFoundError(f"El archivo {archivo} no existe.")

        url = f"{JIRA_BASE_URL}/rest/api/2/issue/{JIRA_ISSUE_KEY}/attachments"
        auth = HTTPBasicAuth(JIRA_USERNAME, JIRA_TOKEN)

        headers = {"Accept": "application/json", "X-Atlassian-Token": "no-check"}

        response = requests.post(
            url,
            headers=headers,
            auth=auth,
            files={"file": (archivo, open(archivo, "rb"), "application-type")},
        )

        if response.status_code != 200:
            raise Exception(f"Error al enviar el archivo: {response.status_code}")

        attachment_data = response.json()[0]
        attachment_url = attachment_data["content"]
        attachment_name = attachment_data["filename"]
        comment_url = f"{JIRA_BASE_URL}/rest/api/3/issue/{JIRA_ISSUE_KEY}/comment"

        headers = {"Accept": "application/json", "Content-Type": "application/json"}

        if estado == "Passed":
            mensaje = "El test ha pasado exitosamente."
            tipo = "success"
        else:
            mensaje = "El test ha fallado."
            tipo = "error"

        payload = json.dumps(
            {
                "body": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "panel",
                            "attrs": {"panelType": tipo},
                            "content": [
                                {
                                    "type": "paragraph",
                                    "content": [{"type": "text", "text": mensaje}],
                                }
                            ],
                        },
                        {
                            "type": "panel",
                            "attrs": {"panelType": "note"},
                            "content": [
                                {
                                    "type": "paragraph",
                                    "content": [{"type": "text", "text": "Evidencias"}],
                                }
                            ],
                        },
                        {
                            "type": "paragraph",
                            "content": [
                                {"type": "text", "text": "1. "},
                                {
                                    "type": "text",
                                    "text": attachment_name,
                                    "marks": [
                                        {
                                            "type": "link",
                                            "attrs": {"href": attachment_url},
                                        }
                                    ],
                                },
                            ],
                        },
                        {
                            "type": "paragraph",
                            "content": [
                                {"type": "text", "text": "2. "},
                                {
                                    "type": "text",
                                    "text": "Build LambdaTest",
                                    "marks": [
                                        {"type": "link", "attrs": {"href": public_url}}
                                    ],
                                },
                            ],
                        },
                        {
                            "type": "paragraph",
                            "content": [
                                {"type": "text", "text": "3. "},
                                {
                                    "type": "text",
                                    "text": "LambdaTest Video",
                                    "marks": [
                                        {"type": "link", "attrs": {"href": video_url}}
                                    ],
                                },
                            ],
                        },
                    ],
                },
                "anonymous": True,
            }
        )

        response = requests.request(
            "POST", comment_url, data=payload, headers=headers, auth=auth
        )

        if response.status_code == 201:
            print("Comentario Automatico creado exitosamente.")
        else:
            print(f"Error al crear comentario: {response.status_code}")

        return attachment_url

    except FileNotFoundError:
        print(f"El archivo '{archivo}' no existe.")
    except Exception as e:
        print(f"Ocurrio un error: {e}")


def enviar_informe_teams(
    estado, fecha_ejecucion, flujo_name, report_name, public_url, video_url
):
    headers = {"Content-Type": "application/json"}

    # Definir color y mensaje basado en el resultado de la prueba
    if estado == "Passed":
        titulo = "Prueba Automatizada Exitosa"
        color_titulo = "Good"
        type_status = "OK"
    else:
        titulo = "Prueba Automatizada Fallida"
        color_titulo = "Attention"
        type_status = "FAIL"

    # Cuerpo de la solicitud con Adaptive Card
    data = {
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "type": "AdaptiveCard",
                    "version": "1.4",
                    "msteams": {"width": "full"},
                    "body": [
                        {
                            "type": "TextBlock",
                            "text": titulo,
                            "weight": "Bolder",
                            "size": "ExtraLarge",
                            "color": color_titulo,
                        },
                        {
                            "type": "TextBlock",
                            "text": f"**Estado:** {type_status}",
                            "weight": "Bolder",
                            "size": "Medium",
                        },
                        {
                            "type": "TextBlock",
                            "text": "**Descripcion:** www.entel.cl",
                            "size": "Medium",
                        },
                        {
                            "type": "TextBlock",
                            "text": f"**Ultima Ejecución:** {fecha_ejecucion}",
                            "weight": "Bolder",
                            "size": "Medium",
                        },
                        {
                            "type": "TextBlock",
                            "text": f"**Flujo:** {flujo_name}",
                            "size": "Medium",
                        },
                        {
                            "type": "ActionSet",
                            "actions": [
                                {
                                    "type": "Action.OpenUrl",
                                    "title": "Descargar Reporte",
                                    "url": report_name,
                                },
                                {
                                    "type": "Action.OpenUrl",
                                    "title": "Reporte LambdaTest",
                                    "url": public_url,
                                },
                                {
                                    "type": "Action.OpenUrl",
                                    "title": "Descargar Video Ejecucion",
                                    "url": video_url,
                                },
                            ],
                        },
                    ],
                },
            }
        ]
    }

    try:
        response = requests.post(TEAMS_TOKEN, headers=headers, json=data)

        response_text = response.text.strip()

        # Verificar la respuesta
        if response.status_code == 200:
            print("Mensaje enviado correctamente.")
        elif response.status_code == 202:
            if response_text:
                print(
                    f"Mensaje aceptado, pero la respuesta indica posible error:\n{response_text}"
                )
            else:
                print("Mensaje aceptado y procesado correctamente en Teams.")
        else:
            print(f"Error al enviar el mensaje a Teams: {response.status_code}")
            print("Detalles de la respuesta:")
            print(response_text if response_text else "Sin detalles en la respuesta.")

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud a Teams: {e}")
