# 使用PIL生成缩略图
```
#image pixelate tool, use the Pillow lib
#2017/01/24 first version
from PIL import Image
import os, sys

#im = Image.open("test.jpg")
#print(im.format, im.size, im.mode)
#im.show()

#out = im.point(1,15)
#print(out)

size = (32, 32)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + "_small.bmp"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile, "bmp")
        except IOError:
            print("cannot create thumbnail for", infile)

```
