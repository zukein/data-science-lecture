
## 母平均の区間推定
---

中心極限定理より、標本数が一定以上の場合には標本平均 $\bar{X}$ の標本分布は正規分布 $
N\left( \mu ,{\displaystyle \frac
    {\sigma ^{2}}
    {n}
} \right)
$ に近づく。この標本分布の両側 $\alpha \%$ 点を $N_{1-\frac{\alpha }{2}},N_{\frac{\alpha }{2}}$ とすると、確率変数 $\overline{X}$ が両側 $\alpha \%$ 点の内側に含まれる確率は

$
\displaystyle P\left( N_{1-\frac
    {\alpha }
    {2}
} < \overline{X} < N_{\frac
    {\alpha }
    {2}
}\right) =1-\alpha
$

で表される。

$\overline{X}$ を標準化した $
\displaystyle \frac
    {\overline{X} -\mu }
    {\sqrt{
        {\displaystyle \frac
            {\sigma ^{2}}
            {n}
        }
    }}
$ は標準正規分布 $N\left( 0,1\right)$ に従い、その両側 $\alpha \%$ 点を $
Z_{1-\frac
    {\alpha }
    {2}
},Z_{\frac
    {\alpha }
    {2}
}
$ とすると、

$
\displaystyle P\left( Z_{1-\frac
    {\alpha }
    {2}
} < \frac
    {\overline{X} -\mu }
    {\sqrt{
        {\displaystyle \frac
            {\sigma ^{2}}
            {n}
        }
    }}
< Z_{\frac
    {\alpha }
    {2}
}\right) =1-\alpha
$

標準正規分布では $
Z_{1-\frac
    {\alpha}
    {2}
}=-Z_{\frac
    {\alpha}
    {2}
}
$ なので、

$P\left( -Z_{\frac
    {\alpha }
    {2}
} < \frac
    {{\displaystyle \overline{X} -\mu } }
    {\sqrt{{\displaystyle \frac
        {\sigma ^{2}}
        {n}
    } }}
< Z_{\frac
    {\alpha }
    {2}
}\right) =1-\alpha $


$\mu$ について整理して

$P\left(\overline{X} -{\displaystyle \frac
    {\sigma }
    {\sqrt{n}}
} Z_{\frac
    {\alpha }
    {2}
} < \mu < \overline{X} +{\displaystyle \frac
    {\sigma }
    {\sqrt{n}}
} Z_{\frac
    {\alpha }
    {2}
}\right) =1-\alpha $

したがって、上の区間内に母平均 $\mu$ が $1-\alpha$ の確率で存在するが、母平均を推定しようとしている場合には一般に母標準偏差 $\sigma$ は未知なので求められない。

ここで、 $\displaystyle \frac{\overline{X} -\mu }{\sqrt{{\displaystyle \frac{\sigma ^{2}}{n}}}}$ の母分散 $\sigma ^{2}$ を標本分散 $s^{2}$ で置き換えた統計量 $t$ は

$
\begin{align}
    t & ={\displaystyle \frac
        {\overline{X} -\mu }
        {\sqrt{{\displaystyle \frac
            {s^{2}}
            {n}
        } }}
    } \\
     \\
     & =\frac
         {\frac
             {{\displaystyle \overline{X} -\mu } }
             {{\displaystyle \sqrt{\frac
                 {\sigma ^{2}}
                 {n}
             }} }
         }
         {{\displaystyle \frac
             {{\displaystyle \sqrt{\frac
                 {s^{2}}
                 {n}
             }} }
             {{\displaystyle \sqrt{\frac
                 {\sigma ^{2}}
                 {n}
             }} }
         } }\\
     \\
     & =\frac
         {\frac
             {{\displaystyle \overline{X} -\mu } }
             {{\displaystyle \sqrt{\frac
                 {\sigma ^{2}}
                 {n}
             }} }
         }
         {{\displaystyle \sqrt{\frac
             {s^{2}}
             {\sigma ^{2}}
         }} }\\
     \\
     & =\frac
         {\frac
             {{\displaystyle \overline{X} -\mu } }
             {{\displaystyle \sqrt{\frac
                 {\sigma ^{2}}
                 {n}
             }} }
         }
         {\sqrt{{\displaystyle \frac
             {1}
             {n-1}
         \frac
             {( n-1) s^{2}}
             {\sigma ^{2}}
         } }}
