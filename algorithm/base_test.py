from functools import cmp_to_key



'''
1、求最后一个单词的长度
   str.rfind() / str.find()的使用
   len() 方法求长度
'''

def get_last_word_length():
    str = input("请输入一个字符串:")
    print(str)
    str1 = " "
    strlen = len(str)
    index = str.rfind(str1,0,strlen)
    # 如果index == -1 那么就是没有空格 那么这个长度就是等于自身
    if -1 == index:
        print(strlen)
    else:
      print(strlen-index-1)

'''
2、统计单词出现的次数
   AaBb => A 的次数是 2
   str.upper()、string.count()方法
   upper()、lower() 转为大写、小写
'''
def count_char_numbers():
    str = input("请输入一个字符串:")
    ch = input("请输入一个需要统计的:")
    str1 = str.upper()
    ch1 = ch.upper()
    count = str1.count(ch1)
    print(count)

'''
3、按照长度去分割字符串 不足8的 用0去补齐  再进行输出
   // => 整除法
   /  => 浮点数除法
'''

def split_str():
   str = input("请输入一个字符串:")
   strlen = len(str)
   list1 = []
   m = strlen // 8
   n = strlen % 8
   begin_index = 0

   if m > 0 :
       for i in range(0,m):
           tempStr = str[begin_index:begin_index+8]
           begin_index = (i+1)*8
           list1.append(tempStr)
    
   if n > 0:
       tempStr = str[begin_index:strlen]
       tempStr += "0"*(8-n)
       list1.append(tempStr)

   #打印
   for item in list1:
       print(item)


'''
4、16进制转换为10进制
   按照进制进行转换
   int(str1,base = 16)
'''
def hex_2_dec():
    str = input("请输入要转换字符串:")
    index = str.find('x')
    str1 = str[index+1:len(str)]
    in1 = int(str1,base=16)
    print(in1)

'''
5、合并key value
    * 0 4
    * 0 1
    * 1 2
    * 2 4  ===》 05 12 24
    dict类型的遍历?
'''    
def merge_key_value():
    n = input("请输入几组key value:")
    dic1 = {}
    for i in range(int(n)):
        key,value = (input("请输入key value 空格分割:").split())
        v1 = dic1.get(key,0)
        temp_v = v1 + int(value)
        dic1[key] = temp_v
    for key,val in dic1.items():
        print(key,end= ":")
        print(val)

'''
6、统计不同字符出现的次数
'''
def static_different_char():
    str = input("请输入一行字符串:")
    set1 = set()
    for ch in str:
        set1.add(ch)
    print(len(set1))

'''
7、数字颠倒输出
   1523  =》 3251
'''
def reverse_numbers():
    m = input("请输入整数:")
    print(m[::-1])

'''
8、获取简单密码
    1--1, abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0 小写字母
    大写字母变小写  再向后移动一位
    数字不变进行原样输出
    ord=> 将字母转换为ASCII码
'''
def get_simple_password():
    dic1 = dict(c=2,f=3,i=4,l=5,o=6,s=7,v=8,z=9)
    str1 = "cfilosvz"
    oldStr = input("请输入原始密码: ")
    newPassword = ""
    index = ''
    for ch in oldStr:
        if(ch.isdigit()):
            newPassword += ch
        elif(ch.islower()):
            for c in str1:
                if c >= ch :
                    index = c
                    break
            newPassword += str(dic1[index])
        elif(ch.isupper()):
            if("Z" == ch):
                newPassword += "a"
            else:
                m = ord(ch.lower()) + 1
                newPassword += chr(m)
        else:
            print("输入字符串不符合规则！")
    print(newPassword)


'''
9、删除出现次数最少的字符串
    aabbbcccdddee ==>bbbcccddd
'''
def dele_less_char():
    line = input("请输入一行字符串:")
    set1 = set(line)
    no_dict = {}
    #统计每个单词出现的次数
    for ch in set1:
        no_dict[ch]= line.count(ch)
    
    #找出最小数量的单词集合
    min_num_set = set()
    min_num = 65535
    
    #items 返回的是可遍历的 (key,value)
    for (key,val) in no_dict.items():
        if min_num > val:
            min_num_set.clear()
            min_num_set.add(key)
            min_num = val
        elif min_num == val:
            min_num_set.add(key)
    
    #遍历输出
    for ch in line:
        if ch not in min_num_set:
            print(ch,end="")


