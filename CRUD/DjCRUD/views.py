from ast import Delete
from django.shortcuts import render
# from django.contrib.auth.models import User
from DjCRUD.models import Users
from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse 
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib import messages
from DjCRUD.serializers import UserlistSerializers


class list_users(APIView):

    def get(self,request):
        try:
            print('####')
            id=request.GET.get('id')
            if id is not None:
                print("in if")
                user_list=Users.objects.filter(id=id)
                print(user_list)
                serialized_data=UserlistSerializers(user_list,many=True)
                return Response({'status':200,'user_list':serialized_data.data})
                

            else:
            
                user_list=Users.objects.filter()
                print("in else")
                print(user_list)
                # serialized_data=UserlistSerializers(user_list,many=True)
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
          
            if Users.objects.filter(username=req_data['username']).exists():
                
                print("already exist")
                return Response({'status':400,'message':'username already exist'})
                
            elif Users.objects.filter(email=req_data['email']).exists():
                
                return Response({'status':400,'message':'email already exist'})
            else:
                new_user = Users(username=req_data['username'],first_name=req_data['first_name'],last_name=req_data['last_name'], email=req_data['email'])
                new_user.set_password(req_data['password'])
                new_user.save()
                print('data is saved')

                

                new_userid = new_user.id

                userinfo=Users.objects.filter(id=new_userid).values('username','id','first_name','last_name','email')
                print('4444',userinfo)

                serialized_data= UserlistSerializers(new_user)

            return Response({'status':200,'message':'user created sucessfully','userinfo':serialized_data.data})
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
            id=request.GET.get('id')
            req_data=request.POST
            upd_user=Users.objects.filter(id=id).update(username=req_data['username'],first_name=req_data['first_name'],last_name=req_data['last_name'])
            return Response({'status':200,'message':'users updated'})   
        except Exception as e:
            return Response({'status':500,'message':str(e)})    


