# 1. 判断正数、零和负数。请输入合法整数。
num = int(input("num="))
if num > 0:
    print(f"{num}是正数")
elif num == 0:
    print(f"{num}等于0")
else:
    print(f"{num}是负数")

# 2. 简易计算器：接着输入两个普通有限数值和运算符。
# match/case 需要 Python 3.10 或更高版本。
num1 = float(input("num1="))
num2 = float(input("num2="))
operator = input("operator=")

match operator:
    case "+":
        print(f"{num1}+{num2}={num1 + num2}")
    case "-":
        print(f"{num1}-{num2}={num1 - num2}")
    case "*":
        print(f"{num1}*{num2}={num1 * num2}")
    case "/" if num2 != 0:
        print(f"{num1}/{num2}={num1 / num2}")
    case "/":
        print("除数不能为 0")
    case _:
        print("不支持的运算符，请输入 +、-、* 或 /")
