from Mockr.models import MockRating

__author__ = 'andreasfalley'

from django.forms import widgets
from rest_framework import serializers


from Mockr.models import MockrUser, BabyName, Mock, Favorite


class MockrUserSerializer(serializers.Serializer):

    class Meta:
        model = MockrUser
        fields = ('mockr_username', 'first_name', 'last_name', 'username',
                  'is_admin', 'created_at', 'updated_at', 'email', 'is_mockr', 'is_facebook')

class BabyNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = BabyName
        fields = ('name ', 'rank')

class MocksSerializer(serializers.ModelSerializer):

    baby_name = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Mock
        fields = ('mock_text', 'rhyming', 'baby_name', 'is_parents_favorite' )


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ('is_favorite')

#
# class BabyMocksSerializer(serializers.ModelSerializer):
#     bn = BabyNameSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Mock,
#         fields = ('mock_text', 'rhyming', 'bn' )

class MockRatingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MockRating
        fields = ('brutality', 'stupidity', 'funny', 'overall')










