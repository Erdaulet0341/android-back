from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Seller, Client, Admin
from django.views.decorators.csrf import csrf_exempt
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

        
class SellerById(APIView):
    def delete(self, request, seller_id):
        try:
            seller = Seller.objects.get(id = seller_id)
        except Seller.DoesNotExist as e:
            return JsonResponse({"error": str(e)})
        
        seller.delete()
        return JsonResponse({"delete": "succesful"})
    

class ClientById(APIView):
    def delete(self, request, client_id):
        try:
            client = Client.objects.get(id = client_id)
        except Seller.DoesNotExist as e:
            return JsonResponse({"error": str(e)})
        
        client.delete()
        return JsonResponse({"delete": "succesful"})