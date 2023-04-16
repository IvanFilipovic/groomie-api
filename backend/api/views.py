from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from groomie.models import UniqueWedding, Guest, BasicWedding, BasicGuest
from customers.models import Customer
from .serializers import WeddingSerializer, GuestSerializerCreate, GuestSerializerDetail, UserSerializer, BasicWeddingSerializer, BasicGuestSerializerCreate
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin

"""
@api_view(['GET', 'PUT']) # wedding GET i PUT - Dashboard detalji vjenčanja i uredi vjenčanje
def wedding_detail(request, wedding_slug):
    try: 
        wedding = Wedding.objects.get(wedding_slug=wedding_slug)
    except Wedding.DoesNotExist: 
        return JsonResponse({'message': 'Vjenčanje ne postoji'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        serializer = WeddingSerializer(wedding) 
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT': 
        wedding_data = JSONParser().parse(request) 
        serializer = WeddingSerializer(wedding, data=wedding_data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET', 'PUT']) # Guest GET i PUT - Pozivnica za svakog gosta individualno
def guest_detail(request, guest_slug):
    try: 
        guest = Guest.objects.get(guest_slug=guest_slug)
    except Wedding.DoesNotExist: 
        return JsonResponse({'message': 'Pozivnica ne postoji'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        serializer = GuestSerializerDetail(guest) 
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT': 
        wedding_data = JSONParser().parse(request) 
        serializer = GuestSerializerDetail(guest, data=wedding_data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['POST']) # wedding POST - Korisnik kreira vjenčanje
def wedding_create(request):
    if request.method == 'POST':
        wedding_data = JSONParser().parse(request)
        serializer = WeddingSerializer(data=wedding_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST']) # Guest POST - Korisnik dodaje pojedinačnog gosta
def guest_add(request, wedding_slug):
    if request.method == 'POST':
        guest_data = JSONParser().parse(request)
        guest_data['wedding_owner'] = wedding_slug
        serializer = GuestSerializerCreate(data=guest_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET']) # GET guest list for wedding - Dashboard - Lista sve goste od određenog vjenčanja
def guest_list(request, wedding_slug):
    try: 
        guest = Guest.objects.all().filter(wedding_owner=wedding_slug)
    except Wedding.DoesNotExist: 
        return JsonResponse({'message': 'Svadba ne postoji'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET': 
        serializer = GuestSerializerCreate(guest) 
        return JsonResponse(serializer.data)
"""

class GuestList(generics.ListAPIView): # GET guest list for wedding - Dashboard
    queryset = Guest.objects.all()
    serializer_class = GuestSerializerCreate

    def get_queryset(self):
        return super().get_queryset().filter(
            wedding_owner=self.kwargs['wedding_slug']
        )

class BasicGuestList(generics.ListAPIView): # GET guest list for wedding - Dashboard
    queryset = BasicGuest.objects.all()
    serializer_class = BasicGuestSerializerCreate

    def get_queryset(self):
        return super().get_queryset().filter(
            wedding_owner=self.kwargs['wedding_slug']
        )

class WeddingViewSet(CreateModelMixin,ListModelMixin,RetrieveModelMixin,UpdateModelMixin,GenericViewSet):
    serializer_class = WeddingSerializer
    def get_queryset(self):
        return UniqueWedding.objects.all()

class BasicWeddingViewSet(CreateModelMixin,ListModelMixin,RetrieveModelMixin,UpdateModelMixin,GenericViewSet):
    serializer_class = BasicWeddingSerializer
    def get_queryset(self):
        return BasicWedding.objects.all()

class GuestForUserViewSet(CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,GenericViewSet):
        serializer_class = GuestSerializerCreate
        def get_queryset(self):
            return Guest.objects.all()

class BasicGuestForUserViewSet(CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,GenericViewSet):
        serializer_class = BasicGuestSerializerCreate
        def get_queryset(self):
            return BasicGuest.objects.all()

class GuestViewSet(RetrieveModelMixin,UpdateModelMixin,GenericViewSet):
    serializer_class = GuestSerializerDetail
    def get_queryset(self):
        return Guest.objects.all()

class UserViewSet(CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,GenericViewSet):
    serializer_class = UserSerializer
    def get_queryset(self):
        return Customer.objects.all()