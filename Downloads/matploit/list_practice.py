animals_con = ['lion', 'cat', 'rabbit','turkey','cat']
print(animals_con[4])
animals_con.append('goat') 
print(animals_con) 
#slicing
print(animals_con[2:4]) 
print(len(animals_con))
#negative indexing
print(animals_con[-4:-2])
animals_con.clear()
animals_con.extend(['goat', 'cat','elephant' ])
copy_list =animals_con.copy()
print(copy_list)
animals_con.extend(copy_list)
print(animals_con)
stored_count =animals_con.count("elephant")
print(stored_count)
copy_list
print("hello, world")
