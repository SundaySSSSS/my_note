# Logistic回归

## 基本概念
### 激活函数
**y^ = sigmoid(z) = 1 / (1 + e^-1^)**

### 损失函数(Less function)
预测值y^和真实值y之间的距离, 通常使用如下形式:
**L(y^, y) = -(ylogy^ + (1-y)log(1-y^))**

### 成本函数(Cost function)
**J(w, b) = (1 / m) * sum(L(y^i, yi)**

### 函数关系
**z =w^T^ x + b**
**y^ = sigmoid(z) = 1 / (1 + e^-1^)**
**L(y^, y) = -(ylogy^ + (1-y)log(1-y^))**
**J(w, b) = (1 / m) * sum(L(y^i, yi)**

## Logistic回归的目标
求合适的w和b, 使得J(w, b)最小

## 梯度下降法
目标: 最小化成本函数J(w, b)
计算出一次结果后, 在w, b方向上计算偏导, 在此方向上进行一次移动, 步长为a(自定义的学习率learning rate)
计算方法:
w := w - a * dJ(w, b) / dw
b := b - a * dJ(w, b) / db

## 计算流程
**z =w^T^ x + b  ->  a = y^ = sigmoid(z) -> L(a. y)**
1. 计算da
定义da = dL / da = -(y / a) + (1 - y) / (1 - a)

2. 计算dz
定义dz = dL / dz = (dL / da) * (da / dz) = a - y
(使用的求导的链式法则)

3, 计算dw和db
dwi = dL / dw = (dL / dz) * (dz / dwi) = (dL / dz) * (d(w^T^ + b) = (dL / dz) * xi = dz * dx
db = dL / db = dL / dz = dz

4, 对w和b进行一次迭代, 重复1 - 4
w := w - a * dJ(w, b) / dw
b := b - a * dJ(w, b) / db
