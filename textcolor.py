import time
import os
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

condition = str("\n Do you Want to Add(+) or Sub(-)")
condition2 = str("\n Do you Want to Multiply(*) or Divide(/) ")
condition3 = str("\n if you Wanna find out Square(***) or Cube(///)")
enter1 = str("\n Enter Num 1 :")
enter2 = str("\n Enter Num 2 :")


print("\n                           Calculator\n")

print(condition)
print(condition2)
print(condition3)

a = str(input())

if a == '+':
    time.sleep(2)
    print("\n Add Detected____----___---___________----")
    time.sleep(2)
    print(Fore.RED + "\n LOADING ______---____--____-___-----")
    os.system("cls")
    time.sleep(2) 
    print(enter1)
    add1 = float(input())
    print(enter2) 
    add2 = float(input())
    res = add1 + add2
    print(f"{Fore.GREEN}PROCESSING--__--___--___--__---__")
    os.system("cls")
    time.sleep(2)
    print("\n            Result : ", res)
elif a == '-':
    time.sleep(2)
    print("\n Sub Detected____----___---___________----")
    time.sleep(2)
    print(Fore.RED + "\n LOADING ______---____--____-___-----")
    os.system("cls")
    time.sleep(2)
    print(enter1)
    sub1 = float(input())
    print(enter2)
    sub2 = float(input())
    res3 = sub1 - sub2
    print(f"{Fore.GREEN}PROCESSING--__--___--___--__---__")
    time.sleep(2)
    print("\n Result : (", res3)
elif a == '/':
    time.sleep(2)
    print("\n Divide Detected____----___---___________----")
    time.sleep(2)
    print(Fore.RED + "\n LOADING ______---____--____-___-----")
    os.system("cls")
    time.sleep(2)
    print(enter1)
    div1 = float(input())
    print(enter2)
    div2 = float(input())
    res4 = div1 / div2
    print(f"{Fore.GREEN}PROCESSING--__--___--___--__---__")
    os.system("cls")
    time.sleep(2)
    print("\n Result : (", res4)
elif a == '*':
    time.sleep(2)
    print("\n Multiply Detected____----___---___________----")
    time.sleep(2)
    print(Fore.RED + "\n LOADING ______---____--____-___-----")
    os.system("cls")
    time.sleep(2)
    print(enter1)
    mu1 = float(input())
    print(enter2)
    mu2 = float(input())
    res5 = mu1 * mu2
    print(f"{Fore.GREEN}PROCESSING--__--___--___--__---__")
    os.system("cls")
    time.sleep(2)
    print("\n Result : (", res5)
elif a == '***':
    time.sleep(2)
    print("\n Square Detected____----___---___________----")
    time.sleep(2)
    print(Fore.RED + "\n LOADING ______---____--____-___-----")
    os.system("cls")
    time.sleep(2)
    print("\n Enter A Num :")
    sq1 = float(input())
    res6 = sq1 * sq1
    print(f"{Fore.GREEN}PROCESSING--__--___--___--__---__")
    os.system("cls")
    time.sleep(2)
    print("\n Result : (", res6)
elif a == '///':
    time.sleep(2)
    print("\n Cube Detected____----___---___________----")
    time.sleep(2)
    print(Fore.RED + "\n LOADING ______---____--____-___-----")
    os.system("cls")
    time.sleep(2)
    print("\n Enter A Num :")
    cu1 = float(input())
    res7 = cu1 * cu1 * cu1 
    print(f"{Fore.GREEN}PROCESSING--__--___--___--__---__")
    os.system("cls")
    time.sleep(2)
    print("\n Result : (", res7)
