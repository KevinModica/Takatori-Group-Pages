
Start with this primer: [SphericalHarmonicInfo](SphericalHarmonicInfo.pdf)
See [Quaternions](Quaternions.md)
The rotation operator $\mathcal{R}$ (called $\nabla_1$ in the above pdf) is used commonly in liquid crystal or active matter literature. It is equivalent to the gradient in spherical coordinates on a unit sphere (aka no radial component).

Given a Cartesian vector on the unit disk or sphere: $\vec{u}$ 
Vector Form:
$$
\mathcal{R} = \vec{u}\times \frac{\partial}{\partial \vec{u}}
$$

--------
In 3D: ($\theta$ is polar ($0,\pi$), $\phi$ is azimuthal ($0,2\pi$))
$$
\mathcal{R}f = \hat{\theta}\frac{\partial f}{\partial \theta} + \hat{\phi}\frac{1}{\sin(\theta)}\frac{\partial f}{\partial \phi}
$$

$$
\mathcal{R}^2f = \frac{1}{\sin(\theta)}\frac{\partial}{\partial \theta}\left(\sin(\theta) \frac{\partial f}{\partial \theta}\right) + \frac{1}{\sin^2(\theta)}\frac{\partial^2 f}{\partial \phi^2}
$$
-----
In 2D: ($\phi \in 0,2\pi$)

$$
\mathcal{R}f = \hat{\phi}\frac{\partial f}{\partial \phi} 
$$
$$
\mathcal{R}^2f = \frac{\partial^2 f}{\partial \phi^2} 
$$
----



# 3D Notes:
Given a Cartesian basis $\hat{e}_x$,$\hat{e}_y$,$\hat{e}_z$ we can right the vector $\vec{u}$ on a unit sphere as:
$$
\vec{u}(t) 
\begin{align}
     &= \begin{bmatrix}
           \sin(\theta)\cos(\phi) \\
           \sin(\theta)\sin(\phi) \\
           \cos(\theta)
         \end{bmatrix}
  \end{align}
$$


The eagle-eyed amongst you might recognize that the rotational gradient operator is related to $\vec{u}$. 

$$
\mathcal{R} = \vec{u}\times \frac{\partial}{\partial \vec{u}}
$$
To actually figure this out, it requires a TON of steps, you will need to incorporate [Chain Rule for Partial and Total Derivatives](Chain%20Rule%20for%20Partial%20and%20Total%20Derivatives.md)


I'm not going to do all of them, but I'll show you the x component to discuss some important pitfalls and subtleties.

https://planetmath.org/derivationofthelaplacianfromrectangulartosphericalcoordinates

For example: finding the $x$-component of the vector derivative will involve:
$$
\frac{\partial f}{\partial u_x} = \frac{\partial f}{\partial \theta}\frac{\partial \theta}{\partial u_x} + \frac{\partial f}{\partial \phi} \frac{\partial \phi}{\partial u_x}
$$

### IMPORTANT NOTE
You might think you can just do it the by taking the reciprocals of the partial derivatives! But that isn't correct.

That is because in this case:
$$\frac{\partial \theta}{\partial u_x}\neq \frac{1}{\partial u_x /\partial \theta} \;, \; \frac{\partial \phi}{\partial u_x}\neq \frac{1}{\partial u_x /\partial \phi}
$$
So in this case:
$$
\frac{\partial f}{\partial u_x} \neq\frac{\partial f}{\partial \theta}\frac{1}{\cos(\theta)\cos(\phi)} + \frac{\partial f}{\partial \phi} \frac{1}{(-\sin(\theta)\sin(\phi))}
$$

You can only flip a partial derivative if we hold the same variables constant. (Like in thermo when we say $[\left(\frac{\partial y}{\partial z}\right)_z = \frac1{\left(\frac{\partial x}{\partial y}\right)_z}]$). 
	See: [Conditions for Inverting Partial Derivatives](https://math.stackexchange.com/questions/4125401/sufficient-conditions-for-partial-derivative-reciprocal)

So in our scenario, we can be more explicit. When we were writing the partial derivatives before, what we were implying was $\frac{\partial \theta}{\partial u_x}|_{u_y,u_z}$ and $\frac{\partial u_x}{\partial \theta}|_{\phi}$ with the variables in the subscripts held constant. As you can see, these are not holding the same variables constant, and as such they aren't reciprocals of each other.

### Important Note 2
Even though this is on the unit sphere: $r = 1$, we can't use that r is a constant in the context of our derivatives because then we have an over-specified problem.

E.g. : $\frac{\partial \theta}{\partial u_x}|_{u_y,u_z}$ means, change x very slightly while keeping y and z constant. To do that means we are by definition going to be changing r. 

$r=\sqrt{(x+\Delta x)^2 + y^2 + z^2} = \sqrt{x^2 + 2\Delta x + \Delta x^2 + y^2 + z^2} = \sqrt{r_0^2+ 2\Delta x+\Delta x^2}$ See the schematic below. We are trying to find the $\Delta \theta / \Delta x$ 

![[Pasted image 20231114154403.png]]

So in the process of performing a derivative, $r$ can vary, and then at the end of the calculation you set it to 1.


$\theta = \cos^{-1}(\frac{u_z}{\sqrt{u_x^2+u_y^2 + u_z^2}})$ therefore $\frac{\partial \theta}{\partial u_x}|_{u_y,u_z} = \cos{(\theta)}\cos{(\phi)}$
$\phi = tan^{-1}(\frac{u_y}{u_x})$ therefore $\frac{\partial \phi}{\partial u_x}|_{u_y,u_z} = -\frac{u_y}{u_x^2+u_y^2}= -\frac{u_y}{1-u_z^2} =-\frac{\sin(\theta)\sin(\phi)}{\sin^2{(\theta)}} =-\sin(\phi)\csc(\theta)$ 

$$
\frac{\partial f}{\partial u_x}|_{u_y,u_z} =  \cos(\phi)\cos(\theta)\frac{\partial f}{\partial \theta} -\sin(\phi)\csc(\theta)\frac{\partial f}{\partial \phi} 
$$

Then to get the rotational gradient operator we would need the other components and then take the cross product. 


Other notes:

[TensorHarmonicsList2D.pdf](TensorHarmonicsList2D.pdf)
[TensorHarmonicsList3D](TensorHarmonicsList3D.pdf)
[RotationalGradientOp.pdf]([RotationalGradientOp.pdf)
[SphericalHarmonicLore](SphericalHarmonicLore.pdf)




