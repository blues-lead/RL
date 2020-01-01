# Q-learning algorithm for solving gym "FrozenLake" problem

Frozen lake is a board with 16 positions (states). There is 33% probability of slipping to neighboring
cell while taking next step.
The problem is solved by:
* Sampling/playing n-random steps and filling several tables:
<<<<<<< HEAD
	* rewards - dict storing rewards. As keys there are (state, action, new_state) values
	* transitions - dict storing all states, where lead one step. As keys there are (state, action) values.
	* values - dict storing value of each state

At first in "main"-function (such function must be here, but being laze I didn't write it) agent plays 100 random episodes
filling rewards, transitions and values dicts. Then agent plays 20 episodes calculating the best possible actions being
in particular state.
=======
  * rewards
  * transitions
  * values
>>>>>>> ea08a345ee7f72ae8d5b0eb71c0466e39d9c47f4
