"""OLX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from user.views import VehiclesView,VehicleDetailsView,ReviewsView,ReviewDetailsView,\
    VehicleViewSetView,VehicleModelViewsetView,ReviewModelViewsetView,UsersView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("user/v1/vehicles",VehicleViewSetView,basename="vehicles")
router.register("user/v2/vehicles",VehicleModelViewsetView,basename="cars")
router.register("user/v1/reviews",ReviewModelViewsetView,basename="reviews")
router.register("register",UsersView,basename="users")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles',VehiclesView.as_view()),
    path('vehicles/<int:id>',VehicleDetailsView.as_view()),
    path('reviews',ReviewsView.as_view()),
    path('reviews/<int:id>',ReviewDetailsView.as_view())

]+ router.urls
