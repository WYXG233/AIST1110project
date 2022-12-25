import gym
import gym_maze.envs
import pygame
import sys
from cmdargs import args
from maze_q_agent_v3 import encode

render_mode = args.mode

episodes = args.episodes
max_steps = args.max_steps
width, height = args.width, args.height

env = gym.make('Maze-v0', render_mode=render_mode, width=width, height=height, seed = args.seed)
env = gym.wrappers.TimeLimit(env, max_episode_steps=max_steps)

if args.fps is not None:
    env.metadata["render_fps"] = args.fps
    
observation, info = env.reset(seed=args.seed)

episode = 0
success_episodes = 0
running = True
step = 0
count = 0

while running and episode < episodes:
    action = None
    if args.mode == "human_control":
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    action = 0
                if event.key == pygame.K_DOWN:
                    action = 1
                if event.key == pygame.K_LEFT:
                    action = 2
                if event.key == pygame.K_RIGHT:
                    action = 3
                if event.key == pygame.K_ESCAPE:
                    running = False         
            if event.type == pygame.QUIT:
                running = False
    else:
        action = env.action_space.sample()  # random
        
    if action is not None:
        if count == 1:
            observation, info = env.reset(seed=args.seed)
            #print(observation['agent'][0])
            episode += 1
            step = 0
            count = 0
            continue
        observation, reward, truncated, done, info = env.step(action)
        #print(observation)
        print(episode, action, observation, reward, info)
        agent = observation['agent']
        #print(encode(agent,width))
        step += 1
        if done or truncated:
            if done:
                print(f"Episode {episode} succeeded in {step} steps ...")
                success_episodes += 1
            else:
                print(f"Episode {episode} truncated ...")
            print('If you want to start a new game, click any direction button!')
            if count == 0:
                count += 1
            
if episode > 0:
    print(f"Success rate: {success_episodes/episode:.2f}")

env.close()
