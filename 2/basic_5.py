code = False

if code :
    print("成立")
    print("成立2")
print("-----")
#%%
if code :
    print("成立")
else :
    print("不成立")
print("-----")

http_response_status = 500

match http_response_status:
        case 400:
            print("Bad request" )
        case 404:
            print( "Not found")
        case 418:
            print( "I'm a teapot")
        case _:
            print( "Something's wrong with the internet")

number = 1
while number <= 3:
    print(f"number is {number}")
    # number_temp = number + 1
    # number = number_temp
    number += 1

print(number)
#%%
number = 1
while number <= 3:
    # list1[1]   # error
    print(f"number is {number}")
    # number_temp = number + 1
    # number = number_temp
    number += 1

print(number)


#for循环
print("-----------------------------------")
movie1 = { "name":"Friends", "language":"En", "Sessions":10, "Other name":"Six of One" }

for key,value in movie1.items():
    print(f"{key} is {value}")

for i in enumerate(movie1.items()):
    print(i)

#list1 = ["rachel","monica","Phoebe","joey"]. 该列表按首字母排序，每个元素变为大写，输出排序后的序号和内容
print("-----------------------------------")
list1 = ["rachel","monica","Phoebe","joey"]

list_upper_sorted = sorted([name.upper() for name in list1])

for i in enumerate(list_upper_sorted):
    print(i)


#打印99乘法表
for i in range(1,10):
    for j in range(1,i + 1):
        print(f"{j} * {i} = {i*j}",end = ' ')
        if j == i:
            print()