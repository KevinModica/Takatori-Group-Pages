
Continuation of: [[Rigid Body Basics]]

As mentioned previously, the orientation of a body (relative to some reference orientation) is described by a **matrix** $\vec{\vec{R}}$ 

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
This is not always obvious, and in the future, we may take shortcuts by omitting the reference.


Rotations can be represented by a matrix (9 entries in 3D), but any rotation can be determined by just 3 degrees of freedom. A common and numerically convenient way is to store them as a unit quaternion (4 entries in 3D). Even though the matrix has 9 entries and the quaternion has 4, both are uniquely determined by just 3 degrees of freedom. (quaternion is a unit quaternion so the 4th entry is determined by the other 3, and the different elements of the matrix have different symmetries).

Also, using quaternions helps to prevent numerical drift. The compactness is related to the drift, the redundant properties of the rotation matrix means that if they lose their relationship that creates drift and error.

Many people describe a quaternion as a scalar $s$ and a vector $\mathbf{v}$, and then have something like $q = [s,\mathbf{v}]$.

**I prefer not to do that, because basis vectors and quaternions multiply differently.**

$$
q = w_0 +w_1 \mathbf{i} + w_2 \mathbf{j} + w_3 \mathbf{k}
$$
Multiplication two quaternions is done using the Hamilton product. It is similar to that of complex numbers, with some extra rules.

$\mathbf{i}^2 = \mathbf{j}^2 = \mathbf{k}^2 = -1$;
$\mathbf{ij} =\mathbf{k}$ , $\mathbf{ji} = -\mathbf{k}$;
$\mathbf{ik} = -\mathbf{j}$, $\mathbf{ki} = \mathbf{j}$;
$\mathbf{jk} = \mathbf{i}$, $\mathbf{kj} = -\mathbf{i}$;

![Pasted image 20231024143316](Pasted%20image%2020231024143316.png)

Therefore, a rotation of $\theta$ radians counterclockwise about a unit axis $\mathbf{u}$
is represented by the unit quaternion $q = \cos(\theta/2) + sin(\theta/2)\mathbf{u}$

In using unit quaternions to represent rotations, if $q_1$ and $q_2$ indicate rotations, then $q_2q_1$ represents the composite rotation of $q_1$ followed by $q_2$. **Note this notation can vary. Sometimes the order can reverse depending upon construction.**  

#### Converting a unit quaternion to a matrix is simple. The reverse has a lot of if statements.

https://en.wikipedia.org/wiki/Rotation_formalisms_in_three_dimensions#Rotation_matrix_%E2%86%94_quaternion

$$\vec{\vec{R}} = ...$$
 ![Pasted image 20231024141848](Pasted%20image%2020231024141848.png)


```python
#(this is a code I copied online, need to check validity)
def rotationMatrixToQuaternion1(m):
    #q0 = qw
    t = np.matrix.trace(m)
    q = np.asarray([0.0, 0.0, 0.0, 0.0], dtype=np.float64)
    if(t > 0):
        t = np.sqrt(t + 1)
        q[3] = 0.5 * t
        t = 0.5/t
        q[0] = (m[2,1] - m[1,2]) * t
        q[1] = (m[0,2] - m[2,0]) * t
        q[2] = (m[1,0] - m[0,1]) * t
    else:
        i = 0
        if (m[1,1] > m[0,0]):
            i = 1
        if (m[2,2] > m[i,i]):
            i = 2
        j = (i+1)%3
        k = (j+1)%3
        t = np.sqrt(m[i,i] - m[j,j] - m[k,k] + 1)
        q[i] = 0.5 * t
        t = 0.5 / t
        q[3] = (m[k,j] - m[j,k]) * t
        q[j] = (m[j,i] + m[i,j]) * t
        q[k] = (m[k,i] + m[i,k]) * t
    return q

```

### PS:  If you absolutely must describe them as a scalar and vector


$$
q = [s,\mathbf{v}]= s+v_x \mathbf{i} + v_y \mathbf{j} + v_z \mathbf{k}
$$

Then remember to describe multiplication like this.

$$
[s_1, \mathbf{v_1}][s_2,\mathbf{v_2}] = [s_1 s_2 - \mathbf{v_1} \cdot \mathbf{v_2}\;, \;s_1\mathbf{v_2} + s_2 \mathbf{v_1} + \mathbf{v_1} \times \mathbf{v_2}]
$$
