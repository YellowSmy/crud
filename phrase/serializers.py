from django.db.models import fields
from rest_framework import serializers
from .models import Phrase

class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = ('id', 'phrase')