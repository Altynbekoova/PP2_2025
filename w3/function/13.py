import random
def guess():
    print("hello, what is your name")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1,20)
    count = 0
    
    while True:
        print("Take a guess")
        guess = int(input())
        count += 1
        
        if guess < number:
            print("is too low")
        elif guess > number:
            print("is too high")
        else:
            print(f"good job {name}!, you guessed number in {count} guesses")
            break
guess()
    