import gym
import pygame
from gym import spaces
import numpy as np
import random
import time
from colorama import init
from colorama import Fore, Back, Style

def surroundingCells(rand_wall,maze):
	s_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
		s_cells +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
		s_cells += 1
	return s_cells

def init_maze(width = 27,height = 11):
	wall = 'w'
	cell = 'c'
	unvisited = 'u'
	maze = []

	init()

	for i in range(0, height):
		line = []
		for j in range(0, width):
			line.append(unvisited)
		maze.append(line)

	starting_height = int(random.random()*height)
	starting_width = int(random.random()*width)
	if (starting_height == 0):
		starting_height += 1
	if (starting_height == height-1):
		starting_height -= 1
	if (starting_width == 0):
		starting_width += 1
	if (starting_width == width-1):
		starting_width -= 1

	# Mark it as cell and add surrounding walls to the list
	maze[starting_height][starting_width] = cell
	walls = []
	walls.append([starting_height - 1, starting_width])
	walls.append([starting_height, starting_width - 1])
	walls.append([starting_height, starting_width + 1])
	walls.append([starting_height + 1, starting_width])

	# Denote walls in maze
	maze[starting_height-1][starting_width] = 'w'
	maze[starting_height][starting_width - 1] = 'w'
	maze[starting_height][starting_width + 1] = 'w'
	maze[starting_height + 1][starting_width] = 'w'

	while (walls):
		# Pick a random wall
		rand_wall = walls[int(random.random()*len(walls))-1]

		# Check if it is a left wall
		if (rand_wall[1] != 0):
			if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
				# Find the number of surrounding cells
				s_cells = surroundingCells(rand_wall,maze)

				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = 'c'

					# Mark the new walls
					# Upper cell
					if (rand_wall[0] != 0):
						if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
							maze[rand_wall[0]-1][rand_wall[1]] = 'w'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])


					# Bottom cell
					if (rand_wall[0] != height-1):
						if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
							maze[rand_wall[0]+1][rand_wall[1]] = 'w'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])

					# Leftmost cell
					if (rand_wall[1] != 0):	
						if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
							maze[rand_wall[0]][rand_wall[1]-1] = 'w'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])
				

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Check if it is an upper wall
		if (rand_wall[0] != 0):
			if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == 'c'):

				s_cells = surroundingCells(rand_wall,maze)
				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = 'c'

					# Mark the new walls
					# Upper cell
					if (rand_wall[0] != 0):
						if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
							maze[rand_wall[0]-1][rand_wall[1]] = 'w'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])

					# Leftmost cell
					if (rand_wall[1] != 0):
						if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
							maze[rand_wall[0]][rand_wall[1]-1] = 'w'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])

					# Rightmost cell
					if (rand_wall[1] != width-1):
						if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
							maze[rand_wall[0]][rand_wall[1]+1] = 'w'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Check the bottom wall
		if (rand_wall[0] != height-1):
			if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c'):

				s_cells = surroundingCells(rand_wall,maze)
				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = 'c'

					# Mark the new walls
					if (rand_wall[0] != height-1):
						if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
							maze[rand_wall[0]+1][rand_wall[1]] = 'w'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])
					if (rand_wall[1] != 0):
						if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
							maze[rand_wall[0]][rand_wall[1]-1] = 'w'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])
					if (rand_wall[1] != width-1):
						if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
							maze[rand_wall[0]][rand_wall[1]+1] = 'w'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)


				continue

		# Check the right wall
		if (rand_wall[1] != width-1):
			if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c'):

				s_cells = surroundingCells(rand_wall,maze)
				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = 'c'

					# Mark the new walls
					if (rand_wall[1] != width-1):
						if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
							maze[rand_wall[0]][rand_wall[1]+1] = 'w'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])
					if (rand_wall[0] != height-1):
						if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
							maze[rand_wall[0]+1][rand_wall[1]] = 'w'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])
					if (rand_wall[0] != 0):	
						if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
							maze[rand_wall[0]-1][rand_wall[1]] = 'w'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Delete the wall from the list anyway
		for wall in walls:
			if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
				walls.remove(wall)

	for i in range(0, height):
		for j in range(0, width):
			if (maze[i][j] == 'u'):
				maze[i][j] = 'w'
	return maze

