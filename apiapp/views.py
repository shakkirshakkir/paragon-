from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework import status
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import authentication,permissions
from rest_framework.decorators import action
# Create your views here.




class MessageList(APIView):

    def get(self,request,*args,**kwargs):
        dishes=Chat.objects.all()
        dser=ChatSerializer(dishes,many=True)
        return Response(data=dser.data)
    def post(self,request,*args,**kwargs):
        ser=ChatSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
           
            return Response({"msg":"ok"})
        else:
            return Response({"msg":ser.errors},status=status.HTTP_404_NOT_FOUND)
        # return Response({"msg":"error"})
class ChatItem(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("mid")
        item=Chat.objects.get(id=id)
        dser=ChatSerializer(item)
        return Response(data=dser.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("mid")
        item=Chat.objects.get(id=id)
        ser=ChatSerializer(data=request.data)
        
        if ser.is_valid():
            participants=ser.validated_data.get("participants")

            item.participants=participants
            item.save()
            return Response({"msg":"updated"})
        return Response({"msg":"error"})
        

class UserView(APIView):
    def post(self,request,*args,**kwargs):
        ser=UserModelSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"registered"})
        else:
            return Response({"msg":ser.errors},status=status.HTTP_404_NOT_FOUND)


class ChatView(ViewSet):
    def list(self,request,*args,**kwargs):
        item=Chat.objects.all()
        dser=ChatModelSer(item,many=True)

        return Response(data=dser.data)

    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        item=Chat.objects.get(id=id)
        dser=ChatModelSer(item)
        return Response(data=dser.data)
    

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        item=Chat.objects.get(id=id)
        ser=ChatModelSer(data=request.data,instance=item)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"updated"})
        else:
            return Response({"msg":ser.errors},status=status.HTTP_404_NOT_FOUND)

    def create(self,request,*args,**kwargs):
        ser=ChatModelSer(data=request.data,files=request.files)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"added"})
        else:
            return Response({"msg":ser.errors},status=status.HTTP_404_NOT_FOUND)

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        item=Chat.objects.get(id=id)
        item.delete()
        return Response({"msg":"deleted"})


class ChatModelViewSet(ModelViewSet):
    serializer_class=ChatModelSer
    model=Chat
    queryset=Chat.objects.all()
 
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    
   
        






