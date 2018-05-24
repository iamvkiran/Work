
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print('The first item is', grocery_list[1])

# You can change the value stored in a list box
grocery_list[0] = "Green Juice"
print(grocery_list)

# You can get a subset of the list with [min:up to but not including max]

print(grocery_list[1:3])

# You can put any data type in a a list including a list
other_events = ['Wash Car', 'Pick up Kids', 'Cash Check']
to_do_list = [other_events, grocery_list]

print(to_do_list)

print(to_do_list[1][1])