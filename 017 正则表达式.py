import re

# =================================匹配模式=================================
# 一对一的匹配
# \w与\W
print(re.findall('\w', 'hello egon 123'))  # ['h', 'e', 'l', 'l', 'o', 'e', 'g', 'o', 'n', '1', '2', '3']
print(re.findall('\W', 'hello egon 123'))  # [' ', ' ']

# \s与\S
print(re.findall('\s', 'hello  egon  123'))  # [' ', ' ', ' ', ' ']
print(re.findall('\S', 'hello  egon  123'))  # ['h', 'e', 'l', 'l', 'o', 'e', 'g', 'o', 'n', '1', '2', '3']

# \d与\D
print(re.findall('\d', 'hello egon 123'))  # ['1', '2', '3']
print(re.findall('\D', 'hello egon 123'))  # ['h', 'e', 'l', 'l', 'o', ' ', 'e', 'g', 'o', 'n', ' ']

# \A 指定匹配必须出现在字符串的开头（忽略 Multiline 选项）
# \Z 指定匹配必须出现在字符串的结尾或字符串结尾的 \n 之前（忽略 Multiline 选项）
print(re.findall('\Ahe', 'hello egon 123'))  # ['he'],\A==>^
print(re.findall('123\Z', 'hello egon 123'))  # ['he'],\Z==>$

# ^ 指定匹配必须出现在字符串的开头或行的开头
# $ 指定匹配必须出现在以下位置：字符串结尾、字符串结尾的 \n 之前或行的结尾。
print(re.findall('^h', 'hello egon 123'))  # ['h']
print(re.findall('3$', 'hello egon 123'))  # ['3']

# 重复匹配：| . | * | ? | .* | .*? | + | {n,m} |
# .
print(re.findall('a.b', 'a1b'))  # ['a1b']
print(re.findall('a.b', 'a1b a*b a b aaab'))  # ['a1b', 'a*b', 'a b', 'aab']
print(re.findall('a.b', 'a\nb'))  # []
print(re.findall('a.b', 'a\nb', re.S))  # ['a\nb']
print(re.findall('a.b', 'a\nb', re.DOTALL))  # ['a\nb']同上一条意思一样

# * 左侧字符重复0次或无穷次，性格贪婪
print(re.findall('ab*', 'bbbbbbb'))  # []
print(re.findall('ab*', 'a'))  # ['a']
print(re.findall('ab*', 'abbbb'))  # ['abbbb']

# + 左侧字符重复1次或无穷次，性格贪婪
print(re.findall('ab+', 'a'))  # []
print(re.findall('ab+', 'abbb'))  # ['abbb']

# ? 左侧字符重复0次或1次，性格贪婪
print(re.findall('ab?', 'a'))  # ['a']
print(re.findall('ab?', 'abbb'))  # ['ab']
# 匹配所有包含小数在内的数字
print(re.findall('\d+\.?\d*', "asdfasdf123as1.13dfa12adsf1asdf3"))  # ['123', '1.13', '12', '1', '3']

# .*默认为贪婪匹配
print(re.findall('a.*b', 'a1b22222222b'))  # ['a1b22222222b']

# .*?为非贪婪匹配：推荐使用
print(re.findall('a.*?b', 'a1b22222222b'))  # ['a1b']

# {n,m}
# {0,} ==> *
# {1,} ==> +
# {0,1} ==> ?
# {n} ==> 单独一个n代表出现n次
print(re.findall('ab{2}', 'abbb'))  # ['abb']
print(re.findall('ab{2,4}', 'abbb'))  # ['abb']
print(re.findall('ab{1,}', 'abbb'))  # 'ab{1,}' ===> 'ab+'
print(re.findall('ab{0,}', 'abbb'))  # 'ab{0,}' ===> 'ab*'

# [] 匹配指定字符一个
print(re.findall('a[1*-]b', 'a1b a*b a-b'))  # []内的都为普通字符了，且如果-没有被转意的话，应该放到[]的开头或结尾
print(re.findall('a[^1*-]b', 'a1b a*b a-b a=b'))  # []内的^代表的意思是取反，所以结果为['a=b']
print(re.findall('a[0-9]b', 'a1b a*b a-b a=b'))  # []内的^代表的意思是取反，所以结果为['a=b']
print(re.findall('a[a-z]b', 'a1b a*b a-b a=b aeb'))  # []内的^代表的意思是取反，所以结果为['a=b']
print(re.findall('a[a-zA-Z]b', 'a1b a*b a-b a=b aeb aEb'))  # []内的^代表的意思是取反，所以结果为['a=b']

# \# print(re.findall('a\\c','a\c')) #对于正则来说a\\c确实可以匹配到a\c,但是在python解释器读取a\\c时，会发生转义，然后交给re去执行，所以抛出异常
print(re.findall(r'a\\c', 'a\c'))  # r代表告诉解释器使用rawstring，即原生字符串，把我们正则内的所有符号都当普通字符处理，不要转义
print(re.findall('a\\\\c', 'a\c'))  # 同上面的意思一样，和上面的结果一样都是['a\\c']

# ():分组
print(re.findall('ab+', 'ababab123'))  # ['ab', 'ab', 'ab']
print(re.findall('(ab)+123', 'ababab123'))  # ['ab']，匹配到末尾的ab123中的ab
print(re.findall('(?:ab)+123', 'ababab123'))  # findall的结果不是匹配的全部内容，而是组内的内容,?:可以让结果为匹配的全部内容
print(re.findall('href="(.*?)"', '<a href="http://www.baidu.com">点击</a>'))  # ['http://www.baidu.com']
print(re.findall('href="(?:.*?)"', '<a href="http://www.baidu.com">点击</a>'))  # ['href="http://www.baidu.com"']

# |
print(re.findall('compan(?:y|ies)', 'Too many companies have gone bankrupt, and the next one is my company'))
