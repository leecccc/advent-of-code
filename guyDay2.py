f = open('./guyInput2.txt', 'r')

total = 0
er    = 0

for c in f:
    split = c.split("x")

    s1 = int(split[0])
    s2 = int(split[1])
    s3 = int(split[2])

    area  = 2*s1*s2 + 2*s2*s3 + 2*s3*s1
    extra = min(s1*s2, s2*s3, s3*s1)
    sp    = min((2*s1 + 2*s2), (2*s2 + 2*s3), (2*s3 + 2*s1))
    er   += sp + s1*s2*s3

    total += area + extra

print ("Total is: " + str(total) + ", square feet."
   + "\nTotal is: " + str(er) + ", feet of ribbon.")
