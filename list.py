s = [1,2,3,"A","Hello",True]    #可以不同数据类型
print(s[0])     #正向索引
print(s[-6])    #反向索引

s[2] = "B"  #下标不能溢出
print(s)

del s[4]
print(s)

