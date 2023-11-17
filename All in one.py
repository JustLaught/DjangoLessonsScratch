##############################################################################
###################################################  DAY - 1    ##############
##############################################################################
# print("Hello \nWorld!")
# Hot-Ket Ctrl+/ Зробити коментар з виділеного
#
#
# print("555", "wasd", "444", "dsaw")
# Кома автоматично ставить пробіл
#
#
# print("Hello", end="")
# print("World", end="")
# print("Successful")
#
#
# sep=  separate Пропуски між аргументами
#
#
# print("Hello"*4)
# print("Hello" + "" + "wold")
# print("5" + "4", "wsad" + "3")
# + = склейка ,= через можна добавляти аргументи з пробілом між ними
# * = кількість раз вивводу аргументів в межах одної команди print(><)
#
#
#Правила змінних:Не починається з чисел, без пробілів
#
# import time
# import math


# 3
#ЗМІННІ
#x = 4 # int
#y = 13.3 # float
#x1 = "111" # str
#
# print(type(x))
# print(type(y))
# print(type(x1))
#TYPE показує ти данних
#
#
# name = "Ostap"
# age = 22
#
# print("Name:", name, " and my age is", age)
# print("Name:" + name + " and my age is", age)
# print(f"Name: {name} and my age is {age}")
#
# f = форматовна стрічка(підставляє тип данних)
#
# name = "Ostap"
# address = "address is: Lviv.Vinniki"
# age = 22
# hobbi = "And i'm love Minecraft"
# phoneNumb = "+380731662876"
# print("Hello my name is", name)
# print(address)
# print("My age is", age)
#print("My phone nummber: ",phoneNumb)
# print(hobbi)
#
#print("Hello""\n\tMy name is", name,"\n", "\t", "My", address, "\n" , "\t"*1, "My phone nummber:", phoneNumb, "\n\t\tMy age is:", age, "\n\t\t\t", hobbi)
#
# import keyword
# print(keyword.kwlist)
# Слова які не можна використовувати для змінних
##############################################################################
###################################################  DAY - 2    ##############
##############################################################################
# x = 5
# y = 3
# print(x + y)
# print(x - y)
# print(x / y)
#
# print(x ** y) Піднесення в степінь
# print(x % y) Ділення по модулю
# print(x // y) Цілочисельне діленння
#
# print(round(x/y, 2)) Заокруглення
#
#
# x = 10
# y = 10
#
# print(bool(1))
# print(x == y)
# print(x != y)
# print(x < y)
# print(x > y)
# print(x <= y)
# print(x >= y)
#
# login = "vac"
# input_login = input("Login = ")
# if login == input_login:
#     print("Right!")
# if login != input_login:
#     print("Wrong!")
#
# x = int(input("Введіть число =  "))
# if x > 0:
#     print("Число додатнє")
# if x == 0:
#     print("ZEROOO")
# if x < 0:
#     print("Число відємне")
#
# num_1 = int(input("Введіть число =  "))
# if num_1 % 2 == 0:
#     print("Парне")
# if num_1 % 2 != 0:
#     print("Не парне")
#
# login = '1234a'
# password = '4321b'
# login_input = input("Login = ")
# if login != login_input:
#     print("Wrong login")
# password_input = input("Password = ")
# if password != password_input:
#         print("Wrong password")
# if login == login_input:
#     if password == password_input:
#         print("DONE!")
#
# login = '1234a'
# password = '4321b'
# login_input = input("Login = ")
# password_input = input("Password = ")
#
# is_login = False
#
# if login == login_input:
#     if password == password_input:
#         print("DONE!")
#         is_login = True
#
# if is_login == False:
#     print("Incorrect data!!")
##############################################################################
###################################################  DAY - 3    ##############
##############################################################################
# age = int(input("Enter your age ="))
# if age >= 18:
#     print("Accepted")
# else:
#     print("Sorry to early 4 u")
#
# num_1 = int(input("Enter number =  "))
# if num_1 % 2 == 0:
#     print("Even")
# else:
#     print("Not Even")
#
# color =input("Chose Blue, Red or Green  ---->  "))
# if color == "Blue":
#     print("1")
# else:
#     if color == "Red":
#         print("2")
#     else:
#         print("3")
#
# day_week = input("Write any day of week ---->")
# if day_week == "monday":
#     print("Alarm clock at 7 p.m")
# elif day_week == "wednesday":
#     print("Alarm clock at 10 p.m")
# elif day_week == "thursday":
#     print("Alarm clock at 3 a.m")
# else:
#     print("Alarm clock is not set for that day")
#
# jacket_color = input("Enter your jacket clor ---->>")
# city_at = input("Enter your city ---->>")
# name = input("Enter your name ---->>")
# if jacket_color == "Black" and name == "Jack da Ripper" and city_at == "London":
#     print("\tYou failed dude!!!")
# else:
#     print("Chill mate")
#
# num_1 = str(input("number = "))
# for d in num_1:
#     print(d)
#
# num_1 = int(input("number = "))
# num_2 = num_1 % 10
# num_3 = num_1 // 10
# print(num_1, num_3, num_2)
#
# num_1 = int(input("number = "))    СКОРОЧЕНІ ОПЕРАТОРИ
# num_1 %= 10
# num_1 //= 10
# print(num_1)
#
# num_1 //= 10
# print(num_1 % 10)
#
# num_1 = int(input("number = "))
# print(num_1 // 10)
# num_1 %= 10
# print(num_1)
#
#Для 4-х чисел
# num = 1324
#
# print(num % 10)
#
# num //=10
# print(num % 10)
#
# num //=10
# print(num % 10)
#
# num //=10
# print(num % 10)
#
# num //=10
# print(num % 10)
#
#
#
# num = 1324
#
# a = num % 10
# num //=10
# b = num % 10
# num //=10
# c = num % 10
# num //=10
# if c + num > a + b:
#     print("Left")
# elif c + num < a + b:
#     print("Right")
# else:
#     print("Equal")
#
# start_phone_hour = int(input("Enter start hour  = "))
# start_phone_min = int(input("Enter start min  = "))
# end_phone_hour = int(input("Enter end hour  = "))
# end_phone_min = int(input("Enter end min  = "))
#
# result_phone_hour = (end_phone_hour - start_phone_hour) * 60
# result_phone_min = end_phone_min - start_phone_min
# if result_phone_min < 0:
#     result_phone_hour -= 60
#     result_phone_min += 60
#
# print(((result_phone_min + result_phone_hour) * 60) // 100)
##############################################################################
###################################################  DAY - 3    ##############
##############################################################################
# x = 5
# if x > 10:
#     x = 15
# else:
#     x = 0
#
# print(x)
#
# x = 5
# x = 15 if x > 10 else 0 #Тринарний оператор
#
# print(x)
#
# x = 11
# x = print("even") if x % 2 == 0 else print("not even")
#
# what = input ("Введіть бажану дію: + - Додати, - - Відняти, * - Помножити, / - Поділити  =")
# a = float (input ("Введіть перше число  "))
# b = float (input ("Введіть друге число  "))
# what = input ("Введіть бажану дію: + - Додати, - - Відняти, * - Помножити, / - Поділити  =")
#
# res = a + b if what == "+" else (((a - b if what == "-" else (a * b if what == "*" else(a / b if what == "/" else "wrong")))))
# print(res)
#
# num = 0
# res = "A" if num else "B"
#
# flag = True
# if not flag:
#     print("A")
#
# while True:
#     print("a")
#     print("b")
#     print("c")
#
#
# i = 0
# while i < 5:
#     print(i)
#     if i == 3:
#         i = 7
#     i += 1
# print(i)
#
# i = int(input("Num 1 =  "))
# b = int(input("Num 2 =  "))
# while i <= b:
#     print(i)
#     i += 1
#
# count = int(input("Enter repeat count  =  "))
# while count > 0:
#     print(count)
#     count -=1
#
# x, y = 13, 15
# a, b = input(), input()
#
# x, y = y, x
#
#
# start = int(input("Num 1 = "))
# end = int(input("Num 2 = "))
# sum = 0
# while start != end + 1:
#     print(f"{sum} = {start}")
#     sum += sum
#     start += 1
# print(f"sum = {sum}")
#
#
# num_1 = int(input("Enter number = "))
# if num_1 < 10:
#     print("1")
# elif num_1 < 100:
#     print("2")
# elif num_1 < 1000:
#     print("3")
# else:
#     print("IDK!!")
#
# num = int(input("Enter num = "))
# count = 0
# while num:
#     num //= 10
#     count += 1
# print(f"Count is = {count}")
#
# Користувач вводить 10 чисел вивести найбільше з них!!!!
# cycle_num = 0
# cycle = 10
# num = 0
# while cycle_num != cycle:
#     num_input = int(input("Enter number = "))
#     if cycle_num == 0:
#         num = num_input
#     elif num_input > num:
#         num = num_input
#     cycle_num += 1
# print(num)
#
# i = 0               NOT MINE
# max_num = 0
# while i < 3:
#     num = int(input("Enter number = "))
#     if i == 0:
#         max_num = num
#     elif num > max_num:
#         max_num = num
#     i += 1
# print(max_num)
##############################################################################
###################################################  DAY - 4    ##############
##############################################################################
# num = int(input("Enter number = "))
# tnp_num = num
# i = 1
# while i <= num:               1
#     print("*  " * i)
#     i += 1
#
# text = ""
# while num > 0:
#     text += "*  "
#     print(text)
#     num -= 1
#
# print("\n2\n")
#
# num = tnp_num                 2
#
# while num > 0:
#     print("* " * num)
#     num -= 1
# while i <= num:
#     print("▢  " * num)
#     i += 1
#                                                   3
#
# i = num
# while i > 0:
#     if i == num or i == 1:
#         print("*  " * num)
#     else:
#         print("*  " + "   " * (num - 2) + "*")
#     i -= 1
# count = 0
# text = ""
# while True:
#     word = input("Enter word ")
#     if word == "Stop":
#         print(f"Count = {count}\n{text}")
#         break
#     text += word + ", "
#     count += 1
#
# count = 0
# sum = 0
# while True:
#     num = int(input("Enter number =  "))
#     sum += num
#     count += 1
#     if sum > 50:
#         print("!")
#         print(sum, count)
#         break
# x = 10
# while x > 0:
#     x -= 1
#     if x % 2 == 0:
#         continue
#     print(x)
#
# while True:
#     num = int(input("Enter number = "))
#     if num % 2 == 0:
#         continue
#     print(num)
#     if num == 0:
#         print("ZERO")
#         break
#
# while True:
#     num = int(input("Enter number = "))
#     if num == 0:
#         print("ZERO")
#         break
#     if num % 2 == 0:
#         continue
#     print(num)
##############################################################################
###################################################  DAY - 5    ##############
##############################################################################
# res = 0
# rounds = 0
# circle = int(input("Enter how much digits =  "))
# while rounds != circle:
#     num = int(input("Enter number =  "))
#     rounds += 1
#     res = res * 10 + num
# print(res)
#
# user_1, login_1, pin_1, balance_1 ="Oleg", "5443", "3122", 2380
# user_2, login_2, pin_2, balance_2 ="Ivan", "5343", "3112", 1480
# user_3, login_3, pin_3, balance_3 ="Alex", "5243", "3123", 4780
#
# cur_user, cur_pin, cur_balance = "", "", 0
# attempts = 0
# bank_money = 2000
# while attempts < 3:
#     input_log = input("Enter login =  ")
#     input_pin = input("Enter pin =  ")
#     if input_log == login_1 and input_pin == pin_1:
#         cur_user, cur_pin, cur_balance = user_1, pin_1, balance_1
#         break
#     elif input_log == login_2 and input_pin == pin_2:
#         cur_user, cur_pin, cur_balance = user_2, pin_2, balance_3
#         break
#     elif input_log == login_3 and input_pin == pin_3:
#         cur_user, cur_pin, cur_balance = user_3, pin_3, balance_3
#         break
#     attempts += 3
#
# else:
#     print("\n\tInvalid data!!\n\t")
#
# while attempts < 3:
#     if attempts >= 0:
#         print(f"\nWelcome {cur_user}!!")
#     do = int(input("\nWhat you want to do: \n1)Check balance, \n2)Withdraw, \n3)Deposit, \n0)Exit! \n\t>>>>  "))
#     if do == 1:
#         print(f"\nYou`r balance is = {cur_balance}")
#
#     elif do == 2:
#         withdraw = int(input("\nHow much you want to withdraw"))
#         if cur_balance >= withdraw > 0:
#             if bank_money <= withdraw:
#                 cur_balance -= withdraw
#                 bank_money -= withdraw
#             else:
#                 do = int(input(f"Sorry that`s only {bank_money} u can withdraw do you want to [1:yes/2:no] = "))
#                 if do == 1:
#                     cur_balance -= bank_money
#                     bank_money -= bank_money
#     elif do == 3:
#         put_on = int(input("\nHow much you want to deposit"))
#         if put_on > 0:
#             cur_balance += put_on
#             bank_money += put_on
#
#     elif do == 0:
#         print(f"\nGoodbye {cur_user} !!")
#
# for x in 3, 7, 13, 22, 56, -2, -9, 5:
#     print(x)
#
# text = input("Enter text")
# i = 0
# for letter in text:
#     print(f"{i=}\t{letter=}")
#
# for i in range(2):
#     print(i)
#
# for i in range(3, 8):
#     print(i)
#
# for i in range(5, 20, 5):
#     print(i)
#
# for _ in range(5):
#     print("Hello!")
#
# text = "Hello"
# print(text[0])
# print(text[-1])
#
# text =input("Enter text =  ")
# letter = input("Enter letter =  ")
# count = 0
# if letter in text:
#     for i in text:
#         print(f"{i} == {count}")
#         if i == letter:
#             count += 1
#             print("WORK!")
#     print(f"{count=}")
#
# text = "abracadabra"
# print(text[2])
# print(text[3:5])
#
# print(text[:5])
# start = 0
# stop = 0
# letter_1 = input("Enter letter =  ")
# letter_2 = input("Enter letter =  ")
# count = 0
# if letter_1 and letter_2 in text:
#     for i in range(len(text)):
#         print(f"{letter_1} = {text[i]} ,  {i}")
#         if letter_1 == text[i]:
#             start = i
#             break
#     for d in range(len(text)):
#         if letter_2 == text[d]:
#             stop = d
#             break
# if start < stop:
#     print(text[start:stop])
# else:
#     print("Something wrong!!! lul :>)\_-.-_/")
#
# text = "abracadabra"
# start = 0
# stop = 0
# letter_1 = input("Enter letter =  ")
# letter_2 = input("Enter letter =  ")
# if letter_1 and letter_2 in text:
#     for i in range(len(text)):
#         print(f"{letter_1} = {text[i]} ,  {i}")
#         if letter_1 == text[i]:
#             for d in range(i, len(text)):
#                 if stop == text[d]:
#                     print(text[i:d+1])
#                     break
#             break
#
# for i in range(1, 10):
#     for b in range(1, 10):
#         print(i * b)
#
# size = int(input("Size = "))
# for i in range(1, size + 1):
#     for b in range(1, size + 1):
#         print(i * b, end="\t")
#     print()
#
# PRICE = 0.4
# sms = input("Enter text:\n-->  ")
# cost = 0
# for i in range(len(sms)):
#     cost += PRICE
# print(f"{cost} --> hohlobaksiv$")
#
# text = "abracadabra"
# for i in text:
#    if i == "a":
#        i = "*"
#    print(i)
##############################################################################
###################################################  DAY - 6    ##############
##############################################################################
# storage = [1, 2, 5, 6, 7, 9]
# sum = 0
# for i in storage:
#     sum += i
# print (sum)
#
# text = r"C\\lemko\Documents"
# print(text)
#
# print(ord("A"))
# print(ord("a"))
# print("Ab" > "Cd")
#
# text = "Hello"
#
# print(text.upper())
# print(text.lower())
#
# user_input = input("Enter text: ")
# if user_input.lower() == "hi":
#     print("Work!")
#
# text = "1234"
# if text.isdigit():
#     print("Work!")
#
# x = input("Enter num: ")
# y = input("Enter num: ")
#
# if x.isdigit() and y.isdigit():
#     print(int(x) + int(y))
# else:
#     print("Something goes wrong !")
#
# text = "abc"
# qqq = "123"
#
# res = text.join(qqq)
# print(res)
#
# text = "123-456-789"
# text = text.replace("-", "a")
# print(text)
#
# text = "shlak"
# print(text.find("l"))
#
# text = "lo lo lo shka"
# print(text.count("lo"))
#
# text = "Welcome1good2morning3people"
# form_text = " "
# for i in text:
#     if not i.isdigit():
#         form_text += i
# print(form_text)
#
# import random
# rand_text = random.choice(["Apple", "Keyboard", "Moon", "Assassin"])
# rand_text_copy = rand_text
# guessed_word = ""
# print(len(rand_text) * "*")
# while True:
#     answer = input("Enter letter: ")
#     if guessed_word.find(answer) != -1:
#         print("You already try this latter!")
#         continue
#     if answer in rand_text:
#         rand_text = rand_text.replace(answer, '*')
#         guessed_word += answer
#     tmp_word = ""
#     for i in range(len(rand_text)):
#         if rand_text[i] == "*":
#             tmp_word += rand_text_copy[i]
#         else:
#             tmp_word += "*"
#     if tmp_word == rand_text:
#         break
#     print(tmp_word)
#
# list_values = [1, 2, 3]
# list_values_2 = list([1, 2, 3])
#
# print(list_values == list_values_2)
#
# list_values = [1, 2, 3, "hello", True, 4.15]
# for value in list_values:
#     print(type(value))
#
# for i in range(len(list_values)):
#     print(list_values[i])
#
# for i in range(len(list_values)):
#     print(f"Index = {i}\tValue = {list_values[i]}")
#
# i = 0
# while i < len(list_values):
#     print(list_values[i])
#     i += 1
#
# a = [5, 7, 9] * 3
# print(a)
#
# a = [5, 7, 9]
# x, y, z = a
# print(x)
# print(y)
# print(z)
#
##############################################################################
###################################################  DAY - 7    ##############
##############################################################################
#
# lst = [False, "hello", 13, False]
# lst.append(3.14)
#
# print(*lst)
#
# lst.insert(0, "text")
# print(*lst)
#
# lst_2 = [13, "hi"]
#
# # lst = lst + lst_2
# lst.extend(lst_2)
# print(*lst)
#
# value = 13
# if value in lst:
#     lst.remove(value)
# else:
#     print("Not found!")
# print(*lst)
#
#
# value = "hello"
# if value in lst:
#     print(lst.index(value))
#
# deleted_value = lst.pop()
# print(*lst)
# print(deleted_value)
#
# deleted_value = lst.pop(3)
# print(*lst)
# print(deleted_value)
#
# value = lst.count(False)
# print(value)
# print(len(lst))
#
# lst.clear()
#
# lst = [13, 7, -2, 10, 50]
#
# print(min(lst))
# print(max(lst))
#
# lst.sort(reverse=True)
# print(*lst)
#
# x = sorted(lst)
# print(*x)
#
# lst = [0, 4, 8]
# # x = lst
# x = lst.copy()
# #x = list(lst)
# lst[0] = "Hello"
# print(*lst)
# print(*x)
#
# lst = input("Enter digit`s with space:  ")
# lst = lst.split()
# print(sorted(lst, reverse=True))
# lst = [int(value) for value in input().split()]
# lst = sorted(lst, reverse=True)
# print(*lst)
#
#
# text = "abracadabra"
# lst = list(text)
# lst[0] = "!"
# lst[6] = "*"
# print(*lst)
#
# text = "".join(lst)
# print(text)
# lst = ["Carrot", "Milk", "Potato"]
# lst_2 = input("Enter product`s list:  ").split()
# lst_2 = list(lst_2)
# # lst = lst + lst_2
# lst.extend(lst_2)
# print(*lst)
#
# lst = ["Carrot", "Milk", "Potato"]
# lst_2 = input("Enter product`s list:  ").split()
# lst_2 = list(lst_2)
# lst_2.extend(lst)
# print(*lst_2)
#
# lst = ["Carrot", "Milk", "Potato"]
# lst_2 = input("Enter product`s list:  ").split()
# lst_2 = list(lst_2)
# lst_2.extend(lst)
# lst = lst_2 + lst
# print(*lst_2)
#
# mark = [int(value) for value in input("Enter mark`s list: ").split()]
# mark = sum(mark) / len(mark)
# print(round(mark, 1))
#
# field = []
# for _ in range(9):
#     field.append(-1)

