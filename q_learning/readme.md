# Q-learning algorithm for solving gym "FrozenLake" problem

Frozen lake is a board with 16 positions (states). There is 33% probability of slipping to neighboring
cell while taking next step.
The problem is solved by:
* Sampling/playing n-random steps and filling several tables:
- rewards
- transitions
- values
