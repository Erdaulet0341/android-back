from rest_framework import serializers
import bcrypt
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta
from django.utils import timezone

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = bcrypt.hashpw(password.encode('utf-8'),
                                         bcrypt.gensalt())
        validated_data['password'] = hashed_password.decode('utf-8')  
        return super().create(validated_data)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = bcrypt.hashpw(password.encode('utf-8'),
                                         bcrypt.gensalt())
        validated_data['password'] = hashed_password.decode('utf-8')  
        instance =  super().create(validated_data)
    
        refresh = RefreshToken.for_user(instance)
        instance.refresh_token = str(refresh)
        instance.refresh_token_expiry = timezone.now() + timedelta(weeks=1)
        instance.save()
        return instance


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class LikedSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeProducts
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'