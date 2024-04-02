

The most exact definition of a rigid body $\mathcal{B}$ is as a collection of points or a manifold that encloses a region. 

For convenience, a rigid body (like rods or active particles) can be mapped onto a set of state variables describing their **position** and **orientation**. 

Assuming a Cartesian coordinate system, the position of a body center of mass (relative to the origin) is described by a **vector** $\vec{x}$

$$
\vec{x}(t) 
\begin{align}
     &= \begin{bmatrix}
           x_{1} \\
           x_{2} \\
           x_{3}
         \end{bmatrix}
  \end{align}
$$

The orientation of a body (relative to some reference orientation) is described by a **matrix** $\vec{\vec{R}}$ 

$$
\vec{\vec{R}}(t) 
\begin{align}
     &= \begin{bmatrix}
           R_{1,1} & R_{1,2} & R_{1,3}  \\
           R_{2,1} & R_{2,2} & R_{2,3} \\
           R_{3,1} & R_{3,2} & R_{3,3}
         \end{bmatrix}
  \end{align}
$$

**I stress that the orientation of a body is always in reference to some reference/initial orientation.** 
This is not always obvious, and in the future, we may take shortcuts by omitting the reference our orientation is based on.  **Even though there are 9 entries in the matrix, there are only 3 independent components of the matrix.**   

## Position and Orientation 
(from [[Rigidbody_ref.pdf]])
The location of a particle in space at time t can be described as a vector x(t), which describes the translation of the particle from the origin. Rigid bodies are more complicated, in that in addition to
translating them, we can also rotate them. To locate a rigid body in world space, we’ll use a vector
x(t), which describes the translation of the body. **We must also describe the rotation of the body,
which we’ll do (for now) in terms of a 3 × 3 rotation matrix R(t). We will call x(t) and R(t) the
spatial variables of a rigid body.**

A rigid body, unlike a particle, occupies a volume of space and has a particular shape. Because a
rigid body can undergo only rotation and translation, we define the shape of a rigid body in terms of a fixed and unchanging space called body space. Given a geometric description of the body in body space, we use x(t) and R(t) to transform the body-space description into world space (Figure 1).

![Pasted image 20231017155324](Pasted%20image%2020231017155324.png)

In order to simplify some equations we’ll be using, we’ll require that our description of the rigid body in body space be such that the center of mass of the body lies at the origin, (0, 0, 0). We’ll define the center of mass more precisely later, but for now, the center of mass can be thought of as a point in the rigid body that lies at the geometric center of the body. In describing the body’s shape, we require that this geometric center lie at (0, 0, 0) in body space. If we agree that R(t) specifies a rotation of the body about the center of mass, then a fixed vector r in body space will be rotated to the world- space vector R(t)r at time t. Likewise, if p0 is an arbitrary point on the rigid body, in body space, then the world-space location p(t) of p0 is the result of first rotating p0 about the origin and then translating it:


# Python Code example

```python
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from matplotlib import cm

def f(x, y):
    return np.sqrt(x ** 2 + y ** 2)
```

First we create a rigid body as a collection of points.

$\mathcal{B} = [\vec{x}_1 \; \vec{x}_2 \; \vec{x}_3 \; \cdots]$



```python
u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:80j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = f(x, y)
rBody = np.vstack([x.ravel(),y.ravel(),z.ravel()])


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(rBody[0,:], rBody[1,:], rBody[2,:], c= rBody[2,:])
ax.set_xlabel('x');
ax.set_ylabel('y');
ax.set_zlabel('z');
```


    
![png](rb_2023output_2_0.png)
    



```python
Rmat = np.array([[1,0,0],
				 [0,0,-1],
				 [0,1,0]])

rotatedrBody = Rmat@rBody

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter(rotatedrBody[0,:], rotatedrBody[1,:], rotatedrBody[2,:], c= rBody[2,:])
#colored by old coordinates to demonstrate
ax.set_xlabel('x');
ax.set_ylabel('y');
ax.set_zlabel('z');
```

    
![png](rb_2023output_3_1.png)
    



See:
https://rotations.berkeley.edu/kinematics-of-rigid-bodies/
https://www.cs.cmu.edu/~baraff/sigcourse/notesd1.pdf


