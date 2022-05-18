"""View module for handling requests about categories"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareV2Api.models import Categories


class CategoryView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single category
        
        Returns:
            Response -- JSON serialized category
        """
        try:
            category = Categories.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Categories.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle GET requests to get all categories

        Returns:
            Response -- JSON serialized list of categories
        """
        categories = Categories.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized category instance
        """
        serializer = CreateCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a category

        Returns:
            Response -- Empty body with 204 status code
        """

        category = Categories.objects.get(pk=pk)
        category.label = request.data["label"]
        category.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE requests for a category

        Returns:
            Response -- Empty body with 204 status code
        """
        category = Categories.objects.get(pk=pk)
        category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    """
    class Meta:
        model = Categories
        fields = ('id', 'label')
        
class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'label']        
        