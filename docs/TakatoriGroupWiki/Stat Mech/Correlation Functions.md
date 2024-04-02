#CorrelationFunctions

Correlation functions in general measure the covariance of random variables at different lag times $\tau$ and distances $r$.

Wikipedia provides a good mathematical description of the correlation function in statistical mechanics https://en.wikipedia.org/wiki/Correlation_function_(statistical_mechanics).

I also like this intro [Grigera_2021_J._Phys._Complex._2_045016](Grigera_2021_J._Phys._Complex._2_045016.pdf)


The most general description of correlation function is as the average of the scalar product of two random (possibly vectorial or tensorial) variables at a distance $\mathbf{r}$ and lag time $\tau$. 

$$
C_{v1,v2}(\mathbf{r},\tau) = \langle \mathbf{v}_1(\mathbf{R+r},t+\tau) \cdot \mathbf{v}_2^*(\mathbf{R},t) \rangle 
$$
*It is a matter of convention whether one subtracts the uncorrelated product.* $\langle \mathbf{v}_1(\mathbf{R+r},t+\tau)\rangle \cdot \langle \mathbf{v}_2^*(\mathbf{R},t)\rangle$ , but the uncorrelated product is often zero anyway. Similarly, it is a matter of convention whether to divide by the standard deviations of the individual variables. Generally I think it is good practice to do so though because it normalizes between 0 and 1, but that is not included in the formula above. 
**WIP Have to check how r is made a scalar?**


More commonly people split them into two **types** of correlation functions. 
1. A time correlation function, including auto-correlation. (aka the same particle or location changing with time so $\mathbf{r=0}$)
2. A spatial correlation function. (aka $\tau=0$)  (see [Radial distribution functions - GROMACS 2023.3 documentation](Radial%20distribution%20functions%20-%20GROMACS%202023.3%20documentation.pdf)
3. Radial distribution functions)

I then find it useful to consider the **calculation** of the correlation function in two ways:
1. The ***continuous*** way (aka the path of the theorist)
2. The ***discrete*** way (aka the path of the simulator)


# Time Correlation Functions
## Autocorrelation function
[ChemLibre link](https://chem.libretexts.org/Bookshelves/Biological_Chemistry/Concepts_in_Biophysical_Chemistry_(Tokmakoff)/06%3A_Dynamics_and_Kinetics/22%3A_Biophysical_Reaction_Dynamics/22.05%3A_Time-Correlation_Functions)
 #Autocorrelation 
Often, the correlation function is going to be the correlation of the **same value** across time.  (density - density, orientation - orientation, velocity - velocity). Cross correlations are more confusing and I will address those later.

The classical (auto)correlation function can be obtained rigorously from an equilibrium probability distribution as:
$$
C_{AA}(t−t')=\int dp\int dq\; P_{eq}(p,q)\left[\mathbf{A}(p,q;t)\cdot \mathbf{A}^*(p,q;t')\right]
$$
Think of this like the covariance of variable $\mathbf{A}$ at time $t$ and variable $A$ at time $t'$. $\mathrm{E}[A(t)A(t')]$ 

In practice, correlation function are more commonly obtained from trajectories by taking a time average -- not an expected value/ ensemble average like we did above:

