# 1. 字面量：# 表示注释（字符串中的 # 除外）。
print(100)              # int：整数
print(3.14)             # float：浮点数
print(True)             # bool：布尔值
print(False)            # True 和 False 的首字母必须大写
print("Hello World")    # str：字符串
print("___________")    # 字符串字面量需要引号
print(None)             # 空值 None 的类型是 NoneType

# 2. 变量与赋值
num = 100
print(num)              # 100

num += 1               # 对这里的整数，相当于 num = num + 1
print(num)              # 101

num = "OK"             # 同一个名字重新绑定到字符串
print(num)              # OK

a, b = 1, 2
print("sum=", a + b)    # sum= 3

# 3. 查看类型与判断类型
x = True
print(type(x))         # <class 'bool'>
print(type("True"))    # <class 'str'>
print(type("x"))       # <class 'str'>：这里是文本，不是变量 x

print(isinstance(a, int))  # True
print(isinstance(b, str))  # False

# 4. 字符串的三种定义方式
s1 = "hello"
s2 = 'python'
s3 = """hello
周一:
    周二:
"""
print(s1)
print(s2)
print(s3)              # 保留字符串内的换行和缩进

# 5. 字符串拼接与类型转换
str1 = "hello" "world"  # 相邻的字符串字面量可以自动拼接
print(str1)            # helloworld
str2 = "hello" + "world"
print(str2)            # helloworld
s1 = "hello"
s2 = "world"
s3 = 123
print("python:" + s1 + "," + s2 + str(s3))  # python:hello,world123

# 6. 字符串格式化输出
name = "lisi"
age = 18
print("name:%s,age:%d" % (name, age))  # name:lisi,age:18
print(f"name:{name},age:{age}")       # name:lisi,age:18

# 7. 字符串输入：每次输入后按 Enter；input() 返回字符串。
name = input("name:")
print(f"name:{name}")
age = input("age:")
print(f"age:{age}")     # 此时 age 是 str，不再是上面的 int
