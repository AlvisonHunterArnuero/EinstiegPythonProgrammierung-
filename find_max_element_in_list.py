numbers_lst = [1, 2, 3, 4, 50, 6, 3, 2, 3, 8]

# 1- Fast approach using built in max function
print("Using Max Built-in function: ", max(numbers_lst))

# 2- Manual Approach iterating all the elements of the list
max_num = numbers_lst[0]

for n in numbers_lst:
    max_num = n if n >= max_num else max_num

print("Manual Iteration: ", max_num)

# 3- Using comprehensions, in this case for the list
max_num = numbers_lst[0]
[max_num := n for n in numbers_lst if n >= max_num]
print("List Comprehension: ", max_num)

# 4- Sort the list in ascending order and print the last element in the list.
numbers_lst.sort()

# printing the last element, which is in this case the largest one
print("Using the sort list method:", numbers_lst[-1])

# 5 - Using the built in sorted function and getting
# the last list element afterwards
sorted_lst = sorted(numbers_lst, reverse=True)
max_num = sorted_lst[0]
print("Sorted List: ", max_num)

# 6 - Using the built-in reversed function to reverse
# the list, convert it to a list and print first item
print(list(reversed(numbers_lst))[0])

# Another nice shortcut for this approach should be this:
print(numbers_lst[::-1][0])