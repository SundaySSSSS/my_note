# Python获取用户输入


## input
```
x = input("x: ")
```
## raw_input
```
name = raw_input("What is your name")
```
## 区别
input认为用户输入的是一个Python表达式
例如
```
x = input("x: ")
输入20, 则会认为x是一个数值, 而非字符串
```
raw_input无论输入什么都认为是字符串