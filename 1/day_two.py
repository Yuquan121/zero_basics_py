#Tuple
t1 = ('x', 'y', 'z')
#set
color = ('r','g','b','b','r','g','r')
color_set = set(color)
print(color_set)

new_color = tuple(color_set.difference(color))

print(new_color)

list1 = [ 'r', 'g', 'b', 'g', 'b', 'r', 'g' ]
tuple1 = tuple(set(list1))
print(tuple1)
del list1
del tuple1
del color_set
del new_color

# dict
print("-------------------------------------")
list1 = [ 'name1', 'name2', 'name3' ]
list2 = [ '1111', '2222', '3333']
dict1 = dict(zip(list1, list2))
print(dict1)

items = dict1.items()
print(items)

dict2 = {'Tom':'Tom@gmail.com','Jack':'Jack@gmail.com','John':'John@gmail.com'}
tom_mail = dict2.get('Tom')
print(tom_mail)
for key, value in dict2.items():
    print(f'{key} - {value}')

dict__setdefault = dict2.setdefault('Tom2','Tom2@gmail.com')
print(dict2)

print('=================================================')
#address book
name = list()
nick_name = list
name.insert('Tom')
p_name = dict()
address_book = dict()






