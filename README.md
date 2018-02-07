# Random walk #

### Problem ###
The city is defined in N x N dimension, where two blocks(squares) represent the starting point and the 'home' point. What is the combination of 'start' and 'home' block so that people of the city can random walk their way back in the shortest manner.

### Appraoch ###
For each possibility of start and home block in the city, test out the random walking. For each possible combination of 'start' and 'home', 50 random walkers are tested to track the distance they took to arrive home. At the end of each combination of blocks, the average distance of the 50 walkers are recorded along with the positions of the 'start' and 'home'. 

### Assumption ###
When the random walker reach the boundary, the walker cannot move past the boundary (e.g. walker cannot move left when the x-position is at 0). However this is still considered as a movement in this algorithm. 

