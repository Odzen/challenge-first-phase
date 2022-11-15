def turnToMinutes(time):
  
  formatedTime = time[:-2].split(":") # Take hours and minutes
  
  # Convert to military time
  if time[-2:] == "AM":
    formatedTime = [int(formatedTime[0]), int(formatedTime[1])]
  else:
    formatedTime = [int(formatedTime[0])+12, int(formatedTime[1])]
  
  if (formatedTime[0]==12 or formatedTime[0]==24):
    formatedTime[0] = formatedTime[0]-12
  
  return formatedTime[0] * 60 + formatedTime[1]

def MostFreeTime(strArr):
  evalutedInput = eval(strArr)
   
  listTimeMinutes = []
  
  for time in evalutedInput:
    listTimeMinutes.append([turnToMinutes(element) for element in time.split("-")])
    
  listTimeMinutes.sort()
  
  mostfreeTime =  0
  for i in range(len(listTimeMinutes)-1):
    freeTimeGap  = listTimeMinutes[i+1][0] - listTimeMinutes[i][1]
    
    # Check each gap of free time
    if freeTimeGap > mostfreeTime:
      mostfreeTime = freeTimeGap
    
  return "%02d:%02d" %(mostfreeTime/60, mostfreeTime%60) 
  

print(MostFreeTime(input()))