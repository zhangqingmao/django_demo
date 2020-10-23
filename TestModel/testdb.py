# Create your views here.
import random
import redis
from django.shortcuts import render
from django.core.cache import cache
from TestModel.SMS import SMS
from TestModel.models import Test

r = redis.Redis(host='182.92.61.254', port=6379,password=932467, decode_responses=True)

def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    test1.name = '花花公子'
    test1.save()
    return render(request, 'index.html', {'name': '添加成功'})


def login(request):
    return render(request, 'login/login.html')


def zc(request):
    return render(request, 'login/zc.html')


def index(request):
    return render(request, 'index.html')


def sendSms(request):
    para = get_random_number_str(6)
    print(para)
    res = SMS.sendSms('15290946377', para)
    r.set('15290946377', para, ex=60)
    return render(request,'index.html',{'name':'发送成功'})

def get_random_number_str(length):
    num_str = ''.join(str(random.choice(range(10))) for _ in range(length))
    return num_str