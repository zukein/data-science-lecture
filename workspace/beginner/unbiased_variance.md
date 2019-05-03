
## 標本分散の不偏性の証明
---

確率変数 $X$ について

$
\left\{\begin{aligned}
    E( X) & =\mu \\
    V( X) & =\sigma ^{2}
\end{aligned}\right.
$

標本分散 $s^2$ を

$
\begin{align}
    s^{2} & =\frac
        {{\displaystyle \sum ^{n}_{i=1}\left( X_{i} -\overline{X}\right)^{2}} }
        {n-1}\\
     \\
     & =\frac
         {\left( X_{1} -\overline{X}\right)^{2} +\left( X_{2} -\overline{X}\right)^{2} +\dots +\left( X_{n} -\overline{X}\right)^{2}}
         {n-1}
\end{align}
$

とおき、確率変数 $Y=X-\mu$ とすると、期待値の性質 (線型性 $E( aX+bY) =aE( X) +bE( Y)$ ) より

$
\begin{align}
    E( Y) & =E( X-\mu )\\
     & =E( X) -E( \mu )\\
     & =\mu -\mu \\
     & =0
\end{align}
$

$Y$ から抽出された標本の標本平均 $\bar{Y}$ は

$
\begin{align}
    E\left(\overline{Y}\right) & =E\left(\overline{X} -\mu \right)\\
     & =E\left(\overline{X}\right) -E( \mu )\\
     & =\mu -\mu \\
     & =0
\end{align}
$

となる。

したがって、

$
\begin{align}
    E\left( s^{2}\right) & =E\left(\frac
        {{\displaystyle \sum ^{n}_{i=1}\left( X_{i} -\overline{X}\right)^{2}} }
        {n-1}
    \right)\\
     \\
     & =\frac
         {E\left({\displaystyle \sum ^{n}_{i=1}\left(( X_{i} -\mu ) -\left(\overline{X} -\mu \right)\right)^{2}} \right)}
         {n-1}\\
     \\
     & =\frac
         {E\left({\displaystyle \sum ^{n}_{i=1}\left( Y_{i} -\overline{Y}\right)^{2}} \right)}
         {n-1}\\
     \\
     & =\frac
         {E\left({\displaystyle \sum ^{n}_{i=1}\left( Y^{2}_{i} -2\overline{Y} Y_{i} +\overline{Y}^{2}\right)} \right)}
         {n-1}\\
     \\
     & =\frac
         {E\left({\displaystyle \sum ^{n}_{i=1} Y^{2}_{i} -2\overline{Y}\sum ^{n}_{i=1} Y_{i} +\sum ^{n}_{i=1}\overline{Y}^{2}} \right)}
         {n-1}\\
     \\
     & =\frac
         {E\left({\displaystyle \sum ^{n}_{i=1} Y^{2}_{i} -2n\overline{Y}^{2} +n\overline{Y}^{2}} \right)}
         {n-1}
     \ \because \sum ^{n}_{i=1} Y_{i} =n\overline{Y} ,\ \sum ^{n}_{i=1}\overline{Y}^{2} =n\overline{Y}^{2}\\
     \\
     & =\frac
         {E\left({\displaystyle \sum ^{n}_{i=1} Y^{2}_{i}} \right) -n\overline{Y}^{2}}
         {n-1}
\end{align}
$

ここで、

$
\begin{align}
    V( Y) & =E\left(( Y-\mu _{Y})^{2}\right) & \\
     & =E\left( Y^{2} -2\mu _{Y} Y+\mu ^{2}_{Y}\right) & \\
     & =E\left( Y^{2}\right) -2\mu _{Y} E( Y) +\mu ^{2}_{Y} & \\
     & =E\left( Y^{2}\right) & \because E( Y) =\mu _{Y} =0
\end{align}
$

([分散の計算](mean_and_variance.ipynb#variance)参照)

また、

$
\begin{align}
    V(Y) & =V(X) \\
    & =\sigma^2
\end{align}
$

よって、

$
\begin{align}
    E\left(\sum ^{n}_{i=1} Y^{2}_{i}\right) & =nE\left( Y^{2}\right)\\
     & =nV( Y)\\
     & =n\sigma ^{2}
\end{align}
$

さらに、

$
\begin{align}
    \overline{Y}^{2} & =V\left(\overline{Y}\right) &  & \because \mu _{\overline{Y}} =0\\
     & =V\left(\frac
         {X_{1} +X_{2} +\dots +X_{n}}
         {n}
     \right) &  & \\
     & =\frac
         {V( X_{1} +X_{2} +\dots +X_{n})}
         {n^{2}}
     &  & \because V( aX) =a^{2} V( X)\\
     & =\frac
         {n\sigma ^{2}}
         {n^{2}}
     &  & \\
     & =\frac
         {\sigma ^{2}}
         {n}
     &  & 
\end{align}
$

したがって、

$
\begin{align}
    E\left( s^{2}\right) & =\frac
        {E\left({\displaystyle \sum ^{n}_{i=1} Y^{2}_{i}} \right) -n\overline{Y}^{2}}
        {n-1}\\
     \\
     & ={\displaystyle \frac
         {{\displaystyle n\sigma ^{2} -n\frac{\sigma ^{2}}{n}} }
         {n-1}} \\
     \\
     & =\frac
         {( n-1) \sigma ^{2}}
         {n-1}\\
     \\
     & =\sigma ^{2}
\end{align}
$
