while True:    
    h = int(input("Height: "))
    if h <= 8 and h >= 1:
        break

for i in range(1,h+1):
    print(" " * (h-i) + "#" * i)