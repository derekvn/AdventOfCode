import numpy as np

with open('input', 'r') as f:
    input = f.read()

partone = 0
parttwo = 0
for line in input.strip().split('\n'):
    arr = [ x.split('-') for x in line.split(',')]
    a = list(range(int(arr[0][0]),int(arr[0][1])+1)) 
    b = list(range(int(arr[1][0]),int(arr[1][1])+1))
    if set(a).issubset(set(b)) or set(b).issubset(set(a)):
        partone += 1
    if True in np.isin(a,b) or True in np.isin(b,a):
        parttwo += 1
print("Part one: %s" % (str(partone)))
print("Part two: %s" % (str(parttwo)))

