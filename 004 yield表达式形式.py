# yield表达式形式
def dog(name):
    print('道哥{}准备吃东西了'.format(name))
    fool_list = []
    while True:
        # x拿到的是yield接收到的值
        x = yield fool_list
        print('道哥{}吃了{}'.format(name, x))
        fool_list.append(x)


g = dog('alex')  # 创建生成器对象
g.send(None)  # 等同于next(g)，在生成器刚开始的时候要send None值
res = g.send("一根骨头")  # 将send传参的值传递给yield
print(res)
