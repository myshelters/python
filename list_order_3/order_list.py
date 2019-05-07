#使用sorted ，sort ,reverse对列表进行排序
#罗旭阳 ，2019/1/28
places = [ 'ggsde', 'fdsdf',  'sdfsf', 'asdf','jhhd',]

#输出原始顺序列表
print(places)
print("\n")

#sorted 打印该表,并检查原始序列
print(sorted(places))
print(places)
print("\n")

#sorted 相反顺序打印该表
print(sorted(places, reverse = True))
print(places)
print("\n")

#reverse 改变顺序
places.reverse()
print(places)

#引发一个列表出界错误
num = len(places)
print(num)
print(places[5])