#创建一个字典， 在其中存储三条大河流及其流经的国家
#罗旭阳, 2019/01/29
river_across = {"nile" : "eqypt"}

for name in river_across.keys():
	print(name.title() )

for country in river_across.values():
	print(country.title() )