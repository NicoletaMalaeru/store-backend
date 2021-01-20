from rest_framework import serializers
from .models import *


class ProductsSerializer(serializers.ModelSerializer):
	category = serializers.SlugRelatedField(read_only=True, slug_field='category')
	class Meta:
		model = Product
		fields = '__all__'
