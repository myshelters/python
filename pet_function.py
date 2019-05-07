#查看缺少实参的错误提示
#罗旭阳，2019/01/30
def pet(pet_name, animal_type = "dog"):
	print("My pet name is " + pet_name.title() + "." )
	print("And it is a " + animal_type + ".")

#位置形参，加默认值实参
pet("alice")

#缺少一个参数
#pet()

#关键字参数对
pet(animal_type = "cat", pet_name = "jack")
