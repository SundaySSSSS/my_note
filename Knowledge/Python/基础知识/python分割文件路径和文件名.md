# python分割文件路径和文件名

```python
import os.path

spath="D:/360Downloads/testFile1/folder2/testFile1.txt"
#case 1: 分割目录和文件名
p,f=os.path.split(spath);
print("dir is:" + p)
# dir is:D:/360Downloads/testFile1/folder2
print("file is:" + f)
# file is:testFile1.txt

#case 2:  分割盘符 <- windows有效, Unix系没有尝试
drv,left=os.path.splitdrive(spath);
print("drive is:" + drv)
# drive is:D:
print("left is:" + left)
# left is:/360Downloads/testFile1/folder2/testFile1.txt

#case 3: 分割拓展名
f,ext = os.path.splitext(spath);
print("f is:" + f)
# f is:D:/360Downloads/testFile1/folder2/testFile1
print("ext is:" + ext)
# ext is:.txt

```
