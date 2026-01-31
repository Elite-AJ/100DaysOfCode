#List Comprehension
numbers  = [1, 2, 3]
new_num = [n+1 for n in numbers]
print (new_num)

new_range = [i*2 for i in range(1,5)]
print(new_range)

#Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name)  >  5]
print(short_names)

long_names = [name.upper() for name in names if len(name)  >  5]
print(long_names)