from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework import status
from rest_framework.generics import ListAPIView,DestroyAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework.generics import GenericAPIView


class getlist2(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class getlistitem(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class updateview(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class deleteview(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class getlist(APIView):
    def get(self,request):
        todolist = Todo.objects.all()
        serializer = TodoSerializer(todolist,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TodoSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


def index(request):

    context = {
        'todos' : Todo.objects.all()
    }

    return render(request,'index.html',context)

def details(request,pk):

    context = {
        'todo' : Todo.objects.get(id = pk)
    }
    return render(request,'details.html',context)

def add(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title,text=text)
        todo.save()

        return redirect('/todos')
    else:
        return render(request,'add.html')