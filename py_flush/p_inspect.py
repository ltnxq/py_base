import inspect
import p_promotion

#拿到p_promotion 模块的所有函数  py中模块也是属于对象的一种
promos = [func for name ,func in inspect.getmembers(p_promotion,inspect.isfunction)]

print(len(promos))
print(promos[0])
print(promos[1])
print(promos[2])