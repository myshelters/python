#可以接受任何数量的关键字形参的函数,并打印
#罗旭阳，2019/01/30
def make_car(build_man, size, **more_inform_dic):
	car_inform = {}
	print("制造商：" + build_man + ".")
	print("型号：" + size + ".")
	car_inform["build_man"] = build_man
	car_inform["size"] = size
	for key, value in more_inform_dic.items():
		car_inform[key] = value
	return car_inform
	pass

def main():
	car = make_car(
		"subaru", 
		"outback",
		color = "blue", 
		twu_package = True
		)
	print(car)
	pass

main()