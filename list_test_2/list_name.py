#晚餐邀请名单列表
#罗旭阳， 2019/1/28
names = ['alice', 'batman', 'jack', 'stark']
print(names[0].title())

#输出不可参加晚餐的人员，并用新成员代替,并输出新的信息
print(names[3].title() + " can't join the dinner")
names[3] = 'joe'
print(names)
print(names[-1].title())

#使用inset，append添加新的嘉宾
names.insert(0,'john')
names.insert(2,'black')
names.append("blue")
print(names)

#pop，del缩减名单
poped_name = names.pop(2)
message = "Dear " + poped_name.title() + ", you're fuck out of the dinner"
print(message)
del names[0]
print(names)