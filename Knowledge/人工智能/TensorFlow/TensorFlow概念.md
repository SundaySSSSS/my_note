# TensorFlow概念

## 常量(constant)
```
a = tf.constant(2)
y_hat = tf.constant(36, name='y_hat') 
```

## 变量(Variable)
```
loss = tf.Variable((y - y_hat)**2, name='loss')
```

## placeholder
placeholder是一个能稍后赋值的对象
```
x = tf.placeholder(tf.int64, name = 'x') # 此时并未指定x的值, 需要之后feed进去
```
