import re

from bs4 import BeautifulSoup

html_doc = ""
with open("baidu.html", encoding="utf-8") as f:
    for line in f:
        html_doc = html_doc + line

# 创建一个BeautifulSoup解析对象
soup = BeautifulSoup(html_doc, "html.parser")

# ==============================文档的遍历======================================
print(soup.head.contents[1])

# ==============================文档的搜索======================================
# (1)find_all
# 字符串过滤: 会查找与字符串完全匹配的标签
print(soup.find_all("a"))

# (2)正则表达式搜索: 会查找包含字符串的标签
print(soup.find_all(re.compile('a')))


# (3)方法: 传入一个函数,按照函数的要求来搜索
def name_is_exists(tag):
    return tag.has_attr("name")


t_list = soup.find_all(name_is_exists)
print(t_list)

# (4)kwargs: 参数
t_list = soup.find_all(rel="dns-prefetch")
print(t_list)

t_list = soup.find_all(class_=True)  # 表示有class的属性
print(t_list)

# (5)text: 参数
t_list = soup.find_all(text="hao123")  # 根据文本搜索
print(t_list)
t_list = soup.find_all(text=["hao123", "地图", "贴吧"])
print(t_list)
t_list = soup.find_all(text=re.compile("\d"))  # 可以结合正则表达式
print(t_list)

# (6)limit: 参数
t_list = soup.find_all("a",limit=3)
print(t_list)

# (7)CSS选择器
t_list = soup.select("title")  # 通过标签查找
print(t_list)
t_list = soup.select(".mnav")  # 通过类查找
print(t_list)
t_list = soup.select("#s_top_wrap")  # 通过id查找
print(t_list)
t_list = soup.select("a[href='https://pan.baidu.com?from=1026962h']")  # 通过属性来查找
print(t_list)
t_list = soup.select("head > title")  # 通过子标签来查找
print(t_list)
