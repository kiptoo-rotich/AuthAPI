from django.http import request
from django.shortcuts import redirect, render, resolve_url
from rest_framework import serializers, status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password

from login.serializers import LoginSerializer,RegisterSerializer

from .forms import LoginForm, RegisterForm
from .models import Login, Register



def home(request):
    if request.method=="POST":
        form=LoginForm(request.POST,request.FILES)
        if form.is_valid():
            if Register.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
                content = {'Login successful!'}
                return render(request,'register.html', {'content':content})
            else:
                content={'incorrect username/password'}
                return render(request,'register.html', {'content':content})
        else:
            content={'Invalid request'}
            return render(request,'register.html', {'content':content})
    else:
        form=LoginForm()
    return render(request,'index.html', {'form':form})

def register(request):
    form=RegisterForm()
    if request.method=="POST":
        if form.is_valid():
            if Register.objects.filter(username=request.POST['username']).exists():
                content = {'Username taken!'}
                print(content)
            elif request.POST['password']!=request.POST['repeatpassword']:
                content={'Password does not match'}
                print(content)
            elif request.POST['password']==request.POST['repeatpassword']:
                user = form.save(commit=False)

                # Cleaned(normalized) data
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                repeatpassword = form.cleaned_data['repeatpassword']

                #  Use set_password here
                user.set_password(password)
                user.save()

                content={'Account created successfully!'}
                print(content)
            else:
                content={'Unknown error'}
                print(content)
        else:
            content={'Invalid request'}
            print(content)
    else:
        form=RegisterForm()
    return render(request,'register.html', {'form':form})


class HomeView(APIView):
    def get(self, request, format=None):
        all_users=Register.objects.all()
        serializers=LoginSerializer(all_users,many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = LoginSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def get(self, request, format=None):
        all_users=Register.objects.all()
        serializers=RegisterSerializer(all_users,many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = RegisterSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
