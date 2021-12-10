'''
MATH 482: COMB ALGORITHMS
Project: Pizza Slice Instant Insanity
Group Members: Fernando Vargas, Brian Bales, Kinjal Patel, Gisela Calva, Angel Rinos
Purpose: The program below will take in a list of 3 sided pizza slices and attempt to stack them all, if it cannot then the program will display the minimum obstacle. 
'''
import math
from itertools import combinations

def patterns(value, patterNumber):
  if patterNumber == 1:
    pattern_value = 1 + ((math.floor(value*17*((math.pi)**6)) % 31))
  if patterNumber == 2:
    pattern_value = 1 + ((math.floor(value*17*((math.e)**6)) % 31))
  if patterNumber == 3:
    pattern_value = 1 + ((math.floor(value*17*((math.e)**8)) % 31))
  if patterNumber == 4:
    pattern_value = 1 + ((math.floor(value*11*((math.e)**8)) % 31))
  if patterNumber == 5:
    pattern_value = 1 + ((math.floor(value*101*((math.e)**2)) % 31))
  if patterNumber == 6:
    pattern_value = 1 + ((math.floor(value*101*((math.e)**8)) % 31))

  return pattern_value

# BELOW: Generates all the colors into an index in all_patterns
# EX. the values for pattern number 1 are in all_patterns[0]
def generate_colors(): #Returns a list of colors generated with max of 3 per color
  all_patterns = []
  puzzle_colors = []
  for i in range(1, 7):
    for j in range(1, 250):
        new_color = patterns(j, i)
        if(puzzle_colors.count(new_color) > 2):
          continue #skip that color
        else:
          puzzle_colors.append(new_color)
    all_patterns.append(puzzle_colors)
    puzzle_colors = []
  return all_patterns

def list_split(givenList, n): #splits the list into subsets of 3
  for x in range(0, len(givenList), n):
      every_chunk = givenList[x: n+x]

      if len(every_chunk) < n:
          every_chunk = every_chunk + \
              [None for y in range(n-len(every_chunk))]
      yield every_chunk


def split_list(all_patterns): #appends the subsets as a list into a master list of 6 total subsets
  new_list_split = []
  master_list = []
  for i in range(0, 6):
    new_list_split = list(list_split(all_patterns[i], 3))
    master_list.append(new_list_split)
   # print("\n\nPuzzle #" + str(i+1)+ " number of slices: " + str(len(master_list[i])))
   ## print(new_list_split)

  return master_list



# ABOVE: Generating Colors for all Puzzles
#-------------------------------------------------------------

def rotate_right(listHere): #Change this name
  listHere = listHere[-1:] + listHere[:-1]
  return listHere

def isSolution(orig_list_main): #CheckSolutions
  orig_list = orig_list_main.copy()
  #print(f"Looking for a solution for the list:")
  first_face = []
  second_face = []
  third_face = []
  rotations_list = [0] * len(orig_list) #0s for size of list
  sec_list = []

  for i in range(0, 1):
    first_face.append(orig_list[0][0])
    second_face.append(orig_list[0][1])
    third_face.append(orig_list[0][2])

  i = 1
  while(i < len(orig_list)):
    original_sec = orig_list[i]
    flag = 0
    while(orig_list[i][0] in first_face or orig_list[i][1] in second_face or orig_list[i][2] in third_face): #wont be true during obstacle
      #print(i)
      rotations_list[i] += 1
      rotations_list[i] = rotations_list[i] % 3
      #rotate_right()
      #print(f"BEFORE IF: {orig_list}")

      if(rotations_list[i] != 0): #we have to rotate
        sec_list = rotate_right(original_sec)
        orig_list[i] = sec_list
        #print(f"AFTER IF: {orig_list}")
        #break

      else:
        #print("ELSE")
        while True:
          i-= 1
          sec_list = orig_list[i] 
          sec_list = rotate_right(sec_list)
          orig_list[i] = sec_list
          rotations_list[i] += 1
          rotations_list[i] = rotations_list[i] % 3
          if(rotations_list[i] != 0 or i == 0):
            break
           
        #print(i)
        flag = 1
        first_face = []
        second_face = []
        third_face = []
        for j in range(0, i):
          first_face.append(orig_list[j][0])
          second_face.append(orig_list[j][1])
          third_face.append(orig_list[j][2])
        if(i == 0):
          #print("NO SOLUTION.. Looking for Obstacle")
          #print(f"OG LIST IN SOLUTION METHOD: {orig_list}")
          #print(f"OBSTACLE: {original_sec}")
          return False
          #break
    if (flag == 0):
      i+= 1
      first_face.append(original_sec[0])
      second_face.append(original_sec[1])
      third_face.append(original_sec[2])
  #print(orig_list)

  return True


# ABOVE: Rotating Algorithm
#-------------------------------------------------------------
# Below: Finding Subsets and checking if they are obstacles or solutions


def findSubsetsList(givenList, subsetSize):
  all_combinations = combinations(givenList,subsetSize)
  all_combinations = list(all_combinations)
  return all_combinations 


#call with checkSolution(puzzle)  call check solution first to see what it has (True/False)
def subsetCheck(orig_list): #Our 2nd function
  mini_obstacle = orig_list #up to break point
  #print("No Solution Found... Locating Minimum Obstacle...")
  i = len(orig_list)
  #for i in range(len(orig_list), 1):
  subsets_list = []
  for i in range(len(orig_list) - 1, 1, -1):
    found_obstacle = False
    #print(f"Looking for all subsets of size: {i}..\n")
    subsets_list = findSubsetsList(orig_list, i) #generate subsets in list of size i #should i check starting from crash index?

    #for all values in the subsetlist
    true_counter = 0
    for j in range(0, len(subsets_list)):
      if (isSolution(list(subsets_list[j])) == True): #attempt to solve  the stack and continue checking all stacks
        true_counter += 1
        #print("Solved")
      
      else:
        #print(f"Unable to stack here: {subsets_list[j]}") #if stack is unsolvable we found a our minimum obstacle
        mini_obstacle = subsets_list[j]
        found_obstacle = True
        continue
    
      if(found_obstacle == True):
        #If we found an obstacle while iterating through subsets
        #print("We found an obstacle..\n")
        #print(f"Minimum Obstacle: {mini_obstacle}")
        #continue
        break
    print(f"Obstacle Found: {mini_obstacle}")
  print(f"\nFINAL Min Obstacle: {mini_obstacle}")



def main():

  main_puzzles_list = generate_colors()
  #first_puzzle = main_puzzles_list[0] #values from first puzzle
  master_list = split_list(main_puzzles_list)
  puzzle_one = master_list[0] #puzzle 1


  our_main_list = [[5,3,1], [5,4,2], [6,4,2], [1,5,3], [1,4,2], [6,3,6], [6, 6, 6]]

  isSolutionValue = isSolution(puzzle_one)

  if(isSolutionValue == True):
    print("PROGRAM DONE!")
  else:
    print("CALLING SUBSET CHECKER")
    subsetCheck(puzzle_one)


if __name__ == "__main__":
    main()