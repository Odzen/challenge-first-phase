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

# Backwards Greedy approach, from Home to dog
def CharlietheDog(strArr):
  
  inputString = eval(strArr)
  maze = []
  for row in inputString:
    maze.append([*row])
  
  totalDistance = 0
  
  
  numItems, items, initialPositionDog, currentPosition  = proccessMatrix(maze)
  
  while len(items) > 0:
    
    lowest =  10000
    lowestIndex = 0;
    lowestPosition = []
    
    for i in range(len(items)):
      distance = Manhattan(items[i], currentPosition)
      
      if distance < lowest:
        lowest = distance
        lowestPosition = items[i]
        lowestIndex = i
    
    totalDistance += lowest
    currentPosition = lowestPosition
    items.pop(lowestIndex)
  
  # From last point to the dog
  totalDistance += Manhattan(currentPosition, initialPositionDog)
    
  return totalDistance


print(CharlietheDog(input()))