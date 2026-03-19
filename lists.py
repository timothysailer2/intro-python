# used to store multiple items in a single var
#container holding many items of any kind

my_list =[10, 20, 30, 40, 50]
print(my_list)
mix_list =[2, 'apple', 3.5, True]
print(mix_list[2])
print(mix_list[-2])
#modify list items
mix_list[0] = 'nope'
print(mix_list)
#add items
mix_list.append(15)
print(mix_list)
mix_list.insert(1, 'kiwi')
print(mix_list)
mix_list.remove('apple')#use .pop to remove last index
print(mix_list)

print(mix_list)
#looping through list
for item in mix_list:
    print(item)

#check item exist
if 2 in mix_list:
    print("yeah")

#list length
print(len(mix_list))
