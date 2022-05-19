from datetime import date, datetime
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareV2Api.models import Post, Comments, RareUser
from django.core.exceptions import ValidationError
from rest_framework.decorators import action

class CommentView(ViewSet):
    """Level up Event s view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single Event 

        Returns:
            Response -- JSON serialized Event 
        """
        comment = Comments.objects.get(pk=pk)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)
        

    def list(self, request):
        """Handle GET requests to get all Event s

        Returns:
            Response -- JSON serialized list of Event s
        """
        user = RareUser.objects.get(user=request.auth.user)
        comments = Comments.objects.all().order_by("created_on")
        serializer = CommentsSerializer(comments, many=True)
        # current_post = Post.objects.get(pk=request.data['post'])
        return Response(serializer.data)
    
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized event instance
        """
        author = RareUser.objects.get(user=request.auth.user)
        post = Post.objects.get(pk=request.data['post'])
        request.data['created_on']=datetime.today()
        serializer = CreateCommentsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=author, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a comment

        Returns:
            Response -- Empty body with 204 status code
        """
        comment = Comments.objects.get(pk=pk)
        serializer = CreateCommentsSerializer(comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        comment = Comments.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class CommentsSerializer(serializers.ModelSerializer):
    """JSON serializer for Comments
    """
    class Meta:
        model = Comments
        fields = ('id', 'post', 'author','content', 'created_on')
        depth=3
        
class CreateCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'post_id','content', 'created_on']