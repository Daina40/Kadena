from rest_framework import serializers
from Production_app.models import ProductionModel

class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionModel
        fields = '__all__'