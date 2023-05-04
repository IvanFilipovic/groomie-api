from rest_framework import generics, viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from groomie.models import UniqueWedding, UniqueGuest, BasicWedding, BasicGuest
from customers.models import Customer
from .serializers import WeddingSerializer, CountSerialize, GuestSerializerCreate, GuestSerializerDetail, UserSerializer, BasicWeddingSerializer, BasicGuestSerializerCreate
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20

class UniqueWeddingGuestCount(RetrieveModelMixin,GenericViewSet):
    serializer_class = CountSerialize
    #permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return UniqueWedding.objects.all()
    
class GuestList(generics.ListAPIView): # GET guest list for wedding - Dashboard
    queryset = UniqueGuest.objects.all()
    serializer_class = GuestSerializerCreate
    #permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return super().get_queryset().filter(
            wedding_owner=self.kwargs['wedding_slug']
        )

class BasicGuestList(generics.ListAPIView): # GET guest list for wedding - Dashboard
    queryset = BasicGuest.objects.all()
    serializer_class = BasicGuestSerializerCreate
    #permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

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
            return UniqueGuest.objects.all()

class BasicGuestForUserViewSet(CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,GenericViewSet):
        serializer_class = BasicGuestSerializerCreate
        def get_queryset(self):
            return BasicGuest.objects.all()

class GuestViewSet(RetrieveModelMixin,UpdateModelMixin,GenericViewSet):
    serializer_class = GuestSerializerDetail
    def get_queryset(self):
        return UniqueGuest.objects.all()

class UserViewSet(CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,GenericViewSet):
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.all()
    
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])        
    def me(self, request, *args, **kwargs):
        self.kwargs.update(pk=request.user.id)
        return self.retrieve(request,*args, **kwargs)