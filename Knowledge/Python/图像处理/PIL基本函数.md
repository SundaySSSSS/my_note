# PIL基本函数

```
1. 首先需要导入需要的图像库：
     import Image
2. 读取一张图片：
     im=Image.open('/home/Picture/test.jpg')
3. 显示一张图片：
    im.show()
4. 保存图片：
    im.save("save.gif","GIF")      #保存图像为gif格式
5. 创建新图片：
    Image.new(mode, size)  
    Image.new(mode, size, color)  
    栗子：newImg = Image.new("RGBA",(640,480),(0,255,0))
               newImg.save("newImg.png","PNG")
6. 两张图片相加：
    Image.blend(img1, img2, alpha)    # 这里alpha表示img1和img2的比例参数
7. 点操作：
    im.point(function) #,这个function接受一个参数，且对图片中的每一个点执行这个函数
    比如：out = im.point(lambda i : i*1.5)#对每个点进行50%的加强
8. 查看图像信息：
    im.format, im.size, im.mode
9.  图片裁剪：
    box = (100,100,500,500)  #设置要裁剪的区域 
    region = im.crop(box)     #此时，region是一个新的图像对象。
10. 图像黏贴（合并）
    im.paste(region, box)#粘贴box大小的region到原先的图片对象中。 
11. 通道分离：
   r,g,b = im.split()#分割成三个通道  ，此时r,g,b分别为三个图像对象。
12. 通道合并：
   im = Image.merge("RGB", (b, g, r))#将b,r两个通道进行翻转。
13. 改变图像的大小：
   out = img.resize((128, 128))#resize成128*128像素大小
14. 旋转图像：
   out = img.rotate(45) #逆时针旋转45度  
   有更方便的：
   region = region.transpose(Image.ROTATE_180）
15. 图像转换：
   out = im.transpose(Image.FLIP_LEFT_RIGHT)#左右对换。
  out= im.transpose(Image.FLIP_TOP_BOTTOM)#上下对换
16. 图像类型转换：
    im=im.convert("RGBA")
17. 获取某个像素位置的值：
   im.getpixel((4,4))
18.  写某个像素位置的值：
   img.putpixel((4,4),(255,0,0))

```



