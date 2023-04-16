from rest_framework import serializers
from groomie.models import UniqueWedding, Guest, BasicWedding, BasicGuest
from customers.models import Customer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields ='__all__'

class WeddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniqueWedding
        fields = [
            'customer',
            'wedding_slug',
            'groom_fname',
            'groom_lname',
            'bride_fname',
            'bried_lname',
            'wedding_date',
            'response_date',
            'church_name',
            'church_time',
            'restaurant_name',
            'restaurant_time',
            'groom_gathering',
            'groom_gathering_time',
            'bride_gathering',
            'bride_gathering_time',
        ]

class BasicWeddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicWedding
        fields = [
            'customer',
            'wedding_slug',
            'groom_fname',
            'groom_lname',
            'bride_fname',
            'bried_lname',
            'wedding_date',
            'response_date',
            'church_name',
            'church_time',
            'restaurant_name',
            'restaurant_time',
            'groom_gathering',
            'groom_gathering_time',
            'bride_gathering',
            'bride_gathering_time',
        ]

class GuestSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = [
            'guest_slug',
            'wedding_owner',
            'guest_fname',
            'guest_lname',
            'plusone_fname',
            'plusone_lname',
            'guest_type',
            'couple',
            'plusone',
            'coming',
            'kids',
            'message',
        ]

class BasicGuestSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = BasicGuest
        fields = [
            'guest_slug',
            'wedding_owner',
            'guest_fname',
            'guest_lname',
            'plusone_fname',
            'plusone_lname',
            'with_kids',
            'plusone',
            'coming',
            'kids',
            'message',
        ]

class GuestSerializerDetail(serializers.ModelSerializer):
    groom_name = serializers.ReadOnlyField(source='wedding_owner.groom_fname')
    bride_name = serializers.ReadOnlyField(source='wedding_owner.bride_fname')
    wedding_date = serializers.ReadOnlyField(source='wedding_owner.wedding_date')
    response_date = serializers.ReadOnlyField(source='wedding_owner.response_date')
    groom_gathering = serializers.ReadOnlyField(source='wedding_owner.groom_gathering')
    groom_gathering_time = serializers.ReadOnlyField(source='wedding_owner.groom_gathering_time')
    bride_gathering = serializers.ReadOnlyField(source='wedding_owner.bride_gathering')
    bride_gathering_time = serializers.ReadOnlyField(source='wedding_owner.bride_gathering_time')
    church_name = serializers.ReadOnlyField(source='wedding_owner.church_name')
    church_time = serializers.ReadOnlyField(source='wedding_owner.church_time')
    restaurant_name = serializers.ReadOnlyField(source='wedding_owner.restaurant_name')
    restaurant_time = serializers.ReadOnlyField(source='wedding_owner.restaurant_time')


    class Meta:
        model = Guest
        fields = [
            'wedding_owner',
            'guest_fname',
            'plusone_fname',
            'guest_type',
            'couple',
            'plusone',
            'coming',
            'kids',
            'groom_name',
            'bride_name',
            'wedding_date',
            'response_date',
            'groom_gathering',
            'groom_gathering_time',
            'bride_gathering',
            'bride_gathering_time',
            'church_name',
            'church_time',
            'restaurant_name',
            'restaurant_time',
            'message',
            ]