# Instead of printing the elements one by one, make a new list that has all the elements less than 10 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.



my_lists = [1, 10, 2, 5, 6, 8, 9, 20]

new_list = []

for element in my_lists:
    if element < 10:
        new_list.append(element)
print(new_list)
