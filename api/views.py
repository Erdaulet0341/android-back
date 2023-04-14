from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from .serializers import *

@api_view(['GET'])
def adminList(request):
    admins = Admin.objects.all()
    adminsSer = AdminSerializer(admins, many=True)
    return Response(adminsSer.data)


class Sellers(APIView):
    def get(self, request):
        sellers = Seller.objects.all()
        serializer = SellerSerializer(sellers, many = True)
        return Response(serializer.data)
    
    def post(self, request):
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

class Clients(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            "error":"invalid client"
        })

        
class SellerById(APIView):

    def get(self, request, seller_id):
        try:
            seller = Seller.objects.get(id = seller_id)
            sellerSer = SellerSerializer(seller, many=False)
            return Response(sellerSer.data)
        except Seller.DoesNotExist as e:
            return JsonResponse({"error": str(e)})

    def delete(self, request, seller_id):
        try:
            seller = Seller.objects.get(id = seller_id)
        except Seller.DoesNotExist as e:
            return JsonResponse({"error": str(e)})
        
        seller.delete()
        return JsonResponse({"delete": "succesful"})
    

class ClientById(APIView):

    def get(self, request, client_id):
        try:
            client = Client.objects.get(id = client_id)
            clientSer = ClientSerializer(client, many = False)
            return Response(clientSer.data)
        except Client.DoesNotExist as e:
            return Response({"error": str(e)})

    def delete(self, request, client_id):
        try:
            client = Client.objects.get(id = client_id)
        except Client.DoesNotExist as e:
            return JsonResponse({"error": str(e)})
        client.delete()
        return JsonResponse({"delete": "succesful"})
    

class Categoties(APIView):
    def get(self, request):
        categories = Category.objects.all()
        categoriesSer = CategorySerializer(categories, many = True)
        return Response(categoriesSer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            "error":"invalid category"
        })


class Products(APIView):
    def get(self, request):
        products = Product.objects.all()
        productSer = ProductSerializer(products, many = True)
        return Response(productSer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            "error":"invalid category"
        })
    
class GetAllProductsDetails(APIView):
    def get(self, request):
        products_det = Product_Details.objects.all()
        productSer_det = ProductDetailsSerializer(products_det, many = True)
        return Response(productSer_det.data)
    
    def post(self, request):
        serializer = ProductDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            "error":"invalid category"
        })
    
class RatingsView(APIView):
    def get(self, request):
        rating = Rating.objects.all()
        ratingSer = RatingSerializer(rating, many = True)
        return Response(ratingSer.data)
    
    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            "error":"invalid category"
        })