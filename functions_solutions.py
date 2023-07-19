# 2. stats dashboard
def stats(list):
    print("min: " + str(min(list)))
    print("max: " + str(max(list)))
    print("avg: " + str(sum(list)/len(list)))

stats([10, 20, 30])

# 3. compress
def compress(string):
    ctr = 1
    output = string[0]
    initial = string[0]

    for i in string[1:]:
        if i == initial:
            ctr += 1
        else:
            output = output + str(ctr)
            ctr = 1
            initial = i
            output = output + initial

    output = output + str(ctr)
    print(output)

compress("aaaabbcddd")