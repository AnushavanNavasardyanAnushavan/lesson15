# ///////fibonachi
# def fib(n):
#     if n == 0:
#         return 0 
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 2) + fib(n - 1)
# print(fib(7))

# N1
# def calculator(num1, num2, arg):
#     if arg == "+":
#         return num1 + num2
#     elif arg == "-":
#         return num1 - num2
#     elif arg == "*":
#         return num1 * num2
#     else:
#         return num1 / num2

# num1 = int(input("num 1 -- "))
# num2 = int(input("num 2 -- "))
# arg = input("Enter argument -- ")
# print(calculator(num1, num2, arg))


# N2
# def func(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# num1 = int(input("Enter number 1st ---- "))
# num2 = int(input("Enter number 2sd ---- "))

# print(func(num1, num2))


# N3
# def listFanc(myList):
#     res = 0
#     for i in myList:
#         res += int(i)
#     print(res)
# list1 = input("Enter list --- ")
# list1 = list1.split(" ")
# listFanc(list1)


# N4
# def multiply(allMultiply):
#     res = 1
#     for i in allMultiply:
#         res *= i
#     return res

# list1 = [1, 2, 3, 4, 5]
# print(multiply(list1))


# N5
# def textsum(a):
#     numCount1 = 0
#     strCount1 = 0
#     for i in a:
#         if i.isdigit():
#             numCount1 += 1
#         else:
#             strCount1 += 1

#     return numCount1, strCount1
# text = "python39555"
# print(textsum(text))


# N6
# dict1 = {
#     "Name1": 16,
#     "Name2": 10,
#     "Name3": 18
# }
# def dictFanc(d):
#     sortDictValue = sorted(d.values())
#     sortDictKey = sorted(d.keys())
#     sortDict = {}
#     for i in range(0, len(sortDictValue) - 1):
#         if sortDictValue[i] < 16:
#             del sortDictValue[i]
#             del sortDictKey[i]
#     for i, j in zip( sortDictKey, sortDictValue):
#         sortDict.setdefault(i, j)
#     return sortDict
#     # return sortDictValue, sortDictKey

# print(dictFanc(dict1))