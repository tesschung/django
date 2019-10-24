from django.shortcuts import render, get_object_or_404
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework import serializers

@api_view(['GET'])
def music_list(request):
    # 만약에 artist_pk가 넘어온다면, artist_pk로 필터링한 값만 응답한다.
    # 그렇지 않다면 전체 음악을 응답한다.

    # 1. params dict 생성
    params = {}
    # 2. artist_pk 값을 가져오는데,
    artist_pk = request.GET.get('artist_pk')

    # 3. artist_pk 가 None이 아니라면,
    if artist_pk is not None:
        # artist_id라는 곳에 artist_pk를 넣는다.
        params['artist_id'] = artist_pk

    # 4. dict에 있는 모든 값을 넣겠도록 **params 처리
    musics = Music.objects.filter(**params)
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)

# view함수 하나로 분기를 GET PUT DELETE로 나눠 실행
@api_view(['GET', 'PUT', 'DELETE'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    if request.method == 'GET':
        # 하나만 반환하므로 many=True를 할 필요 없다.
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MusicSerializer(data=request.data, instance=music)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    else:
        music.delete()
        return Response({'message':'Comment has been deleted.'})

@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    # 하나만 반환하므로 many=True를 할 필요 없다.
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def comments_create(request, music_pk):
    print(request.data)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True): # 검증에 실패하면 400 Bad Request 오류를 발생
        serializer.save(music_id=music_pk)
    return Response(serializer.data)

# view에 ['PUT', 'DELETE'] 지정한 기능만 사용 가능
@api_view(['PUT', 'DELETE'])
def comments_update_and_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        # 위에서 가져온 comment를 넣어준다.
        # 그리고 serializer에 담아준다.
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data) #  Response({'message': 'Comment has been updated.'})
    else: # ==> 'DELETE'
        comment.delete()
        return Response({'message':'Comment has been deleted.'})


