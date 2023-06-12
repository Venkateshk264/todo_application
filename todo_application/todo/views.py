from django.shortcuts import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
import jwt
from django.conf import settings
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer



def History(request):
    if request.method=="GET":
        result=Task.objects.all()
        serializers=TaskSerializer(result)
        return Response(serializers.data)

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
    permission_classes = [IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        # try:
        #     res ={"WOW":"wow - 1"}
        #     Type = self.request.GET.get('type')
        #     start_date = self.request.GET.get("start_date")
        #     end_date = self.request.GET.get("end_date")
        #     if Type == "table":
        #         res = table(request,start_date,end_date)
        #     elif Type == "bar":
        #         res = bar(request,start_date,end_date)
        #     elif Type == "pie":
        #         res = pie(request,start_date,end_date)
        #     elif Type == "emi":
        #         res = emi(request)
        #     return JsonResponse(res)
            
        # except Exception as e:
        #     return Response({'error': str(e)})
        pass