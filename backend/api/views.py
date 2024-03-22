from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status , generics
from rest_framework.response import Response
from .models import Student
from .serializers import studentserializer
# Create your views here.



class studentview(APIView):
    
    serializer_class = studentserializer
    
    def post(self , request , format = None):
        
        serializer = self.serializer_class(data=request.data)
        
        
        if serializer.is_valid():
            
            queryset = Student.objects.filter(sid = serializer.data.get("sid"))
            
            if not queryset.exists() :
                
                sid = serializer.data.get("sid")
                name = serializer.data.get("name")
                age = serializer.data.get("age")
                
                data = Student(sid =sid ,name = name , age = age )
                data.save()
                
                return Response(studentserializer(data).data , status=status.HTTP_200_OK)
                
            else:
                
                return Response({"massege":"This Value All ready Exist"} , status=status.HTTP_201_CREATED)
                
        else:
            
            return Response({"Bad Reques": "Invalid Data"} ,  status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
        
class studentData(APIView):
    
    
   
    
            
    
    
    def post(self, request, format=None):
        
            queryset = Student.objects.all()
            
            serializer = studentserializer(queryset, many=True)
            
            return Response(serializer.data , status=status.HTTP_200_OK)
    
    
    
    
    