list1 = [1,2,3,'a','b',[4,'c']]
print(list1)
print(list1[0])
print(list1[-1][0])
print(list1[-1][1])
del list1[-1]
print(list1)
del list1
print("-------------------------")
list1 = [1,2,3,'a','b',[4,'c']]
list1.insert(0,"first")
list1.insert(-1,"last")
print(list1)
list1.append("read_last")
print(list1)
list1.remove('last')
list1.pop(-3)
print(list1)