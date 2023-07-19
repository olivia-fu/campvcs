ctr = 0

while True:
    c = float(input("Change Owed? "))
    c = round(c * 100)
    if c > 0:
        break

while c >= 25:
    c -= 25
    ctr += 1
while c >= 10:
    c = c - 10
    ctr = ctr + 1
while c >= 5:
    c = c - 5
    ctr = ctr + 1
while c >= 1:
    c = c - 1
    ctr = ctr + 1

print(ctr)