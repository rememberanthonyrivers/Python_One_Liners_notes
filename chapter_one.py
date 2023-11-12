# using the key word in to check for occurences within the data struct
# the in keyword returns a boolean

list_of_nums = [4, 5, 3, 45, 6, 7, 4, 32, 22]
list_of_strings = ['hello world!!!!!','hello world?','hello world!!!','hello world?','hello world!!',]
list_of_multiples = [24, 'hello', 22, 'world!', 50, 'this', 'is', 100]

# list comprehension -> [ expression : x + context : for x in list]
# list comprehension -> print([ expression : x + context : for x in list])

print([x * 2 for x in list_of_nums])