from dataclasses import field
from rest_framework import serializers
from DjCRUD.models import Users

class UserlistSerializers(serializers.ModelSerializer):
   class Meta:
        model=Users
        fields=('username','first_name','last_name')


    # def create(self, validated_data):
    #     return Comment(**validated_data)