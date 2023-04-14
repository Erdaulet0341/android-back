from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Seller, Client, Admin
from .serializers import SellerSerializer, ClientSerializer, AdminSerializer


@api_view(['GET'])
def getOverView(request):
    return Response({
        'api':'All datas',
        'api/users': 'All users'
    })


@api_view(['GET'])
def getAllSeller(request):
    sellers = Seller.objects.all()
    serializer = SellerSerializer(sellers, many = True)
    return Response(serializer.data)


@api_view(['POST'])
def createSeller(request):
    serializer = SellerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response({
        "error":"invalid seller"
    })


@api_view(['GET'])   
def getAllClient(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createClient(request):
    serializer = ClientSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response({
        "error":"invalid client"
    })


@api_view(['GET'])
def adminList(request):
    admins = Admin.objects.all()
    adminsSer = AdminSerializer(admins, many=True)
    return Response(adminsSer.data)