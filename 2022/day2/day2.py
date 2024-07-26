
dict_part_one = { 'A':'r','B':'p','C':'s','Y':'p','X':'r','Z':'s'}
dict_part_two = { 'A':'r','B':'p','C':'s','Y':'t', 'X':'l', 'Z': 'w'}
with open("input", "r") as f:
    day2 = f.read()

def whoWins(a,b):
    if a == b:
        return 't'
    elif a == 'r':
        if b == 's':
            return 'l'
        else:
            return 'w'
    elif a == 'p':
        if b == 'r':
            return 'l'
        else:
            return 'w'
    elif a == 's':
        if b == 'p':
            return 'l'
        else:
            return 'w'
def getScore(a,b):
    score = 0
    match whoWins(a,b):
        case 't':
            score = 3
        case 'w':
            score = 6

    match b:
        case 'r':
            score += 1
        case 'p':
            score += 2
        case 's':
            score += 3
    return score

def calculateWin(a,b):
    match b:
        case 't':
            return a
        case 'w':
            if a == 'p':
                return 's'
            elif a == 'r':
                return 'p'
            elif a == 's':
                return 'r'
        case 'l':
            if a == 'p':
                return 'r'
            elif a == 's':
                return 'p'
            elif a == 'r':
                return 's'

all = [ r.split(" ") for r in [r for r in day2.strip().split('\n')]]

part_one_score = 0
part_two_score = 0
for play in all:
    part_one_score += getScore(dict_part_one[play[0]], dict_part_one[play[1]])
    part_two_score += getScore(dict_part_two[play[0]], calculateWin(dict_part_two[play[0]], dict_part_two[play[1]]))
print("[*] Part one: " + str(part_one_score))
print("[*] Part two: " + str(part_two_score))
