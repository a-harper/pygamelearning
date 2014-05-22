__author__ = 'harpera'
import random

answer = random.randrange(1, 100)
guess = 0
attemptCount = 1
attemptLimit = 7
print("Hi! I'm thinking of a random number between 1 and 100.")
while guess != answer:
    if attemptCount > attemptLimit:
        print("Aw, you ran out of tries. The number was", answer)
        break
    print("Attempt: ", attemptCount)
    guess = int(input("Guess what number I am thinking of: "))
    if guess > answer:
        print("Too high")
    if guess < answer:
        print("Too low")
    if guess == answer:
        print("Correct! The answer was:", answer)
        break
    attemptCount += 1