from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('wedding/<wedding_slug>/guests/', views.GuestList.as_view(), name='guests-list'), #Dashboard - lista gostiju    
    path('basic-wedding/<wedding_slug>/guests/', views.BasicGuestList.as_view(), name='guests-list'), #Dashboard - lista gostiju
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

router = DefaultRouter()
router.register(r'user', views.UserViewSet, basename='customer') #Dashboard vjenčanje
router.register(r'user/<username>', views.UserViewSet, basename='customer_details') #Dashboard vjenčanje
router.register(r'wedding', views.WeddingViewSet, basename='wedding') #Kreiranje unique vjenčanja 
router.register(r'wedding/<slug:wedding_slug>', views.WeddingViewSet, basename='wedding_detail')# Edit/Get vjenčanja
router.register(r'guests', views.GuestForUserViewSet, basename='guests')#Post gositju
router.register(r'guests/<slug:guest_slug>', views.GuestForUserViewSet, basename='guests_list')# Edit/Get gostiju za uniqe vjencanje
router.register(r'pozivnica/<slug:guest_slug>', views.GuestViewSet, basename='guest_detail')#Osobna pozivnica za uniqe wedding
router.register(r'gosti', views.BasicGuestForUserViewSet, basename='basic_guests')#Post gostiju na basic vjenčanje
router.register(r'gosti/<slug:guest_slug>', views.BasicGuestForUserViewSet, basename='basic_guests_list')# Edit/Get gostiju za basic vjenčanje
router.register(r'basic-wedding', views.BasicWeddingViewSet, basename='basic_wedding') #Kreiranje basic vjenčanja
router.register(r'basic-wedding/<slug:wedding_slug>', views.BasicWeddingViewSet, basename='basic_wedding_detail')# Edit/Get vjenčanja - Main endpoint za basic vjenčanje

urlpatterns += router.urls