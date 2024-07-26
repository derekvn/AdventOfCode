with open('input', 'r') as f:
    input = f.read()

totals = [ sum([int(elf_i) for elf_i in elf.split('\n')]) for elf in input.strip().split('\n\n') ]

a = sorted(totals, reverse=True)

print('[*] Part one: ' + str(a[0]))
print('[*] Part two: ' + str(a[0]+a[1]+a[2]))

