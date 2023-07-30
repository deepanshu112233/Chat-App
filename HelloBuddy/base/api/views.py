from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import JsonResponse
from base.models import Room
from .serializers import RoomSerializers

@api_view(['GET']) #http method allowed to access views like,'POST','PUT' but we allow GET so users are allowed only to get data
def getRoutes(request):
    routes=[
        'GET /api',
        'GET /api/rooms',             #api so that people can see alla routes
        'GET /api/rooms/:id'
    ]
    # return  jsonResponse(routes,safe=False)
    # #False basically means we are using more than dictionary inside of response,Safe allow list to be json data to use this uncomment line 3
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms=Room.objects.all()
    serializer=RoomSerializers(rooms,many=True)#many means there are multiple objects that need to be serilalize
    #serializer now become object here 
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request,pk):
    room=Room.objects.get(id=pk)
    serializer=RoomSerializers(room,many=False)#single object will be return
    #serializer now become object here 
    return Response(serializer.data)