# lst_field = [-1, 0, -1, 1, 0, -1, -1, 0, 1]
#
# while True:
#    for i in range(len(lst_field)):
#        if lst_field[i] == -1:
#            print(" ", end="  ")
#        elif lst_field[i] == 1:
#            print("X", end="  ")
#        else:
#            print("O", end="  ")
#
#    input()
#
##############################################################################
###################################################  DAY - 8    ##############
##############################################################################
# lst_field = []
# turn = False
# for _ in range(3):
#     lst_field.append([-1, -1, -1])
# while True:
#     for i in range(3):
#         for j in range(3):
#             if lst_field[i][j] == -1:
#                 print("-", end="  ")
#             elif lst_field[i][j] == 1:
#                 print("X", end="  ")
#             else:
#                 print("O", end="  ")
#         print()
#     choice = input("Enter Row and Col: ").split()
#     if len(choice) == 2:
#         for v in choice:
#             if not(v.isdigit()) or int(v) not in range(3):
#                 print("\n\t Invalid data!!!\n")
#                 break
#         else:
#             # MOVE`s`
#             if lst_field[int(choice[0])][int(choice[1])] == -1:
#                 lst_field[int(choice[0])][int(choice[1])] = int(turn)
#                 turn = not turn
#                 #Win Check
#                 for i in range(3):
#                     if lst_field[i][0] == lst_field[i][1] == lst_field[i][2] and lst_field[i][2] != -1:
#                         print("In a row")
#                     elif lst_field[0][i] == lst_field[1][i] == lst_field[2][i] and lst_field[2][i] != -1:
#                         print("In a col")
#                     else:
#                         #Diagonal check
#                         if lst_field[0][0] ==  lst_field[1][1] == lst_field[2][2] and lst_field[1][1] != -1:
#                             print("\n\tDiagonal win\n")
#                         elif lst_field[0][2] ==  lst_field[1][1] == lst_field[2][0] and lst_field[1][1] != -1:
#                             print("\n\tDiagonal win\n")
#                     for i in range(3):
#                         if lst_field[i][i] != -1:
#                             print("\n\tTIE!!!\n")
#             else:
#                 print("This place is already taken!!")
#     else:
#         print("\n\t Enter 2 value`s!\n")
##############################################################################
###################################################  DAY - 9    ##############
##############################################################################
# a = [1, 2, 3]
# b = (1, 2, 3)
# print(a.__sizeof__())
# print(b.__sizeof__())
# print(b[2])
# print(b[-1])
#
# c = 2, 5, 8
# print(c)
# print(type(c))
#
# d = (1, )
# e = tuple(d)
# print(id(d))
# print(id(e))
#
# print(d)
# print(type(d))
#
# a = (1, )
# b = (3, 8, 11, 8)
# c = a + b
# print(c)
# if 13 in c:
#     print(c.count(13))
# print(c.index(8))
# print(c.count(8))
# a = (True, False, 14, "Hello", [1, 2, 3, "HI"])
# print(id(a))
# a[4][0] = 999
# print(id(a))
# print(a)
#
# a += ("asd", )
# print(a)
# a = (True, False, 14, "Hello", [1, 2, 3, "HI"])
# for i, value in enumerate(a, 8):
#     print(f"Index = {i}  Value = {value}")
#
# a = tuple()
# for _ in range(4):
#     a += (input(), )
#     print(id(a))
# print(a)
#
# b = list()
# for _ in range(3):
#     b.append(input())
#     print(id(b))
# print(b)
#
# print(a.__sizeof__())
# print(b.__sizeof__())
#
# a = (3, 66, 81, )
# a += tuple(input("Enter number`s:  ").split())
# print(a)
#
# a = (3, 66, 81, )
# a += tuple(int(value) for value in input("Enter number`s:  ").split())
# print(a)
#
# a = tuple(input("Enter city`s:  ").split)
# if "Lviv" not in a:
#     a += ("Lviv", )
# print(a)
#
# a = ("a", "b", "c", )
# print(a[1:])
#
# citys = ("London", "Paris", "Kyiv", "lviv", "Odesa", "Dnipro", )
# if "Lviv" in citys:
#     i = citys.index("lviv")
#     print(citys[:i], citys[i+1:])
#
#
##############################################################################
###################################################  DAY - 10    #############
##############################################################################
# a = dict(one='hello')
# user = {
#     'name': 'Vlad',
#     'age': 13,
#     'isMarried': False,
#     'languages': ['Ukr', 'Eng', 'Spa']
# }
#
# print(user['languages'])
# if 'languages' in user:
#     print(user['languages'])
# else:
#     print('Not key')
#
# print(user.setdefault('languages'))
# user.setdefault('city', 'Lviv')
# print(user)
#
# user['test'] = 'test text'
# print(user)
#
# print(user.setdefault('a', 13))
# user['age'] = 90
#
# print(user.get('age12'))
# print(user)
#
# x = user.popitem()
# print(x[0])
# print(x[1])
# print(user)
#
# x = user.pop('age')
# print(x)
# print(user)
# for keys in user.keys():
#     print(keys)
# for value in user.values():
#     print(value)
# print(f"Keys = {keys}\t\tValue = {value}")
# user.clear()
# print(user)
#
# x = user.copy()
# print(x)
# print(id(x))
# print(id(user))
# x["age"] = 777
# print(x)
#
# a = {
#     1: "a",
#     "hi": "hello"
# }
# b = {
#     2: "b",
#     "hi": "bye"
# }
# c = a | b
# print(c)
#
# user = {
#     'name': 'Vlad',
#     'age': 13,
#     'isMarried': False,
# }
# a = user.setdefault("Lang ", ['Ukr', 'Eng', 'Spa']).append("Uru")
# print(a)
# print(user)
#
# user = {
#     'name': 'Vlad',
#     'age': 13,
#     'isMarried': False,
# }
# a = user.setdefault("Lang", ['Ukr', 'Eng', 'Spa']).append("Uru")
# res = " - ".join(user["Lang"])
# print(res)
# for value in user.values()
#     print(value)
#
# morse = {
#     1: "•----",
#     2: "••---",
#     3: "•••--",
#     4: "••••-",
#     5: "•••••",
#     6: "-••••",
#     7: "--•••",
#     8: "---••",
#     9: "----•",
#     0: "-----"
# }
# number = input("Enter numbers:  ")
# for x in number:
#     print(morse[int(x)], end=", ")
# lst = list(morse[int(x)] for x in number)
# print(" | ".join(lst))
#
# members = dict()
# for _ in range(5):
#     lst = input("Enter: ").split()
#     members.setdefault(lst[0], []).append(lst[1])
# print(members)
# for key, value in members.items():
#     print(f"{key}: {', '.join(value)}")
#
##############################################################################
###################################################  DAY - 11    #############
##############################################################################
#
# lst_users = [
#     {
#         "login": "test@ua",
#         "password": "123",
#         "nick": "Tester"
#     },
#     {
#         "login": "test_1@ua",
#         "password": "123",
#         "nick": "Tester2"
#     },
# ]
# while True:
#     choice = input("1: Login\n2: Registration\n\t-->> ")
#     if choice == "1":
#         login = input("Enter your login:  ")
#         password = input("Enter your password:  ")
#         for user in lst_users:
#             if login == user["login"] and password == user["password"]:
#                 print(f"Hello {user['nick']}")
#                 break
#         else:
#             print("User not found or incorrect data!")
#     elif choice == "2":
#         login = input("Enter your login:  ")
#         for user in lst_users:
#             if login == user["login"]:
#                 print("Login already created!\n\tTry again!")
#                 break
#         else:
#             password = input("Enter your password:  ")
#             nick = input("Enter your name:  ")
#             lst_users.append({
#                 "login": login,
#                 "password": password,
#                 "nick": nick
#             })
#             print("\tSuccess! \^-^/")
#
#
# a = set()
# b = {"Oleg", 1, "Vlad", 1}
# print(b)
# for value in b:
#     print(value)
#
# a = {1, 2, 3}
# a.add("abs")
# a.update([5, 8, 9, ("hello", "Bye")])
# print(a)
# print(a)
# a.remove(7)
# print(a)
# a.discard(3)
# print(a)
# x = a.pop()
# print(x)
# print(a)
# a.clear()
# print(a)
# a = {1, 2, 3}
# b = {3, 4, 5}
# c = a.difference(b)
# c = a.intersection(b)
# print(c)
#
# txt = input("Enter text:  ")
# a = set()
# for t in txt:
#     if t.isdigit():
#         a.add(t)
# b = sorted(a)
# if b:
#     print("Digits are missing!!")
# print(*b)
# a = sorted({int(value) for value in input() if value.isdigit()})
# print(*a)
#
##############################################################################
###################################################  DAY - 12    #############
##############################################################################
#
# def func():
#     print("Kek")
#     print("Lol")
#     print("WoW")
#
#
# func()
#
# import calendar
#
#
# def month_info():
#     imp = input("Enter month in digit:  ")
#     if imp.isdigit() and 1 <= int(imp) <= 12:
#         print(f'In {calendar.month_name[int(imp)]}, we have {calendar.monthrange(2023, int(imp))[1]}, day`s')
#
#
# month_info()
#
# def say_hello(name, age):
#     print(f"Name - {name}\nAge - {age}")
#
#
# say_hello("Cornelius", 87)
#
# def weight(weight, name):
#     print(f"Weight of {name} is {weight}")
#
#
# weight(33, "Chicken")
# def math(nums):
#     print(f"Min digit = {min(nums)}\nMax digit = {max(nums)}\nSum of digit`s = {sum(nums)}")
#
#
# math([int(value) for value in input("Enter mark`s list: ").split()])
#
# def rectange(length, height):
#     print(f"Length = {length}, height = {height}, perimetr of rectangle = {(length + height) * 2} ")
#
#
# rectange(int(input("Enter length=  ")), int(input("Enter height=  ")))
#
# import calendar
# def month_info(month):
#     if month.isdigit() and 1 <= int(month) <= 12:
#         print(f'In {calendar.month_name[int(month)]}, we have {calendar.monthrange(2023, int(month))[1]}, day`s')
#     else:
#         print("Incorrect data")
#
#
# month_info(input("Enter number of a month:  "))
#
# def edit(text, spec_symb):
#     return spec_symb + text + spec_symb
#
#
# play = edit("Heart", "♥")
# print(play)
#
# def math(num, power):
#     return num ** power
#
#
# def edit():
#     sepr = 0
#     edit = ""
#     for i in str(x):
#         edit += i
#         sepr += 1
#         if sepr in (3, 6, 9, 12):
#             edit += " "
#     print(edit)
#
#
# x = math(int(input("......")), int(input("......")))
# edit()
#
# def plus_minus(firs, second):
#     if firs > second:
#         return print(second)
#     else:
#         return print(firs)
#
#
#
# plus_minus(int(input("Enter first digit:  ")), int(input("Enter second digit:  ")))
# def plus_minus(firs, second):
#     return firs if firs < second else second
#
#
# print(plus_minus(int(input("Enter first digit:  ")), int(input("Enter second digit:  "))))
# def min_num(x, y):
#     return x if x < y else y
#
#
# x = int(input("Enter number:  "))
# y = int(input("Enter number:  "))
# z = int(input("Enter number:  "))
# res = min_num(x, y)
# print(min(res, z))
#
##############################################################################
###################################################  DAY - 13    #############
##############################################################################
#
# x = 0
#
#
# def outer():
#     x = 1
#     def inner():
#         x = 2
#         print(f"INNER = {x}")
#     inner()
#     print(f"OUTER = {x}")
#
#
# outer()
# print(f"GLOBAL = {x}")
#
#
# x = 22
#
#
# def outer():
#     global x
#     print(x)
#     x += 2
#
#
# outer()
# print(x)
#
#
# x = 0
#
#
# def outer():
#     x = 1
#     global x
#     def inner():
#         global x
#         x = 3
#         print(f"INNER = {x}")
#     inner()
#     print(f"OUTER = {x}")
#
#
# outer()
# print(f"GLOBAL = {x}")
#
#
# x = 0
#
#
# def outer():
#     global x
#     x = 1
#     def inner():
#         nonlocal x
#         x = 3
#         print(f"INNER = {x}")
#     inner()
#     print(f"OUTER = {x}")
#
#
# outer()
# print(f"GLOBAL = {x}")
#
#
# *x, y = (1, 2, 3, 4, 5, 6, 7, 8, 20, 40, 156)
#
# print(f"x = {x}")
# print(f"y = {y}")
#
# x, *y = (1, 2, 3, 4, 5, 6, 7, 8, 20, 40, 156)
#
# print(f"x = {x}")
# print(f"y = {y}")
#
#
# *x, y = "Hello"
#
# print(f"x = {x}")
# print(f"y = {y}")
#
# x, *y = "Hello"
#
# print(f"x = {x}")
# print(f"y = {y}")
#
#
# a = 1, 2, 3, 4
# q = [54, "Hello", True, 3424]
# b = (a, )
# c = (*a, *q, )
# print(b)
# print(c)
#
#
# a = -2, 4print(range(a))  #не працює
# print(range(*a)) #розпаковане і працює
# print([*range(*a)])
# print(*[*range(*a)])
#
#
# *lst, a, b, c = [1, 2, 3, 4, 5, 6]
# print(*lst)
# *lst, a, b, c = [int(x) for x in input().split()]
# print(*lst)
#
#
# def func(c, a, b):
#     print(f"A = {a}, B = {b}, C = {c}")
#
#
# func(b=3, a=8, c="Hello")
#
#
# def func(a, name, ):
#     print(f"A = {a}, C = {name}")
#
#
# func(input("Age:  "), name="Hello")
#
#
# def func(a, b="Lol"):   #<--- Formal
#     print(f"A = {a}, B = {b}")
#
#
# func(18, "Kek") #<--- Fact або наоборот
#
#
# def func(x, y, operation=False):
#     if operation:
#         return x + y
#     return x - y
#
#
# print(func(27, 9))
#
#
# def func(arg1, agr2, *arg3):
#     print(f"A = {arg1}, B = {agr2}, C = {arg3}")
#
#
# func(12, 17, 18, "Hello", "Bye", False, 12, "KeK")
#
#
# def func(num, lst=[]):
#     lst.append(num)
#     return lst
#
#
# x = func(5)
# x = func(6)
# x = func(10)
# print(x)
#
#
# def func(num, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(num)
#     return lst
#
#
# x = func(5)
# x = func(6)
# x = func(10)
# print(x)
#
#
# def func(num, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(num)
#     return lst
#
#
# x = func(10, [1, 5])
# print(x)
#
#
# def func(x ,*args ,**kwargs):
#     print(x)
#     print(args)
#     print(kwargs)
#
#
# func(15, 16, 17, "kek" ,name="Kek", age=20, city="London")
#
#
# def func(*args ,x ,**kwargs):
#     print(x)
#     print(args)
#     print(kwargs)
#
#
# func(15, 16, 17, "kek", x="LoL",name="Kek", age=20, city="London")
#
#
# def func(*args, x, y, state=False ,**kwargs):
#     print(args, kwargs)
#
#
# func("kek", 15, 18, x=49, y=16, state=False, name="Jack", age="100",city="London")
#
#
##############################################################################
###################################################  DAY - 14    #############
##############################################################################
#
#
# x = lambda a, b: a + b
# print(x(1, 6))
#
# if lambda: 3 + 6 < 15:
#     print("Work")
#
# a = [lambda: print(input("Enter number:  ")), lambda: print("I`m lambda function")]
# for value in a:
#     value()
#
#
# def get_filtered(data, filter, lst=None):
#     if lst is None:
#         lst = []
#
#     for value in data:
#         if filter(value):
#             lst.append(value)
#
#     return lst
#
#
# a = [1, 3, 6, 4, 8, 6, 0, -12, 16, 44, 32, 33, 65]
# print(get_filtered(a, lambda num:num % 2 == 0, [77, 99]))
# print(get_filtered(a, lambda num:num > 5))
#
#
#Оголосіть анонімну функцію з одним параметром яка буде підносити число до квадрату
# x = lambda num, power:num**power
# print(x(int(input("Enter number:  ")), int(input("Enter number:  "))))
#
#
#Оголосіть анонімну функцію з двома параметрами, в якій необхідно повернути результат від ділення x на y, якщо y не ноль, в іншому випадку повертати None.
# l = lambda num_1, num_2:num_1 / num_2 if num_2 else None
# print(l(int(input("Enter digit:  ")), int(input("Enter digit:  "))))
#
#
#Оголосіть анонімну функцію з двома параметрами фактичним і формальним, фактичний для дійсного числа, формальний для цілого, який буде вказувати на к-сть знаків після коми (по замовчуванню = 1). Відобразити це форматоване число.
# l = lambda a, b=1:round(a, b)
# print(l(123.5436, 3))
#
#
#Оголосіть анонімну функцію, яка буде приймати стрічку і повертати True якщо в цій стрічці присутній фрагмент стрічки ‘or’, в іншому випадку False.
# l = lambda txt:True if "or" in txt else False
# print(l(input("Enter text:  ")))
#
#
# def rec(num):
#     print(num)
#     if num < 10:
#         rec(num + 1)
#     print(num)
#
#
# rec(1)
#
#
# def rec(num):
#     if num > 1:
#         rec(num - 1)
#     print(num)
#
# rec(15)
#
#
#Нарізати число на окремі числа, та показати їх (псс, використовуйте ділення по модулю, остачу від ділення ;) )
# def rec(num):
#     if num >= 10:
#         rec(num // 10)
#     print(num % 10)
#
# rec(31234)
#
#
# def slice_n(num):
#     if num <= 10:
#         return num
#     return num % 10 + slice_n(num // 10)
#
#
# print(slice_n(734))
#
#
# def rec(num):
#     if num == 1:
#         return 1
#     return rec(num - 1) * num
#
#
# print(rec(5))
#
#
##############################################################################
###################################################  DAY - 15    #############
##############################################################################
#
#
# def rec(num, lst=None):
#     if num < 10:
#         return [num]
#     return rec(num // 10) + [num % 10]
#
#
# print(rec(1234))
#
#
# def rec(data, lst=[]):
#     for j in data:
#         if type(j) == list:
#             rec(j)
#         else:
#             lst.append(j)
#     return lst
#
#
# rec([26, -3, ['Hello', False], [True, "Bye", [200.1, 45.12], ['recursion', [777, -321]]], 'i`m last element ;D'])
#
#
# gl = "Kek"
#
#
# def outer(text):
#     def inner():
#         print(text,gl)
#     return inner()
#
#
# x = outer("Hello")
# x()
#
#
# def counter(count=0):
#     def tick():
#         nonlocal count
#         count += 1
#         return count
#     return tick
#
#
# c_1 = counter()
# print(c_1())
# print(c_1())
# print(c_1())
#
# c_2 = counter(5)
# print(c_2())
# print(c_2())
# print(c_2())
#
#
# def add_10():
#     def func(num):
#         return num + 10
#     return func
#
#
# x = add_10()
# print(x(5))
#
#
# def add_10():
#     return lambda num: num + 10
#
# print(add_10()(10))
#
#
# def add_10(tag):
#     return lambda txt:f"<{tag}>{txt}</{tag}>"
#
# print(add_10("♥")("Hello World!"))
#
#
# def add_10(tag):
#     def func(txt):
#         return f"<{tag}>{txt}</{tag}>"
#     return func
#
# x = add_10("♥")
# print(x("Hello World!"))
#
#
#Зовнішня функція приймає в параметр text якусь стрічку, внутрішня, анонімна, стрічку чисел введених через пробіл. Якщо text буде рівний 'list', повернути список чисел, інакше кортеж чисел.
#
#
##############################################################################
###################################################  DAY - 14    #############
##############################################################################
#
#
# def func_decorator(func):
#     def wrapper():
#         print("DO BEGIN")
#         func()
#         print("DO AFTER")
#     return wrapper
#
#
# def my_print():
#     print("Func my print work!")
#
#
# @func_decorator
# def say_hello():
#     print("Hello")
#     print("Bye")
#
#
# my_print = func_decorator(my_print)
# my_print()
# say_hello()
#
#
# def func_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("DO BEGIN")
#         res = func(*args)
#         print("DO AFTER")
#         return res
#     return wrapper
#
# @func_decorator
# def my_print(text, *args, **kwargs):
#     print(f"Text is = {text}, else {args}")
#     return "New Vegas " + text
#
#
# a = my_print("GG", "WP", 666)
# print(a)
#
#
# def func_dec(func):
#     def wrapper(*args):
#         start = time.time()
#         func(*args)
#         end = time.time()
#         return f"Func time is = {end - start}"
#     return wrapper
#
#
# @func_dec
# def asd(count):
#     i = 0
#     while i < count:
#         print(i)
#         i += 1
#
#
# print(asd(10000))
#
#
#Створіть функцію з назвою get_rec_square, яка вираховує площу прямокутника за параметром width та height. Вона повертає лише результат. Створіть декоратор, який буде показувати результат у вигляді стрічки "Rectangle square = *value*".
# def deco(func):
#     def wrapper(*args):
#         #return f"Rectangle value = {func(*args)}"
#         value = func(*args)
#         print(f"Rectangle value = {value}")
#     return wrapper
#
# @deco
# def get_rec_square(width, height):
#     return width * height
#
#
# get_rec_square(int(input("Enter width:  ")), int(input("Enter height:  ")))
#
#
#Створити функцію, яка приймає перелік продуктів в одну стрічку через пробіл, ця функція перетворює цю стрічку у список продуктів, та повертає його. Створіть декоратор, який виведе перелік продуктів у форматі:
# def deco(func):
#     def wrapper(*args):
#         for index, value in enumerate(func(*args), 1):
#             print(f"{index}. {value.capitalize()}")
#     return wrapper
#
# @deco
# def products(text):
#     return text.split()
#
#
# products(input("Enter product`s:  "))
#
#
#Користувач вписує числа в одну стрічки через пробіл, створіть функцію convert_to_list, яка буде приймати цю стрічку та повертати список чисел. Використовуючи декоратор, відсортуйте ці числа по зростанню, та відобразіть їх.
# from functools import wraps
#
#
# def deco(func):
#     @wraps(func)
#     def wrapper(*args):
#             print(sorted(func(*args)))
#     return wrapper
#
# @deco
# def conver_to_lst(text):
#     """"This is cover_to_lst function"""
#     return [int(v) for v in text.split()]
#
#
# conver_to_lst(input("Enter number`s:  "))
# print(conver_to_lst.__doc__)
# print(conver_to_lst.__name__)
#
#
# def abc():
#     """"This is idk function"""
#     print("I don`t know")
#
#
# print(abc.__doc__)
# print(abc.__name__)
#
#
# def deco(new_text):
#     def wrapper(func):
#         def inside(*args):
#             print(f"{new_text},  {func(*args)}")
#         return inside
#     return wrapper
#
#
# @deco(new_text="It`s some new text")
# def abc(text):
#     return text
#
#
# abc(input())
#
#
#Вводиться стрічки цілих чисел через пробіл, функція перетворює цю стрічку у список чисел, та повертає їхню суму.
#Створити декоратор з одним параметром name, його використовуємо для формування стрічки "{name} = {сума_чисел}, поверніть її, відобразіть її.
#
#
# def deco(name="It`s some text"):
#     def wrapper(func):
#         def inside(*args):
#             print(f"{name} = {func(*args)}")
#         return inside
#     return wrapper
#
#
# @deco("It`s sum of numbers")
# def abc(nums):
#     return sum([int(value) for value in nums.split()])
#
#
# abc(input("Enter number`s to plus with space:  "))
##a = deco(input("Enter some name:  "))(abc)
##a(input("Enter number`s to plus with space:  "))
#
#
##############################################################################
###################################################  DAY - 15    #############
##############################################################################
#
#
# def outer(func):
#     def f1(a):
#         def f2(b):
#             func(a, b)
#         return f2
#     return f1
#
#
# def my_p(a, b):
#     print(f"A = {a}\nB = {b}")
#
#
# my_p("Hello", "World")
# my_p("Hello", "People")
# my_p("Hello", "Some text")
#
# print("***************")
#
# x = outer(my_p)("Hello")
# x("World")
# x("People")
# x("Some text")
#
#
# def outer(func):
#     def f1(f_name):
#         def f2(l_name, age=None):
#             def f3(age):
#                 res = func(f_name, l_name, age)
#                 return res
#             return f3
#         return f2
#     return f1
#
#
# def my_p(f_name, l_name, age):
#     return f"Your first name - {f_name}\nYour lats name is - {l_name}\nYour age - {age}"
#
#
# f, l, a = input("Enter you`r first name:  "), input("Enter you`r last name:  "), input("Enter you`r age:  ")
# print(outer(my_p)(f)(l)(a))
#
#
# a^2 + 2ab + b^2
#
# def divide(func):
#     def f1(a):
#         def f2(b):
#             res = func(a,b)
#             return res
#         return f2
#     return f1
#
#
# def math(a, b):
#     return a**2 + 2*a*b + b**2
#
#
# f, s = 5, 7
# print(divide(math)(f)(s))
#
#
# from functools import partial
#
#
# def math(a, b):
#     return a**2 + 2*a*b + b**2
#
# x = partial(math, a=3)
# print(x(b=4))
#
# x = partial(math)
# print(x(b=4, a=3))
#
#
# x = list(map(int, input().split()))
# print(x)
# y = tuple(map(lambda x: x+2, input().split()))
# print(y)
#
#
# res = map(lambda x: x + "a", "Hello")
# for _ in range(5):
#     print(next(res))
#
#
# lst = iter([5, 7, 8])
# print(lst)
# print(next(lst))
# print(next(lst))
# print(next(lst))
#
#
#Користувач вводить дійсні числа в одну стрічку через пробіл. За допомогою функції map перетворити їх в дійсні числа, та відобразити лише перші 2, за умову що буде введено як мінімум 2.
#
#
# lst = list(map(float, input().split()))
# if len(lst) >= 2:
#     print(lst[1], lst[2])
#
#
# lst = map(float, input().split())
# for _ in range(2): print(next(lst))
#
#
#Користувач вводить цілі числа в одну стрічку через пробіл (як від'ємні, так і додатні), за допомогою функції map, перетворіть цю стрічку в список цілих чисел по модулю
# s = "-4 -6 4 3 1 -2 56 -76"
#
#
# def a(val):
#     return abs(int(val))
#
#
# print(*list(map(a, s.split())))
# print(*list(map(lambda x: abs(int(x)), s.split())))
#
#
# a = "aaa=111 bbb=222 ccc=333 ddd=444"
# print(tuple(map(lambda v: tuple(v.split("=")), a.split())))
#
#
# a = [3, 5, 6, 9, 10, 15, 30, 46, 13 ,5]
# res =list(filter(lambda x: x >= 10, a))
# print(res)
#
#
# c = "Lviv Odessa Kharkiv Kyiv Dnipro London Pitsburg Amsterdam Paris"
# res = list(filter(lambda x: len(x) > 5, c.split()))
# print(*res)
#
# c = "Lviv Odessa Kharkiv Kyiv Dnipro London Pitsburg Amsterdam Paris"
# res = filter(lambda x: len(x) > 5, c.split())
# for _ in range(6): print(next(res))
#
#
# n = "1 7 5 8 35 2 15 47 23 15 -1 -2 -3 -4 -12 -32 -54"
# res = list(filter(lambda x: len(x) == 2, input().split()))
# print(*res)


