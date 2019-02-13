
## 平均 (期待値) と分散の性質
---
確率変数 $X,\ Y$ と定数 $c$ の間には以下の関係が成り立つ。

$
\begin{align}
    E( X+c) & =E( X) +c & ( 1)\\
    E( cX) & =cE( X) & ( 2)\\
    E( X+Y) & =E( X) +E( Y) & ( 3)\\
     &  & \\
    V( X+c) & =V( X) & ( 4)\\
    V( cX) & =c^{2} V( X) & ( 5)
\end{align}
$

## 分散の計算<a name="variance"></a>
---
分散 $V(X)=E(X^2)-\left(E(X)^2\right)$ で計算できる。

### 証明
---
分散の定義 $V(X)=E\left((X-\mu)^2\right)$ より

$
\begin{align}
    V( X) & =E\left( X^{2} -2\mu X+\mu ^{2}\right) &  & \\
     \\
     & =E\left( X^{2}\right) -2\mu E( X) +\mu ^{2} &  & \because ( 1)( 2)( 3)\\
     \\
     & =E\left( X^{2}\right) -2E( X)^{2} +E( X)^{2} &  & \because E( X) =\mu \\
     \\
     & =E\left( X^{2}\right) -E( X)^{2} &  & 
\end{align}
$

## 分散の加法性
---
確率変数 $X,\ Y$ が独立のとき、

$V(X\pm Y)=V(X)+V(Y)$

が成り立つ。

期待値 $\mu$ ・分散 $\sigma^2$ の同一の確率分布に従う複数の確率変数 $X_1,\ X_2,\ \dots,\ X_n$ の場合には

$V(X_1+X_2+\dots+X_n)=n\sigma^2$
