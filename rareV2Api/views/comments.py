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
        comments = Comments.objects.all()
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized event instance
        """
        user = RareUser.objects.get(user=request.auth.user)
        post = Post.objects.get(pk=request.data['post_id'])
        serializer = CreateCommentsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CommentsSerializer(serializers.ModelSerializer):
    """JSON serializer for Comments
    """
    class Meta:
        model = Comments
        fields = ('id', 'post', 'author','content', 'created_on')
        
class CreateCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'post_id', 'author_id','content', 'created_on']