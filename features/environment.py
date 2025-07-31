from datetime import datetime, timedelta
import os
from config.init_config import init_config
from utils.report_handler import (
    generar_informe,
    enviar_informe_jira,
    enviar_informe_teams,
)

public_url = None
video_url = None
flujo_name = None
estado = "Failed"


def before_all(context):
    os.environ["ENVIRONMENT"] = context.config.userdata.get("environment", "produccion")
    context.jira_issue_key = context.config.userdata.get("jira_issue_key")
    context.fecha_ejecucion = (datetime.now() + timedelta(hours=-3)).strftime(
        "%Y-%m-%d %H:%M"
    )
    context.report_name = f"Reporte_QA_{context.fecha_ejecucion}".replace(":", "_")
    if not context.jira_issue_key:
        raise ValueError("No existe jira_issue_key.")

    current_tags = str(context.config.tags)
    if not current_tags:
        raise ValueError("No existe TAG global de ejecucion.")


def before_scenario(context, scenario):
    init_config(context, scenario)


def after_scenario(context, scenario):
    if context.driver:
        status = "failed" if scenario.status == "failed" else "passed"
        globals()["estado"] = "Passed" if status == "passed" else "Failed"

        context.driver.execute_script(f"lambda-status={status}")
        print(f"Ejecucion LambdaTest: {status}")
        context.driver.quit()

    print(f"Test: {status}")
    globals().update(
        {
            "public_url": context.public_url,
            "video_url": context.video_url,
            "flujo_name": context.flujo_name,
        }
    )


def after_all(context):
    generar_informe(context.report_name)
    print("Enviando informe Allure a Jira...")

    attachment_name = enviar_informe_jira(
        context.jira_issue_key,
        globals()["estado"],
        context.report_name,
        globals()["public_url"],
        globals()["video_url"],
    )

    # enviar_informe_teams(
    #     globals()["estado"],
    #     context.fecha_ejecucion,
    #     globals()["flujo_name"],
    #     attachment_name if attachment_name else context.report_name,
    #     globals()["public_url"],
    #     globals()["video_url"],
    # )


# def before_scenario(context, scenario):
#     init_config(context, scenario)


# def after_scenario(context, scenario):
#     context.driver.quit()
