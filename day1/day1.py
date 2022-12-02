with open("input", "r") as f:
    input = f.read()
totals = []
c = 0
for elf in input.strip().split("\n\n"):
    for elf_i in elf.split("\n"):
        c += int(elf_i)
    totals.append(c)
    c = 0

a = sorted(totals, reverse=True)

print("[*] Part one: " + str(a[0]))
print("[*] Part two: " + str(a[0]+a[1]+a[2]))

