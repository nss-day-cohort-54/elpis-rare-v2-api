from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareV2Api.models import Tags
from rareV2Api.models import RareUser


class TagView(ViewSet):
    
    def retrieve(self, request,pk):
        
        try:
            tag = Tags.objects.get(pk=pk)
            serializer = TagsSerializer(tag)
            return Response(serializer.data)
        except Tags.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
            
    def list(self, request):
        tags = Tags.objects.all()
        serializer = TagsSerializer(tags,many=True)
        return Response(serializer.data)
    
    def create(self, request):
        
        rareUser = RareUser.objects.get(user=request.auth.user)
        serializer = CreateTagsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(rareUser=rareUser)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        # Handle Put requests for a tag
        
        tag = Tags.objects.get(pk=pk)
        serializer = CreateTagsSerializer(tag, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        tag = Tags.objects.get(pk=pk)
        tag.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
            
            
            
class TagsSerializer(serializers.ModelSerializer):
    """JSON serializer for tags
    """
    class Meta:
        model = Tags
        fields = ('id', 'label')
        depth = 1
        
class CreateTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'label')
            
            

            