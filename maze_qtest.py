import gym
import gym_maze.envs
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from cmdargs import args
from maze_q_agent_v3 import encode
import pandas as pd

mode = args.mode
width, height = args.width, args.height
# for random agent, use play v1 script with -m human_control
assert mode != "human_control"

env = gym.make('Maze-v0', render_mode=mode, width=width, height=height, seed = args.seed)

if args.fps is not None:
    env.metadata["render_fps"] = args.fps

# Load the Q-table from file
filename = f"trained_model/maze_{width}x{height}_{args.seed}.txt"
if args.file is not None:
    filename = args.file
Q = np.loadtxt(filename)

# Test the agent
test_episodes = args.episodes
max_steps = args.max_steps

print("Testing started ...")
success_episodes = 0
t = tqdm(range(test_episodes), ncols=70)
for episode in t:
    t.set_description(f"Testing process: {episode:0>4}")
    state = env.reset(seed=args.seed)[0]  # [0] for observation only
    agent_location_1 = state['agent']
    state = encode(agent_location_1, width)
    #state = encode(state)
    total_testing_rewards = 0
    for step in range(max_steps):
        state_action = Q[state, :]     
        state_action = pd.DataFrame(state_action)
        state_action = state_action.reindex(
                np.random.permutation(
                    state_action.index))  
        action = int(state_action.idxmax())
        #print(action)
        #action = np.argmax(Q[state, :])
        #print(Q[state, :])
        new_state, reward, terminated, done, info = env.step(action) # take action and get reward      
        state = new_state
        # print(state, action)
        agent_location_1 = state['agent']
        state = encode(agent_location_1, width)
        if terminated: # End the episode
            #t.write(f"Episode {episode} succeeded in {step+1} steps ...")
            success_episodes += 1
            break
    #else:
        #t.write(f"Episode {episode} truncated ...")

print(f"Success rate: {success_episodes/test_episodes:.2f}")

env.close()
