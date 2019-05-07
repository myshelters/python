#按顺序遍历字典中的所有键
#罗旭阳，2019/01/29
favorite_languages = {
	"jen" : "python",
	"sarah" : "c",
	"ahh" : "r",
}

#关键是使用sorted()对键进行排序
for name in sorted(favorite_languages.keys() ):
	print(name.title() + ",thank you for taking the pool.")
