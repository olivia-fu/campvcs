greeting = input("Greeting: ")

def bank(string):
    if string[:5].lower() == "hello":
        print("$0")
    elif string[0].lower() == "h":
        print("$20")
    else:
        print("$100")
        
bank(greeting)