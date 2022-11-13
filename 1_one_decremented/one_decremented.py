def OneDecremented(strParam):
  if len(strParam) < 1:
    return
  
  counter = 0
  
  for index in range(0, len(strParam) - 1):
    if int(strParam[index]) - int(strParam[index+1]) == 1:
      counter+=1  
      
  return counter

print(OneDecremented(input()))