f = open('./input1.txt', 'r')

p  = 0
i  = 0
fc = 0

for c in f.read():
    i += 1
    if c == "(":
        p += 1
    if c == ")":
        p -= 1
    if p < 0 and fc == 0:
        fc = i

print ("A: " + str(p) + "  B: " + str(fc))
