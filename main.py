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


def compare_first_two(long_list):
  first_list = long_list[0]
  sec_list = long_list[1]
  fixed_order_first = []
  fixed_order_first.append(first_list)
  for i in range(0, 1):
    rotations = 0

    while(first_list[0] == sec_list[0] or first_list[1] == sec_list[1] or first_list[2] == sec_list[2]):

      original_sec = sec_list
      sec_list = rotate_shit(sec_list)

      rotations += 1
      if(rotations == 3):
        print(f"THIS IS A OBSTACLE DUDE {sec_list} ")
        #print(sec_list)
        break
    fixed_order_first.append(sec_list)
  return fixed_order_first

def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

def compare_next_values(orig_list): #CheckSolutions
  first_face = []
  second_face = []
  third_face = []
  rotations_list = [0] * len(orig_list) #0s for size of list
  sec_list = []
  missing_values_here = 1

  for i in range(0, 1):
    first_face.append(orig_list[0][0])
    second_face.append(orig_list[0][1])
    third_face.append(orig_list[0][2])

  i = 0
  while(i < len(orig_list)):
    original_sec = orig_list[i]
    flag = 0
    while(orig_list[i][0] in first_face or orig_list[i][1] in second_face or orig_list[i][2] in third_face): #wont be true during obstacle
      print(i)
      rotations_list[i] += 1
      rotations_list[i] = rotations_list[i] % 3
      #rotate_right()
      print(f"BEFORE IF: {orig_list}")

      if(rotations_list[i] != 0): #we have to rotate
        sec_list = rotate_right(original_sec)
        orig_list[i] = sec_list
        print(f"AFTER IF: {orig_list}")

      else:
        print("ELSE")
        i-= 1
        sec_list = orig_list[i] 
        sec_list =rotate_right(sec_list)
        orig_list[i] = sec_list
        rotations_list[i] += 1
        rotations_list[i] = rotations_list[i] % 3   
           
        print(i)
        flag = 1
        first_face = []
        second_face = []
        third_face = []
        for j in range(0, i):
          first_face.append(orig_list[j][0])
          second_face.append(orig_list[j][1])
          third_face.append(orig_list[j][2])
        if(i == 0):
          print("NO SOLUTION")
          print(f"OBSTACLE: {original_sec} it is slice #{i + 1}!")
          return False
          #break
    if (flag == 0):
      i+= 1
      first_face.append(original_sec[0])
      second_face.append(original_sec[1])
      third_face.append(original_sec[2])

  print("\n\n\n")
  print(orig_list)

  return True


def rotate_backwards(orig_list): #need it to return the list and the current crash
  orig_list.reverse()
  first_two = compare_first_two(orig_list)
  list_still_backwards = compare_next_values(first_two, orig_list) #calling with reversed list
  return list_still_backwards


def return_min_obstacle(list):
  lists = [[]]
  list_subsets = []
  for i in range(len(list) + 1):
      for j in range(i):
          lists.append(list[j: i])
      lists.append(0)
  #list_subsets.append(lists)
  return lists

# ABOVE: Rotating Algorithm
#-------------------------------------------------------------
# Below: Finding Subsets and checking if they are obstacles or solutions



'''
def findSubsetsList(givenList, subsetSize):
  all_combinations = combinations(givenList,subsetSize)
  all_combinations = list(all_combinations)
  return all_combinations 


#call with checkSolution(puzzle)  call check solution first to see what it has (True/False)
def subsetCheck(fixed_list, isSolution): #Our 2nd function
  if(isSolution == True): #check if puzzle is stackable
    print("Solution Found After Rotations:")
    print("No Obstacles :) \n")
    print(fixed_list) #prints the fixed list with no obstacles
    print("\n")

  else: #if the puzzle has an obstacle
    mini_obstacle = fixed_list #up to break point
    print("No Solution Found... Locating Minimum Obstacle...")
    for i in xrange(crash_index: 1): #crash_index choose n #generate all combs

      found_obstacle = False
      print(f"Looking for all subsets of size: {i}..\n")
      subsets_list = []
      subsets_list = findSubsetsList(fixed_list, i) #generate subsets in list of size i #should i check starting from crash index?

      #for all values in the subsetlist
      for j in range(0, len(subset_list)):
        if (checkSolution(subsets_list[j]) == True): #attempt to solve  the stack and continue checking all stacks
          true_counter += 1
          print("Solved")
        
        else:
          print(f"Unable to stack here: {subsets_list[j]}") #if stack is unsolvable we found a our minimum obstacle
          mini_obstacle = subsets_list[j]
          found_obstacle = True
          continue
      
        if(found_obstacle == True):
          #If we found an obstacle while iterating through subsets
          print("We found an obstacle..\n")
          print(f"Minimum Obstacle: {mini_obstacle}")
          #continue
          break
    print(f"Min Obstacle: {mini_obstacle}")
'''


