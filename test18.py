class BlackMedium:
    feature = 'Ugly'

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def sell_house(self):
        print('%s 黑中介卖房子啦,傻逼才买呢,但是谁能证明自己不傻逼' % self.name)

    def rent_house(self):
        print('%s 黑中介租房子啦,傻逼才租呢' % self.name)


b1 = BlackMedium('万成置地', '回龙观天露园')

# 检测是否含有某属性
print(hasattr(b1, 'name'))
print(hasattr(b1, 'sell_house'))

# 获取属性
n = getattr(b1, 'name')
print(n)
func = getattr(b1, 'rent_house')
func()

# getattr(b1,'aaaaaaaa') #报错
print(getattr(b1, 'aaaaaaaa', '不存在啊'))

# 设置属性
setattr(b1, 'sb', True)
setattr(b1, 'show_name', lambda self: self.name + 'sb')
print(b1.__dict__)
print(b1.show_name(b1))

# 删除属性
delattr(b1, 'addr')
delattr(b1, 'show_name')
delattr(b1, 'show_name111')  # 不存在,则报错

print(b1.__dict__)
