#函数打印列表中魔术师的名字，使用函数对列表进行修改
#1.原列表数据改变
#2.原列表不改变
#罗旭阳，2019/01/30
#定义打印名字的函数
def show_magicians(magicians):
	print("Magicians' name is :")
	for magician in magicians:
		print("\t" + magician.title() )
	pass

#对魔术师列表进行修改 1，每个魔术师前都加入字样“the Great”
def make_great(magicians):
	'''
	建造一个空列表changed_magicians,改变后的元素存储在这里面
	'''
	changed_magicians = []

	for magician in magicians:
		current_magician = "the Great " + magician.title()
		changed_magicians.append(current_magician)
	pass

#删除magicians，将修改后的列表赋值给他
	#del magicians[:]
	#magicians = changed_magicians[:]
	return changed_magicians

#方法二，修改 1,不建立新列表
def new_make_great(magicians):
	'''
	don't make other list to finish the purpose 
	'''
	for magician_num in range( len(magicians) ):
		current_magician = magicians.pop(0)
		magicians.append("the Great " + current_magician.title() )

	return magicians


def main():
	magicians = ["alice", "stack", "black"]
	show_magicians(magicians)

	new_magicians = make_great(magicians)
	show_magicians(new_magicians)

#修改二，不改变原有数据
	now_magicians = make_great(magicians[:])
	print("\n")
	show_magicians(now_magicians)
	show_magicians(magicians)
	
main()