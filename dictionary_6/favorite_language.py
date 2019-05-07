#创建一个应该会接受调查的人员名单
 #其中有些人已包含在字典中 , 而其他人未包含在字典中。
#遍历这个人员名单， 对于已参与调查的人， 打印一条消息表示感谢。
# 对于还未参与调查的人， 打印一条消息邀请他参与调查。
people_names = {
	'edward': 'ruby',
	'phil': 'python',
	'jen': 'python',
	'sarah': 'c',
}

favorite_languages = {
'jen': 'python',
'sarah': 'c',

}

#找出那些没有参加，哪些参加的人,在总人数里面抽取待测人名
for people_name in people_names:
	if people_name not in favorite_languages :
		print("Hello! " + people_name + 
			" ,please join us soon") 
	else:
		print("Thank you " + people_name + ",you are vvery kind")