\end{align}
$

ここで $
Z=\frac
    {{\displaystyle \overline{X} -\mu } }
    {{\displaystyle \sqrt{
        \frac
            {\sigma ^{2}}
            {n}
    }} }
,\ \chi ^{2} ={\displaystyle \frac
    {( n-1) s^{2}}
    {\sigma ^{2}}}
$ とすると、

$
\begin{eqnarray}
    t=\frac
        {Z}
        {
            \begin{eqnarray}
                \sqrt{\frac
                    {\chi^2}
                    {n-1}
                }
            \end{eqnarray}
        }
\end{eqnarray}
$

$Z$ は標準正規分布 $N(0,\ 1)$ に従う。

$
\begin{align}
    \chi ^{2} & =\frac
        {( n-1) s^{2}}
        {\sigma ^{2}}\\
     & =\frac
         {( n-1)\frac
             {{\displaystyle \sum ^{n}_{i=1}\left( X_{i} -\overline{X}\right)^{2}}}
             {n-1}
         }
         {\sigma ^{2}}\\
     & =\sum ^{n}_{i=1}\frac
         {\left( X_{i} -\overline{X}\right)^{2}}
         {\sigma ^{2}}\\
     & =\sum ^{n}_{i=1}\left(\frac
         {X_{i} -\overline{X}}
         {\sigma }
     \right)^{2}
\end{align}
$

であり、これは 自由度 $n-1$ の $\chi^2$ 分布 $\chi^2(n-1)$ に従う。

そして、 $Z$ と $\chi^2$ は独立なので、 $t$ は自由度 $n-1$ の $t$ 分布に従う。

したがって、確率変数 $t$ が両側 $\alpha \%$ 点の内側に含まれる確率は

$
\displaystyle P( t_{1-\frac
    {\alpha }
    {2}
} < t< t_{\frac
    {\alpha }
    {2}
}) =1-\alpha
$

で表される。

$
\displaystyle t=\frac
    {\overline{X} -\mu }
    {\sqrt{
        {\displaystyle \frac
            {\sigma ^{2}}
            {n}
        }
    }}
$ より

$
\begin{array}{ c c c }
    P\left( t_{1-\frac
        {\alpha }
        {2}
    } < \frac
        {{\displaystyle \overline{X} -\mu } }
        {{\displaystyle \sqrt{\frac
            {s^{2}}
            {n}
        }} }
    < t_{\frac
        {\alpha }
        {2}
    }\right) & = & 1-\alpha \\
    \\
    P\left( -t_{\frac
        {\alpha }
        {2}
    } < \frac
        {{\displaystyle \overline{X} -\mu } }
        {{\displaystyle \sqrt{\frac
            {s^{2}}
            {n}
        }} }
    < t_{\frac
        {\alpha }
        {2}
    }\right) & = & 1-\alpha \\
    \\
    P\left(\overline{X} -{\displaystyle \frac
        {s}
        {\sqrt{n}}
    } t_{\frac
        {\alpha }
        {2}
    } < \mu < \overline{X} +{\displaystyle \frac
        {s}
        {\sqrt{n}}
    } t_{\frac
        {\alpha }
        {2}
    }\right) & = & 1-\alpha 
\end{array}
$

以上より、母平均 $\mu$ が $1-\alpha \%$ で含まれる範囲は、 $
\displaystyle \left(\overline{X} -\frac
    {s}
    {\sqrt{n}}
t_{\frac
    {\alpha }
    {2}
} ,\overline{X} +\frac
    {s}
    {\sqrt{n}}
t_{\frac
    {\alpha }
    {2}
}\right)
$ で表される。
