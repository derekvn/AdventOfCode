with open('input', 'r') as f:
    input = f.read()

for i in range(len(input)):
    if len(input[i:i+4]) == len(set(input[i:i+4])):
        print('Day one: %s' % str(i+4))
        break

for i in range(len(input)):
    if len(input[i:i+14]) == len(set(input[i:i+14])):
        print('Day two: %s' % str(i+14))
        break
