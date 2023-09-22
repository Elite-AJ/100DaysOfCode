
#MAJOR CODE
##HANGMAN
#Generate Random Word
import Hangman_words
import Hangman_ART
import random

from Hangman_ART import logo
print(logo)
from Hangman_words import word_list
chosen_word = random.choice(word_list)
stages = Hangman_ART.stages
#Accept input
display = []
for i in chosen_word:

    display += ("_")

#Live control and loop
lives = 6
code_end = False
while not code_end:
    rand_letter = input("Guess a Letter: ").lower()
    
    if rand_letter in display:
        print(f"{rand_letter} already guessed")
    #Replacing blank spaces with the right alphabets    
    from Hangman_ART import stages
    space = 0
    for alpha in chosen_word:
        space += 1
        if alpha == rand_letter:
            display[space - 1] = rand_letter
    print(display)

    if rand_letter not in chosen_word:
        print(f"You guessed {rand_letter}, that's not in the  word. You lose a life.")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            code_end = True
            print("You lose")
            
    
    print(f"{' '.join(display)}")
    print (f"The word is {chosen_word}")

    if "_" not in display:
        code_end = True
        print("You Win")
