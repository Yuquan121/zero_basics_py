import pprint as pp
from distutils.command.clean import clean

#读取文件
with open("basic_3_demo.txt") as f:
    # file_contents_read = f.read()
    file_contents = f.readlines()
    # pp.pprint(file_contents)
print(type(file_contents))

#文件行数
file_rows = len(file_contents)
print(file_rows)

#非空格行数
print(len(file_contents) - file_contents.count("\n"))

#统计单词I出现个数
print(str(file_contents).split(" ").count("I"))

print(str(file_contents).lower().split(" ").count("you"))

# print(type(str(file_contents).split(" ")))

#每个单词存入字典
dict_words = {}
words  = str(file_contents).lower().replace("\\n"," ").split(" ")
for word in words:
    clean_word = word.strip(".,!?;:\"(){}[]’")
    dict_words[clean_word] = dict_words.get(clean_word, 0) + 1

print(dict_words)

