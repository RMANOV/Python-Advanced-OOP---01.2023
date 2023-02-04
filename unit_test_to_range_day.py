

import unittest

class TestTargets(unittest.TestCase):
  def test_shooted_targets(self):
    # given initial configuration where all targets are hit
    field = [[".", ".", "x", ".", "."], ["A", ".", "x", ".", "."], [".", ".", "x",
    "x", "."], [".", ".x", ".", ".", "."], [".", ".x", 	".",".","."]]

    global position, all_targets, shooted_targets, directions

    position = [[0, 2]] 
      for i in range(5) if ['A'] in field[i]][0] 

    count_of_commands = int('1') 

    directions = {"right": (0, 1),	"left": (0, -1),	"up": (-1, 0),	"down": (1, 0)}

    all_targets = sum([row.count('x') for row in field]) #3 targets on board  

    shooted_targets = [] #empty list of shooted targets 

    command = input("shoot right").split()  #command to shoot right 

      for _ in range('1'):    
        command = input().split()   #run the command to shoot right        
        if command[0] == 'shoot':
            direction = command[1]   #direction is right             
            new_position = (position[0] + directions[direction][0],  #calculate new position of target using direction      	     position[1] + directions[direction][1], )            
            while 0 <= new_position[0] < 5 and 0 <= new_position[1] < 5:                                               		if field[new_position[0]][new_position[1]] == 'x':   #if target found            	     field[new_position[0]][new_position[1]] == '.'          #aim at target                                                shooted.targets.append("MISSED!")                    break                         new