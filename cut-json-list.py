# 本脚本用于裁剪 json 文件中某个 list 的项数
# 例如，你抓包了一个商品列表接口的数据，里面有20项商品数据
# 你想做 mock 用的 json 文件，分别测试商品个数为0、1、2、4、8、16时的页面显示效果
# 这种场景就可以用本脚本对 list 进行裁剪
# 
# @author KeLan-柯烂
# @time 2021.4
# @version 1.0.0-beta210413a

import json
import sys
import getopt

# 开启 log
DEBUG = True

def cutJSONList():
    # 输入参数
    name = sys.argv[0]
    opts, neverUse = getopt.getopt(sys.argv[1:], 'hi:k:c:')
    srcPath = ''
    keypath = ''
    count = -1
    for opt, arg in opts:
        if opt == '-h':
            help = f"""
-h 查看帮助
-i（必须） 输入文件的路径
-k（必须） 目标 list 的 keypath 
-c（必须） 目标 list 要保留的项数
示例
python3 {name} -i input.json -k data.list -c 5
            """
            print(help)
            return
        elif opt == '-i':
            srcPath = str(arg)
        elif opt == '-k':
            keypath = str(arg)
        elif opt == '-c':
            count = int(arg)
    if len(srcPath) == 0 or len(keypath) == 0 or count < 0:
        print("参数错误，请使用 -h 参数查看本脚本使用方式")
        return
    
    # 读入 json
    srcFile = open(srcPath, "r")
    srcJson = json.load(srcFile)
    srcFile.close()

    # 找到目标 list
    keylist = keypath.split(".")
    tempJson = srcJson
    parent = tempJson
    listKey = ""
    for key in keylist:
        if isinstance(tempJson, dict) and key in tempJson:
            parent = tempJson
            tempJson = tempJson[key]
            listKey = key
        else:
            print("keypath 查找失败")
            return
    if isinstance(tempJson, list):
        srcList = tempJson
    else:
        print("keypath 对应的值不是 list")
        return

    # 校验输入参数
    count = min(max(count, 0), len(srcList))

    # 裁剪
    srcList = srcList[:count]
    # list 设置回 json 对象中
    parent[listKey] = srcList

    # 命名
    destPath = f"output-count{count}.json"
    print(destPath)

    # 输出新的 json 文件
    destFile = open(destPath, "w")
    json.dump(srcJson, destFile, indent=4, ensure_ascii = False)
    destFile.close()
    print(f"已生成文件：{destPath}")

# main
if __name__ == "__main__":
    cutJSONList()