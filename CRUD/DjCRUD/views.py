from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib import messages


class list_users(APIView):

    def get(self,request):
        try:
            print('####')
            user_list=User.objects.filter().values('username','id','first_name','last_name','email')

            print(user_list)
            return Response({'status':200,'user_list':user_list})
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
          
            if User.objects.filter(username=req_data['username']).exists():
                
                print("already exist")
                return Response({'status':200,'message':'already exist'})
                
            elif User.objects.filter(email=req_data['email']).exists():
                
                return Response({'status':200,'message':'email already exist'})
            else:
                data = User(username=req_data['username'],first_name=req_data['first_name'],last_name=req_data['last_name'], email=req_data['email'])
                data.save()
                print('data is saved')
            
            # userinfo=User.object.filter().latest('username')
            # print('4444',userinfo)

            return Response({'status':200,'message':'user created sucessfully','userinfo':userinfo})
        except Exception as e:
            return Response({'status':500,'message':str(e)})    
            

# def Profile(request):
#     x=request.POST['password']
#     y=request.POST['username']



