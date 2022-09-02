import time

# 一: time
# 时间分为三种格式
# 1、时间戳：从1970年到现在经过的秒数
#    作用：用于时间间隔计算
print(time.time())

# 2、按照某种格式显示的时间:2022-09-01 09:14:32
#     作用：用于展示时间
print(time.strftime('%Y-%m-%d %H:%M:%S'))

# 3、结构化的时间
#    作用：用于单独获取时间的某一部分
res = time.localtime()
print(res)
print(res.tm_year)

# 二: datetime
import datetime

print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(day=3))
