x = int(input("Number: "))

def fizzbuzz(x):
    if x % 3 == 0:
        print("fizz", end="")
    if x % 5 == 0:
        print("buzz")
    
fizzbuzz(x)