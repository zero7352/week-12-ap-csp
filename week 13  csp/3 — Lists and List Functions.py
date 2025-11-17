# Lists are ordered collections of items, mutable, meaning that you can change their content.
# Lists are created using square brackets []

my_list = ["apple", "banana", "cherry", "date"]

print(my_list[0])     # apple
print(my_list[1])     # banana
print(my_list[-1])    # date
print(my_list[1:3])   # ['banana', 'cherry']

print(my_list[0])     # apple
print(my_list[1:])    # ['banana', 'cherry', 'date']

# Reverse the list
my_list.reverse()
print(my_list)

# Test each feature:
my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)

# Practice Problems:

foods = ["pizza", "sushi", "tacos", "pasta", "ice cream"]

print(foods[1])   # sushi
print(foods[-1])  # ice cream

foods.append("burger")
print(foods)

foods.pop(0)
print(foods)

foods.reverse()
print(foods)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][1])   # middle element → 5

list_of_items = list(range(1, 1001))
print(list_of_items)
print(len(list_of_items))
list_of_items.extend(range(1001, 2001))
print(len(list_of_items))