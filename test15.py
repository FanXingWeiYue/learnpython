# 1、什么是哈希hash
#    hash是一类算法、该算法接受传入的内容，经过运算得到一串hash值
#    hash值的特点
# I 只要传入的内容一样，得到的hash值必然是一样
# II  不能由hash值反解成内容
# III 不管传入的内容有多大，只要使用的hash算法不变，得到的hash值长度一定

# 2、hash值的用途
# 用途1: 特点II 用于密码密文文件传输与验证
# 用途2: 特点I、III 用于文件完整性验证

# 3、如何用
import hashlib

m = hashlib.md5()
m.update("hello".encode("utf-8"))  # 给hash工厂传入原材料，传入的必须是bytes类型
m.update("world".encode("utf-8"))  # 可以继续传入
res = m.hexdigest()  # 进行加工
print(res)
