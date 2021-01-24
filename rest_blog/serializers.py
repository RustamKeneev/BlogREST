from rest_framework import serializers
from rest_blog.models import Post,Comment

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = 'id title image description date_added comments'.split()

    def get_comments(self,obj):
        comments = Comment.objects.filter(post=obj)
        return CommentSerializer(comments,many=True).data

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'id comment date_added'.split()




