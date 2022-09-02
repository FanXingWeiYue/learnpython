import subprocess  # 子进程模块

# Popen基本格式：subprocess.Popen(‘命令’, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#
# shell=True 表示要在终端中运行的命令
# stdout=sbuprocess.PIPE 表示当命令存在的时候，把结果写入到stdout管道
# stderr=sbuprocess.PIPE 表示当命令不存在的时候，把结果吸入到stderr管道
obj = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
res = obj.stdout.read()
print(res.decode("gbk"))  # 因为windows系统是gbk格式编码的，所以用gbk解码
