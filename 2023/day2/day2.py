#!/usr/bin/env python3
with open('input_sample', 'r') as f:
    input = f.read()

color_cubes = { 'red' : 12, 'blue' : 14, 'green' : 13 }


games = [ { 'no' : line.split(":")[0].replace('Game ',''),  'sets' : line.split(":")[1].strip().split("; "), 'valid' : True, 'red' : 99, 'blue' : 99, 'green': 99 }  for line in input.strip().split("\n") ]

for idx, game in enumerate(games):
    for item in game['sets']:
        pairs = item.split(', ')
        for pair in pairs:
            color = pair.split(' ')[1]
            num = int(pair.split(' ')[0])
            if num > color_cubes[color]:
                games[idx]['valid'] = False
            if num < games[idx][color]:
                games[idx][color] = num
            
print(games)

print("[*] Day 1:  {}".format(sum([int(game['no']) for game in games if game['valid'] == True])))
print("[*] Day 2:  {}".format(sum([ game['red'] * game['blue'] * game['green'] for game in games if game['valid'] == True])))
