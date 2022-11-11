from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import Vehicles,Reviews
from user.serializer import VehicleSerializer,ReviewSerializer,UserSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
from rest_framework.decorators import action

class VehiclesView(APIView):
    def get(self,request,*args,**kwargs):
        qs = Vehicles.objects.all()
        serializer = VehicleSerializer(qs,many=True)
        return Response(data = serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = VehicleSerializer(data=request.data)

        if serializer.is_valid():
            Vehicles.objects.create(**serializer.validated_data)
            return Response(data = serializer.data)

        else:
            return Response(serializer.errors)

class VehicleDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        vehicle = Vehicles.objects.get(id = id)
        serializer = VehicleSerializer(vehicle,many=False)
        return Response(data = serializer.data)

    def delete(self,request,*args,**kwargs):
        id = kwargs.get("id")
        Vehicles.objects.get(id = id).delete()
        return Response(data="deleted")

    def put(self,request,*args,**kwargs):
        id = kwargs.get("id")
        serializer = VehicleSerializer(data= request.data)

        if serializer.is_valid():
            Vehicles.objects.filter(id=id).update(**serializer.validated_data)
            return Response(data = serializer.data)
        else:
            return Response(data= serializer.errors)


class ReviewsView(APIView):

    def get(self,request,*args,**kwargs):
        reviews = Reviews.objects.all()
        serializer = ReviewSerializer(reviews,many=True)
        return Response(data = serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = ReviewSerializer(data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(data= serializer.errors)

class ReviewDetailsView(APIView):

    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        qs = Reviews.objects.get(id = id)
        serializer = ReviewSerializer(qs,many = False)
        return Response(data = serializer.data)

    def put(self,request,*args,**kwargs):
        id = kwargs.get("id")
        object = Reviews.objects.get(id = id)
        serializer = ReviewSerializer(instance=object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self,request,*args,**kwargs):
        id = kwargs.get("id")
        Reviews.objects.get(id = id).delete()
        return Response(data="deleted")

class VehicleViewSetView(ViewSet):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs = Vehicles.objects.all()
        serializer = VehicleSerializer(qs,many=True)
        return Response(data=serializer.data)

    def create(self,request,*args,**kwargs):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def retrieve(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        vehicle = Vehicles.objects.get(id = id)
        serializer = VehicleSerializer(vehicle,many = False)
        return Response(data=serializer.data)

    def update(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        object = Vehicles.objects.get(id=id)
        serializer = VehicleSerializer(instance=object,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        Vehicles.objects.get(id=id).delete()
        return Response(data="deleted")

class VehicleModelViewsetView(ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicles.objects.all()

    @action(methods=["POST"],detail=True)
    def add_review(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        vehicle = Vehicles.objects.get(id=id)
        user = request.user
        Reviews.objects.create(vehicle=vehicle,customer=user,comment=request.data.get("comment"),rating=request.data.get("rating"))
        return Response(data="created")

class ReviewModelViewsetView(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Reviews.objects.all()
    def list(self,request,*args,**kwargs):
        all_reviews = Reviews.objects.all()
        if 'user' in request.query_params:
            all_reviews=all_reviews.filter(user=request.query_params.get("user"))
        serializer = ReviewSerializer(all_reviews,many=True)
        return Response(data=serializer.data)

class UsersView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()







