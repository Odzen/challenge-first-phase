def OverlappingRectangles(strArr):

  # code goes here
  return isOverlapping(strArr)


def proccessingData(str):
  formatedString = str.replace("[", "").replace("]", "").replace('"', "")
  
  indexFirstRectangle = 0
  indexSecondRectangle = 0
  counting = 0
  
  for index, element in enumerate(formatedString):
    if element == ')':
      counting+=1
    
    if counting == 4 and indexFirstRectangle == 0:
      indexFirstRectangle = index
    if counting == 8 and indexSecondRectangle == 0:
      indexSecondRectangle = index
  
  first = formatedString[0:indexFirstRectangle + 1]
  second = formatedString[indexFirstRectangle + 1: indexSecondRectangle + 1]
  
  return list(eval(first)), list(eval(second[1:]))


""" def checkRangeXY(list):
  for coordinateFirst in firstRectangle:
    x = coordinateFirst[0]
    y = coordinateFirst[1]
  
  
  return rangeX, rangeY """
  

def isOverlapping(strArr):
  
  firstRectangle, secondRectangle = proccessingData(strArr)
  
  for coordinateFirst in firstRectangle:
    x = coordinateFirst[0]
    y = coordinateFirst[1]
    
    
    
    for tupleSecond in secondRectangle:
      
  
  

# keep this function call here 
print(OverlappingRectangles(input()))