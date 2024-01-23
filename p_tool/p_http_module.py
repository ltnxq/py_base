import requests
import json

host = "http://127.0.0.1:18069/"

'''
1、基本的get请求
   respose status_code的数据类型是int
   response.text  是str类型
   response.json() 返回的响应体是dict格式  如果要进行遍历dict打印
   response.headers 返回响应头
   response.cookies 返回响应的cookie
'''
def get():
   print("1"+"-"*60)
   response = requests.get(host + "video/token")
   print(type(response.status_code))
   print(response.status_code)
   print(type(response.text))
   print(response.text)
   print(type(response.json()))
   print(response.json())
   # 遍历返回的body
   # for key,value in response.json().items():
   #     print(key+":"+str(value))
   print(type(response.headers))
   print(response.headers)

'''
2、基本get请求,带param参数
'''
def get_with_param():
   print("2"+"-"*60)
   param_data = {"user":"admin"}
   response = requests.get(host + "login",params=param_data)
   print(type(response.cookies))
   print(response.cookies)

   for key,value in response.cookies.items():
      print(key + ":" +value)


'''
3、基本的post请求
   如果接口需要body参数 那么就必须设置对应的header 设置为application/json支持的格式
   并且对应的参数应该是json = data
'''
def post():
   print("3"+"-"*60)
   headers={'content-type': 'application/json'}
   data = {'name': 'germey', 'age': '22'}
   response = requests.post(host+"video/onlineStatus",json=data,headers=headers)
   print(response.json())


if __name__ == "__main__":
   pass