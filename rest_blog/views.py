from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_blog.models import Post
from rest_blog.serializers import PostSerializer


@api_view(['GET'])
def get_all_posts(request):
    post = Post.objects.all()
    data = PostSerializer(post,many=True).data
    return Response(data=data)

@api_view(['GET'])
def get_post(request,id):
    try:
        posts = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(data={'result':'сообщение не существует'},status=status.HTTP_404_NOT_FOUND)
    data = PostSerializer(posts).data
    return Response(data=data,status=status.HTTP_200_OK)

