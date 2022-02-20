# LIST COMPREHENSION
numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

my_range = range(1, 5)
print(my_range)
new_range = [n*2 for n in my_range]
print(new_range)

# CONDITIONAL LIST COMPREHENSION
# new_list = [new_item for item in list if test]

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
new_names = [name[::-1] for name in names if len(name) > 5]
print(new_names)