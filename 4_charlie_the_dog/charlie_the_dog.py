def proccessMatrix(maze):
  numItems = 0
  itemsPositions = []
  positionDog = []
  positionHouse = []
  
  for row in range(len(maze)):
    for column in range(len(maze)):
      if maze[row][column] == 'F':
        numItems+=1
        itemsPositions.append([row, column])
        
      if maze[row][column] == 'C':
        positionDog = [row, column]
      
      if maze[row][column] == 'H':
        positionHouse = [row, column]
        
  return numItems, itemsPositions, positionDog, positionHouse

def Manhattan(pointA, pointB):
    return abs(pointB[0] - pointA[0]) +  abs(pointB[1] - pointA[1])

def nextMovement(numItems, itemsPositions, initialPositionDog, positionHouse):
  
  distances = []
  nextPositionsDog = []
  
  # down, up, right, left
  nextPositionsDog.append([initialPositionDog[0], initialPositionDog[1] + 1])
  nextPositionsDog.append([initialPositionDog[0], initialPositionDog[1] - 1])
  nextPositionsDog.append([initialPositionDog[0] + 1, initialPositionDog[1]])
  nextPositionsDog.append([initialPositionDog[0] - 1,  initialPositionDog[1]])
  
  print("NEXT POSITIONS:", nextPositionsDog)
  
  for nextPosition in  nextPositionsDog:
    for item in itemsPositions:
      distances.append([Manhattan(item, initialPositionDog), item, nextPosition])
    
  print("Menor: ", min(distances))
  # for i in range(len(distances) - 1):
    
  #   print(distances[i + 1][0],distances[i][0] )
  #   if distances[i + 1][0] < distances[i][0]:
  #     smaller = distances[i + 1]
  #   else:
  #     smaller = distances[i]
  
  # print(distances, smaller)  
  
  return  min(distances)[2]


def CharlietheDog(strArr):
  
  inputString = eval(strArr)
  maze = []
  for row in inputString:
    maze.append([*row])
  print("MAZE: ", maze)
  
  inHouse = False
  numItems = 1000
  
  while numItems != 0 and inHouse != True:
    numItems, itemsPositions, initialPositionDog, positionHouse  = proccessMatrix(maze)
    newPositionDog = nextMovement(numItems, itemsPositions, initialPositionDog, positionHouse)
    
    print("NEW POSITION DOG: ", newPositionDog)
    
    if newPositionDog[0] == positionHouse[0] and newPositionDog[1] == positionHouse[1]:
      inHouse = True
    
    for itemsPosition in itemsPositions:
      if newPositionDog[0] == itemsPosition[0] and newPositionDog[1] == itemsPosition[1]:
        numItems-=1
    
    maze[initialPositionDog[0]][initialPositionDog[1]] = 'O'
    maze[newPositionDog[0]][newPositionDog[1]] = 'C'
    print("NEW MAZE: ", maze)
    

    
  
  return strArr


print(CharlietheDog(input()))