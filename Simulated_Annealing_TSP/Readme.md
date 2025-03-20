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
