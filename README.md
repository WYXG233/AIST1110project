# Maze Game Project
This is our maze game project for AIST 1110.
## Intro
We are group 14, and this file contains our game project for AIST1110. 

Firstly, we build a gym environment called MazeEnv, and it has three render_modes: "human_control", "human_view", and "rgb_array". In "human_control", you can control the game agent through the arrow keys on the keyboard. And in "human_view", you can watch the screen to see what the computer is doing, but you can't influence it through the keyboard or mouse. As for "rgb_array", this is a faster model for computer to play, which is more recommended to be used in training model.

Besides, we also generate a Q-Learning program to train our model. In this maze game, our Q-table has just {width} * {height} states because to ensure the reproducibility of the results, we use the seed of random number to regulate the state of each board. Therefore, in this case, the path and end point of the maze are determined. Our Q-table only needs the location of the agent to represent the entire observation space.

I guess you can't wait to play or train the model by yourself(maybe not?!), so let's get started!

## Dependency
------------------------------
To run our program, firstly you need a Python :).

1. python >= 3.9.

After that, you can download the following packages easily through:
`pip install {package name}` for each package.
Or you can simply run:
`pip install -r requirement.txt`

1. colorama

1. gym

1. matplotlib

1. numpy

1. pygame

1. pandas

1. tqdm

## Running
------------------------------

### human_control

you can play our maze game through the following code:
`python maze_play_v1.py -m human_control {other command line arguments}`
then you can use your arrow keys to control the little bear to home. You can add more command line arguments(cla) after that to try more cases, and the cla will be introduced later.

### human_view
you can watch our maze game playing by gym through the following code:
`python maze_play_v2.py -m human_view {other command line arguments}`
then you can see the little bear will start walking randomly, and may not be able to find the path after many tries. That's why we need the training to let it know how to get back home.

### train
you can train our Q-Learning model through the following code:
`python maze_train_v3.py {other command line arguments}`
then the program will start to learn how to find the path.The efficiency and results of training depend on the set maximum steps and training times.

### test
you can test our Q-Learning model through the following code:
`python maze_qtest.py {other command line arguments}`
it will output the total success rate after 1000 times tries.

## Command Line Argument
------------------------------

|Name or Flags|Type|Description|Choices|Metavar|Default|
|:---:|:----:|:----:|:----:|:----:|:----:|
|-m, --mode|str|The render mode|human_view, human_control,rgb_array|None|rgb_array|
|-w, --width|int|The grid width|range(9,16)|[9 – 15]|9|
|-he, --height|int|The grid height|range(9,16)|[9 – 15]|14|
|-s, --seed|int|The seed for random number generator|None|None|None|
|-e, --episodes|int|The number of episodes|None|None|1000|
|-ms, --max_steps|int|The maximum number of steps in an episode|None|None|100|
|-fps, --fps|int|The rendering speed in frames per second|None|None|None|
|-f, --file|str|The file name of the Q-table file|None|None|None|

## Reference
------------------------------
Some part of our code(the function init_maze and surroundingCells) in `maze_env.py` are from https://github.com/OrWestSide/python-scripts/blob/master/maze.py, we use it to generate our maze board.
