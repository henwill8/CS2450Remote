import random

print("Hello, I will try to guess your age.")
name = input("What is your name? ")
while True:
    guess = random.randint(15, 40)
    if input(f"Are you {guess} years old? (y/n) ").lower() = "y":
        print(f"{name} is {guess} years old.")
        break
    print("Rats.")
