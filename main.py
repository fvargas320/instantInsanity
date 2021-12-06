import math

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


'''
Check if there is an obstacle
'''


def rotate_shit(listHere):
  listHere = listHere[-1:] + listHere[:-1]
  #listHere = listHere[1:] + [listHere[0]]
  return listHere


def print_list(givenList):
  for i in range(0, len(givenList)):
    print(givenList[i])

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
  #print_list(fixed_order_first)
  return fixed_order_first
  #first_side.append(fixed_order[i][0])
  #sec_side.append(fixed_order[i][1])
  #third_side.append(fixed_order[i][2])
  #print(rotations)

def compare_next_values(first_two, orig_list):
  first_face = []
  second_face = []
  third_face = []
  sec_list = []
  fixed_order = []
  obstacles = []
  for i in range(0, len(first_two)):
    first_face.append(first_two[i][0])
    second_face.append(first_two[i][1])
    third_face.append(first_two[i][2])

  #print(f"FIRST FACE: {first_face}")



  for i in range(2, len(orig_list)):
    original_sec = orig_list[i]
    rotations = 0
    if((orig_list[i][0] in first_face or orig_list[i][1] in second_face or orig_list[i][2] in third_face)):
      
      '''
      print(f"first:face inside if: {first_face}")
      print(f"2nd:face inside if: {second_face}")
      print(f"3rd:face inside if: {third_face}")
      '''

      print(f"NUMBER OF ROTATION:{rotations}")
      while(orig_list[i][0] in first_face or orig_list[i][1] in second_face or orig_list[i][2] in third_face):
        sec_list = rotate_shit(original_sec)
        orig_list[i] = sec_list
        rotations += 1
        #print("HELLOOO")
        if(rotations >=3):
          print(f"THIS IS A OBSTACLE {original_sec} even when rotated to become {sec_list} it is slice #{i + 1}!")
          obstacles.append(original_sec)
          break

      fixed_order.append(sec_list)
      first_face.append(sec_list[0])
      second_face.append(sec_list[1])
      third_face.append(sec_list[2])
      first_two.append(sec_list)

      '''
      UNCOMMENT IF NEED ALL LISTS SIDE BY SIDE
      
      #print(f"\nNEW ROTATED LIST: {first_two} ")
      #print_list(first_two)
      '''
      print(" ORIGINAL       FIXED")
      res = "\n".join("{} {}".format(x, y) for x, y in zip(orig_list, first_two))
      print(res)


    else:
      fixed_order.append(original_sec)
      first_face.append(original_sec[0])
      second_face.append(original_sec[1])
      third_face.append(original_sec[2])
      first_two.append(original_sec)

  

  '''

  '''
  #print(f"first_face: {first_face}") #doesnt include first 2
  #print(f"first_face: {second_face}") #doesnt include first 2
  #print(f"first_face: {third_face}") #doesnt include first 2

  #print("\n List of all Obstacles!")
  #print(obstacles)
  

  #print(f"\nNEW ROTATED LIST: {first_two} ")

  #return first_two


  #print(f"\n FIRST FACE VALUES {first_face}")
  #print(f"\n SEC FACE VALUES {second_face}")
  #print(f"\n THIRD FACE VALUES {third_face}")



def find_solution(listHere):
  print("THIS IS UNLIKELY")
  return puzzle_solution

  


def main():
  all_patterns_list = generate_colors() #generating list of colors
  master_list = split_list(all_patterns_list) #splitting it into a master list of 3 subsets


  #2,3,1
  #list_fucked = [[1,2,3], [3, 1, 2], [1,3, 2]]
  #2,3,1 3,1,2
  list_fucked = [[1, 4, 2], [3,1,5], [6, 4, 2], [2,5,4], [5,3,1]]


  list_fucked.reverse()

  
  #long_list = [[5,5 ,1],[5,1,1], [4, 4, 4], [7, 7, 7], [2,2,3], [3,3,2], [4,1,1]]

  #first_list = master_list[0]
  first_list = list_fucked
  #print(master_list[0])
  #print("\nORIGINAL LIST:")
  #print_list(first_list)

  #print("\nFIRST TWO BELOW")
  first_two = compare_first_two(first_list)
  compare_next_values(first_two, first_list)
  #print(final_chart)
  #fixed_solution = compare_next_values(first_two, first_list)
  #fixed_solution.reverse()
  #new_solution = fixed_solution + list_fucked[5:]
  #first_two_for_new = compare_first_two(new_solution)
  #fixed_solution_two = compare_next_values(first_two_for_new, new_solution)
  #print(f" first_two_for_new: {first_two_for_new}")
  #print(f"NEW SOLUTION: {new_solution}")
  #print(f"FINAL: SOLUTION: {fixed_solution_two}")






if __name__ == "__main__":
    main()