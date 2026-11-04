s = [1,2,3,"A","Hello",True]    #可以不同数据类型
print(s[0])     #正向索引
print(s[-6])    #反向索引

s[2] = "B"  #下标不能溢出
print(s)

del s[4]
print(s)

s1 = ["A","B","C","D","E","F"]
s2 = s1[1:5:2]  #不包括5下标
s3 = s1[:5]
print(s2)



ss = [56, 90, 88, 65, 90, 100, 209, 72, 145]
print(ss)

#append():在列表尾部追加元素
ss.append(188)
print(ss)

#insert():在指定索引之前，插入元素
ss.insert(2,80)
print(ss)

# remove():移除列表中第一个匹配到的元素
ss.remove(90)
print(ss)

#pop():删除列表中指定索引位置的元素并返回(如果未指定，默认删除最后一个)
e = ss.pop(1)
print(e)

e = ss.pop()
print(e)

# sort():排/序
ss.sort()
print(ss)
# reverse():反转列表元素
ss.reverse()
print(ss)


