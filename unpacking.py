arr = ['a','b','c']
for i in range(len(arr)):
    print(i, arr[i])

tuples = [(1,2),(3,4)]
for i, (a,b) in enumerate(tuples):
    print(i, a, b)
    
def function(a, b, c, d=None):
    print(a, b, c, d)

function(*arr)