from django.shortcuts import render
from django.http import response
from TestModel.models import Test
# Create your views here.
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    test1.name = '花花公子'
    test1.save()
    return render(request,'index.html',{'name':'添加成功'})

def login(request):
    return render(request,'login/login.html')

def zc(request):
    return render(request,'login/zc.html')

def index(request):
    return render(request,'index.html')