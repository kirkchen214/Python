# 注释标志
print(100)              # int
print(3.14)             # float
print(True)             # bool
print(False)            # 首字母必须大写
print("Hello World")    # str
print("___________")    # 字符串必须使用引号
print(None)             # none

num =100
print(num)

num +=1
print(num)

num = "OK"
print(num)

a,b = 1,2
print("sum=",a+b)

x = True
print(type(x))
print(type("True"))
print(type("x"))

print(isinstance(a,int))
print(isinstance(b,str))


s1 = "hello"  
s2 = 'python' 
s3 = """hello
周一:
    周二:
"""
print(s1)
print(s2)
print(s3)


str1 = "hello" "world"
print(str1)
str2 = "hello"+"world"
print(str2)
s1 = "hello"
s2 = "world"
s3 = 123
print("python:"+s1+","+s2+str(s3))

name = "lisi"
age = 18
print("name:%s,age:%d"%(name,age))
print(f"name:{name},age:{age}")

name = input("name:")
print(f"name:{name}")
age = input("age:")
print(f"age:{age}")