def main():


  #all_patterns_list = generate_colors() #generating list of colors
  #master_list = split_list(all_patterns_list) #splitting it into a master 
  #subsets 4
  #subects 3
  #subsets 2


  our_main_list = [[5,3,1], [5,4,2], [6,4,2], [1,5,3], [1,4,2], [6,3,6]]
  compare_next_values(our_main_list)


  '''
  print("SUBSETS")
  subsetCount = 3
  comb = findSubsetsList(our_main_list, subsetCount) #generate all possible combinations of subsets for given {size}
  print(f"Size {len(comb)} list of all subsets at value {subsetCount}: {comb[0]}")
  print("SUBSETS\n\n\n")

  #our_main_list = [[5,3,1], [5,4,2], [6,4,2], [1,5,3], [1,4,2], [6,3,6]]
  temp_main = our_main_list.copy() #original full list


  first_two = compare_first_two(temp_main)
  new_value = compare_next_values(first_two, temp_main) #returns new list -> 
  print(new_value)
  current_crash = new_value[1]
  full_list = new_value[0]
  crash_index = new_value[0].index(current_crash)
  #current_list = new_value[0:crash_index + 1]
  print(f"CURRENT CRASH: {current_crash} at index: {crash_index}")
  print(f"FULL LIST: {full_list}")
  print("\n\n\n\nHEREEEEE")
  
  rotation = 1

  #list_subsets = return_min_obstacle(our_main_list)
  #print(list_subsets)

  first_two = compare_first_two(temp_main)
  new_value = compare_next_values(first_two, temp_main) #returns new list -> 

  current_crash = new_value[1]
  full_list = new_value[0]
  crash_index = new_value[0].index(current_crash)
  #current_list = new_value[0:crash_index + 1]
  print(f"CURRENT CRASH: {current_crash} at index: {crash_index}")
  print(f"FULL LIST: {full_list}")

  print(f"MAIN LIST UNTOUCHED: {our_main_list}")
  #print(new_value)
  our_main_list[0:crash_index + 1] = full_list[0:crash_index + 1]

  print(f"MAIN LIST REJOINED: {our_main_list}")


  print("\n\n\n\nHEREEEEE")
  rotation = 2
  list_obstacle = []
  list_obstacle.append(current_crash)

  while(current_crash != None):
    if(rotation % 2 == 0):
      #call it a 2nd time even = call backwards
      print("\n\n\nCALLING BACKWARD")
      new_value = rotate_backwards(full_list[0: crash_index + 1])

      current_crash = new_value[1]
      full_list = new_value[0]
      crash_index = new_value[0].index(current_crash)
      print(f"CURRENT CRASH: {current_crash} at index: {crash_index}")
      print(f"FULL LIST: {full_list}")
      list_obstacle.append(current_crash)

      rotation += 1

    else:
      print("\n\n\n3rd iter: CALLING Forward")
      full_list.reverse()

      first_two = compare_first_two(full_list[0: crash_index + 1])
      new_value = compare_next_values(first_two, full_list[0: crash_index + 1])
      current_crash = new_value[1]
      full_list = new_value[0]
      crash_index = new_value[0].index(current_crash)
      #current_list = new_value[0:crash_index + 1]
      print(f"CURRENT CRASH: {current_crash} at index: {crash_index}")
      print(f"FULL LIST: {full_list}")
      list_obstacle.append(current_crash)

      rotation += 1
  '''

if __name__ == "__main__":
    main()