# TensorFlow基本运算

## 创建矩阵
```
# 创建一个4行3列的常矩阵
W = tf.constant(np.random.randn(4, 3), name="W")
```

## 矩阵加法
```
tf.add(A, B)
```
## 矩阵乘法
```
tf.matmul(A, B)
```