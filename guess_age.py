import random

print("Hello, I will try to guess your age.")
name = input("What is your name? ")
guessed_ages = set()
for i in range(1, 6):
    guess = random.randint(15, 40)
    while guess in guessed_ages:
        guess = random.randint(15, 40)
    if input(f"[Guess {i}/5] Are you {guess} years old? (y/n) ").lower() = "y":
        print(f"{name} is {guess} years old.")
        break
    guessed_ages.add(guess)
    print("Rats.")
    # cool comment

print("I could not guess it")
