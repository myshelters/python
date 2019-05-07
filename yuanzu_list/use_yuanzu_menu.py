#使用元组存储菜单，并尝试修改元组，验证改变元组的方法，尝试改变元组的顺序
#罗旭阳，2019/01/29
menus = ('egg', 'dinner', 'vegetable', 'table', 'host')

#打印元组
for menu in menus:
	print(menu)

#修改元组元素
#menus[0] = "water"
#TypeError: 'tuple' object does not support item assignment

print("\n")
#重新定义元组
menus = ("host", "egg", "dinner")
for menu in menus:
	print(menu)

#尝试改变元组顺序,reverse()失败，sort()失败，sorted成功
#print(menus.sort())
#print(menus.reverse())
print(sorted(menus))
menus = sorted(menus)
print(menus)