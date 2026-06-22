import random
words = ["superman", "spiderman", "ironman", "antman", "batman"]
word = random.choice(words)
guess_word = []
for i in word:
    guess_word.append("_")

chance = 6
print("welcome to Hangman Game")
while chance > 0:
    print("\nword:  ", end="")
    for i in guess_word: 
        print(i, end=" ")

    letter = input("\nEnter a letter: ").lower()

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                 guess_word[i] = letter
        print("Correct Guess!")

    else: 
        chance -= 1
        print("Wrong Guess!")
        print("Chance Left:", chance)

    if "_" not in guess_word:
        print ("\nCongratulations! You won.")
        print("The word was:", word) 
        break
if "_" in guess_word:
    print("\nGame Over!")
    print("The word was: ", word)
               