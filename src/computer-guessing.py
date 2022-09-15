# The following code is just to setup the exercise. You do not need to
# understand but can jump to the game below.


def input_selection(prompt: str, options: list[str]) -> str:
    """Get user input, restrict it to fixed options."""
    modified_prompt = "{} [{}]: ".format(
        prompt.strip(), ", ".join(options)
    )
    while True:
        inp = input(modified_prompt)
        if inp in options:
            return inp
        # nope, not a valid answer...
        print("Invalid choice! Must be in [{}]".format(
            ", ".join(options)
        ))


print("Please thing of a number from 1 to 20, both included.")
print("Let me know how good my guess is.\n")

# Here, we implement the computer's strategy for guessing
# the number you are thinking of. Don't lie to the
# computer. It won't punish you, but it will frown upon it.

# The first strategy

for guess in range(1, 21):
    result = input_selection(
        "I'm guessing {}\nHow is my guess?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break

    print("I must have been too low, right?", result)

# The second strategy

for guess in reversed(range(1, 21)):
    result = input_selection(
        "I'm guessing {}\nHow is my guess?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break

    print("I must have been too high, right?", result)

# The third strategy

guess = 10
guess_lowest = 1
guess_highest = 20
while True:
    result = input_selection(
        "I'm guessing {}\nHow is my guess?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break
    if result == "low":
        new_range = range[guess:guess_highest]
        guess = new_range[len(new_range)//2]
        guess_highest = new_range[-1]
        guess_lowest = new_range[0]
        print("I must have been too high, right?", result)
    if result == "high"
        new_range = range[guess_lowest:guess]
        guess = new_range[len(new_range)//2]
        guess_highest = new_range[-1]
        guess_lowest = new_range[0]
        print("I must have been too high, right?", result)