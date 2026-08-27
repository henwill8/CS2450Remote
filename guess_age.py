import random

print("Hello, I will try to guess your age.")
name = input("What is your name? ")
for i in range(1, 6):
    guess = random.randint(15, 40)
    if input(f"[Guess {i}/5] Are you {guess} years old? (y/n) ").lower() = "y":
        print(f"{name} is {guess} years old.")
        break
    print("Rats.")
    # cool comment

print("I could not guess it")
