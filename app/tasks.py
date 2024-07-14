from __future__ import absolute_import, unicode_literals
import logging
import subprocess

from celery import shared_task


logger = logging.getLogger(__name__)


@shared_task
def executar_codigo_externo(caminho_script):
    try:
        result = subprocess.run(['python', caminho_script], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script: {e.stderr}")

