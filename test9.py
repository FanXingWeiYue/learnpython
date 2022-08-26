import json

# json.loads()  #把json字符串转换成dict格式
# json.dumps()  #把dict格式转换成json字符串
# json.load()   #从文件读取字符串转换成python对象
# json.dump()   #将python对象转换成json字符串并存入文件

# 1.字符串(json) --> 字典
color = '{"1":"red","2":"green","3":"blue","4":"black"}'
color_dict = json.loads(color)
print("color_dict:", color_dict)

# 2.字典 --> json
color_json = json.dumps(color_dict)
print("color_json:", color_json)

# 3.(json)文件 --> 字典
with open("color.json") as f:
    dt = json.load(f)
print("dt:", dt)

# 4.dict --> (json)文件
with open("color.json", "w") as f1:
    json.dump(dt, f1)  # 将python字典数据写入color1.json

# 输出 ：
color_dict: {'1': 'red', '2': 'green', '3': 'blue', '4': 'black'}
color_json: {"1": "red", "2": "green", "3": "blue", "4": "black"}
dt: {'1': 'red', '2': 'green', '3': 'blue', '4': 'black'}
