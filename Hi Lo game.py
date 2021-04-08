low = 1
high = 1000

print(f"Please think of a number between {low} and {high} ")
input("Press ENTER to start")

guesses = 1
while True:
    print()
    print(f"Guessing in the range of {low} to {high}")
    print()
    guess = low + (high - low) // 2
    high_low = input(f"My guess is {guess} Should I guess higher or lower?"
                     f" Enter h or l, or c if my guess was correct: ").casefold()

    if high_low == "h":
        low = guess + 1

    elif high_low == "l":
        high = guess - 1

    elif high_low == "c":
        print(f"I got it correct in {guesses} guesses.")
        break
    else:
        print("Enter h,l or c")

    guesses += 1
