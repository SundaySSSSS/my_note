# MathJax矩阵
# 基本表示

注意, 在markdown下, 换行需要四个\， 而不是标准MathJax的两个\(Markdown本身进行了一次转义)
$$
\begin{matrix}
	1 & x & x^2 \\\\
	1 & y & y^2 \\\\
	1 & z & z^2 \\\\
\end{matrix}
$$

## 矩阵两端的括号
通过改变{matrix}来实现, 效果如下
### 圆括号
$$
\begin{pmatrix}
	1 & x & x^2 \\\\
	1 & y & y^2 \\\\
	1 & z & z^2 \\\\
\end{pmatrix}
$$
### 方括号
$$
\begin{bmatrix}
	1 & x & x^2 \\\\
	1 & y & y^2 \\\\
	1 & z & z^2 \\\\
\end{bmatrix}
$$
### 花括号
$$
\begin{Bmatrix}
	1 & x & x^2 \\\\
	1 & y & y^2 \\\\
	1 & z & z^2 \\\\
\end{Bmatrix}
$$
### 两条竖线(行列式)
$$
\begin{vmatrix}
	1 & x & x^2 \\\\
	1 & y & y^2 \\\\
	1 & z & z^2 \\\\
\end{vmatrix}
$$
