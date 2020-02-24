```c++
#include <RcppArmadillo.h>
using namespace Rcpp;

// [[Rcpp::export]]
Rcpp::NumericVector matvec( Rcpp::NumericMatrix & A, Rcpp::NumericVector & x) {
    
    int nrow = A.nrow(), ncol = A.ncol();
    
    arma::mat X(A.begin(), nrow, ncol, false);
    arma::colvec y(x.begin(), nrow, false);
    
    for(int iter=0; iter<1000; ++iter) {
      y = X * y;
    }
    
    
    return x;
  }
```

```R
n <- 1000
A <- matrix(c(1:(n*n)),nrow=n,ncol=n)
x <- rep(1,n)
t0 <- Sys.time()
x = matvec(A, x)
t1 <- Sys.time()
print(t1-t0)
```
Time difference of 0.19031 secs