##############################################################################
###################################################  DAY - 16    #############
##############################################################################


# a = [1, 2, 3, 4]
# b = [6, 7, 8, 9]
# c = list(zip(a, b))
# print(c)


# lst_name = ["Vlad", "Oleg", "Stephan"]
# lst_phones = ["789", "332", "228", "1337"]
# lst_age = [23, 56, 44]
# c = tuple(zip(lst_name, lst_phones, lst_age))
# print(c)


# lst_1 = [3, 5, 7, 9]
# lst_2 = [2, 4, 6, 8]
# res = list(map(lambda v: v[0] * v[1], zip(lst_1, lst_2)))
# print(*res)


# a = [1, 2, 3, 4]
# b = [6, 7, 8, 5, 7]
# c = [10, 11, 15, 22]
# d = [5, 10, 13]
# res = zip(a, b, c, d)
# for v in zip(*res):
#     print(*v)


# from functools import reduce
#
#
# def dod(x, y):
#     print(f"x = {x}\ty = {y}")
#     return x + y
#
#
# res = reduce(dod, (1, 3, 4, 5, 6, 7, 9))
# print(res)
# res_1 = reduce(lambda a, b: a * b, [3, 6, 9, 12])
# print(res_1)


# txt = input("Enter txt:  ").split()
# res = reduce(lambda a, b: a + " " + b, txt)
# print(res)


