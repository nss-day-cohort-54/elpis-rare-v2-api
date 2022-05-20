from django.db.models.functions import Lower
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareV2Api.models.rareuser import RareUser

class RareUserView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single category
        
        Returns:
            Response -- JSON serialized category
        """
        try:
            rare_user = RareUser.objects.get(pk=pk)
            serializer = RareUserSerializer(rare_user)
            return Response(serializer.data)
        except RareUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle GET requests to get all categories

        Returns:
            Response -- JSON serialized list of categories
        """
        rare_users = RareUser.objects.all().order_by(Lower('user__username'))
        serializer = RareUserSerializer(rare_users, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized category instance
        """
        serializer = CreateRareUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a category

        Returns:
            Response -- Empty body with 204 status code
        """

        rare_user = RareUser.objects.get(pk=pk)
        rare_user.bio = request.data["bio"]
        rare_user.profile_image_url = request.data["profile_image_url"]
        rare_user.created_on = request.data["created_on"]
        rare_user.active = request.data["active"]
        rare_user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE requests for a category

        Returns:
            Response -- Empty body with 204 status code
        """
        rare_user = RareUser.objects.get(pk=pk)
        rare_user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class RareUserSerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    """
    class Meta:
        model = RareUser
        fields = ('id', 'user', 'bio', 'profile_image_url', 'created_on', 'active')
        depth = 4
        
class CreateRareUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RareUser
        fields = ['bio', 'profile_image_url', 'created_on', 'active']        
        