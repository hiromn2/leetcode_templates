#Two pointers: one input, opposite ends

def fn(array):
  left = ans = 0
  right = len(array) - 1

  while left < right:
    #do something
    if CONDITION: 
      left += 1
    else: 
      right -= 1
  return ans


# Two pointers: two inputs, exhaust both
def fn(arr1, arr2):
  i = j = ans = 0

  while i < len(arr1) and j < len(arr2):
    #do some logic here
    if CONDITION:
      i += 1
    else:
      j += 1

  while i < len(arr1):
    # do logic
    i += 1

  while j < len(arr2):
    # do logic
    j += 1

  return ans

#WAKARANAI
#Sliding Window
def fn(arr):
  left = ans = curr = 0
  for right in range(len(arr)):
    # do logic here to add[right] to curr
    while WINDOW_COMPETITION_BROKEN:
      # remove arr[left] from curr
      left += 1
    # update ANS
  return ans


#WAKARANAI
#Build a Prefix Sum
def fn(arr):
  prefix = [arr[0]]
  for i in range(1, len(arr)):
    prefix.append(prefix[-1] + arr[i])
    
  return prefix

#WAKARANAI
# arr is a list of characters
def fn(arr):
  ans = []
  for c in arr:
    ans.append(c)
    
  return "".join(ans)


