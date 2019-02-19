# Python获取剪贴板中的图片

``` Python
from PIL import ImageGrab # pip install pillow

image = ImageGrab.grabclipboard()
image.save('pic.png')

```