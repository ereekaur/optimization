
 Suppose we have a sparse binary matrix containing information about watched movies meaning that
1 = watched and 0 = not watched. Our aim is to consider a problem of movie recommendation for certain user. Suppose that 100000 users have all liked
the same particular movie. Let A be a 100000 x 1000 matrix where $A_{ij}$ tells that user i has watched the movie j. Consider

$${\color{green}
\begin{equation*}
max ~c^t x \quad
Ax \leq b \quad
x \geq 0
\end{equation*}}
$$

 <p float="left" align= "center">
 <img src="https://raw.githubusercontent.com/ereekaur/finance/main/SPARSE.png" width="400" height="400">
  <em>100x100 block from the matrix A </em>
</p>


where c is a weight vector, b contains the maximum amount of movies we want to recommend. Note that in the case of square matrix it is well-known that the time complexity is at most polynomial as the
Gauss-Jordan method has the time complexity of $O(n^3)$. For solving rectangle systems the system is usually being transformed into equation form and then so called Simplex method is introduced in which at every
iteration step one checks the values at the vertices which are intersection points of the linear subspaces constructed from the constraints. There also exist so called interior point methods in which the convergence
towards to the solution is made within interior points. From the picture

<p float="left" align= "center">
 <img src="https://raw.githubusercontent.com/ereekaur/finance/main/SimplexVsHighs.png" width="400" height="400">
</p>

it comes clear that for our 100000 x 1000 matrix we would need ridiculous amount of time to solve the system using (revised) simplex method; interior point methods are more efficient. Here I used Python library called linprog and compared
the Highs and Revised simplex. For a 100000 x 1000 matrix the calculation using highs took roughly one minute. Can this be reduced further? As our matrix does not have any a priori structure to take advantage it might be good idea to 
consider matrix reordering i.e. find permutation of rows and columns which reduces fill-in when factorizing the system.

