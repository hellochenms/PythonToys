# 将文件中 unicode（类似 \uxxxx） 转中文
# @author KeLan-柯烂
# @time 2021.4
# @version 1.0.0-beta210419a

import sys
import re

def decode():
    if len(sys.argv) < 2:
        print(f"请输入文件名，示例如下：\npython3 {sys.argv[0]} xxx.json")
        return
    path = sys.argv[1]
    ext = path.split(".")[-1]
    # read
    string = open(path, "r").read()
    # decode
    unicodes = re.findall(r"\\u\w{4}", string)
    for u in unicodes:
        string = string.replace(u, u.encode("utf-8").decode("unicode_escape"))
    # write
    dest = open(f"unicode-decode-output.{ext}", "w")
    dest.write(string)

if __name__ == "__main__":
    decode()