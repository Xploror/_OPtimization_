## Implementation
`Inputs as set of cartesian coordinates and number of annealing iteration` are fed to the algorithm where initially a distance matrix is calculated which is used to create an ising model that for this specific case considers distance as a metric for the ising interactions. After both the state matrix and the ising model is computed, these are used to simulate annealing to find optimal spin configuration using random sampling and continually updating the spin state matrix with each iteration to update the links. (Analogous to the Ising model implementation on electron spin configuration to achieve min energy possible)

## Functions
#### $$\color{green}{create\ distance\ matrix()}$$ - Inputs the list of 2D cartesian coordinates representing every point (can be extrapolated to 3D scenarios)
#### $$\color{green}{create\ ising\ model()}$$ - Inputs the the distance matrix for the entire graph and setups the initial ising model, state matrix and node vector to establish links and metrics.
#### $$\color{green}{update\ spin\ mat()}$$ - Inputs the node vector and the computed swap pair to update the node vector by diligently swapping the points. After the swaps the satte matrix is recomputed and th eresults reflect an update on the state matrix.
#### $$\color{green}{simulate\ annealing()}$$ - The simulated annealing iterative process is implemented in this function that inputs the ising model, initial state matrix, the node vector and the number of iterations. The `update_spin_mat()` is called within this function for each iteration and at each (time) epoch and an analogous energy is calculated for the whole system that tracks the minimum energy with each iteration.
#### $$\color{green}{find\ shortest\ path()}$$ - Main function that chronologically calls other functionalities.
<br>

<p align="center">
  <img width="460" height="300" src="https://github.com/user-attachments/assets/4f655d15-c916-4e08-a29d-bcbba89a1881">
</p>
<p align="center">
  Temporal visualization of the optimization
</p>

## Example Results:

### CASE-1: Uneven distribution

The image below shows the resulting path that the algorithm concluded as the most optimal trajectory to hop over all the nodes in the problem and returning back to the starting node. The starting node was taken as `(0,0)` with a total of `15 nodes unevenly spread`.

<p align="center">
  <img width="460" height="300" src="https://github.com/user-attachments/assets/93b74e15-c651-4811-b781-ba8fbf954ce3">
</p>

### CASE-2: Even distribution

The image below shows the resulting path that the algorithm concluded as the most optimal trajectory to hop over all the nodes in the problem and returning back to the starting node. The starting node was taken as `(0,0)` with a total of `18 nodes evenly spread`. 

> Note that due to the odd number of rows, the optimal path had to periodically go over the nodes jumping from one node to another in order to ultimately catch the last node that can bring it back to the last row to meet the origin.

<p align="center">
  <img width="460" height="300" src="https://github.com/user-attachments/assets/83e70173-2000-4b14-ab8a-678d1f3d3258">
</p>

### CASE-3: Circular Paths

The image below shows the resulting path that the algorithm concluded as the most optimal trajectory to hop over all the nodes in the problem and returning back to the starting node. The starting node was taken as `(0,0)` with a total of `32 nodes evenly spread`. `16 each nodes corresponding to the inner and outer circle`. Computation time around `~6mins`

<p align="center">
  <img width="460" height="300" src="https://github.com/user-attachments/assets/73b38ce6-7e6c-43f8-987c-3b75a10b7793">
  <img width="460" height="300" src="https://github.com/user-attachments/assets/905d12f3-8434-45d5-8032-5a6e9b7a38f8">
</p>
