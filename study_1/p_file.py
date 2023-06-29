#open 完整的语法格式
#file-文件路径 newline-区分换行符 
#open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#相关API
#close、flush、fileno（返回整型的文件描述符）、isatty(判断是否连接到终端设备)、read([size])、readline([size])、readlines、seek、tell、truncate([size])
#write(str)、writelines(sequence) 换行需要自己加入换行符

#可以使用 with open("xxxx","w") as file  相当于 java的try-with-resource语法