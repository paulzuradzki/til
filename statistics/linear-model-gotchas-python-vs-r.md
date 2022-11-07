# Linear Model Gotchas with Python vs R

# Problem

* You would think the ordinary least squares regression outputs would be consistent and deterministic between Python and R given that the solution to multiple linear regression is pretty simple and elegant.
  * $\hat{\beta} = \left(  X^\top X  \right)^{-1}X^\top y$
  * For more, see: https://book.stat420.org/multiple-linear-regression.html#matrix-approach-to-regression
  * However, for ill-posed problems like reduced rank (a.k.a., rank deficient) design matrices where the number of observations is greater than the number of parameters, Python and R currently have different implementations on how to handle that scenario.

# Discussion

A design matrix $X_{n \times p}$ is rank-deficient if (i) $p>n$ or (ii) $n > p$ but rank(X) < p (e.g., some columns are identical). When $X$ is rank deficient, solutions to the least squares problem are not unique. That is, the set
$B = \{ \tilde{\beta}: \| y - X \tilde{\beta}\|^2 = \min_{\beta}  \| y - X \beta\|^2\}$
contains more than one element. 

- R picks one of the most sparse solutions (well, such solutions may not be unique either), i.e., pick $\beta$ from the set $B$ with the smallest $\|\beta\|_0$. 

- Python picks $\beta$ from the set $B$ with the smallest $\|\beta\|_2$. 
