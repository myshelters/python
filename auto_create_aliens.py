#使用range（）使for循环执行相应次数，同时创建相对应的外星人
#罗旭阳，2019/01/29
#创建一个存储外星人的空列表
aliens = []

# 创建30个外星人
for alien_num in range(30):
	new_alien = {"color" : "green", "point" : 5, "speed" : "slow"}
	aliens.append(new_alien)

#显示前五个外星人
for alien in aliens[:5]:
	print(alien)

print("... ...")

#显示到底创建多少个外星人
print("Total number of aliens : " + str(len(aliens)))
