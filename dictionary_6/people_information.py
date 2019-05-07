#使用一个字典来存储一个熟人的信息， 包括名、 姓、 年龄和居住的城市。 
#该字典应包含键first_name 、 last_name 、 age 和city 。 将存储在该字典中
#的每项信息都打印出来。
#罗旭阳，2019/01/29
people_infor = {
	"first_name" : "alice",
	"last_name" : "jack",
	"age" : "18",
	"city" : "China"
	}
inform_s = ["first_name", "last_name", "age", "city"]

for inform in inform_s:
	print(people_infor[inform])

for key, value in people_infor.items():
	print("\nKey is :" + key)
	print("Value is : " + value)
