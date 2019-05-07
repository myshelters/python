#定义一个函数，使他的返回值为字典
#罗旭阳，2019/01/30
def build_person(first_name, last_name):
	"""返回一个字典，其中包含有关一个人的信息"""
	person = {"first_name": first_name, "last_name" : last_name}
	return person
	pass

#打印音乐家的名字字典
musician = build_person("allen", "wlack")
print(musician)

#打印名字并首字母大写
musician_names = musician.values()
print(musician_names)
print("The musician's name is : ")
for musician_name in musician_names:
	print(musician_name.title() )