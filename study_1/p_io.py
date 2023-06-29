# abspath = "D:\\zyz\\java\\project\\study\\python_s\\study_1\\temp\\foo.txt"
relaPath = "study_1\\temp\\foo.txt"
f = open(relaPath,"r",encoding  = "utf-8")
# # f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print(f.read())
f.close()

#当前位置指的是项目的根目录

# pickle dump 持久化文件
'''
import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()


'''

#使用pickle模块反序列化

import pickle ,pprint
#二进制读取
pkl_file = open('data.pkl','rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()

#爬虫示例
from urllib import request
res = request.urlopen("http://localhost:8080/#/common/index")
fi = open("nxpower.txt",'w')
page = fi.write(str(res.read()))
fi.close()