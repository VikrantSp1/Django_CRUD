from ast import Delete
from urllib import response
from django.shortcuts import render
# from django.contrib.auth.models import User
from DjCRUD.models import Address, Users
from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse 
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib import messages
from rest_framework import status
from DjCRUD.serializers import UserlistSerializers,NewUserSerializers,AddressSerializers,UserSerializer
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
import io
from rest_framework.authtoken.models import Token

class RegisterUser(APIView):
    
    def post(self,request):
        try:
            serializer=UserSerializer(data=request.POST)
            print('$$$$$$',request.POST)
            print('$$$$$$',serializer)

            if serializer.is_valid():

                serializer.save()    

                user = Users.objects.get(username=serializer.data['username'])
                token_obj = Token.objects.get_or_create(user=user)
                print("in if")
                return Response({'status':200,'payload':serializer.data,'message':'successful','token':str(token_obj)})
               

            # serializer.save()    

            # user = Users.objects.get(username=serializer.data['username'])
            # token_obj = Token.objects.get_or_create(user=user)
            else:   
                return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})

        except Exception as e:
            return Response({'status':500,'message':str(e)})    

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class list_users(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        try:
            print('####')
            id=request.GET.get('id')
            if id is not None:
                print("in if")
                # user_list=Users.objects.filter(id=id)
                # print(user_list)
                user_list=Users.objects.get(id=id)
                print(user_list)
                serialized_data=UserlistSerializers(user_list)
                return Response({'status':200,'user_list':serialized_data.data})
                

            else:
            
                user_list=Users.objects.filter()
                print("in else")
                print(user_list)
                serialized_data=UserlistSerializers(user_list,many=True)
                return Response({'status':200,'user_list':serialized_data.data})
            
        except Exception as e:
            return Response({'status':500,'message':str(e)})    

            
    def post(self,request):
        try:
            req_data=request.POST
            print('#############',request.data)
            #username=req_data['username']
            # print('%%%%%%%%%%',username)
            # # id=request.POST.get('id')
            # firstname=req_data['first_name']
            # print(firstname)
            # lastname=request.POST.get('last_name')
            # email=request.POST.get('email')
            password = req_data["password"]
            Confirm_password = req_data["confirm_password"]
            if password==Confirm_password:
                if Users.objects.filter(username=req_data['username']).exists():
                    
                    print("already exist")
                    return Response({'status':400,'message':'username already exist'})
                    
                elif Users.objects.filter(email=req_data['email']).exists():
                    
                    return Response({'status':400,'message':'email already exist'})
                else:
                    new_user = Users(username=req_data['username'],first_name=req_data['first_name'],last_name=req_data['last_name'], email=req_data['email'],password=req_data['password'])
                    new_user.set_password(req_data['password'])
                    new_user.save()
                    print('data is saved')

                

                    new_userid = new_user.id

                    # just see to the data that is created above
                    userinfo=Users.objects.filter(id=new_userid).values('username','id','first_name','last_name','email')
                    print('4444',userinfo)

                    serialized_data= UserlistSerializers(new_user)

                    return Response({'status':200,'message':'user created sucessfully','userinfo':serialized_data.data})
            else:
                return Response({'status':500,'message':'password not matching'})  
        except Exception as e:
            return Response({'status':500,'message':str(e)})    
            

    def delete(self,request):
        try:
            id=request.GET.get('id')
            del_user=Users.objects.filter(id=id).delete()
            return Response({'status':200,'message':'users deleted'})   
        except Exception as e:
            return Response({'status':500,'message':str(e)})   

    def put(self,request):
        try:
            print("00000")
            id=request.GET.get('id')

            req_data=request.POST
            print("111111")
          
            if Users.objects.exclude(id=id).filter(username=req_data['username']):
                print("222222")
                return Response({'status':500,'message':'usernamename already exist'})
            print("7882222222")    
            if Users.objects.filter(email=req_data['email']).exclude(id=id):
                print("33333")
                return Response({'status':500,'message':'email already exist'})   
            print("2222222222")
            if req_data['username'] == "":
                print("44444")
                return Response({'status':500,'message':'usernamename is required'})    
            if req_data['first_name'] == "":
                print("55555")
                return Response({'status':500,'message':'first_name is required'})    
            if req_data['last_name'] == "":
                print("66666")
                return response({'status':500,'message':'last_name is required'})    
            else:
                 user=Users.objects.filter(id=id).update(username=req_data['username'],first_name=req_data['first_name'],last_name=req_data['last_name'])
            return Response({'status':200,'message':'users updated'})   
        except Exception as e:
            return Response({'status':500,'message':str(e)})



class newUser(APIView):

    def post(self,request):
        try:
            req_data=request.POST 
        # print(req_data)

            if Users.objects.filter(username=req_data['username']):
                return Response({'status':400,'message':'user already exist'})
                
            serializer = NewUserSerializers(data=req_data)
            if serializer.is_valid():

                USER=serializer.save()
                USER.set_password(req_data['password'])
                USER.save()
            # stream = io.BytesIO(new_user)
            # data = JSONParser().parse(stream)
            # if serializer.is_valid():
            # print(serializer.validated_data)
                print('4444444',serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else: 
                return Response({'errors':serializer.errors ,'status':status.HTTP_400_BAD_REQUEST})
            # id=new_user.id
            # user_data=Users.objects.filter(id=id).values('username','first_name','last_name')
            # print(user_data)


        # #user table se username firstname lastname dedo
        # return Response({'status':200,'message':'api working','user':user_data})
        except Exception as e:
            return Response({'status':500,'message':str(e)}) 

    def put(self,request):
        try:
            id=request.GET.get('id')
            req_data=request.POST
            print("11111")
            user_obj=Users.objects.get(id=id)
            serializer = NewUserSerializers(user_obj,data=req_data)
            print('####',serializer)
            if serializer.is_valid():
            # user=Users.objects.filter(id=id).update(username=req_data['username'],first_name=req_data['first_name'],last_name=req_data['last_name'])
                serializer.save()
                print('$$$$$$$')
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else: 
                return Response({'errors':serializer.errors ,'status':status.HTTP_400_BAD_REQUEST})
        except Exception as e:
            return Response({'status':500,'message':str(e)}) 

class address(APIView):
    
    def post(self,request):

        print('%$%$%$%$%$%$%$%')
        try:
            req_data=request.POST 
            print('####')
                 
            userserializer = NewUserSerializers(data=req_data)
            if userserializer.is_valid():
                addressserializer = AddressSerializers(data=req_data)
                if addressserializer.is_valid():
                    print('111111')


                    user=Users.objects.create(username=req_data['username'],first_name=req_data['first_name'],last_name=req_data['last_name'], email=req_data['email'])
                    user.set_password(req_data['password'])
                    print('222222')
                    user.save()
                    print('333333')
             
                    # if req_data.get('address2') and req_data.get('city') and req_data.get('postel_code')


                    Address.objects.create(user=user,address1=req_data['address1'],address2=req_data.get('address2'),phonenumber=req_data['phonenumber'], city=req_data.get('city'),postel_code=req_data.get('postel_code'))
                    


                    print('4444444')
                    return Response({'satus':200,'message':'data inserted'})
                else:
                    return Response({'errors':addressserializer.errors ,'status':status.HTTP_400_BAD_REQUEST})    
            else:
                return Response({'errors':userserializer.errors ,'status':status.HTTP_400_BAD_REQUEST})   
        except Exception as e:
            user.delete()
            return Response({'status':500,'message':str(e)})    

    def put(self,request):
        try:
            id=request.GET.get('id')
            req_data=request.POST
            print('last',req_data)


            user_obj=Users.objects.get(id=id)
         
            # address=Address.objects.get(user_id=id)

            userserializer=UserlistSerializers(user_obj,data=req_data)

            if userserializer.is_valid():
                user_obj.set_password(req_data['password'])
               
                add_obj=Address.objects.get(user_id=id)
                addressserializer = AddressSerializers(add_obj,data=req_data)
                if addressserializer.is_valid(): 

                    userserializer.save()
                    addressserializer.save()



                    # user=Users.objects.filter(id=id).update(username=req_data['username'],first_name=req_data['first_name'],last_name=req_data['last_name'])

                    # address=Address.objects.filter(user_id=id).update(address1=req_data['address1'],
                    # address2=req_data['address2'])
                   


                    return Response({'satus':200,'message':'data updated'})
                else:
                    return Response({'errors':addressserializer.errors ,'status':status.HTTP_400_BAD_REQUEST})

            else:
                return Response({'errors':userserializer.errors ,'status':status.HTTP_400_BAD_REQUEST})
                

        
        except Exception as e:
            return Response({'status':500,'message':str(e)})    

    
        






