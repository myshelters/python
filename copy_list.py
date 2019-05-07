#复制一个简单列表，并验证复制列表的方法
#罗旭阳，2019/01/29
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print(my_foods)
print("\n")
print(friend_foods)

#核实确实有两个列表
my_foods.append("ice cream")
friend_foods.append("egg")

print(my_foods)
print("\n")
print(friend_foods)

#如果不使用切片复制列表会怎么样？
friend_foods = my_foods

#现在验证是否有两个列表
friend_foods.append("hhh")
my_foods.append("eat")

print(my_foods)
print("\n")
print(friend_foods)

#由此可见，要使用切片的方法，复制列表