from  tinydb import TinyDB,Query

#
with open("./day_4_demo.csv") as f:
    file_data = f.readlines()
    print(file_data)

#指定存通讯录的文件
db = TinyDB("./db.json")


# 将CSV格式的文件，进行格式转换，存入通讯录文件
friend_1 = {'name' : file_data[0].split(',')[0], 'source' : file_data[0].split(',')[1], 'tel' : file_data[0].split(',')[2].strip()}
friend_2 = {'name' : file_data[1].split(',')[0], 'source': file_data[1].split(',')[1], 'tel' : file_data[1].split(',')[2].strip()}
friend_3 = {'name' : file_data[2].split(',')[0], 'source': file_data[2].split(',')[1], 'tel' : file_data[2].split(',')[2].strip()}

#用循环优化一下
contacts = []
for line in file_data:
    part = line.strip().split(',')
    contacts.append({
        'name' : part[0],
        'source' : part[1],
        'tel' : part[2],
    })

db.insert_multiple(contacts)

print(db.all())

friend = Query()
friend_info = db.search(friend.name == "张三")
print(friend_info)
print(f" {friend_info[0]['name']} 的电话是 {friend_info[0]['tel']} ")

db.truncate()
db.close()

