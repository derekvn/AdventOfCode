import re

with open('input', 'r') as f:
    input = f.read()


a = [ ord(x)-(96 if ord(x) > 96 else 38) for x in [list(set(line[:len(line)//2]).intersection(set(line[len(line)//2:])))[0] for line in input.strip().split('\n')]]
b = [ ord(x)-(96 if ord(x) > 96 else 38) for x in [list(set(w[0]).intersection(set(w[1]), set(w[2])))[0] for w in re.findall(r'(.*)\n(.*)\n(.*)\n',input,re.M) ]]

print("Part 1: " + str(sum(a)))
print("Part 2: " + str(sum(b)))
