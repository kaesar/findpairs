import sys

def getInput():
  listInput = raw_input("Input integers (separated with commas): ")
  print("List: ", listInput)

  sumInput = raw_input("Sum expected (integer value): ")
  print("Sum: ", sumInput)

  intList = []
  if len(listInput):
    intList = [int(x) for x in listInput.split(",")]
  intSum = 0
  if len(sumInput):
    intSum = int(sumInput)
  return intList, intSum

def findPairs(list, sum):
  hash = dict()
  i = 0
  n = len(list)

  while i < n:
    x = sum - list[i]
    if (x in list and x != list[i]):
      hash[x] = list[i]
      list.pop(i)
    else:
      i = i + 1
    
    if (i >= len(list)):
      break
  
  return hash

def test_findPairs():
  assert sys.version.index("2.7") == 0, "Test Python Version"
  assert findPairs([1,4,5,0,2,3], 5) == {0: 5, 3: 2, 4: 1}, "Test 1"
  assert findPairs([3,5,4,9,0,11,-2], 9) == {0: 9, 4: 5, -2: 11}, "Test 2"
  assert findPairs([1,9,5,0,20,-4,12,16,7], 12) == {16: -4, 12: 0, 7: 5}, "Test 3"
  assert findPairs([1,2,3,0], 4) == {3: 1}, "Test 4"
  print ("Find pairs tests passed. This is ready with Python 2!")

if __name__ == '__main__':
  test_findPairs()

  intList, intSum = getInput()
  result = findPairs(intList, intSum)
  if len(result):
    print("Pairs", result)
  else:
    print("Oops!")
