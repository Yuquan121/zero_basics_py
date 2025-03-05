import time
from functools import reduce,wraps

#高级函数 map() filter(),reduce(),lambda &装饰品
from functools import reduce
from time import sleep

user = [{'Name':'xiaoming','age':18,'tel':'123456'},
        {'Name':'xiaohong','age':17,'tel':'123457'},
        {'Name':'xiaolan','age':19,'tel':'123458'}]

selected_names = map(lambda x: x['Name'],filter(lambda x: x['age']>=18,user))
print(*selected_names,sep='\n')

nums = [1,2,4,5,6,7,8,34,5,76,84,354]

counts = reduce(lambda x, y: x + y, nums)
print(counts)

def time_count(func):
    @wraps(func)
    def wrapper(func):
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return wrapper(func)

@time_count
def run():
    print("run函数开始")
    sleep(1)
    print("run函数结束")