$$
C_{AA}(\tau)=\overline{\mathbf{A}(τ)\cdot\mathbf{A}^*(0)}=\lim_{T\to∞} \frac{1}{T}\int^T_0 dt' \mathbf{A}(τ+t')\cdot \mathbf{A}^*(t')
$$

If the time-average value of $C_{AA}$ (as $T \rightarrow \infty$ ) is equivalent to the equilibrium ensemble average value of $C_{AA}$, we say the system is considered ergodic.

**Note: in the above expression, the "start" time $t'$ has no bearing on the autocorrelation.** If you expect that your start time $t'$ has importance (aka you are not at equilibrium), see ??? for what to do.


## Autocorrelation in practice: watch out.

You need to consider, what variable you are trying to get, and what is the order of operation you need to get it. 

Consider an MD simulation of $N_{part}$ particles running for time $T$. You are told to get the velocity autocorrelation for the system. You could interpret that as the:
1. Average of velocity autocorrelation. 
2. Autocorrelation of average velocity. 

**These are two different things, and you will get different answers if you compute them properly.**
#### 1. Average of velocity autocorrelation
For particle $i$, the autocorrelation will be.
$$C_{v_iv_i}(\tau)=\overline{\mathbf{v}_i(τ)\cdot\mathbf{v}_i^*(0)}=\lim_{T\to∞} \frac{1}{T}\int^T_0 dt' \mathbf{v}_i(τ+t')\cdot \mathbf{v}_i^*(t')$$ Then, the average of the velocity autocorrelation will be.

$$C_{vv}(\tau) = \frac{1}{N_{part}} \sum_{i=1}^{N_{part}} C_{v_iv_i}(\tau)$$ 
#### 2. Autocorrelation of average velocity 
Unless your system has some net drift, the average velocity of the system is going to be zero always. 

$$C_{\langle v \rangle\langle v \rangle}(\tau)=\lim_{T\to∞} \frac{1}{T}\int^T_0 dt' (\frac{1}{N_{part}} \sum_{i=1}^{N_{part}} \mathbf{v}_i(τ+t'))\cdot (\frac{1}{N_{part}} \sum_{i=1}^{N_{part}}\mathbf{v}_i^*(t'))$$
$$C_{\langle v \rangle\langle v \rangle}(\tau)=0$$
***Sometimes you might want autocorrelation of the average. Just make sure to think about which quantity you are going for.***

## In Practice: time autocorrelation function of discrete data.

For a scalar variable $f$ that depends on time (and particle index). We usually cannot get the analytic value of the integral.

$$
C_{ff}(\tau)=\lim_{T\to∞} \frac{1}{T}\int^T_0 dt' f(τ+t') f^*(t')
$$

In general, we can't get data for the limit of large $T$, but we simulate up until a certain time, and then approximate the integral using a Riemann sum.


$$
C_f(j\Delta t) = \frac{1}{N-j} \sum_{i=0}^{N-1-j} f((i+j)\Delta t)f^*(i\Delta t)
$$

This expression works, but it has some caveats. 
- The accuracy of the ACF is changes for different lag times. We have N-1 data points for $C_f(\Delta t)$, but only 1 data point for $C_f((N-1)\Delta t)$.  

If you care about having consistent accuracy, while losing long time information and sacrificing short time accuracy. Instead only use the first half or so of your data. For: $M \leq N/2$  

$$
C_f(j\Delta t) = \frac{1}{M} \sum_{i=0}^{N-1-M} f((i+j)\Delta t)f^*(i\Delta t)
$$


## Numerical Speedup
Correlation functions are a form of convolution (see [Convolutions](Convolutions.md)), which means they can be performed faster using an FFT. Usually this is too involved for what we need (especially for multidimensional data). Just including it because many packages will use the FFT formula under the hood. 




# Code Examples (from Chat GPT check.)

```python
import numpy as np

def autocorrelation(data):
    """
    Calculate the autocorrelation function of a complex variable.
    
    Parameters:
        data (numpy.ndarray): Array of complex numbers.
	    If data is real, you don't need np.conj(data)
    Returns:
        numpy.ndarray: Autocorrelation function.
    """
    n = len(data)
    acf = np.zeros(n)
    for lag in range(n):
        acf[lag] = np.sum(data[:n-lag] * np.conj(data[lag:]))
        acf[lag] /= n - lag
    return acf.real


```


```python
import numpy as np

def fast_autocorrelation(data):
    """
    Calculate the autocorrelation function of a complex variable.
    
    Parameters:
        data (numpy.ndarray): Array of complex numbers.
    
    Returns:
        numpy.ndarray: Autocorrelation function.
    """
    n = len(data)
    fft_data = np.fft.fft(data)
    acf = np.fft.ifft(fft_data * np.conj(fft_data))
    acf = acf[:n//2] / (n - np.arange(n//2))
    return acf.real

```


