#使用各种方法删除元素
#罗旭阳， 2019/1/28

#del 删除指定位置元素
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[2]
print(motorcycles)

#pop 删除列表末尾元素,弹出的元素用popped_motorcycles存储
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

#pop也可以弹出指定位置的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
last_owned = motorcycles.pop(-1)
print("the first motorcycle I owned was a " + first_owned.title())
print("the last motorcycle I owned was a " + last_owned.title() )

#remove 根据值删除元素honda,元素值需要加引号
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove("honda")
print(motorcycles)