# res = reduce(lambda a, b: a * b, range(1,int(input("Enter num:  ")) + 1))
# print(res)

#### DAY - 8
# from random import choice
#
#
# lst_guess_word = ["слово", "криза", "папір", "кавун"]
#
#
# def check_word_decoartor(func):
#     def wrapper(*args, **kwargs):
#         print(args)
#         print(func(*args, **kwargs))
#     return wrapper
#
#
# @check_word_decoartor
# def check_word(guess, answer):
#     if guess == answer:
#         return True
#     return False
#
#
# lives = 6
# while lives > 0:
#     rand_word = choice(lst_guess_word)
#     print(rand_word)
#     user_answer = input("Введіть слово:  ")
#     res = check_word(guess=rand_word, answer=user_answer)


##############################################################################
###################################################  DAY - 17    #############
##############################################################################


# from random import choice


# lst_guess_word = ["слово", "криза", "папір", "кавун", "вітер", "корма", "форма"]


# def check_word_decoartor(func):
#     used_words = []
#     def wrapper(*args, **kwargs):
#         nonlocal used_words
#         if kwargs["answer"] in used_words:
#             return True
#         used_words += [kwargs["answer"]]
#         if func(*args, **kwargs):
#             return kwargs["answer"]
#         return False
#     return wrapper


# @check_word_decoartor
# def check_word(guess, answer, *args, **kwargs):
#     if guess == answer:
#         return True
#     return False


# def translate_decorator(func):
#     txt = ""
#     def wrapper(*args, **kwargs):
#         nonlocal txt
#         for zna in zip(kwargs["answer"],kwargs["guess"]):
#             if zna[0] == zna[1]:
#                 txt += "+"
#             else:
#                 if zna[0] in kwargs["guess"]:
#                     txt += "*"
#                 else:
#                     txt += "-"
#         print(" ".join(kwargs["answer"]))
#         print(" ".join(txt))
#         txt += "\n"
#         func(*args, **kwargs)
#     return wrapper


# @translate_decorator
# def translate(answer, **kwargs):
#     return answer.lower(), kwargs


# lives = 6
# rand_word = choice(lst_guess_word)
# while lives > 0:
#     user_answer = input("Введіть слово:  ")
#     if len(user_answer) == 5:
#         res = check_word(guess=rand_word, answer=user_answer, lst_guess_word=lst_guess_word)
#     else:
#         print("\nДовжина слова не рівна 5-ти символам\n")
#         continue
#     if type(res) is not bool:
#         lst_guess_word.remove(res)
#         print(f"\n\n\t\t♥♥♥ CONGRATULATION ♥♥♥\n\n")
#         break
#     elif res:
#         print(f"\nВи вже використовували це слово {user_answer}\n")
#         continue
#     translate(answer=user_answer, guess=rand_word)
#     lives -= 1
#     print(f"\nУ вас залишилось {lives} спроб\n")


##############################################################################
###################################################  DAY - 18    #############
##############################################################################


# from random import randint


# def generate_lst():
#     l = []
#     for _ in range(21):
#         while True:
#             rand_num = randint(-10, 10)
#             if rand_num not in l:
#                 l.append(rand_num)
#                 break
#     return l


# def bubble_sort(lst):
#     for i in range(len(lst)):
#         for j in range(1, len(lst) - i):
#             if lst[j - 1] > lst[j]:
#                 lst[j - 1], lst[j] = lst[j], lst[j - 1]
#     return lst


# data = generate_lst()
# print(data)
# print(bubble_sort(data))


# def generate_lst():
#     l = []
#     for _ in range(21):
#         while True:
#             rand_num = randint(-10, 10)
#             if rand_num not in l:
#                 l.append(rand_num)
#                 break
#     return l
#
#
# def selected_sort(lst):
#     for i in range(len(lst) - 1):
#         min_n = i
#         for j in range(i + 1, len(lst)):
#             if lst[min_n] > lst[j]:
#                 min_n = j
#         lst[i], lst[min_n] = lst[min_n], lst[i]
#     return lst
#
#
# data = generate_lst()
# print(data)
# print(selected_sort(data))


##############################################################################
###################################################  DAY - 19    #############
##############################################################################


# from random import randint
#
#
# def generate_lst():
#     lst = []
#     for _ in range(21):
#         while True:
#             rand_num = randint(-10, 10)
#             if rand_num not in lst:
#                 lst.append(rand_num)
#                 break
#     return lst
#
#
# lst = generate_lst()
# srtd = sorted(lst)
# print(lst)
#
# x = int(input("Enter digit to find:  "))
#
#
# def binary_serch(lst, x):
#     low = 0
#     high = len(lst) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if x == lst[mid]:
#             return mid
#         elif x > lst[mid]:
#             low = mid + 1
#         elif x < lst[mid]:
#             high = mid - 1
#     return None
#
#
#
# print(binary_serch(srtd, x))

# print("a")
# print("b")
# "Hello"[10]
# print("d")
# print("c")

# print("a")
# print("b")
# try:
#     "Hello"[10]
# except IndexError:
#     print("Incorrect data!")
# print("d")
# print("c")


# while True:
#     try:
#         a = int(input("--->"))
#     except ValueError:
#         print("ENTER NUMBERS")
#     else:
#         print(f"-..){a}(..-")
#         break

# b = [1, "helen", 2, True, 3, 4, 5, False, 6, 7, 8, 9]
#
#
# while True:
#     try:
#         a = int(input("--->"))
#     except ValueError:
#         print("ENTER NUMBERS (-.-)")
#     else:
#         try:
#             print(f"-..){b[a]}(..-")
#         except IndexError:
#             print("Wack Index")
#             break

# while True:
#     try:
#         a = int(input("--->"))
#         print(f"-..){b[a]}(..-")
#         break
#     except ValueError:
#         print("ENTER NUMBERS (-.-)")
#     except IndexError:
#          print("Number is TOOOOO BIIIGGGG!!!")

