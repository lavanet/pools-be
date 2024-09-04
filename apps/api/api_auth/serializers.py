from django.contrib.auth import get_user_model
from rest_framework import serializers


def _get_field_names(model, private=('password', 'key')):
    return [field.name for field in model._meta.fields if field.name not in private]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = _get_field_names(model)

    def save(self, **kwargs):
        # This serializer is read-only because it allows too many fields to be changed.
        raise Exception('Saving is forbidden in this package.')
