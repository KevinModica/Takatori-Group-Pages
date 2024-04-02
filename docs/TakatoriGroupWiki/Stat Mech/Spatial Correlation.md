

Microscopic density:
$$
\rho_A(\mathbf{r}) = \sum_i^{N_{A}} \delta(\mathbf{r} - \mathbf{r}_i)
$$

For discrete cases, the delta function is approximated by a rectangular kernel. $\Pi(\frac{r-r_{ij}}{\Delta r})/\Delta r$

If the system is considered isotropic
$$
\xi_2(|x_2-x_1|) = \langle \delta(x_2) \delta(x_1) \rangle
$$

See [[rdf_explained.pdf]]

The radial distribution function is given as:

$$
g_{AB}(r) = 
\lim_{dr \rightarrow 0}\frac{n_{AB}(r)}{(N_{pairs}/V_{tot})4\pi r^2 dr}$$
$N_{pairs} = N (N-1)$ if $A$ is $B$, otherwise $N_{pairs} = N_AN_B$ 

So most people will have $N_{pairs}/V_{tot} = \rho (N-1)$ or $N_{pairs}/V_{tot} = \rho_A N_B$
or $N_{pairs}/V_{tot} = \rho_B N_A$ 


### For particles of the same type


$$
g_{AA}(r) = \sum_{i=1}^{N-1} \sum_{j=1, j\neq i}^N \frac{\delta(r-r_{ij})}{\rho (N-1) V_{shell}(r)}
$$
The complexity of the calculation can be simplified by recognizing that there are pairs we can skip over and avoid counting twice the long way. 

$$
g_{AA}(r) = \sum_{i=1}^{N-1} \sum_{j=i+1}^N 2\frac{\delta(r-r_{ij})}{\rho (N-1) V_{shell}(r)}
$$
For the purpose of calculation, we divide the function into bins of size $\Delta r$, making a histogram instead of the delta function. 

$$
g_{AA}(r) = \sum_{i=1}^{N-1} \sum_{j=i+1}^N 2\frac{\Pi(\frac{r-r_{ij}}{\Delta r})/\Delta r}{\rho (N-1) V_{shell}(r)}
$$

Where $\Pi(\frac{r-r_{ij}}{\Delta r})/\Delta r$ is the rectangle kernel approximation to the delta function. 



### For different types
$$
g_{AB}(r) = \sum_{i=1}^{N_A} \sum_{j=1}^{N_B} \frac{\delta(r-r_{ij})}{\rho_B N_A V_{shell}(r)}
$$