# file = open("123.txt", encoding="utf-8")
# res = file.read()
# res = file.readline()
# res = file.readlines()
# print(res)

##############################################################################
###################################################  DAY - 20    #############
##############################################################################


# file = open("123.txt", encoding="utf-8")

# res = file.read()
# print(res)
# res = file.readlines()
# print(res)

# print(file.tell())
# file.readline()
# print(file.tell())
# file.readline()
# print(file.tell())
#
# file.seek(1)
# res = file.readline()
# print(res)
#
# file.close()


# try:
#     file = open("123.txt", encoding="utf-8")
#     try:
#         res = file.read()
#         print(res)
#     except ValueError:
#         print("File data not numeric")
#     finally:
#         file.close()
# except FileNotFoundError:
#     print("File not found")


# try:
#     with open("123.txt", encoding="utf-8") as file:
#         res = file.read()
#         try:
#             print(int(res))
#         except ValueError:
#             print("File data not numeric")
# except FileNotFoundError:
#     print("File not found")


# try:
#     with open("test.txt", encoding="utf-8") as file:
#         try:
#             country = file.readline()
#             capital = file.readline()
#             much = file.readline()
#             neighbors = file.readline()
#             space_skip = file.readline()
#             print(f"Country = {country}Capital = {capital}Population = {much}Neighbors = {neighbors}")
#         except ValueError:
#             print("File data not numeric")
# except FileNotFoundError:
#     print("File not found")


# try:
#     with open("test.txt", encoding="utf-8") as file:
#         try:
#             res = file.read().split("\n")
#             for i in res:
#                  print(f" -- = =  {i}")
#         except ValueError:
#             print("File data not numeric")
# except FileNotFoundError:
#     print("File not found")


# try:
#     with open("test.txt", encoding="utf-8") as file:
#         data = tuple()
#         for value in file.read().split("\n\n"):
#             res = value.split("\n")
#             data += ({
#                 "country": res[0],
#                 "capital": res[1],
#                 "population": float(res[2]),
#                 "neighbors": res[3].split(),
#                      },)
# except FileNotFoundError:
#     print("File not found")


# try:
#     with open("test.txt", "w", encoding="utf-8") as file:
#         file.write("123")
#         file.write("asd")
#         file.write("***")
#         file.seek(0)
#         file.write("!!!")
#         file.seek(3)
#         file.write("$$$")
# except FileNotFoundError:
#     print("File not found")


# try:
#     with open("test.txt", "a", encoding="utf-8") as file:
#         file.write(input("Enter text:  ") + "\n")
# except FileNotFoundError:
#     print("File not found")


# try:
#     with open("test.txt", "a+", encoding="utf-8") as file:
#         file.write(input("Enter text:  ") + "\n")
#         file.seek(0)
#         res = file.read()
#         print(res)
# except FileNotFoundError:
#     print("File not found")
#
#
##############################################################################
###################################################  DAY - 21    #############
##############################################################################

# import pickle


# x = ["Hello", 1234, False, 6.324, ["asd", "dsa"], {12: "value"}]
# x = {
#     "W": ["Kira", "Vira", "Ira", "Fira"],
#     "M": ["Oleg", "Stepan", "Oven", "Sheep"]
#      }
#
# with open("abc123.bin", "wb") as file:
#     pickle.dump(x, file)
#
# with open("abc123.bin", "rb") as file:
#     for key, value in pickle.load(file).items():
#         print(f"{key=} {value=}")

# x = [1, 3, 5, 6, 12, 3, 4, 2, 7, 9, 12, 16, 23]
#
# with open("abc123.pkl", "wb") as file:
#     pickle.dump(x, file)
#
#
# with open("abc123.pkl", "rb") as file:
#     res = list(filter(lambda v: v < 10, pickle.load(file)))
#
# with open("abc123.pkl", "wb") as file:
#     pickle.dump(res, file)
#
#
# with open("abc123.pkl", "rb") as file:
#     data = pickle.load(file)
#     print(data)
#
# a = ["a", "b", "c"]
# b = {
#     "v": "v",
# }
# c = 9
#
#
# with open("abc123.bin", "wb") as file:
#     pickle.dump(a, file)
#     pickle.dump(b, file)
#     pickle.dump(c, file)
#
#
# with open("abc123.bin", "rb") as file:
#     a = pickle.load(a, file)
#     b = pickle.load(b, file)
#     c = pickle.load(c, file)
#
#
# print(a, b, c, sep="\n")


# import pickle
# from random import randint
#
#
# gues_number = randint(1, 100)
# points = {
#     "player1": 0,
#     "player2": 0,
# }
# switch = True
# while True:
#     if switch:
#         with open("abc123.bin", "wb") as file:
#             pickle.dump(gues_number, file)
#         switch = False
#     player1 = int(input("First player enter number from 1 to 100:  "))
#     player2 = int(input("Second player enter number from 1 to 100:  "))
#     with open("abc123.bin", "rb") as file:
#         res = pickle.load(file)


# def num_validation(num):
#     if num <= 0 or num > 100:
#         return True
#     return False
#
#
# def game_start(data):
#     choice = 2
#     if len(data.keys()) != 1:
#         choice = int(input("1)Continue game\n2)New game\nEntere here: ..."))
#         if choice == 2:
#             data = ({
#                         "round": 1,
#                     }, file)
#     if choice == 2:
#         for x in range(1, 3):
#             data[input(f"User {x}, enter yr name:  ")] = 0
#
#
# try:
#     with open("num_game.pkl", "rb") as file:
#         data = pickle.load(file)
# except FileNotFoundError:
#     with open("num_game.pkl", "wb") as file:
#         pickle.dump({
#             "round": 1,
#         }, file)
#     with open("num_game.pkl", "rb") as file:
#         data = pickle.load(file)
#
#
# def check_win(data):
#     if list(data.keys())[1] == list(data.keys())[2]:
#         print("\n\tDRAW!!!")
#     elif list(data.keys())[1] > list(data.keys())[2]:
#         print(f"\n\tUser {list(data.keys()[1])} Win!")
#     elif list(data.keys())[1] < list(data.keys())[2]:
#         print(f"\n\tUser {list(data.keys()[2])} Win!")
#     return {"round": 1,}
#
#
# game_start(data)
# rand_number = randint(1, 100)
# while True:
#     try:
#         num_user_1 = int(input("Enter number in range 1 - 100:  "))
#         num_user_2 = int(input("Enter number in range 1 - 100:  "))
#         if num_validation(num_user_1) or num_validation(num_user_2):
#             raise ValueError
#     except ValueError:
#         print("Error. Enter number decimal number in range 1 - 100!")
#         continue
#     if data["round"] == 6:
#         print("End game 5 rounds done!!")
#         data = check_win(data)
#     elif abs(num_user_1 - rand_number) < abs(num_user_2 - rand_number):
#         print(f"{list(data.keys())[1]} Win!\n")
#         data[list(data.keys())[1]] += 1
#     elif abs(num_user_1 - rand_number) > abs(num_user_2 - rand_number):
#         print(f"{list(data.keys())[2]} Win!\n")
#         data[list(data.keys())[2]] += 1
#     else:
#         print("TIE!\n")
#     data["round"] += 1
#     with open("num_game.pkl", "wb") as file:
#         pickle.dump(data, file)
#     print(data)

##############################################################################
###################################################  DAY - 24    #############
##############################################################################


# class Brush:
#     color = "Black"
#     size = 3
#
#
# print(Brush.color)
# print(Brush.size)
# a = Brush()
# setattr(Brush, "hardness", 100)
# print(Brush.hardness)
# print(a.color)
# print(a.size)
#
# a.color = "red"
#
# print(a.color)
# print(Brush.__dict__)
# print(a.__dict__)
#
# print(getattr(Brush, 'qaz', None))
#
# if hasattr(Brush, "color"):
#     del Brush.color
#
# print(Brush.__dict__)


# class Brush:
#     color = "Black"
#     size = 3
#     def __init__(self, hardness=0):
#         print("DEF Work!")
#         self.hardness = hardness
#
#     def __del__(self):
#         print("DEL Work!")
#
#     def get_brush_setting(self):
#         print("This method  =", self)
#
#     def set_brush_hardness(self, hardness):
#         self.hardness = hardness
#
#     def get_brush_hardness(self):
#         return f"Your brush hardnes = {self.hardness}"
#
#
# a = Brush()
# # b = Brush()
# a.get_brush_setting()
# a.set_brush_hardness(73)
# print(a.get_brush_hardness())
# # b.set_brush_hardness(14)
# # print(b.get_brush_hardness())
#
# a = 3
# print(f"A = {a}")

#Написати клас "Студент", який містить властивості: "ім'я", "прізвище", "вік" та "середній бал". Додати метод для виведення інформації про студента та метод для обчислення стипендії в залежності від середнього балу.

# class Student:
#     def __init__(self, first_name="Empty", last_name="Empty", age=0, avgm=0):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.avgg = avgm
#
#     def gets_student_info(self):
#         print(f"Student first name = {self.first_name}"
#               f"\nStudent last name = {self.last_name}"
#               f"\nStudent age = {self.age}"
#               f"\nAverage = {self.avgg}\n\n")
#
#     def gets_student_scholar_ship(self):
#         if self.avgg > 93:
#             return print(f"{self.first_name} scholarship = 2500\n")
#
#         elif 74 < self.avgg:
#             return print(f"{self.first_name} scholarship = 1700\n")
#
#         else:
#             return print(f"{self.first_name} scholarship = 1000\n")
#
#
# student1 = Student("Vlak", "Krok", 22, 75)
# student2 = Student("Step", "Krek", 25, 45)
# student3 = Student("Ya", "Sam", 22, 95)
#
# student1.gets_student_info()
# student1.gets_student_scholar_ship()
#
# student2.gets_student_info()
# student2.gets_student_scholar_ship()
#
# student3.gets_student_info()
# student3.gets_student_scholar_ship()
#
#
##############################################################################
###################################################  DAY - 25    #############
##############################################################################


# class PersonalComputer:
#     def __init__(self, cpu, ram):
#         self.cpu = cpu
#         self.ram = ram
#
#     def __getattribute__(self, item):
#         print("__getattribute__ WORK!!")
#         if item == "cpi":
#             raise AttributeError("You can`t get this attr")
#         else:
#             return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         print("__setattr__ WORK!!")
#         if key == "tpu":
#             raise ValueError("Incorrect item type")
#         else:
#             return object.__setattr__(self, key, value)
#
#     def __getattr__(self, item):
#         return False
#
#     def __delattr__(self, item):
#         print("__delattr__ WORK!!")
#         return object.__delattr__(self, item)
#
#
# pc_1 = PersonalComputer("i5", 12)
# setattr(pc_1, "gpu", "nvidia")
# print(pc_1.ram)
# print(pc_1.abc)
#
# del pc_1.cpu
#
# print(pc_1.__dict__)
#
# print(pc_1.cpu)


# class PersonalComputer:
#     def __init__(self, uid, cpu, ram):
#         self.cpu = cpu
#         self.__ram = ram
#         self._uid = uid
#
#
# pc_1 = PersonalComputer("12345AB", "Ryzen7", 26)
# print(pc_1._uid)
# print(pc_1.cpu)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def get_x_coord(self):
#         return f"x = {self.__x}"
#
#     def set_x_coord(self, new_value):
#         self.__x = new_value
#
#
# a = Point(3, 6)
# print(a.get_x_coord())
# a.set_x_coord(20)
# print(a.__dict__)
#
# class Client:
#     def __init__(self, name, age, problem):
#         self.name = name
#         self._age = age
#         self.__problem = problem
#
#     def get_client_age(self):
#         return f"{self.name} age: {self._age}"
#
#     def get_client_problem(self):
#         return f"{self.name} problem is {self.__problem}"
#
#     def set_client_problem(self, new):
#         self.__problem = new
#
#
# client_1 = Client("Kris", 25, "DAUN")
# print(client_1.get_client_age())
# print(client_1.get_client_problem())
# client_1.set_client_problem("Brainless")
# print(client_1.get_client_problem())

