my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
my_list.insert(1, 15) #adds 15 in index 1
print(my_list)

my_list.extend([50,60,70]) #extends and adds [50, 60,70] to my_list to have a single list
print(my_list)

my_list.pop() #removes the last element from the list
print(my_list)

my_list.sort() #sort in ascending order
my_list.sort(reverse=True) #sort in descending order
print(my_list)

index_30=my_list.index(30) 
print(index_30)