num = int(input("num="))
if num > 0:
    print(f"{num}是正数")
elif num == 0:
    print(f"{num}等于0")
else:
    print(f"{num}是负数")


num1 = float(input("num1="))
num2 = float(input("num2="))
operator = input("operator=")

match operator:
    case "+":
        print(f"{num1}+{num2}={num1+num2}")
    case "-":
            print(f"{num1}-{num2}={num1-num2}")    
    case "*":
            print(f"{num1}*{num2}={num1*num2}")
    case "/" if num2!=0:
            print(f"{num1}/{num2}={num1/num2}")
    case _:
            print("!!!")
