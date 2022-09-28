"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from blogapi import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router=DefaultRouter()
router.register('api/v4/myg/mobiles',views.MobileModelViewSetView,basename='modelmobiles')
router.register('api/v3/myg/mobiles',views.MobileViewSetView,basename='mobiles')
router.register('api/v3/accounts/register',views.UserRegistrationView,basename='registration'),
router.register('api/v4/myg/cart',views.CartsView,basename="cart"),
router.register('api/v4/myg/my_cart',views.CartsView,basename="cart")

urlpatterns = [
    path('admin/', admin.site.urls),
path('api/v1/myg/mobiles/', views.MobileView.as_view()),
path('api/v1/myg/mobiles/<int:id>/', views.MobileDetailView.as_view()),
path('api/v2/myg/mobiles/',views.MobileModelsView.as_view()),
path('api/v2/myg/mobiles/<int:id>/',views.MobileModelsDetailView.as_view()),
path('api/v4/token',TokenObtainPairView.as_view()),
path('api/v4/token/refresh',TokenRefreshView.as_view()),

# path('accounts/token/',obtain_auth_token),

]+router.urls
