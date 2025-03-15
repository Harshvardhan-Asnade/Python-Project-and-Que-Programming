my_list = [1, 2, 3, 4, 5]

my_list.append(6)
print("After append:", my_list)

my_list.extend([7, 8, 9])
print("After extend:", my_list)

my_list.insert(2, 10)
print("After insert:", my_list)

my_list.remove(3)
print("After remove:", my_list)

popped_element = my_list.pop()
print("After pop:", my_list, "Popped element:", popped_element)

index_of_4 = my_list.index(4)
print("Index of 4:", index_of_4)

count_of_2 = my_list.count(2)
print("Count of 2:", count_of_2)

my_list.sort()
print("After sort:", my_list)

my_list.reverse()
print("After reverse:", my_list)

copied_list = my_list.copy()
print("Copied list:", copied_list)

my_list.clear()
print("After clear:", my_list)