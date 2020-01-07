'''终端的输入输出'''
import sys
print(sys.stdin.encoding)
print(sys.stdout.encoding)
'''打印环境变量'''
print(sys.path)
'添加当前路径到环境变量中'
sys.path.append(".")
"添加当前路径的上一层路径到环境变量中"
sys.path.append("..")
print(sys.path)