from rest_framework import serializers
from .models import User

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    # def create(self, validated_data):
    #     user = User.objects.create_user(
    #         username = validated_data['username'], 
    #         password = validated_data['password']
    #     )

    #     return user
