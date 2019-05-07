#体验range()的步长，并进行乘方运算
#罗旭阳， 2019/01/28

#1-10乘方运算
squares = []
for value in range(1,11):
	square = value ** 2
	squares.append(square)

print(squares)

#删除元素，再进行偶数乘方
for one_square in squares:
	#为什么无法完全删除
	#squares.remove(one_square)
	#print(one_square)
	del squares[-1]
print(squares)

#偶数
even_number = list(range(2, 11, 2))
print(even_number)

#数值加三
foo = list(range(1,11,3))
print(foo)

