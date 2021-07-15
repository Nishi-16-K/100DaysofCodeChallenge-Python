import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
total_index = len(names)
random_index= random.randint(0, total_index-1) 

#Suppose there are in total 5 names, and we get 5 from len function, but since the indexing start from 0. 
#We will use total_index-1, so total indexwill be 4 in case total 5 names.

pay_name = names[random_index]
print("\n")
print(f"{pay_name} will pay today!")
