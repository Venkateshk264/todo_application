from django.shortcuts import HttpResponse,get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
import jwt
from django.conf import settings
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
import pandas as pd



# def History(request):
#     if request.method=="GET":
#         result=Task.objects.all()
#         data = [{"task":result.task_title,"status":task_status,"due_date":due_date}]
#         return JsonResponse(data,safe=False)

class DataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            token = request.META['HTTP_AUTHORIZATION'].split()[1]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['user_id']
            data = {"Userid":user_id}
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=401)
class Analytics(APIView):
   #permission_classes = [IsAuthenticated]
    
    def get(self,request,*args,**kwargs):

       result=Task.objects.all()
       serializers = TaskSerializer(result,many=True)
       list_of_data=serializers.data
       return Response(list_of_data,status=200)
    def post(self,request):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            
           serializer.save()
           return Response({ "data": serializer.data}, status=status.HTTP_200_OK) 
        else:
           return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        result=Task.objects.get(id=id)
        serializer=TaskSerializer(result,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data})
        else:
            return Response({"status":"errors","data":serializer.errors})
        
    def delete(self,request,id=None):
        result=get_object_or_404(Task,id=id)
        result.delete()
        return Response({"status":"success","data":"record deleted"})

     
