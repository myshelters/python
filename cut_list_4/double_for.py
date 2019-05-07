#使用多个for循环，打印食品列表
#罗旭阳，2019/01/29
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

#打印两个食品列表
for my_food in my_foods:
    print("this is my favorite food: ")
    print(my_food)
    for friend_food in my_foods:
    	print("this my friend favorite food: ")
    	print(friend_food)
    	print('\n')