# class Point:
#     description = "some text"
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if self.coord_validation(x) and self.coord_validation(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("ErrorValue!")
#
#     @staticmethod
#     def coord_validation(coord):
#         if type(coord) in (int, float):
#             return coord
#
#     @classmethod
#     def default(cls):
#         x = {
#             "x": 99,
#             "y": 98,
#         }
#         return cls(**x)
#
#     def get_x_coord(self):
#         return f"x = {self.__x}"
#
#     def set_x_coord(self, new_value):
#         self.__x = new_value
#
#     def set_coord(self, new_x, new_y):
#         self.__x = new_x
#         self.__y = new_y
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#
# a = Point(3, 6)
# print(a.get_x_coord())
# a.set_x_coord(20)
# a.set_coord(10, 15)
# a.get_coord()
# b = Point.default()
# print(b.__dict__)

# from datetime import date
#
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def get_age(cls, name, year):
#         age = date.today().year - year
#         return cls(name, age)
#
#     @staticmethod
#     def adult_validation(age):
#         return age >= 18
#
#     def get_info(self):
#         if self.adult_validation(self.age):
#             return f"Name: {self.name}\n" \
#                    f"Age: {self.age}\n"
#         else:
#             return f"Name: {self.name}\n" \
#                    f"Age: Secret data\n"
#
#
# person_1 = User.get_age("Koko", 1997)
# person_2 = User("Yeye", 17)
# print(person_1.get_info())
# print(person_2.get_info())


##############################################################################
###################################################  DAY - 26    #############
##############################################################################

# class Car:
#     def __init__(self, brand, age):
#         self.brand = brand
#         self.age = age
#
#     def get_car_info(self):
#         return f"Brand: {self.brand}\nAge: {self.age}\n\n"
#
#     def __str__(self):
#         return f"Brand: {self.brand}\nAge: {self.age}\n\n"
#
#
# bmw = Car("BNW", 1993)
# print(bmw.get_car_info())
# print(bmw)

# class Phone:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
#
#     def get_phone(self):
#         return self.__brand, self.__model
#
#
# class Person:
#     def __init__(self, name, phone=None):
#         self.__name = name
#         self.__phone = phone
#
#     def add_phone(self, brand, model):
#         self.__phone = Phone(brand, model)
#
#     def __str__(self):
#         return f"Person: {self.__name}\nPhone: {self.__phone.get_phone()}"
#
#
# p1 = Person("Orest")
# p1.add_phone("Apple", "13 Pro Max")
#
# print(p1)

# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
#
#     def get_info(self):
#         return f"Brand - {self.__brand}|Model - {self.__model}"
#
#
# class Dealership:
#     def __init__(self, name):
#         self.__dealername = name
#         self.car = None
#
#     def add_car(self, brand, model):
#         self.__car = Car(brand, model)
#
#     def __str__(self):
#         return f"| Dealership: {self.__dealername} |\n| Has: {self.__car.get_info()}| \n"
#
#
# dealr1 = Dealership("Huston")
# dealr1.add_car("Mercedes-Bens", "E300")
# print(dealr1)

# class Phone:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
#
#     def get_phone(self):
#         return self.__brand, self.__model
#
#
# class Phone:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
#
#     def get_brand(self):
#         return self.__brand
#
#     def set_brand(self, brand):
#         self.__brand = brand
#
#     def __str__(self):
#         return f"Phone: {self.__brand}, Model: {self.__model}"
#
#     brand = property(get_brand, set_brand)
#
# p1 = Phone("Iphone", "13 Pro Max")
# print(p1)
#
# p1.brand = "Samsung"
# print(p1.brand)
#
# print(p1.__dict__)

# class Phone:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
#
#     @property
#     def brand(self):
#         return self.__brand
#     @brand.setter
#     def brand(self, brand):
#         self.__brand = brand
#
#     def __str__(self):
#         return f"Phone: {self.__brand}, Model: {self.__model}"
#
#
# p1 = Phone("Iphone", "13 Pro Max")
# print(p1)
#
# p1.brand = "Samsung"
# print(p1.brand)
#
# print(p1.__dict__)

# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
#
#     def get_info(self):
#         return f"Brand - {self.__brand}|Model - {self.__model}"
#
#
# class Dealership:
#     def __init__(self, name):
#         self.__dealername = name
#         self.__car = None
#         self.__model = None
#
#     def add_car(self, brand, model):
#         self.__car = Car(brand, model)
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, model):
#         self.__model = model
#
#     def __str__(self):
#         return f"| Dealership: {self.__dealername} |\n| Has: {self.__car.get_info()}, {self.__model}| \n"
#
#
# dealr1 = Dealership("Huston")
# dealr1.add_car("Mercedes-Bens", "E300")
# dealr1.model = "S63"
# print(dealr1)


# class BankAccount:
#     __CURRENCY = {
#         "UAH": "₴",
#         "USD": "$",
#         "EUR": "€"
#     }
#     def __init__(self, balance, currency):
#         self.validation_amount(balance)
#         self.currency_validation(currency.upper())
#
#         self.__balance = balance
#         self.__currency = currency.upper()
#
#     @classmethod
#     def validation_amount(cls, balance):
#         if not isinstance(balance, (int, float)) or balance <= 0:
#             raise TypeError("Enter positive number!!")
#
#     @classmethod
#     def currency_validation(cls, currency):
#         if currency not in cls.__CURRENCY.keys():
#             raise KeyError("You should enter: UAH or USD or EUR")
#
#     @property
#     def currency(self):
#         return self.__currency
#
#     def deposite(self, deposite):
#         self.validation_amount(deposite)
#         self.__balance += deposite
#
#     def withdraw(self, withdraw):
#         self.validation_amount(withdraw)
#         if withdraw > self.__balance:
#             raise ValueError("You can`t withdraw more than you have!!")
#         else:
#             self.__balance -= withdraw
#
#     def __str__(self):
#         return f"You have {self.__balance} in {self.__currency} {self.__CURRENCY[self.currency]}"
#
#
# p1 = BankAccount(1300, "uah")
# p1.deposite(1200)
# p1.withdraw(300)
# print(p1)

##############################################################################
###################################################  DAY - 26    #############
##############################################################################

# class Brush:
#     def __init__(self, size, hardness):
#         self.__size = size
#         self.__hardness = hardness
#
    # @classmethod
    # def validation_number(cls, number):
    #     if number <= 0:
    #         raise ValueError()
#
#     @property
#     def size(self):
#         return self.__size
#
#     @size.setter
#     def size(self, size):
#         self.validation_number(size)
#         self.__size = size
#
#     @property
#     def hardness(self):
#         return self.__hardness
#
#     @hardness.setter
#     def size(self, hardness):
#         self.validation_number(hardness)
#         self.__hardness = hardness

# class Number:
#     @classmethod
#     def validation_number(cls, number):
#         if number <= 0:
#             raise ValueError()
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.validation_number(value)
#         setattr(instance, self.name, value)
#
#
#
# class Brush:
#     size = Number()
#     hardness = Number()
#
#     def __init__(self, size, hardness):
#         self.size = size
#         self.hardness = hardness
#
#
# red = Brush(20, 100)
# print(red.size)

# class B:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         setattr(instance, self.name, value)
#
#     def __delattr__(self, item):
#         delattr(self.name, item)
#
#
# class A:
#     price = B()
#     def __init__(self, price):
#         self.price = price
#
#
# x = A(30)

# class SetName:
#     @classmethod
#     def validation(cls, value):
#         if not value.isalpha():
#             raise NameError("Name should be only letters")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.validation(value)
#         setattr(instance, self.name, value)
#
#     def __delattr__(self, item):
#         delattr(self.name, item)
#
#
#
# class Person:
#     First_name = SetName()
#     Mid_name = SetName()
#     Last_name = SetName()
#     def __init__(self, First, Mid, Last):
#         self.First_name = First
#         self.Mid_name = Mid
#         self.Last_name = Last
#
#
# tip = Person("Kek", "Junior", "Wick")
# print(f"Last name: {tip.Last_name}\nFirst name: {tip.First_name}\nMid name: {tip.Mid_name} ")

# class CheckScale:
#     @classmethod
#     def validation(cls, value):
#         if value not in ("C", "K", "F"):
#             raise ValueError("Wrong scale data!!")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.validation(value)
#         setattr(instance, self.name, value)
#
#
# class CheckTemperature:
#     @classmethod
#     def validation(cls, value):
#         if not -237.15 < value < 1000.0:
#             raise ValueError("Wrong temperature data!!")
#
    # def __set_name__(self, owner, name):
    #     self.name = "_" + name
    #
    # def __get__(self, instance, owner):
    #     return getattr(instance, self.name)
    #
    # def __set__(self, instance, value):
    #     setattr(instance, self.name, value)
    #
    # def __delattr__(self, item):
    #     delattr(self.name, item)
#
# class Temperature:
#     value = CheckTemperature()
#     scale = CheckScale()
#     def __init__(self, value, scale):
#         self.value = value
#         self.scale = scale
#
#     def convert(self, to_scale):
#         if self.scale == "C":
#             if to_scale == "F":
#                 return self.value * 9 / 5 + 32
#             elif to_scale == "K":
#                 return self.value + 273.15
#         elif self.scale == "F":
#             if to_scale == "C":
#                 return (self.value - 32) * 5 / 9
#             elif to_scale == "K":
#                 return (self.value - 32) * 5 / 9 + 273.15
#         elif self.scale == "K":
#             if to_scale == "C":
#                 return self.value - 273.15
#             elif to_scale == "F":
#                 return (self.value - 273.15) * 9 / 5 + 32
#
#         raise ValueError("Wrong to_scale data!! > C | K | F <")
#
#
# t1 = Temperature(275.65, "K")
# print(t1.convert("C"))
# print(t1.__dict__)

# class Counter:
#     def __init__(self):
#         self.counter = 0
#
#     def __call__(self, step=1, *args, **kwargs):
#         print("__CALL__ work!!")
#         self.counter += step
#         return self.counter
#
#
# c1 = Counter()
# c2 = Counter()
# c2(5)
# c1()
# c1()
# c1()
# c1()
# c1()
# c2()
# print(c1())
# print(c2())

# class Pluse:
#     def __init__(self, x):
#         self.x = x
#
#     def __call__(self, y, *args, **kwargs):
#         return self.x + y
#
#
# a = Pluse(3)
# print(a(2))
#
#
# def ddble(x):
#     def inner(y):
#         nonlocal x
#         return x + y
#     return inner
#
# print(ddble(2)(3))

# class List:
#     def __init__(self, lst=[]):
#         self._lst = lst
#
#     def __call__(self, *args, **kwargs):
#         return list(filter(args[0], self._lst))
#
# a = List([1, 2, 3, 5, 6 ,8, 9, 10])
# print(a(lambda v: v % 2 == 0))

##############################################################################
###################################################  DAY - 27    #############
##############################################################################


# def deco_pow(func):
#     def inner(x, y):
#         print("BEFORE CALL")
#         res = func(x, y)
#         print(res)
#         print("AFTER CALL")
#         return res
#     return inner
#
# @deco_pow
# def power(num, step=2):
#     return num ** step
#
# print(power(2, 3))

# class MyClass:
#     def __init__(self, func):
#         self.__func = func
#
#     def __call__(self, text, symbol=" ^ ", *args, **kwargs):
#        return symbol.join(self.__func(text))
#
# @MyClass
# def some_func(txt):
#     return txt
#
# # some_func = MyClass(some_func)
# a = some_func("asdqwe", " @ ")
# print(a)

# class Wrapper:
#     __SYMBOL = ["p", "h1", "h2", "h3", "h4", "h5", "h6", "span", "❦"]
#     @classmethod
#     def validation(cls, symbol):
#         if symbol not in cls.__SYMBOL:
#             raise ValueError("Tag not allowed!!")
#
#     def __init__(self, func):
#         self.__func = func
#
#     def __call__(self, text, symbol="h1", *args, **kwargs):
#         self.validation(symbol)
#         return "<" + symbol + ">" + text + "</" + symbol + ">"
#
#
# @Wrapper
# def sender(text, symbol):
#     return text, symbol
#
# a = sender("Love all ^_^", "❦")
# print(a)

#Напишіть клас-декоратор, який перевіряє, чи передані аргументи функції є цілими числами.
# Якщо так функція вираховує суму цих двох чисел, в іншому випадку повернути текст 'Numbers must be integers!

# class PositiveNumber:
#     @classmethod
#     def validation(cls, value):
#         if type(value) != int:
#             raise ValueError("Numbers must be integers!")
#
#     def __init__(self, func):
#         self.__func = func
#
#     def __call__(self, num1, num2, *args, **kwargs):
#         self.validation(num1)
#         self.validation(num2)
#         return self.__func(num1, num2)
#
#
#
#
# @PositiveNumber
# def Summing(num1, num2):
#     return num1 + num2
#
#
# a = Summing(2, 2)
# print(a)

# class Store:
#     def __len__(self):
#         return len(self.product)
#
#     def __init__(self):
#         self.product = []
#
#     def add_product(self, name):
#         self.product.append(name)
#
#     def remove_product(self, name):
#         if name in self.product:
#             self.product.remove(name)
#         else:
#             print(f"{name} not in products list")
#
#
# store = Store()
# store.add_product("aplle")
# store.add_product("banana")
# store.add_product("orange")
# store.add_product("coconut")
# print(len(store))
# store.remove_product('coconut')
# print(len(store))

#Створіть клас "Майстер", в майстра є список автомобілів які очікують роботи
#Cтворіть клас "Автомобіль" з полями: марка, номерний знак, опис проблеми.
#Реалізуйте можливість додавати автомобілі для роботи майстру
#Задійте метод __len__ для розуміння розміру черги машин майстра.

# class Master:
#     def __len__(self):
#         print(f"\nMechanic: {self.MasterName}, have on work {len(self.cars)} car")
#         return len(self.cars)
#
#     def __init__(self, name, lst=None):
#         if lst is None:
#             lst = []
#         self.MasterName = name
#         self.cars = lst
#
#     def add_car(self, brand, licence, describe):
#         self.cars.append((brand, licence, describe))
#
#     def remove_car(self,name):
#         if name in self.cars:
#             self.cars.remove(name)
#
#
# class Car:
#
#     def __init__(self, brand, licence, describe):
#         self.brand = brand
#         self.licence = licence
#         self.describe = describe
#
#     def __str__(self):
#         return f"\nBrand: {self.brand}\nLicence plate: {self.licence}\nProblem: {self.describe}"
#
#
# car1 = Car("BMW", "BC2398CB", "Motor blow")
# car2 = Car("Mercedes", "AH1234HA", "Axel brake")
# masters = Master("David", [car2])
# masters.add_car(car1.brand, car1.licence, car1.describe)
# print(len(masters))


##############################################################################
###################################################  DAY - 28    #############
##############################################################################

# class Number:
#     def __init__(self, value, text):
#         self.value = value
#         self.text = text
#
#     def __add__(self, other):
#         return Number(self.value + other.value, other.text)
#
#     def __str__(self):
#         return f"Number: {self.value}, Text: {self.text}"
#
#
# x = Number(2, "Hello")
# y = Number(6, "hi")
# res = x + y
# print(res)

# class ShopingList:
#     def __init__(self, *args):
#         self.value = self.convert(args)
#
#     def __add__(self, other):
#         return ShopingList(self.value + other.value)
#
#     def __str__(self):
#         return f"United list: {self.value}"
#
#     def convert(self, args):
#         if isinstance(args[0], str):
#             return [value for value in args]
#         return args[0]
#
#
# x = ShopingList(["Orange", "Apple", "Pineapple"])
# y = ShopingList(["Coconut", "Milk", "Watermelon"])
# z = ShopingList("Soda", "Penguin", "Seagoul")
# b = ShopingList("Cat", "Dog", "Mouse")
# res = x + y
# res2 = z + b
# print(res)
# print(res2)


