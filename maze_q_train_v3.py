import gym_maze.envs
from maze_q_agent_v3 import QLearningTable
import pandas as pd
import numpy as np
import gym
from cmdargs import args
import matplotlib.pyplot as plt
from tqdm import tqdm
import copy

def plot_graph(list_):
    fig = plt.figure(figsize=(8, 6))
    lenth = len(list_)
    plt.plot(range(1, lenth + 1),list_)
    plt.xlabel('Episode')
    plt.ylabel('Training total reward')
    plt.title('Total rewards over all episodes in training')
    plt.show()

def update(RL, episodes):
    reward_dict = {}
    reward_list = []
    t = tqdm(range(episodes), ncols=70)
    for episode in t:
        t.set_description(f"Training process: {episode:0>5}")
        whole_reward = 0
        # initial observation
        observation = env.reset(seed = args.seed)
        observation = observation[0]#tuple contain dict
        while True:
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(observation)
            # RL take action and get next observation and reward
            observation_, reward, terminated, done, info = env.step(action)
            #if it stop at the original position, punish it
            """if np.array_equal(observation['agent'], observation_['agent']) and not done:
                reward -= 0.001
                #done = True
            #if it get close to target, reward will increase
            distance_1 = np.linalg.norm(observation['agent'] - observation['target'])
            distance_2 = np.linalg.norm(observation_['agent'] - observation_['target'])
            if distance_2 < distance_1 and not done:
                if observation['agent'] not in reward_dict:
                    reward_dict[observation['agent']] = 1
                    reward += 0.001"""
            # RL learn from this transition
            RL.learn(observation, action, reward, observation_, terminated)
            # swap observation
            observation = copy.deepcopy(observation_)
            whole_reward += reward
            #print(RL.q_table)
            # break while loop when end of this episode
            if done or terminated:
                break
            
        reward_list.append(whole_reward)
        #print(f"time {len(reward_list)} has done")
    # end of game
    print('Training over')
    RL.save_txt()
    #env.destroy()
    env.close()
    return reward_list

if __name__ == "__main__":
    render_mode = args.mode
    episodes = args.episodes
    max_steps = args.max_steps
    width, height = args.width, args.height
    
    env = gym.make('Maze-v0', render_mode=render_mode, width=width, height=height, seed = args.seed)
    env = gym.wrappers.TimeLimit(env, max_episode_steps=max_steps)
    
    if args.fps is not None:
        env.metadata["render_fps"] = args.fps
    #episodes = 100
    
    RL = QLearningTable(env.observation_space, env.action_space, env.width, env.height, seed = args.seed)
    #print(RL.q_table)
    reward_list = update(RL, episodes)
    plot_graph(reward_list)
    