'''
    删除出现次数最少的字符串v2
    aabbbcccdddee ==>bbbcccddd
'''
from collections import Counter
def dele_less_char_v2():
    line = input("请输入一行字符串:")
    #Counter 底层是继承了字典  key value-字符出现的次数
    line_counter = Counter(line)
    min_counts = min(line_counter.values())
    #再使用列表推导
    res = [s for s in line if line_counter[s] > min_counts]
    #使用join方法 构造一个string
    res_str = ''.join(res)    
    print(res_str)
'''
10、逆序输出
    I am a student  ==> student a am I
    $bo**y gi!r#l   ==> l r gi y bo

    倒序输出的办法 slice分片对象的应用
'''
def reverse_output():
    line = input("请输入一行字符串:")
    strList = []
    tempStr = ""
    for ch in line:
        #不是字母那么就进行分割
        if not ch.isalpha():
            if tempStr :
                strList.append(tempStr)
                tempStr = ""
        else:
            tempStr += ch   
    if tempStr :
        strList.append(tempStr)
    
    #进行倒序输出  步长是-1
    for str in strList[::-1]:
        print(str,end = " ")

'''
11、字符串排序
    使用sorted系统函数会返回一个新的string对象
'''
def string_sort():
    str = input("请输入一行字符串:")
    str1 = sorted(str)
    for ch  in str1:
        print(ch,end="")

'''
12、创建一个蛇形矩阵
    1 3 6 10 15  => 2 3 4 5  
    2 5 9 14     => 3 4 5
	4 8 13       => 4 5
	7 12         => 5
	11

    for 循环 
    for j in range(0,m)  j从0开始循环
    for j in range(i,m)  j从i开始循环

    python 是没有自增运算符的
           并且注意赋值运算符的返回值
'''   
def create_snake_matrix():
    m = int(input("请输入矩阵的行数:"))
    first_level_value = 1

    #存储最终的结果
    resultlist = []
    for i in  range(0,m):
        if i > 0:
            first_level_value += i
        
        level_inc_val = i + 2
        prev_value = first_level_value
        templist = []

        for j in range(i,m):
            if i == j :
                templist.append(first_level_value)
            else:
                prev_value = prev_value + level_inc_val
                templist.append(prev_value)
                level_inc_val = level_inc_val + 1
        resultlist.append(templist)
    
    for li in resultlist:
        for l in li:
            print(l,end= " ")
        print("")

'''
13、求完全数
'''
def get_perfect_number():
    n = int(input("请输入一个整数:"))
    re_count = 0
    for m in range(1,n+1):
        #求m的约数
        j = 1
        tempList = []
        while j <= m/2 :
            if(m % j == 0):
                tempList.append(j)
            j+=1
        #求sum 是否等于m
        if sum(tempList) == m:
            re_count +=1
    print(re_count)

'''
14、求密码强度
    ①-密码长度  ②-字母 大小写  ③-数字的个数  ④-特殊字符的个数 ⑤-奖励的分数
'''
def get_password_level():
    password = input("请输入一行密码:")
    pass_len = len(password)
    lower = False
    upper = False
    digit_no = 0
    special_char_no = 0
    final_scores = 0
    for ch in password:
        if not lower and ch.islower():
            lower = True
            continue
        if not upper and ch.isupper():
            upper = True
            continue
        if ch.isdigit():
            digit_no += 1
            continue
        acii_val = ord(ch)
        if (acii_val>=0x21 and acii_val <= 0x2f) or\
              (acii_val>=0x3A and acii_val <= 0x40) or\
                  (acii_val >= 0x5B and acii_val <= 0x60) or \
                    (acii_val >= 0x7B and acii_val <= 0x7E):
           special_char_no += 1
        
    #第一个奖励
    if lower or upper:
        if digit_no > 0:
            final_scores = 2
            if special_char_no > 0:
                final_scores = 3
    if lower and upper and digit_no > 0 and special_char_no>0:
        final_scores = 5

    #密码长度    
    if pass_len <=4 :
        final_scores += 5
    elif pass_len >= 5 and pass_len <= 7:
        final_scores += 10
    else:
        final_scores += 25
    
    #大小写统计
    if not lower and not upper:
        pass
    elif not lower and upper:
        final_scores += 10
    elif lower and not upper:
        final_scores += 10
    elif lower and upper:
        final_scores += 20
    
    #数字统计
    if digit_no == 0:
        pass
    if digit_no == 1:
        final_scores += 10
    else:
        final_scores += 20
    
    #特殊字符统计
    if special_char_no == 0:
        pass
    elif special_char_no == 1:
        final_scores += 10
    else:
        final_scores += 25
    

    if final_scores >= 90 :
        print("VERY_SECURE")
    elif final_scores >= 80:
        print("SECURE")
    elif final_scores >= 70:
        print("VERY_STRONG")
    elif final_scores >= 60:
        print("STRONG")
    elif final_scores >= 50:
        print("AVERAGE")
    elif final_scores >= 40:
            print("WEAK")
    else:
        print("VERY_WEAK")

