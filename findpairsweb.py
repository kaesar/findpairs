import bottle
from bottle import response

def enable_cors(fn):
  def _enable_cors(*args, **kwargs):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

    if bottle.request.method != 'OPTIONS':
      return fn(*args, **kwargs)

  return _enable_cors

app = bottle.app()

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

@app.route("/")
def index():
  return 'Hi there!'

@app.route("/sum/<list>/<sum>")
@enable_cors
def compute(list, sum):
  intList = []
  if len(list):
    intList = [int(x) for x in list.split(",")]
  intSum = 0
  if len(sum):
    intSum = int(sum)
  result = findPairs(intList, intSum)
  return {"pairs": result}

def test_findPairs():
  assert findPairs([1,4,5,0,2,3], 5) == {0: 5, 3: 2, 4: 1}, "Test 1"
  assert findPairs([3,5,4,9,0,11,-2], 9) == {0: 9, 4: 5, -2: 11}, "Test 2"
  assert findPairs([1,9,5,0,20,-4,12,16,7], 12) == {16: -4, 12: 0, 7: 5}, "Test 3"
  assert findPairs([1,2,3,0], 4) == {3: 1}, "Test 4"
  print ("Find pairs tests passed. This is ready!")

test_findPairs()
app.run(host='localhost', port=8080, debug=True, reloader=True)
