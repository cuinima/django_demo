#coding=utf-8
import requests
import json
def test_save_book():
    url = 'http://127.0.0.1:8000/save_book'
    #params = {"name":"python入门到放弃"}
    params = ''
    '''
    json.load()从文件中读取json字符串

    json.loads()将json字符串转换为字典类型
    
    json.dumps()将python中的字典类型转换为json字符串类型
    
    json.dump()将json格式字符串写到文件中

 
    '''
    json_params = json.dumps(params)
    result = requests.post(url=url,data=json_params)
    if result.status_code == 200 and json.loads(result.text)['status'] == 'success':
        print(f'test_save_book调用成功,参数:{params},状态码:{result.status_code},返回值:{result.text}')
    else:
        print(f'test_save_book调用失败,参数:{params},状态码:{result.status_code},返回值:{result.text}')
def test_find_book():

    '''
        url = 'http://127.0.0.1:8000/find_book?'
        拼接get请求地址
        params = 'name=python入门到放弃'
        print(url+params)
        result = requests.get(url=url+params)'''
    url = 'http://127.0.0.1:8000/find_book'
    params = {"name":"python入门到放弃"}
    result = requests.get(url=url,params=params )
    if result.status_code == 200 and json.loads(result.text)['status'] == 'success':
        print(f'test_find_book调用成功,参数:{params},状态码:{result.status_code},返回值:{result.text}')
    else:
        print(f'test_find_book调用失败,参数:{params},状态码:{result.status_code},返回值:{result.text}')
if __name__ == '__main__':
    #test_save_book()
    test_find_book()