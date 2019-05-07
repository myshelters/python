#删除包含特定值的所有列表元素
#罗旭阳，2019/01/30
pets = ["dog", "cat", "dog", "goldfish", "cat", ]
print(pets)

#while循环判断列表元素，并删除特定值
while "cat" in pets:
	pets.remove("cat")
	pass

#再次打印pets列表
print(pets)