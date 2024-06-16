from django.db import models


class Product(models.Model):
    name = models.CharField(
        blank=True,
        null=True, verbose_name='Nome ',
        max_length=2042
    )
    quantity = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Quantidade '
    )
    active = models.BooleanField(
        verbose_name='Ativo: ',
        default=True
    )

    class Meta:
        db_table = 'produtos'

    def __str__(self):
        return self.name
