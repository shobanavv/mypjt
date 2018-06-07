from rest_framework import serializers
from .models import Language

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'paradigm')

#model serializer would take care of destructuring the fields from model.py even from a form