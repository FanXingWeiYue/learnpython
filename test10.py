import re

# 写法一
# 正则表达式，过滤出中国
str = '<div class ="name">中国</div>'
res1 = re.findall(r'<div class =".*">(.*?)</div>', str)
print(res1)

# 写法二
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
pattern = re.compile(r'<div class =".*">(.*?)</div>')  # 匹配模式
res2 = pattern.findall(str)
print(res2)
