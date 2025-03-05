import os
import pathlib as plib
from collections import defaultdict

#1_basic.请使用格式化输出功能，将上述字符进行格式转换，输出格式为：智能助手为你报时，当前时间是2024年5月20日13点14分0秒

date = "2024-05-20 13:14:00"
year, month, day, hour, minute, second = map(int, date.replace('-', ' ').replace(':', ' ').split())
print(f"智能助手为你报时，当前时间是{year}年{month}月{day}日{hour}点{minute}分{second}秒")

number = 123.4567
print(f"{number:010.3f}")

string = """Python 3.11 is up to 10-60% faster than Python 3.10. On average, we measured a 1_basic.25x speedup on the standard benchmark suite. See Faster CPython for details.\n"""

path = plib.Path("a.txt")

def write_a(filename):
    with open(filename, "w") as f:
        f.write(string)
    with open(filename, "r") as f:
        print(f.readline())

if not os.path.exists(path):
    write_a(path)
else:
    if os.access(path, os.R_OK) and os.access(path, os.W_OK):
        print("The file is readable and writable.")
        write_a(path)
print("--------------------------------")
with open("b.txt", "a+") as fb:
    with open("a.txt", 'r') as fa:
        fb.write(fa.read())
        fb.seek(0)
        print(fb.read())

#在homework文件夹下有三个文件夹dira，dirb.txt，dirc.txt，dira下有两个文件夹dira1，dira2，每个文件夹下都有一个与文件夹同名的txt文件，
# 现在需要将这5个txt文件合并成homework.txt并放在homework下，用python实现该需求（这是不是三叉树的遍历？）

def merge_files(root_dir, out_file) -> None:
    file_dict = defaultdict(list)
    max_depth = 0

    for root, dirs, files in os.walk(root_dir):
        depth = root[len(root_dir):].count(os.sep)
        if root == root_dir:
            continue
        dir_name = os.path.basename(root)
        targe_file = os.path.join(root, f"{dir_name}.txt")
        if os.path.exists(targe_file):
            file_dict[depth].append(targe_file)
            max_depth = max(depth, max_depth)

    #按层级合并文件（从浅到深）
    with open(out_file, 'w', encoding='utf8') as out_file:
        for depth in sorted(file_dict.keys()):
            sorted_files = sorted(file_dict[depth])
            for file in sorted_files:
                with open(file, 'r', encoding='utf8') as input_file:
                    out_file.write(f"=========来自层级{depth} 的 {os.path.basename(file)}========\n")
                    out_file.write(input_file.read() + '\n')

if __name__ == "__main__":
    homework_dir = "homework"
    output_file = os.path.join(homework_dir, "homework.txt")
    merge_files(homework_dir, output_file)



