from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from django.http import HttpResponse
from django.http import HttpRequest
def get_html(request):
    return render(request,'get.html')

def get_result(request):
    context = {}
    # 通过request.GET['name']形式获取get表单内容
    # result为重定向到的result.html所使用的变量
    context['result'] = f"你搜索的内容为：{request.GET['q']}"
    return render(request, 'result.html', context)

def post_html(request):
    # 不能和get一样使用render_to_response必须使用render进行重定向，不然服务端不会设置csrf_token
    # return render_to_response('post.html')
    return render(request, 'post.html')
@csrf_exempt
def post(request):
    context = {}
    # 通过request.GET['name']形式获取post表单内容
    # result为重定向到的result.html所使用的变量
    context['result'] = f"你搜索的内容为：{request.POST['q']}"
    return render(request, 'result.html', context)
@csrf_exempt
def save_book(request):
    print(request.POST)
    print(request.body)
    # status ={'status': 'err'}
    # try:
    #     #保存导数据库
    #     pass
    #     status = {'status':'success'}
    # except BaseException as e:
    #     print(f'录入书籍失败!:{e}')
    # finally:
    #     status = {'status': 'err'}
    request_data = json.loads(request.body)
    if request_data:
        status = {'status': 'success'}
        json_data = json.dumps( status)  # 将查询结果进行json序列化
    else:
        status = {'status': 'error'}
        json_data = json.dumps(status)  # 将查询结果进行json序列化
    return HttpResponse(json_data, content_type="application/json")
def find_book(request):
    request_data = request.GET['name']

    if request_data and request_data !='null':
        status = {'status': 'success'}
        json_data = json.dumps(status)  # 将查询结果进行json序列化
    else:
        status = {'status': 'error'}
        json_data = json.dumps(status)  # 将查询结果进行json序列化
    return HttpResponse(json_data, content_type="application/json")