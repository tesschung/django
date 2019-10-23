from rest_framework import serializers
from .models import *


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id', )


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', )


# ArtistSerializers을 상속 받아도 된다.
class ArtistDetailSerializer(ArtistSerializer):
    # 중요
    # MusicSerializers로 serializing을 해서 보내준다.
    musics = MusicSerializer(many=True)
    class Meta(ArtistSerializer.Meta):
        # ArtistSerializer.Meta.fields 이부분도 tuple이여야 한다.
        fields = ArtistSerializer.Meta.fields + ('musics',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
