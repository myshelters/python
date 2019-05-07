#对列表进行排序
#罗旭阳，2019/1/28
names = ['alice',  'jack','batman', 'stark']

#安照字母顺序排序 a-z
names.sort()
print(names)

#z-a排序
names.sort(reverse= True)
print(names)

#临时排序a-z
names = ['alice',  'jack','batman', 'stark']
print(sorted(names))
print("原始顺序：")
print(names)
print(sorted(names,reverse= True))