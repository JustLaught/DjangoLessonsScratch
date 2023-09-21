# import concurrent.futures


# def min_num(num_list):
#   return min(num_list)

# def max_num(num_list):
#   return max(num_list)

# if __name__ == "__main__":
#     num_list = [int(x) for x in input('Enter number: ').split()]

#     with concurrent.futures.ProcessPoolExecutor() as proc:
#         p1 = proc.submit(min_num, num_list)
#         p2 = proc.submit(max_num, num_list)
        
#         print(p1.result())
#         print(p2.result())


# import concurrent.futures

# def summ(lst):
#   res_summ = sum(lst)
#   return res_summ

# def arith(lst):
#   res_arith = sum(lst)/len(lst)
#   return res_arith

# if __name__ == '__main__':
#   numbers = [int(i) for i in input('Enter numbers: ').split()]    
        
#   with concurrent.futures.ProcessPoolExecutor() as proc:
#     t1 = proc.submit(summ, numbers)
#     t2 = proc.submit(arith, numbers)
    
#     print(t1.result())
#     print(t2.result())


# import concurrent.futures

# def process_numbers(filename):
# 	even_nums = []
# 	odd_nums = []

# 	with open(filename, 'r') as file:
# 		numbers = [int(line.strip()) for line in file.readlines()]

# 	for number in numbers:
# 		if number % 2 == 0:
# 			even_nums.append(number)
# 		else:
# 			odd_nums.append(number)
			
# 	return even_nums, odd_nums

# def write_nums(filename, numbers):
# 	with open(filename, 'w') as file:
# 		for number in numbers:
# 			file.write(str(number) + '\n')
# 	return numbers

# def main():
# 	file_path = input("Enter file path: ")

# 	with concurrent.futures.ProcessPoolExecutor() as executor:
# 		future_process = executor.submit(process_numbers, file_path)

# 		future_even = executor.submit(write_nums, 'even_nums.txt', future_process.result()[0])

# 		future_odd = executor.submit(write_nums, 'odd_nums.txt', future_process.result()[1])

# 	even_numbers = future_even.result()
# 	odd_numbers = future_odd.result()
# 	print("Кількість парних елементів: ", len(even_numbers))
# 	print("Кількість непарних елементів: ", len(odd_numbers))

# if __name__ == '__main__':
# 	main()


import concurrent.futures
  
def find(word, text):
	result = text.find(word)
	return result

if __name__ == '__main__':
	path = input('Enter path: ')
	word = input('Enter word: ')
  
	with open(path, 'r') as file:
  		text = file.read()
    

	with concurrent.futures.ProcessPoolExecutor() as proc:
		t1 = proc.submit(find, word, text)
  	
	
	print(t1.result())