from django.db import models


class KeyValue(models.Model):
    key = models.CharField(max_length=64, primary_key=True)
    value = models.JSONField(default=dict)

    def __str__(self):
        return self.key

    @classmethod
    def set(cls, key, value):
        obj, created = cls.objects.update_or_create(key=key, defaults={'value': value})
        return obj

    @classmethod
    def get(cls, key, default=None, save=True):
        try:
            return cls.objects.get(key=key).value
        except cls.DoesNotExist:
            if save:
                return cls.set(key, default).value
            return default

    @classmethod
    def fetch(cls, keys, default=None):
        result = {key: value for key, value in cls.objects.filter(key__in=keys).values_list('key', 'value')}
        return {key: result.get(key, default) for key in keys}
