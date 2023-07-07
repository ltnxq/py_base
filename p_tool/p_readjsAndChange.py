'''
1、读写system.config.js文件 替换对应的 ip + port 
2、重新写回文件
3、必须system.config.js 在当前的工作目录
'''
def read_js_file(file_path):
  try:  
    with open(file_path,mode='r',encoding='utf-8') as file:
        js_code = file.read()
  except Exception as e:
     print("read_js_file error-{}",e)
  return js_code

def write_js_file(file_path,content):
   try:
     with open(file_path,mode='w',encoding='utf-8') as file:
         file.write(content)
   except Exception as e:
      print("write_js_file error-{}",e)


#key的形式 例如-ip:
def read_value_by_key(key):
    #找出  ''的index 一前一后
    ip_index = js_code.find(key)
    pointstr_index = js_code.find("'",ip_index)
    nextpointstr_index = js_code.find("'",pointstr_index+1)

    #进行截取
    value = js_code[pointstr_index+1:nextpointstr_index]
    print(key + "---"+"{}".format(value))
    return value



import sys

if __name__ == "__main__":
    args = sys.argv
    if(len(args) < 3):
      print("arg error at least ip and port")
      exit 

    new_ip =  args[1]
    new_port = args[2]
    if(new_ip and new_port):
       pass
    else:
       print("ip or  port is null")
       exit

    new_ipAndPort = new_ip + ":" + new_port
    print("new_ip_port-{}".format(new_ipAndPort))

    #获取对应的文件目录
    js_file_path = "system.config.js"
    js_code = read_js_file(js_file_path)
    print("js code-{}".format(js_code))

    #读取旧的ip地址和port，ip:port,用新的取代旧的
    old_ip_addr = read_value_by_key("ip:")
    old_port = read_value_by_key("ipPort:")

    old_ip_port = old_ip_addr + ":" + old_port
    print(old_ip_port)

    #替换旧的ip:port  必须进行第一个替换
    new_js_code1 = js_code.replace(old_ip_port,new_ipAndPort)
    #替换旧的ip
    new_js_code2 = new_js_code1.replace(old_ip_addr,new_ip)
    #替换旧的port
    new_js_code3 = new_js_code2.replace(old_port,new_port)



    print("newjscode--{}".format(new_js_code3))

    #取代完整进行文件的写
    write_js_file(js_file_path,new_js_code3)

