from rest_framework import serializers
from user.models import Vehicles,Reviews,Wishlist
from django.contrib.auth.models import User

class VehicleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    company_name = serializers.CharField()
    model = serializers.CharField()
    registration_year = serializers.IntegerField()
    variant = serializers.CharField()
    owner = serializers.CharField()
    fuel = serializers.CharField()
    kilometres = serializers.IntegerField()
    gear_type = serializers.CharField()
    price = serializers.IntegerField()
    colour = serializers.CharField()
    place = serializers.CharField()

    def create(self,validated_data):
        return Vehicles.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.company_name = validated_data.get("company_name")
        instance.registration_year = validated_data.get("registration_year")
        instance.model = validated_data.get("model")
        instance.variant = validated_data.get("variantr")
        instance.owner = validated_data.get("owner")
        instance.kilometres = validated_data.get("kilometres")
        instance.gear_type = validated_data.get("gear_type")
        instance.price = validated_data.get("price")
        instance.colour = validated_data.get("colour")
        instance.place = validated_data.get("place")
        instance.save()
        return instance

# object level validation:

    def validate(self, data):

        price = data.get("price")
        if price not in range(100000, 10000000):
            raise serializers.ValidationError("Invalid Price")

        return data


# field level validation:

    def validate_price(self, value):
        if value not in range(100000, 10000000):
            raise serializers.ValidationError("Invalid Price")
        return value



class ReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.CharField(read_only=True)
    class Meta:
        model = Reviews
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name","last_name","username","email","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class WishlistSerializer(serializers.ModelSerializer):
    vehicle = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    class Meta:
        model = Wishlist
        fields = ["vehicle","user","status"]