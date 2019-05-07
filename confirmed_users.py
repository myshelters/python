#使用while循环，将未验证的用户一道已验证用户列表中
#罗旭阳，2019/01/30
#首先，创建一个待验证用户列表
#和一个用于存储已验证用户的空列表
unconfirmed_users = ["alice", "brian", "jack"]
confirmed_users = []

#验证每一个用户直到没有未验证用户为止
#将每个经过验证的列表都移入已验证用户列表中
while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print("Verifying user : " + current_user.title() )
	confirmed_users.append(current_user)
	pass

#显示所有已验证的用户
print("All confirmed_user  users are : ")
for confirmed_user in confirmed_users:
	print("\t confirmed_user")