# Реалізувати програму для створення та обробки замовлень.
# Нехай ми маємо клас Order, який містить інформацію про замовлення користувачів,
# таку як список товарів та їх кількість.
# В програмі має бути можливість об’єднання двох, або більше замовлень.

# class Order:
#     def __init__(self, value):
#         self.list = value
#
#     def __add__(self, other):
#         new_order = other.list.copy()
#         for key, value in new_order.items():
#             if key in self.list:
#                 self.list[key] += value
#             else:
#                 self.list[key] = value
#
#         return Order(self.list)
#
#     def __str__(self):
#         return f"List: {self.list}"
#
#
# ordr1 = Order({"Apple": 4, "Orange":1})
# ordr2 = Order({"Apple": 2, "Coffe": 1, "Orange": 1})
# res = ordr1 + ordr2
# print(res)

## З використанням метода .get()
# class Order:
#     def __init__(self, value):
#         self.list = value
#
#     def __add__(self, other):
#         new_order = self.list.copy()
#         for key, value in other.list.items():
#             new_order[key] = new_order.get(key, 0) + value
#
#         return Order(new_order)
#
#     def __str__(self):
#         return f"List: {self.list}"
#
#
# ordr1 = Order({"Apple": 4, "Orange":1})
# ordr2 = Order({"Apple": 2, "Coffe": 1, "Orange": 1})
# res = ordr1 + ordr2
# print(res)

# class Words:
#     def __init__(self, lst, num):
#         self.lst = lst
#         self.num = num
#
#     def __getitem__(self, item):
#         return self.lst[item]
#
#     def __setitem__(self, key, value):
#         self.lst[key] = value
#
#     def __delitem__(self, key):
#         if isinstance(key, int) and key <= len(self.lst):
#             self.lst.pop(key)
#         elif isinstance(key, str):
#             self.lst.remove(key)
#
#
# a = Words([1, 2, 3, 6, "hello", 9, 15], 3)
# print(a[3])
# a[2] = 666
#
# print(a.lst)
# del a["hello"]
# print(a.lst)


# Створіть клас Menu, який міститиме словник dishes,
# де ключі - це назви страв, а значення - це об'єкти класу Dish.
# Клас Dish має містити атрибути name (назва страви), price (ціна страви) та description (опис страви).
# Ваш клас Menu має мати методи __getitem__, __setitem__ та __delitem__, які дозволять вам звертатись до страв за їх іменами,
# змінювати їх інформацію та видаляти їх з меню. Наприклад, коли користувач викличе menu['Піца Маргарита'],
# має повертатись об'єкт класу Dish, який містить інформацію про цю страву.
# Коли користувач викличе menu['Піца Маргарита'] = Dish('Піца Маргарита', 10, 'Класична італійська піца з томатним соусом та моцареллою'),
# має змінюватись інформація про страву. Коли користувач викличе del menu['Піца Маргарита'], має видалятись страва з меню.

# class Dish:
#     def __init__(self, name, price, description):
#         self.name = name
#         self.price = price
#         self.description = description
#
#     def __str__(self):
#         return f"Name: {self.name}\nPrice: {self.price}\nDescription: {self.description}"
#
#
# class Menu:
#     def __init__(self):
#         self.dishes = {}
#
#     def __getitem__(self, item):
#         return self.dishes[item]
#
#     def __setitem__(self, key, value):
#         self.dishes[key] = value
#
#     def __delitem__(self, key):
#         del self.dishes[key]

# 
# menu = Menu()
# menu['Піца Маргарита'] = Dish('Піца Маргарита', 123, 'Класична італійська піца з томатним соусом та моцареллою')
# 
# print(menu['Піца Маргарита'])


##############################################################################
###################################################  DAY - 29    #############
##############################################################################


# class Auto:
#     def __init__(self, model, color, age):
#         self.model = model
#         self.color = color
#         self.age = age
#
#     def clear_car(self):
#         print("Car was cleared")
#
#
# class Bmw(Auto):
#     def __init__(self, model, color, age, aroma=False):
#         super().__init__(model, color, age)
#         self.aroma = aroma
#
#     def clear_car(self):
#         print("Car was more cleared")
#
#
# class Audi(Auto):
#     def __init__(self, model, color, age, panorama=False):
#         super().__init__(model, color, age)
#         self.panorama = panorama
#
#
# m3 = Bmw("BMW M3", "Brown", 3)
# a6 = Audi("A6", "NardoGray", 4, True)
#
# print(a6.model)
# print(a6.color)
# print(a6.age)
# print(a6.panorama)
#
# m3.clear_car()
# a6.clear_car()


# class Parent:
#     _a = 5
#     __b = 7
#
#     def _say_hello(self):
#         print("Hello")
#
#
# class Child(Parent):
#     _a = 10
#     def get_smth(self):
#         print(self._a)
#         self._say_hello()
#
#     def get_smth2(self):
#         print(self.__b)
#
#
# class Test:
#     pass
#
#
# x = Child()
# y = Parent()
# x.get_smth()
# x.get_smth2()
#
# print(x._a)
# print(y._a)
#
# print(issubclass(Child, Parent))
# print(issubclass(Test, Parent))
# print(isinstance(x, Parent))
# print(issubclass(int, object))


# class Transport:
#     def __init__(self, name, places, wheels):
#         self.name = name
#         self.places = places
#         self.wheels = wheels
#
#     def wash(self):
#         print("Your transport is washed")
#
#     def __str__(self):
#         return f"Name: {self.name}\n"f"Place`s: {self.places}\n"f"Wheel`s: {self.wheels}\n"
#
#
# class Bus(Transport):
#     def __init__(self, name, places, wheels, stinks=False):
#         super().__init__(name, places, wheels)
#         self.stinks = stinks
#
#     @staticmethod
#     def stop_button():
#         print("!!!!Someone press STOP BUTTON!!!!")
#
#
# class Motorbike(Transport):
#     def __init__(self, name, places, wheels, type="Common"):
#         super().__init__(name, places, wheels)
#         self.type = type
#
#     @staticmethod
#     def make_whellie():
#         print("Wrom wrom")
#
#
# tata = Bus("Tata", 36, 6, True)
# honda = Motorbike("Honda", 2, 2, "Sportbike")
#
# print(tata)
# print(tata.stinks)
# print()
# print(honda)
# print(honda.type,)
#
# honda.make_whellie()
# honda.tuned = False
#
# print(honda.tuned)


# Проєкт лікарня. В програмі може бути лікар-хірург (Surgeon), та пацієнт (Patient).
# Кожен з них має обов’язкові властивості для введення: ім’я, прізвище та рік народження,
# вік задається автоматично функцією __get_age.
#В пацієнта є свої особливості, а саме:
# в нього є інформація про то, хто його лікар-хірург та проблема з якою звернулись
# В хірурга, крім наведених вище властивостей, є ще список його пацієнтів.
# Також у хірурга має бути змога додати нового пацієнта,
# переглянути своїх поточних пацієнтів та їх проблеми.
# from datetime import datetime
#
#
# class Person:
#     def __init__(self, name, last_name, year):
#         self.name = name
#         self.last_name = last_name
#         self.age = self.__get_age(year)
#
#     @classmethod
#     def __get_age(cls, value):
#         return datetime.now().year - value
#
#     def __str__(self):
#         return f"Name: {self.name} {self.last_name}, {datetime.now().year - self.age} year\n{self.age} year`s old.\n"
#
#
# class Surgeon(Person):
#     def __init__(self, name, last_name, year, lst_patient=None):
#         super().__init__(name, last_name, year)
#         if lst_patient is None:
#             lst_patient = []
#         self.patient = lst_patient
#
#     def add_patient(self, patient):
#         self.patient.append(patient)
#
#     def show_patient_info(self):
#         print(f"{self.name} have patient`s:")
#         for v in self.patient:
#             print(f"\t{v.name} {v.last_name}, {v.age} year`s, {v.complaint}")
#
#
# class Patient(Person):
#     def __init__(self, name, last_name, year, doctor, complaint):
#         super().__init__(name, last_name, year)
#         self.doctor = doctor
#         self.complaint = complaint
#
#     def show_my_doc(self):
#         print(f"Your doctor {self.doctor}")
#
#
# s1 = Surgeon("Matt", "Caricer", 1987)
# p1 = Patient("Rob", "Dilahan", 1999, s1, "Broken leg")
# p2 = Patient("Steph", "Cury", 1997, s1, "Head ace")
# p3 = Patient("Ioan", "Khrestutel", 1985, s1, "Moon walk")
# s1.add_patient(p1)
# s1.add_patient(p2)
# s1.add_patient(p3)
# print(s1)
# print(p1)
# s1.show_patient_info()


##############################################################################
###################################################  DAY - 30    #############
##############################################################################


# class Item:
#     def __init__(self, name, price):
#         print("Init from ITEM")
#         super().__init__()
#         self.name = name
#         self.price = price
#
#
# class Log:
#     log = []
#     log_id = 0
#
#     def __init__(self):
#         print("Init from LOG")
#         super().__init__("123")
#
#     def add_log(self):
#         Log.log_id += 1
#         self.log.append(f"Id: {self.log_id}, Item: {self}")
#
#
# class Log2:
#     some_text = "AbC"
#     def __init__(self):
#         print("Init from Log2")
#
#     def test(self):
#         print(self.some_text)
#
#
# class Vegetable(Item, Log, Log2):
#     def __init__(self, name, price, weight):
#         print("Init from VEGETABLE")
#         super().__init__(name, price)
#         self.weight = weight
#
#     def __str__(self):
#         return f"Vegetable: {self.name}"
#
#
# class Book(Item, Log, Log2):
#     def __init__(self, name, price, author):
#         print("Init from Book")
#         super().__init__(name, price)
#         self.author = author
#
#     def __str__(self):
#         return f"Book: {self.name}"
#
#
# veg1 = Vegetable("Onion", 0.8, 3)
# book2 = Book("Harry Poter", 20, "J.O Rolling")
# veg1.add_log()
# book2.add_log()
#
# print(Log.log)
# print(Vegetable.__mro__)
# print(Book.__mro__)
#
# veg1.test()
# book2.test()


# class Car:
#     def __init__(self, model):
#         super().__init__()
#         self.model = model
#
#     def __str__(self):
#         return "Some Car"
#
#
# class CarWash:
#     count = 0
#
#     def __init__(self):
#         print("CarWash init work!")
#
#     def wash(self):
#         CarWash.count += 1
#         print(f"Car {self} was washed")
#
#
# class Audi(Car, CarWash):
#     def __init__(self, model, wheels):
#         super().__init__(model)
#         self.wheels = wheels
#
#     def __str__(self):
#         return self.model
#
#
# class VW(Car, CarWash):
#     pass
#
#
# audi6 = Audi("A6", 4)
# vw1 = VW("Passat")
# audi6.wash()
# vw1.wash()


# class Outer:
#     a = 3
#
#     class Inner:
#         a = 10
#
#         def do_smth():
#             print("do smth from Inner")
#
#
# Outer.Inner.do_smth()
# print(Outer.a)
# print(Outer.Inner.a)


# class University:
#     def __init__(self, student: list=None, name: str="Politech"):
#         self.name = name
#         if student is None:
#             student = []
#         self.student = student
#
#     def __str__(self):
#         print(f"{', '.join(self.student)}")
#
#     class Student:
#         def __init__(self, bio, group):
#             self.bio = bio
#             self.group = group
#
#         def __str__(self):
#             return f"{self.bio=}, {self.group=}"
#
#     def add_student(self, bio, group):
#         self.student.append(self.Student(bio, group))
#
#
# u1 = University()
#
# u1.add_student("Vlad Stepaniv", "KN-13")
# u1.add_student("Ioan Pavin", "KN-33")
#
# print(u1.student)

# Система управління книгами в бібліотеці.
# Створити клас Library, який містить інформацію про книги та список користувачів,
# які беруть їх на читання. Вкладений клас Book містить інформацію про книгу
# - автора, назву, кількість сторінок тощо.
# Вкладений клас User містить інформацію про користувача - його ім'я, номер телефону, адресу тощо.

