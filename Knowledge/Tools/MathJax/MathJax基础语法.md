# MathJax基础语法

## 显示公式
在行中显示的 (inline mode)，就用 $...$ 
单独一行显示 (display mode)，则用 $$...$$

## 希腊字母
要显示希腊字母，可以用 \alpha, \beta, …, \omega，输出α,β,…ω 
想要显示大写的话，就用 \Gamma, \Delta, …, \Omega, 输出 Γ,Δ,…,Ω
例如:
$$\alpha + \Gamma$$
## 上下标
上下标可用 ^ 和 _, 比如$\log_2 x$ 显示2为底, x的对数
上下标符号只能用于接下来一个 Group，即单个字符，或一组花括号内的东西，比如 10的10次方 要写成$10^{10}$

## 括号
小括号、方括号直接输出，花括号要用 \{ 和 \} 
括号不会伸缩，如写 $(\frac{\sqrt x}{y^3})$ 
如果需要伸缩(这里伸缩指在表达式变高后自动变高)，
就需要用 \left(…\right) 来进行自动伸缩，如写 $\left(\frac{\sqrt x}{y^3}\right)$ 

\left 和 \right 的用法在这些中有用：三种括号，绝对值符号 $\vert x \vert $，范数符号，$\Vert x \Vert$ ，尖角符号 $\langle x \rangle$ ⟨x⟩，向上下取整符号 $\lceil x\rceil$ 和 $\lfloor x\rfloor$。如果只需显示一半的符号，可以用 . 来表示另一边为空，如$\left. \frac 1 2 \right \rbrace$ 
当然也可以手动调整括号的大小，如$\Biggl(\biggl(\Bigl(\bigl((x)\bigr)\Bigr)\biggr)\Biggr)$ 
## 求和与积分
求和符号:$\sum_1^n$
积分符号$\int_1^n$ 
也有Group的概念，不止一位时需要花括号
类似的还有连乘号 $\prod$、并集$\bigcup$、交集$\bigcap$ 、多重积分 $\iint$等。

## 分数
有两种方法来显示分数，一种是 $\frac a b$ 来显示a\b，另一种是用 \over， 如${a+1 \over b+1}$ 显示 a+1 \ b+1

## 根号
一般根号:$\sqrt {x^3}$
三次根号: $\sqrt[3] {\frac x y}$

## 三角函数、极限和对数
像 “lim”, “sin”, “max”, “ln”等符号，已包括在roman 字体中，用 \lim等即可，极限可用$\lim_{x\to 0}$来表示

## 特殊符号和记号
有很多，以下是一小部分： 
- $\lt \gt \le \ge \neq$ ，还可以在不等号上加\not，如 $\not\lt$ 
- $\times \div \pm \mp$ ，点乘用\cdot表示,如 $x \cdot y$
- 集合类符号，$\cup \cap \setminus \subset \subseteq \subsetneq \supset \in \notin \emptyset \varnothing$
- 组合数，${n+1 \choose 2k}$ 或 $\binom{n+1}{2k}$
- 箭头，$\to \rightarrow \leftarrow \Rightarrow \Leftarrow \mapsto$ 
- $\land \lor \lnot \forall \exists \top \bot \vdash \vDash$
- $\star \ast \oplus \circ \bullet$
- $\approx \sim \simeq \cong \equiv \prec \lhd$
- $\infty \aleph_0$ $\nabla \partial$ 表示 ∇∂，$\Im \Re$
- 取模，用\pmod，如$a \equiv b\pmod n$
- 省略号，底一点的中的省略用\ldots，如$a_1, a_2, \ldots ,a_n$ 中间位置的的省略用\cdots，如$a_1 + a_2 + \ldots + a_n$

## 空格
MathJax中加入空格不会改变表达式，如果想在表达式中加空格，根据空格的不同，可用$\, \; \quad \qquad ab$
如果想加入一段文字，可用\text{…}，如$\\{x \in s \mid x \text{ is extra large}\\}$，在\text{…}里面还可以嵌套$…$

## 帽(hat)等
重音符可用\hat，如$\hat x$
变音符可用\widehat，如$\widehat {xy}$
$\bar x$ $\overline {xyz}$ 
如果用点号，可用\dot和\ddot，如可用$\frac d{dx}x\dot x = \dot x^2 + x\ddot x$

## 转义符
一般情况下可用\来作转义，但如果想要表示\本身，需要用$\backslash$，因为\\表示换行。