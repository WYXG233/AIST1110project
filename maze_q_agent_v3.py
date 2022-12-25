import numpy as np
import pandas as pd
from gym.spaces import discrete
import time

class UnsupportedSpace(Exception):
    pass

def init_q_table(state, column):
    table = pd.DataFrame(
        np.zeros((state, len(column)), dtype=float),
        columns=column,
    )
    return table

def encode(agent_location, width):
    """Convert the state vector into a scalar for indexing the Q-table"""
    # e.g. for size = 5, there are 5 x 5 x 5 x 5 = 625 states
    # state [1, 2, 3, 4] => (1 * 5 + 2) * 5 + 3) * 5 + 4 = 194
    i = int(agent_location[0])
    i *= width
    i += int(agent_location[1])
    return i

class QLearningTable:
    def __init__(self, observation_space, action_space, width, height, learning_rate=0.8, reward_decay=0.85, e_greedy=0.85, seed=0):
        if not isinstance(observation_space, discrete.Discrete):
            raise UnsupportedSpace('Observation space {} incompatible with {}. (Only supports Discrete observation spaces.)'.format(observation_space, self))
        if not isinstance(action_space, discrete.Discrete):
            raise UnsupportedSpace('Action space {} incompatible with {}. (Only supports Discrete action spaces.)'.format(action_space, self))
        self.observation_space = observation_space
        self.action_space = action_space
        self.action_n = action_space.n
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.width = width
        self.height = height
        self.seed = seed
        np.random.seed(seed)
        
        self._action_to_direction = {
            0: np.array([0, -1]),#up
            1: np.array([0, 1]),#down
            2: np.array([-1, 0]),#left
            3: np.array([1, 0]),#right
        }
        
        self.q_table = init_q_table(observation_space.n,column=['up', 'down', 'left', 'right'])
        
    def check_value(self, state_action):
        original_ = np.zeros(4)
        if np.array_equal(state_action, original_):
            return True
        else:
            return False
        
    def choose_action(self, observation):
        agent_location = observation['agent']
        location = encode(agent_location, self.width)
        state_action = self.q_table.iloc[location, :]
        #print(state_action)
        random_number = np.random.uniform(0, 1)
        if random_number > self.epsilon or self.check_value(state_action.values):
            #print('2')
            action = np.random.randint(0,4)
        else:
            state_action = state_action.reindex(
                np.random.permutation(
                    state_action.index))  
            action = state_action.idxmax()
            #print('1')
            if action == 'up':
                action = 0
            if action == 'down':
                action = 1
            if action == 'left':
                action = 2
            if action == 'right':
                action = 3
            #action = int(state_action.argmax())
        return action
    
    def learn(self, obs1, a, r, obs2, done):
        if a == 0:
            action = 'up'
        if a == 1:
            action = 'down'
        if a == 2:
            action = 'left'
        if a == 3:
            action = 'right'
        agent_location_1 = obs1['agent']
        location_1 = encode(agent_location_1, self.width)
        
        q_predict = self.q_table.loc[location_1, action]
        agent_location_2 = obs2['agent']
        location_2 = encode(agent_location_2, self.width)
        
        if not done:
            q_target = r + self.gamma * self.q_table.loc[location_2, :].values.max()
        else:
            q_target = r
            
        self.q_table.loc[location_1, action] += self.lr * (q_target - q_predict)
    
    def save_txt(self):
        q_table = self.q_table.values
        filename = f"trained_model/maze_{self.width}x{self.height}_{self.seed}.txt"    
        np.savetxt(filename, q_table, fmt='%f')
        
        