# class Library:
#     def __init__(self):
#         self.book = []
#         self.users = []
#         self.lended_books = []
#
#     def __str__(self):
#         print(f"{', '.join(self.users)}")
#
#     class Book:
#         def __init__(self, name, author, pages):
#             self.name = name
#             self.author = author
#             self.pages = pages
#
#         def __str__(self):
#             return f"Book: {self.name}, author: {self.author}, pages: {self.pages}"
#
#     class User:
#         def __init__(self, name, phone, adres):
#             self.name = name
#             self.phone = phone
#             self.adres = adres
#
#         def __str__(self):
#             return f"Name: {self.name}, phone number: {self.phone},\nadres: {self.adres}"
#
#     @classmethod
#     def validation(cls, value):
#         if value in (cls.users, cls.book):
#             return value
#         else:
#             print("User or book did not find")
#
#     def add_book(self, name, author, pages):
#         self.book.append(self.Book(name, author, pages))
#
#     def add_user(self, name, phone, adres):
#         self.users.append(self.User(name, phone, adres))
#
#     def lend_book(self, user, book):
#         if self.validation(book) is not None and self.validation(user) is not None:
#             self.lended_books.append((user, book))
#
#     def return_book(self):
#         pass
#
#     def display_book(self):
#         for num, book in enumerate(self.book):
#
#             print(f"№{num} Title: {book.name}\nAuthor: {book.author}\nPages: {book.pages}\n")
#
#     def display_user(self):
#         for user in self.users:
#             print(f"Name: {user.name}\nPhone number: {user.phone}\nAdres: {user.adres}\n")
#
#     def display_rent_book(self):
#         for rent, user in self.lended_books:
#             print()
#
#
# lib = Library()
# # b1 = Library.Book("Pirates of Caribian", "Some Dude", 200)
# # dude1 = Library.User("Vitto", "+380939393939", "Dortmund ave.RedCarpet 32")
# lib.add_user("Vitto", "+380939233939", "Dortmund ave.RedCarpet 32")
# lib.add_user("Betta", "+380939345939", "Washington, Della 12")
# lib.add_user("Frank", "+3809393123939", "Brest, Caravela 39/1")
#
#
#
# lib.add_book("Pirates of Caribian", "Some Dude", 203)
# lib.add_book("Devid", "Rosalina", 321)
# lib.add_book("Lucifer", "God Bless", 544)
# lib.add_book("Kharatel", "Mike Russo", 430)
#
# while True:
#     menu_choice = int(input("1: Lend book\n0: Exit\nEnter your choice|  "))
#     if menu_choice == 1:
#         while True:
#             lib.display_book()
#             book_index = int(input("Enter your choice: "))
#             if 0 < book_index < len(lib.book):
#                 break
#             else:
#                 print("Incorrect book!!")
#         while True:
#             lib.display_user()
#             user_index = int(input("Enter your choice: "))
#                 if 0 < user_index < len(lib.users):
#                     break
#                 else:
#                     print("Incorrect user!!")
#         lib.lend_book(lib.users[user_index], lib.book[book_index])
#     elif menu_choice == 0:
#         break


##############################################################################
###################################################  DAY - 31    #############
##############################################################################


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def sound(self):
#         return f"Default sound from Animal"
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def sound(self):
#         return f"Cat {self.name} says meaw meaw"
#
#
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def sound(self):
#         return f"Dog {self.name} says woof woof"
#
#
# lst = [Cat("Mia"), Dog("Jack")]
# for obj in lst:
#     print(obj.sound())


# class House:
#     address = "Antonovycha"
#     building = 23
#
#     def get_info(self):
#         return f"{self.address=}, {self.building=}"
#
#
# class Car:
#     brand = "VW"
#
#     def get_info(self):
#         return f"{self.brand=}"
#
#
# class Pen:
#     color = "Black"
#
#     def get_info(self):
#         return f"{self.color=}"
#
#
# lst = [House(), Car(), Pen()]
# for obj in lst:
#     print(obj.get_info())


# class Figure:
#     def area(self):
#         pass
#
#     def write_to_file(self):
#         with open("figure.txt", "a") as file:
#             file.write(f"Name: {self.__class__.__name__}\n"
#                        f"Area: {self.area()}\n\n")
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#
#
# class Circle(Figure):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return round(math.pi * self.radius ** 2, 3)
#
#
# lst = [Square(3), Circle(4), Rectangle(4, 7)]
# for obj in lst:
#     obj.write_to_file()


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.length = 0
#
#     class Node:
#         def __init__(self, element, next_node=None):
#             self.element = element
#             self.next_node = next_node
#
#
#     def append(self, element):
#         if self.head is None:
#             self.head = self.Node(element)
#             self.length += 1
#             return
#
#         node = self.head
#         while node.next_node:
#             node = node.next_node
#
#         node.next_node = self.Node(element)
#         self.length += 1
#
#     def insert(self, index: int, element):
#         if index == 0:
#             old_head = self.head
#             self.head = self.Node(element, old_head)
#             self.length += 1
#             return
#
#         i = 0
#         node = prev_node = self.head
#         while i < index:
#             prev_node = node
#             node = node.next_node
#             i += 1
#
#         prev_node.next_node = self.Node(element, node)
#         self.length += 1
#         # print(f"previous = {self.get_id(prev_node)}")
#         # print(f"node = {self.get_id(node)}")
#
    # def __delitem__(self, key: int):
    #     if key == 0:
    #         self.head = self.head.next_node
    #         self.length -= 1
    #         return
    #     i = 0
    #     node = prev_node = self.head
    #     while i < key:
    #         prev_node = node
    #         node = node.next_node
    #         i += 1
    #     prev_node.next_node = node.next_node
    #     self.length -= 1
    #     # print(f"previous = {self.get_id(prev_node)}")
    #     # print(f"node = {self.get_id(node)}")
#
#     def get_info(self):
#         if self.head is None:
#             return
#         node = self.head
#         i = 0
#         while node.next_node:
#             print(f"{i}. {self.get_id(node)}\tvalue: {node.element}\n\tnext_node={self.get_id(node.next_node)}\n")
#             i += 1
#             node = node.next_node
#         # print(f"{i}.\tvalue: {str(id(node))[5:]}\n\tnext_node={node.next_node}\n")
#         print(f"{i}. {self.get_id(node)}\tvalue: {node.element}\n\tnext_node={self.get_id(node.next_node)}\n")
#
#     @staticmethod
#     def get_id(element):
#         if element is None:
#             return None
#         return str(id(element))[5:]
#
#     def __str__(self):
#         s = "["
#         node = self.head
#         while node.next_node:
#             s += str(node.element) + ", "
#             node = node.next_node
#         s += str(node.element) + "]"
#         return s


# lst = LinkedList()
# lst.append(3)
# lst.append(10)
# lst.append("hello")
# lst.append(-2)
# lst.insert(2, 777)
# lst.get_info()
# del lst[2]
# lst.get_info()


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.length = 0
#
#     class Node:
#         def __init__(self, element, next_node=None):
#             self.element = element
#             self.next_node = next_node
#
#     def push(self, element):
#         self.head = self.Node(element, self.head)
#         self.length += 1
#
#     def pop(self):
#         if self.head is None:
#             return None
#
#         element = self.head.element
#         self.head = self.head.next_node
#         return element
#
#     def get_info(self):
#         if self.head is None:
#             return
#         node = self.head
#         i = 0
#         while node.next_node:
#             print(f"{i}. {self.get_id(node)}\tvalue: {node.element}\n\tnext_node={self.get_id(node.next_node)}\n")
#             i += 1
#             node = node.next_node
#         # print(f"{i}.\tvalue: {str(id(node))[5:]}\n\tnext_node={node.next_node}\n")
#         print(f"{i}. {self.get_id(node)}\tvalue: {node.element}\n\tnext_node={self.get_id(node.next_node)}\n")
#
#     @staticmethod
#     def get_id(element):
#         if element is None:
#             return None
#         return str(id(element))[5:]
#
#     def __str__(self):
#         s = "["
#         node = self.head
#         while node.next_node:
#             s += str(node.element) + ", "
#             node = node.next_node
#         s += str(node.element) + "]"
#         return s
#
#
# lst = LinkedList()
# lst.push(3)
# lst.push(2)
# lst.push(6)
# lst.get_info()
# res = lst.pop()
# lst.get_info()

# class Stack:
#     def __init__(self):
#         self.head = None
#         self.length = 0
#
#     class Node:
#         def __init__(self, element, next_node=None):
#             self.element = element
#             self.next_node = next_node
#
#     def push(self, element):
#         self.head = self.Node(element, self.head)
#         self.length += 1
#
#     def pop(self):
#         if self.head is None:
#             return None
#
#         element = self.head.element
#         self.head = self.head.next_node
#         return element
#
#     def get_info(self):
#         if self.head is None:
#             return
#         node = self.head
#         i = 0
#         while node.next_node:
#             print(f"{i}. {self.get_id(node)}\tvalue: {node.element}\n\tnext_node={self.get_id(node.next_node)}\n")
#             i += 1
#             node = node.next_node
#         # print(f"{i}.\tvalue: {str(id(node))[5:]}\n\tnext_node={node.next_node}\n")
#         print(f"{i}. {self.get_id(node)}\tvalue: {node.element}\n\tnext_node={self.get_id(node.next_node)}\n")
#
#     @staticmethod
#     def get_id(element):
#         if element is None:
#             return None
#         return str(id(element))[5:]
#
#     def __str__(self):
#         s = "["
#         node = self.head
#         while node.next_node:
#             s += str(node.element) + ", "
#             node = node.next_node
#         s += str(node.element) + "]"
#         return s


##############################################################################
###################################################  DAY - 31    #############
##############################################################################


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.length = 0
#
#     class Node:
#         def __init__(self, element, prev_node=None, next_node=None):
#             self.element = element
#             self.prev_node = prev_node
#             self.next_node = next_node
#
#     def append(self, element):
#         if self.head is None:
#             self.head = self.Node(element)
#             self.length += 1
#             return
#
#         node = self.head
#         while node.next_node:
#             node = node.next_node
#         node.next_node = self.Node(element, prev_node=node)
#         self.length += 1
#
#     def insert(self, index, element):
#         if index < 0 or index > self.length:
#             print("Incorrect index!")
#             return
#
#         if index == 0:
#             old_head = self.head
#             self.head = self.Node(element, next_node=old_head)
#             if old_head is not None:
#                 old_head.prev_node = self.head
#                 self.length += 1
#                 return
#
#         if index == self.length:
#             self.append(element)
#             return
#
#         node = previous_node = self.head
#         i = 0
#         while i < index:
#             previous_node = node
#             node = node.next_node
#             i += 1
#         previous_node.next_node = self.Node(element, previous_node, node)
#         node.prev_node = previous_node.next_node
#         self.length += 1
#
#     def __delitem__(self, key: int):
#         if key == 0:
#             self.head = self.head.next_node
#             self.head.prev_node = None
#             self.length -= 1
#             return
#         i = 0
#         node = previous_node = self.head
#         while i < key:
#             previous_node = node
#             node = node.next_node
#             i += 1
#         previous_node.next_node = node.next_node
#         if node.next_node is not None:
#             node.next_node.prev_node = previous_node
#         self.length -= 1
#
#     @staticmethod
#     def get_id(element):
#         if element is None:
#             return None
#         return str(id(element))[6:]
#
#     def get_info(self):
#         i = 0
#         node = self.head
#         while node.next_node:
#             print(f'{i}. {self.get_id(node)}\t value: {node.element}\n'
#                   f'\tprev_node: {self.get_id(node.prev_node)}\n'
#                   f'\tnext_node: {self.get_id(node.next_node)}')
#             i += 1
#             node = node.next_node
#         print(f'{i}. {self.get_id(node)}\tvalue: {node.element}\n'
#               f'\tprev_node: {self.get_id(node.prev_node)}\n'
#               f'\tnext_node: {self.get_id(node.next_node)}')
#
#
# lst = DoublyLinkedList()
# lst.append(5)
# lst.append(13)
# lst.append(-2)
#
# lst.get_info()
#
# lst.insert(0, "INSERT IN START")
# print("\n")
# lst.get_info()
# lst.insert(4, "INSERT IN END")
# print("\n")
# lst.get_info()
# lst.insert(2, "INSERT IN MID")
# print("\n")
# lst.get_info()


##############################################################################
###################################################  DAY - 32    #############
##############################################################################

# #FIFO (First in First out)
# class Queue:
#     def __init__(self, front=None, rear=None):
#         self.front = front
#         self.rear = rear
#         self.length = 0
#
#     class Node:
#         def __init__(self, element, next_node=None, prev_node=None):
#             self.element = element
#             self.next_node = next_node
#             self.prev_node = prev_node
#
#     def push(self, element):
#         if self.front is None:
#             self.front = self.rear =  self.Node(element)
#             self.length += 1
#             return
#
#         self.rear = self.Node(element, prev_node=self.rear)
#         self.rear.prev_node.next_node = self.rear
#         self.length += 1
#
#     def pop(self):
#         if self.length == 0:
#             return None
#
#         tmp_node = self.front
#         self.front = self.front.next_node
#         if self.length > 1:
#             self.front.prev_node = None
#         self.length -= 1
#         return tmp_node.element
#
#     @staticmethod
#     def get_id(element):
#         if element is None:
#             return None
#         return str(id(element))[6:]
#
#     def get_info(self):
#         i = 0
#         node = self.front
#         while node.next_node:
#             print(f'{i}. {self.get_id(node)}\t value: {node.element}\n'
#                   f'\tprev_node: {self.get_id(node.prev_node)}\n'
#                   f'\tnext_node: {self.get_id(node.next_node)}')
#             i += 1
#             node = node.next_node
#         print(f'{i}. {self.get_id(node)}\tvalue: {node.element}\n'
#               f'\tprev_node: {self.get_id(node.prev_node)}\n'
#               f'\tnext_node: {self.get_id(node.next_node)}')
#
#         print(f"\n\tFront = {self.get_id(self.front)}\n\tRear = {self.get_id(self.rear)}\n")
#
# lst = Queue()
# lst.push("Vlad")
# lst.push("Vika")
# lst.push("Olena")
# lst.get_info()
# print(f"{lst.pop()}\n")
# lst.get_info()
# lst.pop()


class BinaryTree:
    def __init__(self, element=None, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right

    def add(self, element):
        if self.element is None:
            self.element = element
            return

        if element < self.element:
            if self.left is None:
                self.left = BinaryTree(element)
            else:
                self.left.add(element)

        elif element > self.element:
            if self.right is None:
                self.right = BinaryTree(element)
            else:
                self.right.add(element)

    @staticmethod
    def get_id(element):
        if element is None:
            return None
        return str(id(element))[6:]

    def print_tree(self, place='root', level=0):
        print(f"[{place}]\t{level}\telement: {self.element}\t"
              f"curr: {self.get_id(self)}\t"
              f"left: {self.get_id(self.left)}\t"
              f"right: {self.get_id(self.right)}\n")
        if self.left is not None:
            self.left.print_tree(place='left', level=level + 1)
        if self.right is not None:
            self.right.print_tree(place='right', level=level + 1)


tree = BinaryTree()
tree.add(3)
tree.add(5)
tree.add(10)
tree.add(7)
tree.print_tree()
