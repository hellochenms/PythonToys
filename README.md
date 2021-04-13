# PythonToys
一些 python 写的小工具，通常很短，只解决一个小问题

#### cut-json-list.py
```Python
# 本脚本用于裁剪 json 文件中某个 list 的项数
# 例如，你抓包了一个商品列表接口的数据，里面有20项商品数据
# 你想做 mock 用的 json 文件，分别测试商品个数为0、1、2、4、8、16时的页面显示效果
# 这种场景就可以用本脚本对 list 进行裁剪
#
# 例如 python3 cut-json-list.py -i goodslist.json -k data.list -c 8
# 就是将 goodslist.json 里的 json对象（假设为 jsonObj）中的 jsonObj["data"]["list"] 这个 list 裁剪到8项
```