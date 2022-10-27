from dataclasses import field
from rest_framework import serializers
from DjCRUD.models import Users,Address
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = Users
      fields = ['username','password']



class UserlistSerializers(serializers.ModelSerializer):
   class Meta:
        model=Users
        fields=('username','first_name','last_name')


    # def create(self, validated_data):
    #     return Comment(**validated_data)


class NewUserSerializers(serializers.ModelSerializer):
   class Meta:
        model=Users
        fields=('username','first_name','last_name','email','password')

        



class AddressSerializers(serializers.ModelSerializer):
   class Meta:
        model=Address
        fields=('address1','address2','phonenumber','city','postel_code')        