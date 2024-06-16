from __future__ import absolute_import, unicode_literals
import logging

from celery import shared_task

from .models import Product


logger = logging.getLogger(__name__)


@shared_task
def add():
    logger.info("Tarefa 'add' iniciada.")
    produtos = Product.objects.all()
    logger.info(f"Produtos encontrados: {produtos.count()}")

    for produto in produtos:
        logger.info(f"Verificando produto: {produto.id} - {produto.name}")
        if produto.quantity == 0:
            logger.info(f"Produto {produto.id} - {produto.name} está com quantidade 0. Desativando.")
            produto.active = False
            produto.save()
            logger.info(f"Produto {produto.id} - {produto.name} desativado e salvo.")
    logger.info("Tarefa 'add' concluída.")
