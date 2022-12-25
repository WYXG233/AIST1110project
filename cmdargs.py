import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--mode', type=str, help="The render mode",
                    choices=['human_view', 'human_control', 'rgb_array'], 
                    default='rgb_array')
parser.add_argument('-w', '--width', type=int, help='The grid width',
                    choices=range(9,16), metavar='[9-15]',
                    default=9)
parser.add_argument('-he', '--height', type=int, help='The grid height',
                    choices=range(9,16), metavar='[9-15]',
                    default=14)
parser.add_argument('-s', "--seed", type=int, 
                    help="The seed for random number generator", 
                    default=None)
parser.add_argument('-e', "--episodes", type=int, 
                    help="The number of episodes.", 
                    default=1000)
parser.add_argument('-ms', "--max_steps", type=int, 
                    help="The maximum number of steps in an episode", 
                    default=100)
parser.add_argument('-fps', "--fps", type=int, 
                    help="The rendering speed in frames per second",
                    default=None)
parser.add_argument('-f', "--file", type=str, 
                    help="The file name of the Q-table file",
                    default=None)
args = parser.parse_args()
print(args)
