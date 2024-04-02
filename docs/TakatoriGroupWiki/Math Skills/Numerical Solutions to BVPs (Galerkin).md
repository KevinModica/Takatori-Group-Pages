

See: Graham and Rawlings Modeling and Analysis Principles for Chemical and Biological Engineers Section 2.9 (pg. 208-220)


There are basically two ways to make a continuous problem (like an ODE or PDE) into a discrete problem.

1. Choose a finite number of points (values of the independent variable) and find an approximate solution there. (ex. Finite Difference)
2. Approximate the original function as a finite number of basis functions that are valid over the whole domain. (FEM, Galerkin, Spectral)

We will focus on the second way in this page.

## Method of Weighted Residuals

Given a linear function

$$
Lu=f(x) \; x\in [a,b]
$$
We choose a set of **trial functions** $\{\phi_i(x)\}$ as our basis to numerically approximate $u$ with $u_n$.

$$
u \approx u_n \;, \; u_n(x) = \sum_{j=1}^n c_j \phi_j(x)
$$
For now, assume that the trial functions satisfy homogeneous boundary conditions (??). 

Additionally, we assume as $n \rightarrow \infty$ , $u_n \rightarrow u$. But for finite $n$, there is a residual (or error) described by.

$$
R(x) = Lu_n(x) -f(x)
$$
So that if $u=u_n$, $R = 0$ everywhere.

We want $R(x)$ to be as small as possible, but how do you define the "smallness" of a function? Using the inner product to get a scalar!

We choose a set of **test functions** (or weight functions) $\{\psi_i(x)\}$ and require that.

$$
\langle R,\psi_i \rangle =0, \; i= 1,2,...,n
$$

So that the residual is **orthogonal** to all test functions. This is important, because the residual $R$ may be nonzero for any finite $n$ test functions, but as $n \rightarrow \infty$ , the only option that gives a zero inner product for infinitely many test functions is the 0 function $R(x) = 0$ everywhere. 

Now, we can plug our definition for $R$ into the above equation, and get.


$$
\langle L u_n(x) -f(x) , \psi_i(x) \rangle = 0 ,\; i=1,2,...,n
$$
Suppressing the $x$ dependence we get.
$$
\langle L \left(\sum_{j=1}^nc_j\phi_j\right) -f , \psi_i \rangle = 0 ,\; i=1,2,...,n
$$

$$
\sum_{j=1}^n  \langle L \phi_j , \psi_i \rangle c_j = \langle f,\psi_i\rangle ,\; i=1,2,...,n
$$

If you squint, you can see that we have written a matrix equation.

$$
A_{ij}c_j=b_i $$
$$ A_{ij} = \langle L\phi_j(x),\psi_i(x)\rangle, \; \; b_i = \langle f(x),\psi_i(x) \rangle 
$$
Note that $A_{ij}$ and $b_i$ do not depend on $x$ because they are the defined by the inner product (as functionals maybe?). And $c_j$ doesn't depend on $x$ because it is just a coefficient.


### Galerkin Methods: Test Function = Trial Function

$\psi_i(x) = \phi_i(x)$. If the trial functions or orthogonal, this approach forces the first $n$ terms in the representation of $R$ in the trial function basis to vanish. (??)


### Collocation Methods: Test function = Delta Function

$\psi_i(x) = \delta(x-x_i)$ where $\{x_i\}$ is a set of collocation points. Since $\langle R(x),\delta(x-x_i)\rangle = R(x_i)$, the collocation method simply requires the residual to be zero at the chosen set of points. You have to find that set of points. 


# Types of Galerkin Methods


WIP
## Finite Element Galerkin

The trial functions are low-order piecewise polynomials localized to small subsets of the domain, known as elements, and are zero elsewhere. 


## Fourier Galerkin and Eigenfunction expansion


## Legendre Galerkin Method



# Types of Collocation Method
## Chebyshev Collocation


