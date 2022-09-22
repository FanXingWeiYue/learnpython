import configparser

config = configparser.ConfigParser()
config.read("config.ini")

# 1、获取sections
print(config.sections())
# 2、获取某一sections下所有的key
print(config.options("mysql1"))
# 3、获取某一sections下所有的items
print(config.items("mysql1"))
# 4、获取某一sections下某一options的值
print(config.get("mysql1",'host'))
print(config.getint("mysql1",'port'))
