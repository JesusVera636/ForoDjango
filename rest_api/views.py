from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from foro.models import Hilo
from .serializers import PostSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_posts(request):
    if request.method == 'GET':
        post = Hilo.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status= status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def vista_post_mod(request, id):
    try:
        p = Hilo.objects.get(idHilo=id)
    except Hilo.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PostSerializer(p)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostSerializer(p, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        p.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)