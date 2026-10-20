# 第一天复习：输入名称和整数电量，增加 5，再输出。
# 保留原变量名 buttery；本题暂不限制电量范围。
name = input("请输入机器人名称：")
buttery = int(input("请输入当前电量（整数）："))
buttery += 5
print(f"机器人{name},充电后电量为{buttery}%")
