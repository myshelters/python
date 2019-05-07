#清除字符串的空白

language = "  python  "

print(language.rstrip())    #去除右边空白
print(language.lstrip())     #去除左边空白
print(language.strip())     #去除两边空白
print(language)              #不过是暂时去除空白，之后还要用之后的数值代替

language = language.strip()    #用两边无空白替换，原有字符串
print(language)
