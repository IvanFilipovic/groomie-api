from rest_framework import serializers
from groomie.models import UniqueWedding, UniqueGuest, BasicWedding, BasicGuest
from customers.models import Customer
from django.db.models import Sum
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs

class UserSerializer(serializers.ModelSerializer):
    unique_wedding = serializers.CharField(source='wedding_on_customer.wedding_slug')
    basic_wedding = serializers.CharField(source='basicwedding.wedding_slug')
    class Meta:
        model = Customer
        fields =[
            'pk',
            'username',
            'email',
            'first_name',
            'last_name',
            'broj_telefona',
            'unique_wedding',
            'basic_wedding',
        ]


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
        model = UniqueGuest
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
        model = UniqueGuest
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
        
class CountSerialize(serializers.ModelSerializer):
    broj_pozivnica = serializers.SerializerMethodField()
    dolaze_solo = serializers.SerializerMethodField()
    ne_dolaze = serializers.SerializerMethodField()
    expected_guests = serializers.IntegerField()
    dolaze_plusone = serializers.SerializerMethodField()
    dolaze_djeca = serializers.SerializerMethodField()

    class Meta:
        model = UniqueWedding
        fields = ('wedding_slug', 'expected_guests', 'broj_pozivnica', 'dolaze_solo', 'ne_dolaze', 'dolaze_plusone', 'dolaze_djeca')

    def get_broj_pozivnica(self, obj):
        return UniqueGuest.objects.filter(wedding_owner=obj).count()
    
    def get_dolaze_solo(self, obj):
        return UniqueGuest.objects.filter(wedding_owner=obj, coming=True, plusone=False, with_kids=False).count()
    
    def get_ne_dolaze(self, obj):
        return UniqueGuest.objects.filter(wedding_owner=obj, not_coming=True).count()

    def get_dolaze_plusone(self, obj):
        return UniqueGuest.objects.filter(wedding_owner=obj, plusone=True).count() * 2
    
    def get_dolaze_djeca(self, obj):
        return UniqueGuest.objects.filter(wedding_owner=obj, with_kids=True).aggregate(Sum('kids'))