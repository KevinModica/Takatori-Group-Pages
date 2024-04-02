Aka: What does SO(3) that have to do with rotations?

## Modica's Maxims
1. Mathematicians have very precise and unintuitive definitions for seemingly common words.
2. When they run out of common words, they make up ones to compensate.


# Sets
Sets are just a collection of element, this is the broadest classification. Often these are represented with curly braces.
Ex:
	Set of natural numbers $\mathbb{N} =\{0,1,...\}$
	Set of integers $\mathbb{Z} =\{...,-1,0,1,...\}$
	Set of rational numbers $\mathbb{Q}$ (fractions $p/q$ with $p, q$ ∈ $\mathbb{Z}$ and $q \neq 0$)
	Set of: Real numbers $\mathbb{R}$, complex numbers $\mathbb{C}$ and so on.

As far as I know, it doesn't need to follow any particular rules. 

**According to wikipedia:** 
>"In a set, all that matters is whether each element is in it or not, so the ordering of the elements in roster notation is irrelevant (in contrast, in a [sequence](https://en.wikipedia.org/wiki/Sequence "Sequence"), a [tuple](https://en.wikipedia.org/wiki/Tuple "Tuple"), or a [permutation](https://en.wikipedia.org/wiki/Permutation "Permutation") of a set, the ordering of the terms matters). For example, {2,4,6} and {4,6,4,2} represent the same set."

# Monoids
A monoid is a set equipped with a binary operation "$\odot$" that has the following properties under that operation. So you would say something like, "This set is a monoid under this operation." Never just "this set is a monoid."

Rule 0: The output of the binary operation must be in the original set. (Usually this rule is included in the definition of the operation, not the definition of the monoid. But I'll keep it here for my sake.)
$$
\odot : M\times M \rightarrow M
$$
**Rule 1**: It has associativity for all $a,b,c \in M$.
$$
a\odot(b\odot c) = (a\odot b)\odot c 
$$
**Rule 2**: It has an element $e\in M$ that is the identity under that operation.
$$
a\odot e = e\odot a = a
$$

# Groups
Similar to monoids, groups are a misleading term. Because a set can never be a group all on its own. A set can be a group under an operation if it has certain properties under that operation.

A group has all the properties of the monoid, in addition to the concept of an "inverse".

A set "$\mathcal{S}$" is a group under a binary operation "$\odot$"  if and only if:


**Rule 0**: The output of the binary operation must be in the original set. (Again, this is often omitted, but I'm keeping it for my learning.)
$$
\odot : G\times G \rightarrow G
$$
**Rule 1**: It has associativity for all $a,b,c \in G$.
$$
a\odot(b\odot c) = (a\odot b)\odot c 
$$
**Rule 2**: It has an element $e\in G$ that is the identity under that operation.
$$
a\odot e = e\odot a = a
$$
**Rule 3** (new): For every $a\in G$, there is an element that is its inverse $a^{-1} \in G$.
$$
a\odot a^{-1} = a^{-1}\odot a = e
$$

## Abelian (or communitive) Groups 

A group is an abelian group if it is also communitive under that operation.
$$
a\odot b = b\odot a
$$


# Important Named Groups

## General Linear Group

The set of $n×n$ invertible matrices with real (or complex) coefficients is a group under matrix multiplication, with identity element the identity matrix $I_n$ . This group is called the general linear group and is usually denoted by $\mathbf{GL}(n, \mathbb{R})$ (or $\mathbf{GL}(n, \mathbb{C})$).

**NOTE: All General Linear Groups are non-abelian for $\mathbf{n\geq2}$ except for SO(2), (but O(2) or SL(2) are non-abelian.)**

- This means that matrix multiplication is not communitive in any dimension greater than $1\times1$ except for the special case that they are $2\times2$ rotation matrices.


### Orthogonal Group (subgroup of GLG)

The set of $n × n$ matrices $Q$ with real (**not complex**) coefficients such that the matrix transpose is equivalent to the matrix inverse $Q^T = Q^{-1}$. 
$$QQ^T = Q^T Q = I_n$$
is a group under matrix multiplication, with identity element the identity matrix $I_n$. This group is called the orthogonal group and is usually denoted by $\mathbf{O}(n)$.

### Special Linear Group (subgroup of GLG)

The set of $n × n$ invertible matrices $A$ with real (or complex) coefficients such that $\det(A) = 1$ is a group under matrix multiplication, with identity element the identity matrix $I_n$ . This group is called the special linear group and is usually denoted by $\mathbf{SL}(n, \mathbb{R})$ (or $\mathbf{SL}(n, \mathbb{C})$).

### Special Orthogonal Group (if it is both Special Linear and Orthogonal)

The set of $n × n$ invertible matrices $Q with real coefficients such that $Q^T=Q^{-1} and $\det(Q) = 1$ is a group under matrix multiplication, with identity element the identity matrix $I_n$. This group is called the special orthogonal group or rotation group and is usually denoted by $\mathbf{SO}(n)$.


