from Mockr.models import MockRating

__author__ = 'andreasfalley'


from rest_framework import serializers


from Mockr.models import MockrUser, BabyName, Mock, Favorite


class MockrUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MockrUser
        fields = ('mockr_user',)


class BabyNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = BabyName
        fields = ('name', 'rank', 'mockr_user')


class MocksSerializer(serializers.ModelSerializer):

    # mockr_user = serializers.SlugRelatedField(slug_field='mockruser', read_only=True)
    baby_name = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Mock
        fields = ('mock_text', 'rhyming', 'baby_name', 'is_parents_favorite', 'mockr_user')


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ('is_favorite', 'mocks', 'mockr_user')

#
# class BabyMocksSerializer(serializers.ModelSerializer):
#     bn = BabyNameSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Mock,
#         fields = ('mock_text', 'rhyming', 'bn' )


class MockRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = MockRating
        fields = ('brutality', 'stupidity', 'funny', 'overall')
