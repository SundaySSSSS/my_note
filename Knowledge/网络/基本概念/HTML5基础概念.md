# HTML5基础概念
```
* HTML5基础概念
** HTML5的基本结构
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
	<head>
		<title>页面标题</title>
		<meta charset="utf-8"/>
	</head>
	<body>
		页面内容部分
	</body>
</html>
#+END_SRC
其中:
<!DOCTYPE html>表示文档类型, 对之前的html进行了简化, 不必再指定版本号
<meta charset="utf-8"/>表示使用的编码集

注意:
不要再<html>和<head>之间插入任何内容
不要再</head>和<body>之间插入任何内容
不要再</body>和</html>之间插入任何内容
** HTML5的语法变化
标签不区分大小写
元素可以省略结束标签
允许省略属性的属性值
允许属性不使用引号

** HTML5环境搭建
推荐使用WebStorm

** 第一个HTML5页面
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
	<head lang="en">
		<title>我的第一个HTML5页面</title>
		<meta charset="utf-8"/>
	</head>
	<body>
		Hello, HTML5
	</body>
</html>
#+END_SRC

** HTML5新增的常用元素
*** 新增的结构性元素
**** 功能简介
| 元素名称 | 功能                                                             |
|----------+------------------------------------------------------------------|
| section  | 定义文档中的节, 比如文章中的章节等                               |
| article  | 特殊的section标签, 表示一个独立的, 完整的内容块                  |
| footer   | 定义section或article的注脚                                       |
| header   | 定义文档的页眉, 通常是引导和导航信息                             |
| nav      | 表示页面中的导航链接部分                                         |
| aside    | 用来装载非正文的内容, 例如文章的注释等, 或者淘宝页面的推荐侧边栏 |
| hgroup   | 用来对网页或section的标题元素(h1-h6)进行组合                     |
| figure   | 用于对元素进行组合,多用于图片和图片描述的组合                    |

**** 利用上述元素构建一个html5页面
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
	<head lang="en">
		<title>我的第一个HTML5页面</title>
		<meta charset="utf-8"/>
	</head>
	<body>
		<header>
			<div id="container">
				<nav>
				  <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="#">Articles</a></li>
                    <li><a href="#">Contacts</a></li>
                  </ul>
				</nav>
			</div>
        </header>
        <div id = "content">
              <aside>
                <div class = "inside">
                  <h2>Latest News</h2>
                  <ul>
                    <li><a href="#">JUNE 30, 2010</a>something happened</li>
                    <li><a href="#">JULY 01, 2010</a>something happened</li>
                    <li><a href="#">JULY 02, 2010</a>something happened</li>
                  </ul>
                </div>
              </aside>
              <section id = "mycontent">
                <h2>About your website</h2>
                <p>第一段内容</p>
                <p>第二段内容</p>
                <h2>About Your Team</h2>
                <ul>
                  <li><img src="1.jpg">this is first pic</li>
                  <li><img src="2.jpg">this is second pic</li>
                </ul>
              </section>
        </div>
	    <footer>
          <div id = "myfooter">
            <a href="#">Website template</a>
          </div>
        </footer>
	</body>
</html>
#+END_SRC



*** 新增的语意性元素
**** 功能简介
| 元素名称 | 功能                                  |
|----------+---------------------------------------|
| mark     | 带有记号的文本                        |
| progress | 运行中的任务进度                      |
| time     | 表示时间日期值                        |
| details  | 补充细节                              |
| datalist | 定义选项列表, 需要和input元素配合使用 |
| ruby     | 定义ruby注释                          |
| menu     | 菜单列表(几乎都不支持)                |
| command  | 定义用户可能调用的命令(几乎都不支持)  |
**** 例子
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
	<head lang="en">
	  <title>Html5新增语意元素</title>
	  <meta charset="utf-8"/>
	</head>
    <body>
      <!--progress使用实例-->
      <progress value="22" max="100"></progress>
      <!--details使用实例-->
      <details>
        <summary>Copyright 1999-2018.</summary>
        <p> All Rights Reserved. </p>
      </details>
      <!--datalist标签使用实例-->
	  <input list="browsers">
      <datalist id="browsers">
        <option value="IE">
        <option value="FIrefox">
        <option value="Chrome">
      </datalist>
    </body>
</html>
#+END_SRC
*** 废除的元素
能用CSS代替的元素,比如basefont,big,center,font,s,strike,tt,u
不再支持frame框架, 只支持iframe框架
只有部分浏览器支持的元素,如applet,bgsound,blink,marquee等
** HTML5新增的表单功能
*** input输入类型
**** 功能简介
| input输入类型 | 功能                                                           |
|---------------+----------------------------------------------------------------|
| email         | 定义用于email地址的字段                                        |
| url           | 定义用于输入url的字段                                          |
| number        | 定义用于输入数字的字段                                         |
| range         | 定义用于精确值不重要的数字输入控件, 会显示一个划块帮助用户输入 |
| Data Pickers  | 日期控件                                                       |
| search        | 定义用于输入搜索字符串的文本字段                               |
| tel           | 用于输入电话号码的字段                                         |
| color         | 拾色器                                                         |
**** 例子
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
	<head lang="en">
	  <title>input输入实例</title>
	  <meta charset="utf-8"/>
	</head>
    <body>
      <!--email-->
      <form action="#" method="get">
        <input type="email" name="user_email"/><br/>
        <input type="submit" value="提交"/>
      </form>
      <!--url-->
      <form action="#" method="get">
        <input type="url" name="user_url"/><br/>
        <input type="submit" value="提交"/>
      </form>
      <!--number-->
      <form action="#" method="get">
        <input type="number" name="user_number" max = "100" min = "1" step = "2"/><br/>
        <input type="submit" value="提交"/>
      </form>
      <!--range-->
      <form action="#" method="get">
        <input type="range" name="user_range" max = "100" min = "1" step = "2"/><br/>
        <input type="submit" value="提交"/>
      </form>
       <!--date-->
      <form action="#" method="get">
        <input type="date" name="user_date"/><br/>
        <input type="month" name="user_month"/><br/>
        <input type="week" name="user_week"/><br/>
        <input type="time" name="user_time" value="12:10:14" min="01:00:00" max="20:00:00"/><br/>
        <input type="submit" value="提交"/>
      </form>
      <!-- search-->
      <form action="#" method="get">
        <input type="search" name="user_search"/><br/>
        <input type="submit" value="提交"/>
      </form>
      <!--tel-->
      <form action="#" method="get">
        <input type="tel" name="user_tel"/><br/>
        <input type="submit" value="提交"/>
      </form>
      <!--color-->
      <form action="#" method="get">
        <input type="color" name="user_color"/><br/>
        <input type="submit" value="提交"/>
      </form>
    </body>
</html>
#+END_SRC
*** input属性
| input属性     | 功能                                           |
|---------------+------------------------------------------------|
| autocomplete  | 是否启用自动完成功能                           |
| autofocus     | 规定当页面加载时自动获得焦点                   |
| form          | 规定<input>元素所属的一个或多个表单            |
| height和width | 规定<input>元素的高度,宽度(只针对type="image") |
| list          | 实现下拉列表框效果                             |
| min,max       | 允许输入的最小值,最大值                        |
*** 新增form元素
**** datalist
前面已经讲过
**** output
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
	<head lang="en">
	  <title>output实例</title>
	  <meta charset="utf-8"/>
	</head>
    <head>
      <script type="text/javascript">
        function multi()
        {
        	a = parseInt(prompt("Please Input The First Number", 0));
	    	b = parseInt(prompt("Please Input The Second Number", 0));
        	document.forms["form"]["result"].value=a*b;
        }
      </script>
    </head>
    <body onload="multi()">
      <form action="#" method="get" name="form">
        两个数的乘积为:
        <output name="result"></output>
      </form>
    </body>
</html>
#+END_SRC
*** 新增form属性
| 属性       | 功能 |
|--------------+------|
| autocomplete | 自动填充 |
| novalidate   | 不再进行形式检查 |

** Canvas绘图
*** 在页面中添加canvas
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
	<head lang="en">
	  <title>canvas实例</title>
	  <meta charset="utf-8"/>
	</head>

    <body>
      <canvas id="myCanvas" width="578" height="200">
        Your Browser not support canvas!!!
      </canvas>
    </body>
</html>
#+END_SRC

*** canvas绘制步骤
1, 在html5中添加canvas元素,定义id属性值以便将来调用
#+BEGIN_SRC html
<canvas id="myCanvas" width="578" height="200"></canvas>
#+END_SRC
2, 使用id寻找页面中的canvas元素
#+BEGIN_SRC javascript
var c = document.getElementById("myCanvas");
#+END_SRC
3, 通过canvas元素的getContext方法来获取其上下文,来进行2D绘图
#+BEGIN_SRC javascript
var context = c.getContext("2d");
#+END_SRC
4, 使用JavaScript进行绘图
#+BEGIN_SRC javascript
context.fillStyle='#ff0000'
context.fillRect(50, 25, 100, 50);
#+END_SRC

*** 具体实例
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
	<head lang="en">
	  <title>canvas_demo</title>
	  <meta charset="utf-8"/>
      <style>
        #myCanvas {
        	border: 1px solid #9c9898;
        }
      </style>
      <script type=text/javascript>
        	window.onload=function(){
        	var canvas = document.getElementById("myCanvas");
        	var context = canvas.getContext("2d");
        	context.fillStyle = "#ff0000";
        	context.fillRect(50, 25, 100, 50);
        }
      </script>
	</head>

    <body>
      <canvas id="myCanvas" width="578" height="200">
        Your Browser not support canvas!!!
      </canvas>
    </body>
</html>
#+END_SRC

*** 直线的绘制
**** 直线相关方法
beginPath() 定义一个新的路径绘制动作的开始
moveTo() 移动绘制点
lineTo() 绘制直线到某个点
stroke() 给所画的线赋予颜色,并使其可见.默认为黑色
**** 直线相关属性
lineWidth 直线的宽度
strokeStyle 直线的颜色
直线端点样式, 包括butt,round,square, 默认为butt, 可以使用lineCap属性进行设定

**** 例子
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
	<head lang="en">
	  <title>canvas_demo</title>
	  <meta charset="utf-8"/>
      <style>
        #myCanvas {
    	    border: 1px solid #9c9898;
	        background-color: #77ffcc;
        }
      </style>
      <script type=text/javascript>
        window.onload = function() {
        	var canvas = document.getElementById("myCanvas");
        	var context = canvas.getContext("2d");
			<!-- The First Line, use lineCap round -->
        	context.beginPath();
            context.moveTo(200, canvas.height/2);
            context.lineTo(canvas.width - 200, canvas.height/2);
            context.lineWidth=20;
            context.strokeStyle="#ff0000";
            context.lineCap="round";
	        context.stroke();
            <!-- The Second Line, use LineCap square -->
        	context.beginPath();
            context.moveTo(200, canvas.height/2 + 50);
            context.lineTo(canvas.width - 200, canvas.height/2 + 50);
            context.lineWidth=20;
            context.strokeStyle="#00ff00";
            context.lineCap="square";
            context.stroke();
            <!-- Thrid Line, use LineCap butt -->
            context.beginPath();
            context.moveTo(200, canvas.height/2 - 50);
            context.lineTo(canvas.width - 200, canvas.height/2 - 50);
            context.lineWidth=20;
            context.strokeStyle="#0000ff";
            context.lineCap="butt";
            context.stroke();
        }
      </script>
	</head>

    <body>
      <canvas id="myCanvas" width="578" height="200">
        Your Browser not support canvas!!!
      </canvas>
    </body>
</html>
#+END_SRC

*** 曲线的绘制
**** 相关方法
arcTo() 在画布上创建介于两个切线之间的弧/曲线
quadraticCurveTo() 绘制二次曲线
bezierCurveTo() 绘制贝塞尔曲线
**** 例子
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
	<head lang="en">
	  <title>canvas_demo</title>
	  <meta charset="utf-8"/>
      <style>
        #myCanvas {
    	    border: 1px solid #9c9898;
	        background-color: #77ffcc;
        }
      </style>
      <script type=text/javascript>
       window.onload = function() {
           var canvas = document.getElementById("myCanvas");
           var context = canvas.getContext("2d");
           //绘制弧线
           context.beginPath();
           context.moveTo(20, 20);
           context.lineTo(100, 20);
           context.arcTo(150, 20, 150, 70, 50);
           context.lineTo(150, 120);
           context.stroke();
           //绘制二次贝塞尔曲线
           context.beginPath();
           context.moveTo(200, canvas.height/2);	//起始点
           context.quadraticCurveTo(288, 0, 388, 150);
           context.lineWidth = 5;
           context.strokeStyle="blue";
           context.stroke();
           //绘制三次贝塞尔曲线
           context.beginPath();
           context.moveTo(500, canvas.height/2130);	//起始点
           context.bezierCurveTo(400, 10, 588, 10, 688, 170);
           context.lineWidth = 5;
           context.strokeStyle="yellow";
           context.stroke();
       }
      </script>
	</head>

    <body>
      <canvas id="myCanvas" width="800" height="200">
        Your Browser not support canvas!!!
      </canvas>
    </body>
</html>
#+END_SRC
*** 线条连接样式
HTML5 canvas支持3种线条的连接样式
miter: 尖角(默认)
round: 圆角
bevel: 斜角
设定连接样式需要使用lineJoin属性
#+BEGIN_SRC html
context.lineJoin = "round"
#+END_SRC

*** 图形的绘制
**** 绘制矩形
rect(x, y, w, h)

**** 绘制圆
arc(centerX, centerY, radius, begin_arc, end_arc, direction)
参数依次为: 圆心x, 圆心y, 半径, 起始度数(规定0度为正右的方向), 终止度数, 方向(true为顺时针)
如果要画一个整圆, 如下:
#+BEGIN_SRC javascript
context.arc(centerX, centerY, radius, 0, 2 * Math.PI, false);
#+END_SRC

**** 图形的颜色填充
fillStyle属性可以设置图形用的颜色(默认为黑色), 然后用fill()方法对图形填充

**** 例子
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
	<head lang="en">
	  <title>canvas_demo</title>
	  <meta charset="utf-8"/>
      <style>
        #myCanvas {
    	    border: 1px solid #9c9898;
	        background-color: #77ffcc;
        }
      </style>
      <script type=text/javascript>
       window.onload = function() {
           var canvas = document.getElementById("myCanvas");
           var context = canvas.getContext("2d");
           //绘制矩形
           context.beginPath();
           context.rect(10, 50, 200, 100);
           context.lineWidth = 5;
           context.strokeStyle = "blue";
           context.stroke();
           context.fillStyle = "#00ff00";
           context.fill();

           //绘制圆
           context.beginPath();
           var centerX = canvas.width/2;
           var centerY = canvas.height/2;
           var radius = 80;
           context.arc(centerX, centerY, radius, 0, 2 * Math.PI, false);
           context.lineWidth = 5;
           context.strokeStyle = "red";
           context.stroke();
           context.fillStyle = "#8ED6FF";
           context.fill();
       }
      </script>
	</head>

    <body>
      <canvas id="myCanvas" width="800" height="500">
        Your Browser not support canvas!!!
      </canvas>
    </body>
</html>
#+END_SRC

*** 绘制阴影和透明度
**** 相关属性
shadowColor: 阴影颜色
shadowBlur: 阴影糢糊度
shadowOffsetX: 阴影与形状的水平距离
shadowOffsetY: 阴影与形状的垂直距离
globalAlpha: 设置或取得当前透明值, 0.0-完全透明 1.0 不透明
**** 例子
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
	<head lang="en">
	  <title>canvas_demo</title>
	  <meta charset="utf-8"/>
      <style>
        #myCanvas {
    	    border: 1px solid #9c9898;
	        background-color: #77ffcc;
        }
      </style>
      <script type=text/javascript>
       window.onload = function() {
           var canvas = document.getElementById("myCanvas");
           var context = canvas.getContext("2d");
           //绘制矩形
           context.beginPath();
           context.rect(10, 50, 200, 100);
           context.lineWidth = 5;
           context.strokeStyle = "black";
           context.stroke();
           context.fillStyle = "#00ff00"
           //添加透明度
           context.globalAlpha = 0.5;
           //添加阴影
           context.shadowColor = "black";
           context.shadowBlur = 20;
           context.shadowOffsetX = 10;
           context.shadowOffsetY = 10;
           //阴影和透明度需要在fill之前完成
           context.fill();
       }
      </script>
	</head>

    <body>
      <canvas id="myCanvas" width="800" height="500">
        Your Browser not support canvas!!!
      </canvas>
    </body>
</html>
#+END_SRC



*** 渐变的绘制
**** 绘制水平渐变
1, 首先用createLinearGradient()创建canvasGradient对象
#+BEGIN_SRC javascript
var grad = context.createLinearGradient(x1, y1, x2, y2)
#+END_SRC
其中x1,y1为渐变起点, x2,y2为渐变终点

2, 使用addColorStop方法定义色标的位置并上色
#+BEGIN_SRC javascript
grad.addColorStop(position, color);//其中position为渐变种色标的相对位置(偏移量)
#+END_SRC

**** 绘制径向渐变
方法和水平渐变类似
创建需要使用如下方法:
#+BEGIN_SRC javascript
var grad = context.createRadiaGradient(x1, y1, r1, x2, y2, r2);
#+END_SRC

**** 例子
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
	<head lang="en">
	  <title>canvas_demo</title>
	  <meta charset="utf-8"/>
      <style>
        #myCanvas {
    	    border: 1px solid #9c9898;
	        background-color: #77ffcc;
        }
      </style>
      <script type=text/javascript>
       window.onload = function() {
           var canvas = document.getElementById("myCanvas");
           var context = canvas.getContext("2d");
           //线性渐变
           var clg = context.createLinearGradient(0, 0, 200, 100);
           clg.addColorStop(0, "#ff0000");
           clg.addColorStop(0.5, "#00ff00");
           clg.addColorStop(1, "#0000ff");
           context.fillStyle = clg;
           context.strokeStyle = clg;
           context.fillRect(10, 10, 200, 200);

           //径向渐变
           var crg = context.createRadialGradient(325, 100, 20, 325, 100, 80);
           crg.addColorStop(0, "#ff0000");
           crg.addColorStop(0.75, "#00ff00");
           crg.addColorStop(1, "#0000ff");
           context.fillStyle = crg;
           context.strokeStyle = crg;
           context.fillRect(230, 10, 200, 200);           
       }
      </script>
	</head>

    <body>
      <canvas id="myCanvas" width="800" height="500">
        Your Browser not support canvas!!!
      </canvas>
    </body>
</html>
#+END_SRC


*** 绘制图案填充
使用上下文对象的createPattern()方法创建一个图案填充对象
#+BEGIN_SRC javascript
context.createPattern(image, type);
#+END_SRC
其中, type必须为以下字符串之一
repeat
repeat-x
repeat-y
no-repeat

例子:(按下不同按钮, 按照不同的type平铺图案. 此例只在chrome中是完全正常的)
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
    <head lang="en">
	    <title>canvas_demo</title>
	    <meta charset="utf-8"/>
        <style>
         #myCanvas {
             border: 1px solid #9c9898;
             background-color: #77ffcc;
         }
        </style>
        <script type=text/javascript>
         function draw(type) {
             var c = document.getElementById("myCanvas");
             var ctx = c.getContext("2d");
             ctx.clearRect(0, 0, c.width, c.height);//清除内容
             var img = document.getElementById("butterfly");
             var pat = ctx.createPattern(img, type);
             ctx.rect(0, 0, 500, 200);
             ctx.fillStyle = pat;
             ctx.fill();
         }
        </script>
    </head>
    <body>
        <img src="images/icon.jpg" id ="butterfly"/><br/>
        <button onclick ="draw('repeat')">Repeat</button>
        <button onclick ="draw('repeat-x')">Repeat-x</button>
        <button onclick ="draw('repeat-y')">Repeat-y</button>
        <button onclick ="draw('no-repeat')">No-Repeat</button>
        <br/>
        <canvas id="myCanvas" width="500" height="200">
            Your Browser not support canvas!!!
        </canvas>
    </body>
</html>
#+END_SRC

*** 绘制图像
**** 常用方法
#+BEGIN_SRC javascript
context.drawImage(imageObj, x, y);//将图片绘制到x,y处
context.drawImage(imageObj, x, y, width, height);//指定图片绘制位置和大小
context.drawImage(imageObj, sx, sy, sw, sh, dx, dy, dw, dh);//指定图片源的一部分(sx,sy,sw,sh),绘制到指定位置(dx, dy, dw, dh)
#+END_SRC
**** 例子
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
    <head lang="en">
	    <title>canvas_demo</title>
	    <meta charset="utf-8"/>
        <style>
         #myCanvas {
             border: 1px solid #9c9898;
             background-color: #77ffcc;
         }
        </style>
        <script type=text/javascript>
         window.onload = function () {
             var canvas = document.getElementById("myCanvas");
             var context = canvas.getContext("2d");
             var imageObj = new Image();
             imageObj.src = "images/bg_cat.jpg";
             imageObj.onload = function() {	//在图片加载完毕后执行
                 context.drawImage(imageObj, 10, 10);
                 context.drawImage(imageObj, 10, 650, 100, 100);
                 context.drawImage(imageObj, 50, 40, 300, 450, 50, 50, 350, 450);
             }
         }
        </script>
    </head>
    <body>
        <canvas id="myCanvas" width="1200" height="800">
            Your Browser not support canvas!!!
        </canvas>
    </body>
</html>

#+END_SRC

*** 图形的变换
移动坐标空间
使用translate()方法,将坐标系进行移动, 表现为整个canvas的移动

旋转坐标空间
使用rotate()方法, 按照指定的弧度将整个canvas进行旋转, 表现为整个canvas的旋转

缩放图形
scale(x, y) ,x,y分别代表横向和纵向的缩放比例, 都是浮点数, 1.0表示不缩放, 小于1.0表示缩小, 大于1.0表示放大

**** 实例
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
    <head lang="en">
	    <title>canvas_demo</title>
	    <meta charset="utf-8"/>
        <style>
         #myCanvas {
             border: 1px solid #9c9898;
             background-color: #77ffcc;
         }
        </style>
        <script type=text/javascript>
         window.onload = function () {
             var canvas = document.getElementById("myCanvas");
             var context = canvas.getContext("2d");
             var rectWidth = 150;
             var rectHeight = 75;
             context.fillStyle = "#ff0000";
             //把坐标原点移动到canvas的中心点
             context.translate(canvas.width / 2, canvas.height / 2);
             //顺时针旋转45度
             context.rotate(0.25 * Math.PI);
             //坐标在纵向上缩小一半
             context.scale(1, 0.5);
             context.fillRect(- rectWidth / 2, - rectHeight / 2, rectWidth, rectHeight);
             
         }
        </script>
    </head>
    <body>
        <canvas id="myCanvas" width="800" height="300">
            Your Browser not support canvas!!!
        </canvas>
    </body>
</html>

#+END_SRC


*** 图形的组合和裁剪
**** 图形的组合
涉及了很多方法, 具体看实例
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
	<head lang="en">
	  <title>canvas_demo</title>
	  <meta charset="utf-8"/>
      <style>
        #myCanvas {
    	    border: 1px solid #9c9898;
	        background-color: #77ffcc;
        }
      </style>
      <script type=text/javascript>
       window.onload = function() {
           var canvas = document.getElementById("myCanvas");
           var context = canvas.getContext("2d");
           //绘制矩形
           context.beginPath();
           context.rect(200, 20, 100, 100);
           context.fillStyle = "blue";
           context.fill();

           //context.globalCompositeOperation = "source-over";//新图形覆盖原有图形
           //context.globalCompositeOperation = "source-atop";//新图形在原有图形之上,但只绘制原有图形范围内的部分
           //context.globalCompositeOperation = "source-in";//只绘制新图形在原有图形范围内的部分, 原图形也不会显示
           //context.globalCompositeOperation = "source-out";//只绘制新图形不再原有图形范围内的部分,原图形也不会显示
           //context.globalCompositeOperation = "destination-atop";//和上面的四个正好相反
           //context.globalCompositeOperation = "destination-in";
           //context.globalCompositeOperation = "destination-out";
           //context.globalCompositeOperation = "destination-over";
           //context.globalCompositeOperation = "lighter";//重叠部分做减色处理
           //context.globalCompositeOperation = "darker";//重叠部分做加色处理
           //context.globalCompositeOperation = "xor";//将重叠部分变透明
           context.globalCompositeOperation = "copy";//只保留新图形

           //绘制圆
           context.beginPath();
           context.arc(320, 120, 60, 0, 2 * Math.PI, false);
           context.fillStyle = "red";
           context.fill();
       }
      </script>
	</head>

    <body>
      <canvas id="myCanvas" width="800" height="500">
        Your Browser not support canvas!!!
      </canvas>
    </body>
</html>

#+END_SRC

**** 图形的裁切
使用clip()方法
裁切后, 只有裁切部分才会显示, 其他部分不再显示

** Canvas绘制文本
*** 绘制文本内容
#+BEGIN_SRC javascript
context.fillText(text, x, y);//绘制文本
context.strokeText(text, x, y);//绘制文本的边缘(空心字体)
context.font = "normal";//设置字体, 还可以为"italic"或者"bold"
context.fillStyle = "red";//设置文本颜色
context.strokeStyle();//设置空心字体的颜色
#+END_SRC
*** 文本的对齐
使用textAlign属性, 可用的选项包括start, end, left, center, right

文本度量方法:
获取文本的尺度信息:measureText()

*** 代码实例
实例1:
演示了文本描画, 文本对齐和文本度量
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
    <head lang="en">
	    <title>canvas_demo</title>
	    <meta charset="utf-8"/>
        <style>
         #myCanvas {
             border: 1px solid #9c9898;
             background-color: #77ffcc;
         }
        </style>
        <script type=text/javascript>
         window.onload = function () {
             var canvas = document.getElementById("myCanvas");
             var context = canvas.getContext("2d");
             var x = canvas.width / 2;
             var y = canvas.height / 2;
             context.font = "italic 40px Arial";
             context.fillStyle = "#ff0000";
             context.fillText("Hello World", x, y);

             context.strokeStyle = "#0000ff";
             context.lineWidth = 2;//设置描边的宽度
             context.textAlign = "center";
             context.strokeText("Hello Stroke Text", x, y + 50);
             var metrics = context.measureText("Hello Stroke Text");
             var width = metrics.width;
             context.font="30pt Arial";
             context.textAlign="center";
             context.fillStyle="#555";
             context.fillText("(" + width + "px width" ,x, y + 100);
             
         }
        </script>
    </head>
    <body>
        <canvas id="myCanvas" width="800" height="300">
            Your Browser not support canvas!!!
        </canvas>
    </body>
</html>

#+END_SRC

实例2:
自动换行的文本, 使用measureText()测量字符串长度, 超过规定范围后换行
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
    <head lang="en">
	    <title>canvas_demo</title>
	    <meta charset="utf-8"/>
        <style>
         #myCanvas {
             border: 1px solid #9c9898;
             background-color: #77ffcc;
         }
        </style>
        <script type=text/javascript>
         function wrapText(context, text, x, y, maxWidth, lineHeight) {
             var words = text.split(" ");//以空格分割字符串, 并存储到数组中
             var line = "";
             for (var n = 0; n < words.length; n++) {
                 var textLine = line + words[n] + " ";
                 var metrics = context.measureText(textLine);
                 var textWidth = metrics.width;
                 if (textWidth > maxWidth) {// 已经达到最大宽度了, 进行描画
                     context.fillText(line, x, y);
                     line = words[n] + " ";
                     y += lineHeight;//换行
                 } else {
                     line = textLine;
                 }
             }
             context.fillText(line, x, y);
         }
         window.onload = function () {
             var canvas = document.getElementById("myCanvas");
             var context = canvas.getContext("2d");
             var text = "All the world's a stage, and all the men and women"
                      + " merely player, They have their exits and their entrances; And one man in"
                      + " his time plays many parts.";
             var maxWidth = 400;//每一行绘制的长度, 超过就换行
             var lineHeight = 25;//行间隔
             var x = (canvas.width - maxWidth) / 2;//绘制的起点坐标
             var y = 60;
             context.font = "16px Arial";
             context.fillStyle="333";
             wrapText(context, text, x, y, maxWidth, lineHeight);
             
         }
        </script>
    </head>
    <body>
        <canvas id="myCanvas" width="800" height="300">
            Your Browser not support canvas!!!
        </canvas>
    </body>
</html>

#+END_SRC


** 保存和恢复canvas状态
save()和restore()方法可以实现对坐标变换状态的保存和恢复
注意:可以连续多次调用save(), 则状态会放入队列中, 每次restore进行一次出队
调用的基本形式
#+BEGIN_SRC javascript
context.save();
//do something
context.restore();
#+END_SRC


** HTML5音频和视频

*** 在HTML5中播放音频
基本形式:
#+BEGIN_SRC html
<audio controls = "controls">
	<source src = "horse.ogg" type="audio/ogg"/>
	<source src = "horse.mp3" type="audio/mpeg"/>
	Your Browser not support audio, Fuck IE
</audio>
#+END_SRC

*** 在HTML5中播放视频
基本形式:
#+BEGIN_SRC html
<video width="320" height="240" controls = "controls">
	<source src = "movie.mp4" type="video/mp4"/>
	<source src = "movie.ogg" type="video/ogg"/>
	Your Browser not support video, Fuck IE
</video>
#+END_SRC
注意: 通常的视频只能播放声音, 需要专程AVC(H264)格式的才行

*** 具体实例:
#+BEGIN_SRC html
<!DOCTYPE html>
<html>
	<head lang="en">
	  <title>audio_video_demo</title>
	  <meta charset="utf-8"/>
	</head>

    <body>
        <audio controls = "controls">
	        <source src = "media/Weight of the World.mp3" type="audio/mpeg"/>
	        Your Browser not support audio, Fuck IE
        </audio>
        <br/>
        <video controls = "controls">
	        <source src = "media/OnlyMyRailgun.mp4" type="video/mp4"/>
	        Your Browser not support video, Fuck IE
        </video>
    </body>
</html>

#+END_SRC

*** 相关属性
src
autoplay
buffered
controls
currentSrc
currentTime
defaultPlaybackRate
duration
loop
muted
networkState
paused
playbackRate
played
preload
readyState
seekable
seeking
volume

*** 相关方法
canPlayType() 判定浏览器是否能够播放此视频, 返回probably-可能行非常高 maybe-有可能可以 ""-不支持
load() 重新加载视频音频
pause() 暂停
play() 播放

*** 相关事件
canplay
canplaythrough
durationchange
loadeddata
loadedmetadata
loadstart
progress
abort
ended
error
pause
play
playing
ratechange
seeked
seeking
stalled
suspend
timeupdate
volumechange
waiting


* CSS3
** 基本概述
CSS 是指层叠样式表(Cascading Style Sheets)

CSS 决定了


```