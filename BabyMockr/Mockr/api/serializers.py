__author__ = 'andreasfalley'

from django.forms import widgets
from rest_framework import serializers


from Mockr.models import MockrUser,BabyName,Mock,Favorite


class MockrUserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)

    mockr_username = serializers.CharField(max_length=50)
    created_at = serializers.DateTimeField()

    is_Mockr = serializers.BooleanField(default=False)
    is_Facebook = serializers.BooleanField(default=False)

    def create(self, validated_data):

        return MockrUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.email = validated_data.get('email', instance.email)
        instance.is_mockr = validated_data.get('is_mockr', instance.is_mockr)
        instance.is_facebook = validated_data.get('is_facebook', instance.is_facebook)
        instance.save()

        return instance


class BabyNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = BabyName
        fields = ('first_name', 'middle_name', 'last_name', 'rank')

class MocksSerializer(serializers.ModelSerializer):

    baby_name = serializers.SlugRelatedField(slug_field='first_name', read_only=True)

    class Meta:
        model = Mock
        fields = ('mock_text', 'brutality', 'stupidity', 'rhyming', 'funny', 'baby_name' )


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ('is_favorite')


class BabyMocksSerializer(serializers.ModelSerializer):
    bn = BabyNameSerializer(many=True, read_only=True)

    class Meta:
        model = Mock
        fields = ('mock_text', 'brutality', 'stupidity', 'rhyming', 'funny', 'bn' )









