# TensorFlow安装_基础使用

## 安装
`pip3 install tensorflow`
这里最好使用python3, 发现python2下一些科学计算包的运行效果不理想

## 导入
```
import tensorflow as tf
```

## 当提示CPU特性警告时
提示
`Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX AVX2`
可以通过如下代码来消除这个
```
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
```

## 基本使用
声明TensorFlow变量`w = tf.Variable()`
例子:
寻找w, 使得`w**2 - 10*w + 25`最小
```python
import tensorflow as tf

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# w是想要优化的变量
w = tf.Variable(0, dtype=tf.float32)
# 构建成本函数
# cost = tf.add(tf.add(w**2, tf.multiply(-10., w)), 25)
cost = w**2 - 10*w + 25  # tensorFlow重载了基本运算, 也可以用上面的形式
# 设置学习率为0.01, 并要求使用梯度下降法最小化cost
train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
# 构建参数初始值
init = tf.global_variables_initializer()
session = tf.Session()
session.run(init)
print(session.run(w))

session.run(train)
print(session.run(w))

for i in range(1000):
    session.run(train)
print(session.run(w))
```

## 当需要外接提供参数时
`tf.placeholder`声明一个承载数据的结构, 等待外接输入
在训练时, 使用`session.run(train, feed_dict={x:coef})`对数据赋值

```python
import numpy as np
import tensorflow as tf

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 在这里提供方程的系数
coefficients = np.array([[1.], [-10.], [25.]])

# w是想要优化的变量
w = tf.Variable(0, dtype=tf.float32)
# 声明x是一个等待后续补充的数据
x = tf.placeholder(tf.float32, [3, 1])
# 构建成本函数
cost = x[0][0]*w**2 + x[1][0]*w + x[2][0]
# 设置学习率为0.01, 并要求使用梯度下降法最小化cost
train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
# 构建参数初始值
init = tf.global_variables_initializer()
session = tf.Session()
session.run(init)
print(session.run(w))

session.run(train, feed_dict={x: coefficients})  # 将待补充的x填上
print(session.run(w))

for i in range(1000):
    session.run(train, feed_dict={x: coefficients})
print(session.run(w))
```
