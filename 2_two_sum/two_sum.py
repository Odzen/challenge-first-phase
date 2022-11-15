def sumTo(equalNumber , number, rest):
  for numInList in rest:
    if number + numInList == equalNumber:
      return number, numInList
  return

def toString(arr):
  string = ''
  for element in arr:
    string = string + str(element[0]) + ',' + str(element[1])+ ' '
  return string

def TwoSum(arr):

  evalutedInput = eval(arr)
  
  first = evalutedInput[0]
  rest = evalutedInput[1:]

  output = []
 
  for i in range(len(rest)):
    result = sumTo(first , rest[i], rest[i+1:])
    if result:
      output.append(result)
  
  if len(output) == 0:
    return -1

  return toString(output)

print(TwoSum(input()))