'''
15、求一个数的位数
'''
def  get_digit_no(number):
    count = 0
    while( number > 0):
        number //= 10
        count += 1
    return count

'''
16、求一个数的自守数
'''
def get_self_serving():
    number = int(input("请输入一个整数:"))
    n = 0
    #1 到 number的循环
    for i in range(0,number+1):
       temp = get_digit_no(i)
       #取temp的十次幂
       temp_power =  10  ** temp
       if i*i % temp_power == i :
           n += 1
    print(n)

'''
去重并且保证插入顺序
'''
def unique_by_origin_sort(iterParam):
    set1 = set()
    for item in iterParam:
        if item not in set1:
          yield item
          set1.add(item)
    
'''
17、按照出现的次数降序排列
    aaddccdc => cda
    aacddd   => dac
    abc      => abc
    aabbcc   => abc
'''
def sort_by_number():
    str = input("请输入一行字符串:")
    str1 = sorted(str,key=lambda s : (-str.count(s),s))
    unique_str = list(unique_by_origin_sort(str1))
    for s in unique_str:
        print(s,end="")

'''
18、两数之和
'''
def sum_of_2_number():
    in_1 = input("请输入一行整数按照空格分割: ").split()
    target = int(input("请输入目标值:"))
    resList = []
    for i in range(len(in_1)-1):
        for j in range(i+1,len(in_1)):
            if int(in_1[i]) + int(in_1[j]) == target :
               resList.append((i,j))
    for item in resList:
        print('{}:{}'.format(item[0],item[1]))

'''
19、判断是否是回文数 左右对称
    121 是  123不是 233 不是
'''
def is_symmetry():
    line = input("请输入待判断的数字: ")
    rser_line_iter = reversed(line)
    for ch in line:
        if ch != next(rser_line_iter):
            print("is not symmetry ")
            return
    print("is symmetry")


'''
20、最长公共前缀
    strs = ["flower","flow","flight"]  最长公共前缀是fl
'''
def get_prefix():
    strs = ["dog","dacecar","dar"]
    sorted_str = sorted(strs,key = lambda str : len(str))
    #长度最短的字符串
    min_str = sorted_str[0]        
    
    i = 0
    is_same = True
    for i in range(len(min_str)):

        for j in range(1,len(strs)):
            if(min_str[i] == sorted_str[j][i]):
                pass
            else:
                is_same = False
                break
        if not is_same:
            break
    print(min_str[0:i])







  

        








        

    


       
    
       
       



# main函数调用入口
if __name__ == "__main__":
    #get_last_word_length()
    #count_char_numbers()
    #split_str()
    #hex_2_dec()
    #merge_key_value()
    #static_different_char()
    #reverse_numbers()
    #get_simple_password()
    #dele_less_char()
    #dele_less_char_v2()
    #reverse_output()
    #string_sort()
    #create_snake_matrix()
    #get_perfect_number()
    #get_password_level()
    #print(get_digit_no(3))
    #get_self_serving()
    #sort_by_number()
    #sum_of_2_number()
    #is_symmetry()
    get_prefix()
    pass