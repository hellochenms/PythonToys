# 将单行的 json 文件，转化为有换行和缩进的样式
# @author KeLan-柯烂
# @time 2021.4
# @version 1.0.0-beta210419a

import sys
import json

def pretty():
	if len(sys.argv) < 2:
		print(f"请输入文件名，示例如下：\npython3 {sys.argv[0]} xxx.json")
		return
	imageName = sys.argv[1]
	with open (imageName, 'r') as f:
	    mock = json.load(f)
	with open ("pretty-output.json", 'w') as f:
	    json.dump(mock, f, indent = 4, ensure_ascii = False)

if __name__ == "__main__":
    pretty()