import re

from bs4 import BeautifulSoup

html_doc = ""
with open("baidu.html", encoding="utf-8") as f:
    for line in f:
        html_doc = html_doc + line

# 创建一个BeautifulSoup解析对象
soup = BeautifulSoup(html_doc, "html.parser")

# 1、BeautifulSoup 整个文档
print(soup)

# 2、Tag 标签及其内容，拿到它所找到的第一个标签
print(soup.a)
print(soup.meta)

# 3、NavigableString 标签里的内容(字符串)
print(soup.title.string)

# 4、dict 标签里的属性
print(soup.meta.attrs)

# 5、Comment 是一个特殊的NavigableString,输出的内容不包含注释符号
print(soup.a.string)

# print("获取特定的URL地址")
# link_node = soup.find('a', href="http://example.com/elsie")
# print(link_node.name, link_node['href'], link_node['class'], link_node.get_text())
#
# print("正则表达式匹配")
# link_node = soup.find('a', href=re.compile(r"ti"))
# print(link_node.name, link_node['href'], link_node['class'], link_node.get_text())
#
# print("获取P段落的文字")
# p_node = soup.find('p', class_='story')
# print(p_node.name, p_node['class'], p_node.get_text())
