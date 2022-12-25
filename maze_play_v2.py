import gym
import gym_maze.envs
from gym.utils import play
import pygame
from cmdargs import args

render_mode = args.mode

episodes = args.episodes
max_steps = args.max_steps
width, height = args.width, args.height


env = gym.make('Maze-v0', render_mode=render_mode, width=width, height=height, seed = args.seed)

mapping = {
    (pygame.K_UP,): 0, 
    (pygame.K_DOWN,): 1,
    (pygame.K_LEFT,): 2,
    (pygame.K_RIGHT,): 3
}

play.play(env, keys_to_action=mapping, noop=None, fps=10)