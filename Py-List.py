list1 = ["Apple", "Banana", "Mango"]
list2 = ["Orange", "Grapes", "Peach"]

combined_list = list1 + list2
print("Combined List:", combined_list)

combined_list[2:3] = ["Kiwi", "Pineapple"]
print("After Replace:", combined_list)

combined_list.pop(0)   
combined_list.pop()    

print("Final List:", combined_list)
