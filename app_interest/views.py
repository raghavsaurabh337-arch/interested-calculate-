# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','POST','PATCH'])
def home(request):
     if request.method=='GET':
          return Response({
               'status':200,
               'rate':300,
               'masg':'django python fremworks',
               'method':'you called GET Methos',
          })
     elif request.method=='POST':
            return Response({
               'status':200,
               'rate':300,
               'masg':'django python fremworks',
               'method':'you called POST Methos',
          })
     elif request.method=='PATCH':
             return Response({
               "status":200,
               'rate':300,
               'masg':'django python fremworks',
               'method':'you called PATCH Methos',
          })
     else:
             return Response({
               "status":200,
               'rate':300,
               'masg':'django python fremworks',
               'method':'you called invaild Methos',
          })
     

