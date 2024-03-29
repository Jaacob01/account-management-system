from django.db import models

from .base import BaseServiceModel


class ElasticSearch(BaseServiceModel):
    elasticPwd = models.CharField(max_length=36, verbose_name="elasticPwd   ", null=True, blank=False)
    kibanaPwd = models.CharField(max_length=36, verbose_name="kibana_system", null=True, blank=True)
    apmPwd = models.CharField(max_length=36, verbose_name='apm_system', null=True, blank=True)
    logstashPwd = models.CharField(max_length=36, verbose_name='logstash_system', null=True, blank=True)
    beatsPwd = models.CharField(max_length=36, verbose_name='beats_system', null=True, blank=True)
    remoteMonitoringPwd = models.CharField(max_length=36, verbose_name='remote_monitoring_user', null=True, blank=True)

    class Meta:
        verbose_name = "Searches"
        verbose_name_plural = "Elastic" + verbose_name