class MazeEnv(gym.Env):
    metadata = {"render_modes": ["human_control", "human_view", "rgb_array"], "render_fps": 4}
    
    def __init__(self, render_mode=None, width=10, height = 10, seed = None):
        self.width = width
        self.height = height
        
        self.cell_size = 50
        self.window_width = self.height * self.cell_size
        self.window_height = self.width * self.cell_size # The size of the PyGame window
        #print('init')
        if seed != None:
            random.seed(seed)
            np.random.seed(seed)
        self.maze = init_maze(self.width, self.height)

        self.observation_space = spaces.Discrete(self.height * self.width)
        # We have 4 actions, corresponding to "right", "up", "left", "down"
        self.action_space = spaces.Discrete(4)
        self.n_actions = self.action_space.n
        
        self._action_to_direction = {
            0: np.array([0, -1]),#up
            1: np.array([0, 1]),#down
            2: np.array([-1, 0]),#left
            3: np.array([1, 0]),#right
        }

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

        self.window = None
        self.clock = None
        self.startime = 0
        self.endtime = 0
        self.step_number = 0 
        self.has_music = self.has_bgm = self.has_position =  0
        self._original_agent = np.array([0, 0])
        self._original_target = np.array([0, 0])
        
    def _get_obs(self):
        return {"agent": self._agent_location, "target": self._target_location}
    
    def _get_info(self):
        return {"distance": np.linalg.norm(self._agent_location - self._target_location, ord=1)}

    def generate_location(self):
        Cell_position = []
        count_i = count_j = 0
        for i in self.maze:
            for j in i:
                if self.maze[count_i][count_j] == 'c':
                    Cell_position.append((count_i,count_j))
                count_j += 1
            count_j = 0
            count_i += 1
        tmp = random.sample(Cell_position,2)
        while True:
            x1, y1 = tmp[0]
            x2, y2 = tmp[1]
            if abs(x1 - x2) + abs(y1 - y2) >= 7:
                break
            else:
                tmp = random.sample(Cell_position,2)  
        position_home_x, position_home_y = tmp[0]
        position_people_x, position_people_y = tmp[1]
        self._agent_location = np.array([position_people_x, position_people_y])
        self._target_location = np.array([position_home_x, position_home_y])
        self._original_agent[0] = int(self._agent_location[0])
        self._original_agent[1] = int(self._agent_location[1])
        self._original_target[0] = int(self._target_location[0])
        self._original_target[1] = int(self._target_location[1])
        #print(self._original_agent, self._original_target)
        #print('change')
        self.has_position = 1
    
    def reset(self, seed=None, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)
        
        # Choose the agent's location
        if self.render_mode == "human_control" :
            self.generate_location()
        elif not self.has_position:
            self.generate_location()
        else:
            self.has_position = 1
            #print('reset')
            self._agent_location[0] = int(self._original_agent[0])
            self._agent_location[1] = int(self._original_agent[1])
            self._target_location[0] = int(self._original_target[0])
            self._target_location[1] = int(self._original_target[1])
        #print(self._original_agent)
        observation = self._get_obs()
        info = self._get_info()
        self.startime = self.endtime
        self.step_number = 0
        self.has_bgm = 0
        if self.has_music:
            pygame.mixer.stop()
            self.has_music = 0
        if (self.render_mode == "human_view") or (self.render_mode == "human_control"):
            self._render_frame()

        return observation, info
    
    def Valid_move(self,direction):
        position_x, position_y = self._agent_location
        if direction == 0:#up
            if position_y - 1 >= 0:
                if self.maze[position_x][position_y - 1] == 'c':
                    return True
        if direction == 1:#down
            if position_y + 1 < self.width:
                if self.maze[position_x][position_y + 1] == 'c':
                    return True
        if direction == 2:#left
            if position_x - 1 >= 0:
                if self.maze[position_x - 1][position_y] == 'c':
                    return True
        if direction == 3:#right
            if position_x + 1 < self.height:
                if self.maze[position_x + 1][position_y] == 'c':
                    return True
        return False
    
    def step(self, action):
        
        self.step_number += 1
        # Map the action (element of {0,1,2,3}) to the direction we walk in
        direction = self._action_to_direction[action]
        #distance_1 = abs(self._agent_location[0] - self._target_location[0]) + abs(self._agent_location[1] - self._target_location[1])
        # We use `np.clip` to make sure we don't leave the grid
        if self.Valid_move(action):
            self._agent_location += direction
        # An episode is done iff the agent has reached the target
        terminated = np.array_equal(self._agent_location, self._target_location)
        #distance_2 = abs(self._agent_location[0] - self._target_location[0]) + abs(self._agent_location[1] - self._target_location[1])
        reward = 1 if terminated else 0
        observation = self._get_obs()
        info = self._get_info()

        if (self.render_mode == "human_view") or (self.render_mode == "human_control"):
            self._render_frame()
            if self.render_mode == "human_control":
                self.move_wav.play()
        
        done = self.finish_point()
        
        return observation, reward, terminated, done, info
    
    def render(self):
        if self.render_mode == "rgb_array":
            return self._render_frame()
    
    def finish_point(self):
        if np.array_equal(self._agent_location, self._target_location):
            self.endtime = time.time()
            return True
        else:
            return False
        
    def load_resources(self):
        #loading part
        self.bg_img = pygame.image.load("Picture/bg.png").convert() #background
        self.bg_img = pygame.transform.scale(self.bg_img,(self.height * self.cell_size,self.width * self.cell_size))
        self.bg_2img = pygame.image.load("Picture/bg2.png").convert() #background
        #self.bg_2img = pygame.transform.scale(self.bg_2img,(self.height * self.cell_size,self.width * self.cell_size))
        self.home_img = pygame.image.load("Picture/home.png").convert_alpha()#home
        self.home_img = pygame.transform.scale(self.home_img,(self.cell_size,self.cell_size))
        self.people_img = pygame.image.load('Picture/people.png').convert_alpha()#people
        self.people_img = pygame.transform.scale(self.people_img,(self.cell_size,self.cell_size))
        self.gameover_img = pygame.image.load("Picture/gameover.jpeg").convert()
        self.gameover_img = pygame.transform.scale(self.gameover_img,(self.height * self.cell_size,self.width * self.cell_size))
        self.move_wav = pygame.mixer.Sound("Sound/move.wav")
        self.move_wav.set_volume(0.2)
        self.startbgm_wav = pygame.mixer.Sound("Sound/startbgm.wav")
        self.startbgm_wav.set_volume(0.2)
        self.runningbgm_wav = pygame.mixer.Sound("Sound/runningbgm.wav")
        self.runningbgm_wav.set_volume(0.2)
        self.endbgm_wav = pygame.mixer.Sound("Sound/endbgm.wav")
        self.endbgm_wav.set_volume(0.2)

    def _render_frame(self):
        if self.window is None and ((self.render_mode == "human_view") or (self.render_mode == "human_control")):
            self.startime = time.time()
            pygame.init()
            pygame.mixer.init()
            self.has_music = 1
            pygame.display.init()
            self.window = pygame.display.set_mode((self.window_width, self.window_height))
            pygame.display.set_caption('Find Path to Home') #Title
            
        if self.clock is None and ((self.render_mode == "human_view") or (self.render_mode == "human_control")):
            self.clock = pygame.time.Clock()

        canvas = pygame.Surface((self.window_width, self.window_height))
        canvas.fill((255, 255, 255))

        '''
        step_text = font.render(f'Step: {Step}', True, pygame.Color('black'))
        self.window.blit(step_text, (8, 10))
        '''

        if self.render_mode == "human_control":
            self.load_resources()
            font = pygame.font.SysFont("Monospace", 30)
            if not self.has_bgm:
                self.runningbgm_wav.play(-1)
                self.has_bgm = 1
            if self.finish_point():
                self.runningbgm_wav.stop()
                pygame.mixer.stop()
                self.endbgm_wav.play(-1)
                
                step_text = font.render(f'Total Step: {self.step_number}', True, pygame.Color('white'))    
                totaltime = abs(self.startime - self.endtime)
                totaltime_text = font.render('Total Time : %.2f s'% totaltime, True, pygame.Color('white'))
                continue_text_1 = font.render('If you want to start a new game', True, pygame.Color('white'))
                continue_text_2 = font.render(', click any direction button!', True, pygame.Color('white'))
                self.window.blit(self.gameover_img,(0,0))
                self.window.blit(step_text,(int(self.cell_size / 2), self.cell_size))  
                self.window.blit(totaltime_text,(int(self.cell_size * (self.height /2) - 5), self.cell_size))
                self.window.blit(continue_text_1,(int(self.cell_size / 2), self.cell_size * (self.width - 2) + (self.cell_size / 2)))
                self.window.blit(continue_text_2,(int(self.cell_size * 2), self.cell_size * (self.width - 1)))
            # The following line copies our drawings from `canvas` to the visible window
            else:
                self.window.blit(canvas, canvas.get_rect())
                self.window.blit(self.bg_2img, (0, 0))
                self.window.blit(self.home_img, (int(self._target_location[0] * self.cell_size), int(self._target_location[1] * self.cell_size)))
                self.window.blit(self.people_img, (int(self._agent_location[0] * self.cell_size), int(self._agent_location[1] * self.cell_size)))
                count_i = count_j = 0
                for i in self.maze:
                    for j in i:
                        if self.maze[count_i][count_j] == 'w':
                            pygame.draw.rect(self.window , (0, 0, 0), (int(self.cell_size * count_i), int(self.cell_size * count_j),self.cell_size ,self.cell_size), width=1)
                        count_j += 1
                    count_j = 0
                    count_i += 1
                step_text = font.render(f'Step: {self.step_number}', True, pygame.Color('black'))
                self.window.blit(step_text, (8, 10))
            pygame.event.pump()
            pygame.display.update()

            # We need to ensure that human-rendering occurs at the predefined framerate.
            # The following line will automatically add a delay to keep the framerate stable.
            #self.clock.tick(self.metadata["render_fps"])
        elif self.render_mode == "human_view":
            self.load_resources()
            font = pygame.font.SysFont("Monospace", 30)
            self.window.blit(canvas, canvas.get_rect())
            self.window.blit(self.bg_2img, (0, 0))
            self.window.blit(self.home_img, (int(self._target_location[0] * self.cell_size), int(self._target_location[1] * self.cell_size)))
            self.window.blit(self.people_img, (int(self._agent_location[0] * self.cell_size), int(self._agent_location[1] * self.cell_size)))
            count_i = count_j = 0
            for i in self.maze:
                for j in i:
                    if self.maze[count_i][count_j] == 'w':
                        pygame.draw.rect(self.window , (0, 0, 0), (int(self.cell_size * count_i), int(self.cell_size * count_j),self.cell_size ,self.cell_size), width=1)
                    count_j += 1
                count_j = 0
                count_i += 1
            step_text = font.render(f'Step: {self.step_number}', True, pygame.Color('black'))
            self.window.blit(step_text, (8, 10))
            pygame.event.pump()
            pygame.display.update()
        else:  # rgb_array
            return np.transpose(
                np.array(pygame.surfarray.pixels3d(canvas)), axes=(1, 0, 2)
            )
            
    def close(self):
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()
    
if __name__ == '__main__':
    env = MazeEnv(render_mode = 'human_view')
    env.reset()
    print(env.observation_space)
    """for i in range(1000):
        env.step(env.action_space.sample())
        print(env._agent_location, env._target_location)"""
