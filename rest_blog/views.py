from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_blog.models import Post, Comment
from rest_blog.serializers import PostSerializer, CommentSerializer


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


class PostApiViews(APIView):
    get_post_method = ['get','post']
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return Response(data=self.serializer_class(posts,many=True).data)

    def post(self,request, *args, **kwargs):
        title = request.data.get('title')
        description = request.data.get('description')
        posts = Post.objects.create(title=title,description=description)
        posts.save()
        return Response(data=self.serializer_class(posts).data)


class CommentApiViews(APIView):
    get_post_method = ['get','post']
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        posts = Comment.objects.all()
        return Response(data=self.serializer_class(posts,many=True).data)

    def post(self,request, *args, **kwargs):
        comment = request.data.get('comment')
        date_added = request.data.get('date_added')
        comments = Post.objects.create(comment=comment,date_added=date_added)
        comments.save()
        return Response(data=self.serializer_class(comments).data)