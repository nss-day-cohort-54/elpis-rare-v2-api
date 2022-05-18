"""View module for handling post requests """

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareV2Api.models import Post
from rareV2Api.models import Categories
from rareV2Api.models import RareUser
from rest_framework.decorators import action



class PostView(ViewSet):
    """Post views"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game
        """
        # After getting the event, it is passed to the serializer. 
        # Lastly, the serializer.data is passed to the Response as the response body. 
        # Using Response combines what we were doing with the _set_headers and wfile.write functions.
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        # The serializer class determines how the Python data should be serialized to be sent 
        # back to the client
    
    def list(self, request):
        """Handle GET requests to get all posts

        Returns:
            Response -- JSON serialized list of posts
        """
        # The post variable is now a list of Post objects
        posts = Post.objects.all().order_by("publication_date")
        
        # The request from the method parameters holds all the information for the request from the client. 
        # The request.query_params is a dictionary of any query parameters that were in the url. Using the 
        # .get method on a dictionary is a safe way to find if a key is present on the dictionary. 
        # If the 'type' key is not present on the dictionary it will return None.
        user = request.query_params.get('user', None)
        if user is not None:
            posts = posts.filter(user=user)
            
        # The serializer class determines how the Python data should be serialized to be sent 
        # back to the client
        serializer = PostSerializer(posts, many=True)
        # This time adding many=True to let the serializer know that a list vs. a single 
        # object is to be serialized.
        return Response(serializer.data)
    
    @action(methods=["get"], detail=False)
    def current_user_list(self, request):
        user = RareUser.objects.get(user=request.auth.user)
        posts = Post.objects.filter(user=user)
        
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """
        # Instead of making a new instance of the Game model, the request.data dictionary is 
        # passed to the new serializer as the data. The keys on the dictionary must match what 
        # is in the fields on the serializer. After creating the serializer instance, call is_valid 
        # o make sure the client sent valid data. If the code passes validation, then the save method 
        # will add the game to the database and add an id to the serializer.
        user = RareUser.objects.get(user=request.auth.user)
        serializer = CreatePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        post = Post.objects.get(pk=pk)
        serializer = CreatePostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts
    """
    # The Meta class hold the configuration for the serializer. We’re telling the serializer 
    # to use the Posts model and to include the id andlabel fields.
    class Meta:
        model = Post
        fields = ('id', 'title', 'publication_date', 'image_url', 'content', 'approved', 'category', 'user')
        depth = 3
        
class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # Since the post comes from the Auth header it will not be in the request body
        fields = ['id', 'title', 'publication_date', 'image_url', 'content', 'approved', 'category']
        
