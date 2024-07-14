import json
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from django.db import models


class TarefaExterna(models.Model):
    nome = models.CharField(max_length=255)
    caminho_script = models.CharField(max_length=255)
    horario = models.ForeignKey(CrontabSchedule, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        args_json = json.dumps([self.caminho_script])
        PeriodicTask.objects.update_or_create(
            name=self.nome,
            defaults={
                'crontab': self.horario,
                'task': 'app.tasks.executar_codigo_externo',
                'args': args_json,
            }
        )
