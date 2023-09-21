# import threading

# new_lst = [int(i) for i in input("Enter your numbers: ").split()]

# def get_max():
#   res = max(new_lst)
#   print(res)

# def get_min():
#   res2 = min(new_lst)
#   print(res2)

# t1 = threading.Thread(target=get_max)
# t2 = threading.Thread(target=get_min)

# t1.start()
# t2.start()

# t1.join()
# t2.join()


# import concurrent.futures

# new_lst = [int(i) for i in input("Enter your numbers: ").split()]

# def summ(lst):
#   res_summ = sum(lst)
#   return res_summ

# def arith(lst):
#   res_arith = sum(lst)/len(lst)
#   return res_arith


# with concurrent.futures.ThreadPoolExecutor() as concur:
#   t1 = concur.submit(summ, new_lst)
#   t2 = concur.submit(arith, new_lst)

# print(t1.result())
# print(t2.result())


# import concurrent.futures

# input_path = input("Enter path:  ")

# with open(input_path, "r") as f:
#     data = f.read().split(",")

# def pair(lst):
#     res = filter(lambda f: f%2==0, lst)
#     with open("Pair", "w") as f:
#         f.write(str(res))

#     return res

# def not_pair(lst):
#     res = filter(lambda f: f%2!=0, lst)
#     with open("Not pair", "w") as f:
#         f.write(str(res))

#     return res

# with concurrent.futures.ThreadPoolExecutor() as con:
#     p1 = con.submit(pair, data)
#     p2 = con.submit(not_pair, data)


# print(p1.result())
# print(p2.result())


import concurrent.futures

path = input('Enter path: ')
word = input('Enter word: ')
with open(path, 'r') as file:
  text = file.read()
  
def find(word, text):
  res = text.find(word)
  return f"Word {word} is on {res} to {res+len(word)}"
  
with concurrent.futures.ThreadPoolExecutor() as exe:
  f = exe.submit(find, word, text)


print(f.result())