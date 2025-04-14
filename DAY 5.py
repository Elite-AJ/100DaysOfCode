# Py_Loops
# Major Task
#* Password Generator
#Minor Task
#* Average Height 

# ---Minor 1 - Average Height---
student_heights = input("Input a list of student heights ").split()
height_sum = 0
height_number = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  height_sum += student_heights[n]
  height_number += 1
average_height = round(height_sum / height_number)
print(average_height)

# ---Minor 2 - High Score---#
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

high_score = 0
for f in student_scores:
  if f > high_score:
    high_score = f
print (high_score)

# ---Minor 3- Adding Even ---#
add_even_no = 1
for numbers in range(1, 101):
  if numbers % 2 == 0:
    add_even_no += numbers
print(add_even_no)

# --- Minor 4 - FizzBuzz ---#
call = 0
for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  elif num % 5 == 0:
    print("Buzz")
  elif num % 3 == 0:
    print("Fizz")
  else:
    call = num
    print(call)

#  ----  MAJOR TASK  ----
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#ALPHABETS
r_alpha = (random.sample(letters, nr_letters))
str_alpha = ""
for alpha in r_alpha:
    str_alpha = str(str_alpha)
    str_alpha += alpha

#SYMBOL
r_sym = (random.sample(symbols, nr_symbols))
str_sym = ""
for sym in r_sym:
  str_sym += sym

#NUMBERS
r_num = (random.sample(numbers, nr_numbers))
str_num = ""
for num in r_num:
  str_num += num
easy_password = (str_alpha + str_sym + str_num)
print(easy_password)

  #Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
fig = (nr_letters + nr_numbers + nr_symbols)
rn_password = list(easy_password)
hard_password = ""
for passs in (random.sample(rn_password, fig)):
    hard_password += passs
print(hard_password)
